#!/usr/bin/env python3
"""Map an adjusted score to the owner-supplied 2025 award/position anchors."""

import argparse
import json


ANCHORS = [(10.0, 0.1), (45.0, 50.0), (55.0, 75.0), (65.0, 90.0), (75.0, 98.0), (90.0, 99.9)]


def interpolate(score: float) -> float:
    if score <= ANCHORS[0][0]:
        return ANCHORS[0][1]
    if score >= ANCHORS[-1][0]:
        return ANCHORS[-1][1]
    for (x0, y0), (x1, y1) in zip(ANCHORS, ANCHORS[1:]):
        if x0 <= score <= x1:
            return y0 + (score - x0) * (y1 - y0) / (x1 - x0)
    raise AssertionError("unreachable")


def award_band(score: float) -> str:
    if score >= 75:
        return "推荐国奖评审（2025校准：前2%）"
    if score >= 65:
        return "省一等奖相对稳定区间（2025校准：前2%-10%）"
    if score >= 55:
        return "省二等奖区间（2025校准：前10%-25%）"
    if score >= 45:
        return "省三等奖区间（2025校准：前25%-50%）"
    return "低于2025校准的省三等奖区间"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--uncertainty", type=float, default=3.0, help="percentile half-width")
    args = parser.parse_args()
    percentile = interpolate(args.score)
    low = max(0.1, percentile - args.uncertainty)
    high = min(99.9, percentile + args.uncertainty)
    result = {
        "adjusted_score": round(args.score, 1),
        "percentile_outperformed": round(percentile, 1),
        "percentile_interval": [round(low, 1), round(high, 1)],
        "equivalent_top_percent": round(100 - percentile, 1),
        "award_band_2025": award_band(args.score),
        "method": "2025 score-anchor calibrated linear interpolation",
        "confidence": "medium",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
