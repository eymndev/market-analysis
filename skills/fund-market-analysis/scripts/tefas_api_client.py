#!/usr/bin/env python3
"""Read-only API helper for the fund analysis skill."""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request


ALLOWED_PREFIXES = ("/api/v1/funds", "/api/v1/fund-info", "/api/v1/befas", "/api/v1/funds-reports", "/info", "/api/v1/healthz")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="documented read-only API path")
    parser.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")
    args = parser.parse_args()
    if not args.path.startswith(ALLOWED_PREFIXES):
        parser.error("path is outside the documented read-only endpoint groups")
    base = os.environ.get("TEFAS_API_BASE_URL", "").rstrip("/")
    if not base.startswith("https://"):
        parser.error("TEFAS_API_BASE_URL must be an https:// URL")
    params: list[tuple[str, str]] = []
    for item in args.param:
        if "=" not in item:
            parser.error(f"invalid --param: {item!r}")
        key, value = item.split("=", 1)
        params.append((key, value))
    url = f"{base}/{args.path.lstrip('/')}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {"Accept": "application/json", "User-Agent": "market-analysis/0.1"}
    key = os.environ.get("TEFAS_API_KEY")
    if key:
        headers[os.environ.get("TEFAS_API_KEY_HEADER", "X-RapidAPI-Key")] = key
    host = os.environ.get("TEFAS_API_HOST")
    if host:
        headers["X-RapidAPI-Host"] = host
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            payload = response.read()
            try:
                parsed = json.loads(payload)
                print(json.dumps(parsed, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                print(payload.decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        request_id = exc.headers.get("X-Request-Id")
        raise SystemExit(f"HTTP {exc.code}; request_id={request_id or 'unavailable'}") from exc


if __name__ == "__main__":
    main()
