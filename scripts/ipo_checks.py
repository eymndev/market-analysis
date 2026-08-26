#!/usr/bin/env python3
"""Check core IPO arithmetic from a JSON fact sheet."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def number(data: dict[str, object], key: str) -> float | None:
    value = data.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be a number")
    return float(value)


def check_close(name: str, actual: float | None, expected: float | None, tolerance: float) -> dict[str, object]:
    if actual is None or expected is None:
        return {"check": name, "status": "not_checked", "actual": actual, "expected": expected}
    difference = actual - expected
    allowed = max(tolerance, abs(expected) * tolerance)
    return {
        "check": name,
        "status": "pass" if math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance) else "fail",
        "actual": actual,
        "expected": expected,
        "difference": difference,
        "allowed_difference": allowed
    }


def run(data: dict[str, object], tolerance: float) -> dict[str, object]:
    price = number(data, "offer_price")
    total = number(data, "total_offered_shares")
    capital = number(data, "capital_increase_shares")
    sale = number(data, "shareholder_sale_shares")
    gross = number(data, "gross_offering_size")
    pre = number(data, "pre_ipo_capital")
    post = number(data, "post_ipo_capital")
    stated_float = number(data, "stated_post_ipo_float_ratio")
    stated_discount = number(data, "stated_discount_rate")
    undiscounted = number(data, "undiscounted_value_per_share")

    checks = [
        check_close("offer composition", total, None if capital is None or sale is None else capital + sale, tolerance),
        check_close("post-IPO capital", post, None if pre is None or capital is None else pre + capital, tolerance),
        check_close("gross offering size", gross, None if price is None or total is None else price * total, tolerance),
        check_close("post-IPO float ratio", stated_float, None if total is None or post in (None, 0) else total / post, tolerance),
        check_close(
            "offer discount",
            stated_discount,
            None if price is None or undiscounted in (None, 0) else 1 - price / undiscounted,
            max(tolerance, 5e-4)
        )
    ]
    return {"checks": checks, "failed": sum(c["status"] == "fail" for c in checks)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    args = parser.parse_args()
    if args.tolerance <= 0:
        parser.error("--tolerance must be positive")
    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    print(json.dumps(run(data, args.tolerance), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
