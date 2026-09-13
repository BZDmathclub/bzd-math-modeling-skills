#!/usr/bin/env python3
"""Estimate award band and position for CUMCM or a smaller contest."""

import argparse
import json


ANCHORS = [(10.0, 0.1), (45.0, 50.0), (55.0, 75.0), (65.0, 90.0), (75.0, 98.0), (90.0, 99.9)]


def interpolate_cumcm(score: float) -> float:
    if score <= ANCHORS[0][0]:
        return ANCHORS[0][1]
    if score >= ANCHORS[-1][0]:
        return ANCHORS[-1][1]
    for (x0, y0), (x1, y1) in zip(ANCHORS, ANCHORS[1:]):
        if x0 <= score <= x1:
            return y0 + (score - x0) * (y1 - y0) / (x1 - x0)
    raise AssertionError("unreachable")


def cumcm_award_band(score: float) -> str:
    if score >= 75:
        return "推荐国奖评审（2025校准：前2%）"
    if score >= 65:
        return "省一等奖相对稳定区间（2025校准：前2%-10%）"
    if score >= 55:
        return "省二等奖区间（2025校准：前10%-25%）"
    if score >= 45:
        return "省三等奖区间（2025校准：前25%-50%）"
    return "低于2025校准的省三等奖区间"


def interpolate_small(score: float) -> float:
    """Uniform fallback on the practical 10-90 score interval."""
    return min(99.9, max(0.1, (score - 10.0) / 80.0 * 100.0))


def small_award_band(score: float) -> str:
    if score >= 75:
        return "一等奖竞争区间（小型竞赛经验锚点）"
    if score >= 65:
        return "二等奖竞争区间（小型竞赛经验锚点）"
    if score >= 55:
        return "三等奖竞争区间（小型竞赛经验锚点）"
    return "低于小型竞赛经验获奖区间"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--contest-type", choices=("cumcm", "small"), required=True)
    parser.add_argument("--uncertainty", type=float, default=None, help="percentile half-width")
    args = parser.parse_args()
    if args.contest_type == "cumcm":
        percentile = interpolate_cumcm(args.score)
        uncertainty = 3.0 if args.uncertainty is None else args.uncertainty
        band = cumcm_award_band(args.score)
        method = "CUMCM 2025 large-field score-anchor interpolation"
    else:
        percentile = interpolate_small(args.score)
        uncertainty = 8.0 if args.uncertainty is None else args.uncertainty
        band = small_award_band(args.score)
        method = "small-contest 10-90 uniform approximation"
    low = max(0.1, percentile - uncertainty)
    high = min(99.9, percentile + uncertainty)
    result = {
        "adjusted_score": round(args.score, 1),
        "percentile_outperformed": round(percentile, 1),
        "percentile_interval": [round(low, 1), round(high, 1)],
        "equivalent_top_percent": round(100 - percentile, 1),
        "contest_type": args.contest_type,
        "award_band": band,
        "method": method,
        "confidence": "medium" if args.contest_type == "cumcm" else "low",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
