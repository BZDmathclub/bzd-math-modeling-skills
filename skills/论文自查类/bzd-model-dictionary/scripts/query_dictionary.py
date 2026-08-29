#!/usr/bin/env python3
"""Search the bundled BZD model dictionary without modifying it."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DICTIONARY = ROOT / "assets" / "model-dictionary.json"


def normalize(value: object) -> str:
    text = str(value or "").casefold().replace("（", "(").replace("）", ")")
    return re.sub(r"[\s_\-—–·/]+", "", text)


def load_dictionary() -> dict:
    with DICTIONARY.open(encoding="utf-8-sig") as handle:
        root = json.load(handle)
    if not isinstance(root, dict) or not isinstance(root.get("数据"), list):
        raise ValueError("Invalid model dictionary structure")
    return root


def score_record(record: dict, query: str) -> tuple[int, int]:
    q = normalize(query)
    name = normalize(record.get("模型名称"))
    if not q:
        return (0, 0)
    if name == q:
        return (4, 0)
    if q in name:
        return (3, len(name) - len(q))
    if name in q:
        return (2, len(q) - len(name))
    searchable = normalize(" ".join(str(record.get(k, "")) for k in ("模型类别", "具体分组", "适用场景")))
    if q in searchable:
        return (1, len(searchable) - len(q))
    return (0, 0)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="model name or unambiguous alias")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--exact", action="store_true")
    args = parser.parse_args()

    root = load_dictionary()
    ranked = []
    for record in root["数据"]:
        rank, distance = score_record(record, args.model)
        if rank and (not args.exact or rank == 4):
            ranked.append((rank, -distance, int(record["序号"]), record))
    ranked.sort(reverse=True, key=lambda item: item[:3])

    fields = [
        "序号", "模型名称", "模型大类", "具体分组", "模型类别", "适用场景",
        "数据要求", "原理讲解", "模型输入", "模型输出", "关键假设", "禁忌点",
        "模型缺陷", "检验方法", "资料使用声明",
    ]
    matches = [{key: rec[key] for key in fields if key in rec} for *_, rec in ranked[: max(1, args.limit)]]
    output = {
        "数据集名称": root.get("数据集名称"),
        "制作方": root.get("制作方"),
        "使用许可": root.get("使用许可"),
        "版权与传播声明": root.get("版权与传播声明"),
        "查询": args.model,
        "匹配总数": len(ranked),
        "返回记录数": len(matches),
        "数据": matches,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

