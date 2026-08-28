#!/usr/bin/env python3
"""Apply transparent CUMCM region, school, advisor and division adjustments."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "references" / "data"


def clamp(value: float, low: float, high: float) -> float:
    return min(high, max(low, value))


def normalize(value: str) -> str:
    value = (value or "").strip().replace("（", "(").replace("）", ")")
    return re.sub(r"\s+", "", value).casefold()


def read_rows(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def exact_row(rows: list[dict[str, str]], column: str, value: str) -> dict[str, str] | None:
    key = normalize(value)
    matches = [row for row in rows if normalize(row.get(column, "")) == key]
    return matches[0] if len(matches) == 1 else None


def number(row: dict[str, str] | None, key: str) -> float | None:
    if not row:
        return None
    raw = (row.get(key) or "").strip()
    try:
        return float(raw)
    except ValueError:
        return None


def truthy(value: str) -> bool:
    return normalize(value) in {"是", "yes", "true", "1"}


def advisor_missing(value: str) -> bool:
    return normalize(value) in {"", "无", "未知", "不详", "none", "unknown"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score", type=float, required=True, help="paper quality final score")
    parser.add_argument("--region", required=True)
    parser.add_argument("--school", required=True)
    parser.add_argument("--advisor", required=True)
    parser.add_argument("--division", choices=("本科组", "高职高专组"), required=True)
    args = parser.parse_args()

    schools = read_rows("school_awards_2021_2026.csv")
    public = read_rows("region_public_statistics.csv")
    difficulty = read_rows("region_difficulty_scores.csv")
    school = exact_row(schools, "school_name", args.school)
    region_public = exact_row(public, "region", args.region)
    region_diff = exact_row(difficulty, "region", args.region)

    if args.division == "本科组":
        national_key = "undergraduate_national_difficulty"
        provincial_key = "undergraduate_provincial_difficulty"
    else:
        national_key = "vocational_national_difficulty"
        provincial_key = "vocational_provincial_difficulty"

    national_difficulty = number(region_diff, national_key)
    provincial_difficulty = number(region_diff, provincial_key)
    # Region difficulty is normalized around 50. National-award competition
    # receives the wider +/-15 range; provincial-award competition uses +/-10.
    national_region_delta = (
        0.0
        if national_difficulty is None
        else clamp((50 - national_difficulty) / 50 * 15, -15, 15)
    )
    provincial_region_delta = (
        0.0
        if provincial_difficulty is None
        else clamp((50 - provincial_difficulty) / 50 * 10, -10, 10)
    )

    school_delta = 0.0
    advisor_delta = 0.0
    award_ceiling = None
    national_probability_ceiling = None
    advisor_status = "not_applicable"
    confidence = "中等"

    if school is None:
        award_ceiling = "省一等奖"
        national_probability_ceiling = 0.0681
        confidence = "低"
    else:
        if truthy(school.get("is_modeling_strong_school", "")):
            school_delta = 1.5
        frequency = number(school, "top_advisor_frequency") or 0.0
        concentrated = truthy(school.get("top_advisor_frequency_over_30pct", ""))
        if concentrated:
            if advisor_missing(args.advisor):
                advisor_status = "missing_advisor_lower_confidence"
                confidence = "中低"
            elif normalize(args.advisor) == normalize(school.get("top_advisor", "")):
                advisor_delta = 0.5
                advisor_status = "matches_top_advisor"
            else:
                advisor_delta = -min(4.0, 1.5 + 5 * max(0.0, frequency - 0.30))
                advisor_status = "different_from_top_advisor"
        else:
            advisor_status = "not_concentrated"

    provincial_score = clamp(args.score + provincial_region_delta, 0, 90)
    national_score = clamp(args.score + national_region_delta + school_delta + advisor_delta, 0, 90)
    if school is None:
        national_score = min(national_score, 74.9)

    public_context = None
    if region_public:
        if args.division == "本科组":
            public_context = {
                "team_count": number(region_public, "undergraduate_team_count"),
                "school_count": number(region_public, "undergraduate_school_count"),
                "strong_school_count": number(region_public, "undergraduate_strong_school_count"),
                "project_985_count": number(region_public, "project_985_count"),
                "project_211_count": number(region_public, "project_211_count"),
                "provincial_first_rate": number(region_public, "provincial_first_rate"),
                "provincial_second_rate": number(region_public, "provincial_second_rate"),
                "provincial_third_rate": number(region_public, "provincial_third_rate"),
            }
        else:
            public_context = {
                "team_count": number(region_public, "vocational_team_count"),
                "school_count": number(region_public, "vocational_school_count"),
                "strong_school_count": number(region_public, "vocational_strong_school_count"),
                "provincial_first_rate": number(region_public, "provincial_first_rate"),
                "provincial_second_rate": number(region_public, "provincial_second_rate"),
                "provincial_third_rate": number(region_public, "provincial_third_rate"),
                "excluded_from_adjustment": ["project_985_count", "project_211_count"],
            }

    result = {
        "paper_quality_final_score": round(args.score, 1),
        "division": args.division,
        "region": args.region,
        "school": args.school,
        "advisor": args.advisor,
        "region_adjustment": {
            "national_difficulty": national_difficulty,
            "national_delta": round(national_region_delta, 2),
            "provincial_difficulty": provincial_difficulty,
            "provincial_delta": round(provincial_region_delta, 2),
        },
        "school_match": school is not None,
        "school_region_consistent": None if school is None else normalize(args.region) == normalize(school.get("region", "")),
        "school_context": None if school is None else {
            "region_in_table": school.get("region"),
            "national_awards_five_years": number(school, "national_five_years"),
            "national_forecast_2026": number(school, "national_forecast_2026"),
            "is_modeling_strong_school": school.get("is_modeling_strong_school"),
            "school_delta": school_delta,
            "top_advisor": school.get("top_advisor"),
            "top_advisor_count": number(school, "top_advisor_count"),
            "top_advisor_frequency": number(school, "top_advisor_frequency"),
            "top_advisor_frequency_over_30pct": school.get("top_advisor_frequency_over_30pct"),
        },
        "advisor_adjustment": {"status": advisor_status, "delta": round(advisor_delta, 2)},
        "provincial_competition_score": round(provincial_score, 1),
        "national_competition_score": round(national_score, 1),
        "award_prediction_ceiling": award_ceiling,
        "national_probability_ceiling": national_probability_ceiling,
        "region_public_context": public_context,
        "confidence": confidence,
        "method": "CUMCM historical competition-context heuristic; not an official award model",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
