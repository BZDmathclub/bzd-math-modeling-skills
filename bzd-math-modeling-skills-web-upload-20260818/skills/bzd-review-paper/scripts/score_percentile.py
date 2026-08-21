#!/usr/bin/env python3
"""Compute a transparent midrank percentile from a reference score distribution."""

import argparse
import csv
import json
from pathlib import Path


def load_scores(path: Path, column: str | None) -> list[float]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if isinstance(data, dict):
            data = data[column or "scores"]
        return [float(x[column]) if isinstance(x, dict) else float(x) for x in data]
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return []
    selected = column or ("score" if "score" in rows[0] else next(iter(rows[0])))
    return [float(row[selected]) for row in rows if row.get(selected, "").strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--distribution", type=Path, required=True, help="CSV or JSON scores")
    parser.add_argument("--column", help="CSV column or JSON object key")
    args = parser.parse_args()
    scores = load_scores(args.distribution, args.column)
    if not scores:
        raise SystemExit("Distribution contains no usable scores")
    below = sum(value < args.score for value in scores)
    equal = sum(value == args.score for value in scores)
    percentile = 100 * (below + 0.5 * equal) / len(scores)
    result = {
        "score": args.score,
        "n": len(scores),
        "below": below,
        "equal": equal,
        "percentile_outperformed": round(percentile, 2),
        "equivalent_top_percent": round(100 - percentile, 2),
        "method": "midrank empirical percentile",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
