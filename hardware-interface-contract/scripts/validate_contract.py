#!/usr/bin/env python3
"""校验硬件接口契约 JSON 文件的基础结构。"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "contract_version",
    "project",
    "generated_from",
    "components",
    "interfaces",
    "pins",
    "power",
    "boot_reset",
    "registers",
    "firmware_tasks",
    "risks",
    "open_questions",
]

LIST_FIELDS = {
    "generated_from",
    "components",
    "interfaces",
    "pins",
    "power",
    "boot_reset",
    "registers",
    "firmware_tasks",
    "risks",
    "open_questions",
}

CONFIDENCE_FIELDS = {
    "components",
    "interfaces",
    "pins",
    "power",
    "boot_reset",
    "registers",
}

VALID_CONFIDENCE = {"high", "medium", "low"}


def fail(message: str) -> None:
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"警告：{message}", file=sys.stderr)


def load_contract(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        fail(f"找不到文件：{path}")
    except json.JSONDecodeError as exc:
        fail(f"JSON 无效，位置为第 {exc.lineno} 行第 {exc.colno} 列：{exc.msg}")

    if not isinstance(data, dict):
        fail("顶层 JSON 值必须是对象")
    return data


def validate(data: dict) -> None:
    missing = [field for field in REQUIRED_TOP_LEVEL if field not in data]
    if missing:
        fail("缺少必需顶层字段：" + ", ".join(missing))

    for field in LIST_FIELDS:
        if not isinstance(data[field], list):
            fail(f"{field} 必须是列表")

    if not isinstance(data["contract_version"], str) or not data["contract_version"].strip():
        fail("contract_version 必须是非空字符串")

    if not isinstance(data["project"], str) or not data["project"].strip():
        fail("project 必须是非空字符串")

    if not data["generated_from"]:
        warn("generated_from 为空，契约将难以审查")

    for field in CONFIDENCE_FIELDS:
        for index, item in enumerate(data[field]):
            if not isinstance(item, dict):
                fail(f"{field}[{index}] 必须是对象")
            confidence = item.get("confidence")
            if confidence not in VALID_CONFIDENCE:
                warn(f"{field}[{index}] 应包含 confidence：high、medium 或 low")
            evidence = item.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                warn(f"{field}[{index}] 应包含非空 evidence")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("用法：validate_contract.py <hardware-interface-contract.json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    data = load_contract(path)
    validate(data)
    print(f"通过：{path} 符合硬件接口契约的基础结构")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
