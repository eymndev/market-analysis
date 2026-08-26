#!/usr/bin/env python3
"""Read-only BISTECH VERDA client using environment-based Basic Auth."""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def request(path: str) -> tuple[bytes, dict[str, str]]:
    base = os.environ.get("BIST_VERDA_BASE_URL", "https://verda.borsaistanbul.com").rstrip("/")
    if not base.startswith("https://"):
        raise SystemExit("BIST_VERDA_BASE_URL must use https://")
    user = os.environ.get("BIST_VERDA_USER")
    password = os.environ.get("BIST_VERDA_PASSWORD")
    if not user or not password:
        raise SystemExit("BIST_VERDA_USER and BIST_VERDA_PASSWORD are required")
    manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, base, user, password)
    opener = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(manager))
    try:
        with opener.open(urllib.request.Request(base + path, headers={"Accept": "application/json"}), timeout=60) as response:
            return response.read(), dict(response.headers.items())
    except urllib.error.HTTPError as exc:
        request_id = exc.headers.get("X-Request-Id")
        raise SystemExit(f"HTTP {exc.code}; X-Request-Id={request_id or 'unavailable'}") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    download = sub.add_parser("download")
    download.add_argument("--type", required=True, type=int, dest="file_type")
    download.add_argument("--year", type=int)
    download.add_argument("--month", type=int)
    download.add_argument("--day", type=int)
    download.add_argument("--hour", type=int)
    download.add_argument("--session", type=int)
    download.add_argument("--json", action="store_true")
    download.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "list":
        payload, _ = request("/files")
        print(json.dumps(json.loads(payload), indent=2, ensure_ascii=False))
        return
    params: dict[str, int | str] = {"type": args.file_type}
    for name in ("year", "month", "day", "hour", "session"):
        value = getattr(args, name)
        if value is not None:
            params[name] = value
    if args.json:
        params["media"] = "json"
    payload, headers = request("/files/download?" + urllib.parse.urlencode(params))
    if args.output:
        args.output.write_bytes(payload)
        print(json.dumps({"output": str(args.output), "bytes": len(payload), "request_id": headers.get("X-Request-Id")}, ensure_ascii=False))
    elif args.json:
        print(json.dumps(json.loads(payload), indent=2, ensure_ascii=False))
    else:
        raise SystemExit("binary downloads require --output")


if __name__ == "__main__":
    main()
