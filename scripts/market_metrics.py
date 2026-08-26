#!/usr/bin/env python3
"""Compute auditable return/risk metrics from a date,close CSV file."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from datetime import date, datetime
from pathlib import Path


def parse_date(value: str) -> date:
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError(f"unsupported date: {value!r}")


def load_prices(path: Path) -> list[tuple[date, float]]:
    rows: list[tuple[date, float]] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not {"date", "close"}.issubset(reader.fieldnames):
            raise ValueError("CSV must contain date and close columns")
        for line, row in enumerate(reader, start=2):
            try:
                value = float((row["close"] or "").replace(",", "."))
                if value <= 0:
                    raise ValueError("close must be positive")
                rows.append((parse_date(row["date"] or ""), value))
            except Exception as exc:
                raise ValueError(f"invalid row {line}: {exc}") from exc
    unique = {day: value for day, value in rows}
    result = sorted(unique.items())
    if len(result) < 2:
        raise ValueError("at least two distinct dates are required")
    return result


def compute(prices: list[tuple[date, float]], periods: int, rf: float) -> dict[str, object]:
    log_returns = [math.log(b[1] / a[1]) for a, b in zip(prices, prices[1:])]
    total_return = prices[-1][1] / prices[0][1] - 1
    elapsed_days = (prices[-1][0] - prices[0][0]).days
    years = elapsed_days / 365.2425 if elapsed_days > 0 else 0
    warnings: list[str] = []
    cagr = (prices[-1][1] / prices[0][1]) ** (1 / years) - 1 if elapsed_days >= 30 else None
    if elapsed_days < 30:
        warnings.append("CAGR omitted because the observation window is shorter than 30 days")
    enough_returns = len(log_returns) >= 20
    volatility = statistics.stdev(log_returns) * math.sqrt(periods) if enough_returns else None
    annualized_return = statistics.mean(log_returns) * periods if enough_returns else None
    if not enough_returns:
        warnings.append("Annualized return, volatility and Sharpe omitted because fewer than 20 returns are available")
    sharpe = (annualized_return - rf) / volatility if volatility and annualized_return is not None else None

    peak_value = prices[0][1]
    peak_date = prices[0][0]
    worst = 0.0
    worst_peak = peak_date
    trough_date = peak_date
    for day, value in prices:
        if value > peak_value:
            peak_value, peak_date = value, day
        drawdown = value / peak_value - 1
        if drawdown < worst:
            worst, worst_peak, trough_date = drawdown, peak_date, day

    return {
        "observations": len(prices),
        "start_date": prices[0][0].isoformat(),
        "end_date": prices[-1][0].isoformat(),
        "start_close": prices[0][1],
        "end_close": prices[-1][1],
        "total_return": total_return,
        "cagr": cagr,
        "annualized_log_return": annualized_return,
        "annualized_volatility": volatility,
        "risk_free_rate": rf,
        "sharpe_approx": sharpe,
        "max_drawdown": worst,
        "drawdown_peak_date": worst_peak.isoformat(),
        "drawdown_trough_date": trough_date.isoformat(),
        "periods_per_year": periods,
        "warnings": warnings
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path, help="CSV with date,close columns")
    parser.add_argument("--periods", type=int, default=252, help="observations per year")
    parser.add_argument("--risk-free", type=float, default=0.0, help="annual decimal rate")
    args = parser.parse_args()
    if args.periods <= 0:
        parser.error("--periods must be positive")
    print(json.dumps(compute(load_prices(args.csv), args.periods, args.risk_free), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
