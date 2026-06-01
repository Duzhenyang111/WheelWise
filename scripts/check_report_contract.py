#!/usr/bin/env python3
"""Validate WheelWise final report structure.

This script checks the concrete failure modes seen in real WheelWise output:
English skill-module headings, missing Chinese report sections, missing visuals,
thin intro/outro, and incomplete UI demo details.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "报告说明与阅读导览",
    "项目标题",
    "想法摘要",
    "交付形态",
    "结论：构建 MVP / 先验证 / 暂停 / 放弃",
    "决策解释摘要",
    "目标用户",
    "问题与紧迫性",
    "市场备注",
    "用户假设",
    "差异化",
    "MVP 范围",
    "产品策略",
    "Build / Buy / Reuse / Fork / Reference 决策",
    "技术实现路径",
    "视觉说明",
    "UI Demo / 交互 Demo",
    "HTML 展示文件",
    "商业化备注",
    "关键风险",
    "验证实验",
    "Codex-ready 执行计划",
    "最终建议与下一步行动",
]

BANNED_ENGLISH_HEADINGS = [
    "Idea Intake",
    "Surface Strategy",
    "Feasibility Review",
    "Product Strategy",
    "Reuse Evaluator",
    "Technical Planning",
    "Risk Review",
    "UI Demo Scope",
    "MVP Execution Plan",
    "Visual Brief",
    "Execution Plan",
]


def has_heading(text: str, title: str) -> bool:
    return bool(re.search(rf"^#{{1,3}}\s+{re.escape(title)}\s*$", text, re.M))


def section_body(text: str, title: str) -> str:
    match = re.search(rf"^#{{1,3}}\s+{re.escape(title)}\s*$", text, re.M)
    if not match:
        return ""
    next_heading = re.search(r"^#{1,3}\s+\S.*$", text[match.end() :], re.M)
    if not next_heading:
        return text[match.end() :]
    return text[match.end() : match.end() + next_heading.start()]


def validate_report(path: Path, *, skip_filename: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []

    if not skip_filename and not re.fullmatch(
        r"wheelwise-report(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?\.md", path.name
    ):
        problems.append(
            "文件名必须是 wheelwise-report.md 或 wheelwise-report-<idea-slug>.md"
        )

    missing = [section for section in REQUIRED_SECTIONS if not has_heading(text, section)]
    if missing:
        problems.append("缺少中文章节：" + "、".join(missing))

    positions = []
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^#{{1,3}}\s+{re.escape(section)}\s*$", text, re.M)
        if match:
            positions.append((section, match.start()))
    for (left, left_pos), (right, right_pos) in zip(positions, positions[1:]):
        if left_pos > right_pos:
            problems.append(f"章节顺序错误：{left} 应位于 {right} 之前")
            break

    banned_found = [
        heading
        for heading in BANNED_ENGLISH_HEADINGS
        if re.search(rf"^#{{1,3}}\s+{re.escape(heading)}\s*$", text, re.M)
    ]
    if banned_found:
        problems.append("禁止使用英文 skill 模块标题：" + "、".join(banned_found))

    intro = section_body(text, "报告说明与阅读导览")
    for keyword in ["报告目的", "适用阶段", "核心结论预览", "阅读方式"]:
        if keyword not in intro:
            problems.append(f"报告说明与阅读导览缺少：{keyword}")

    visual = section_body(text, "视觉说明")
    if not re.search(r"!\[[^\]]+\]\([^\)]+\)|```mermaid", visual):
        problems.append("视觉说明必须包含 Markdown 图片引用或 Mermaid fallback")

    demo = section_body(text, "UI Demo / 交互 Demo")
    for keyword in ["Demo 路径", "运行方式", "核心交互", "mock 数据", "未接入真实后端"]:
        if keyword not in demo:
            problems.append(f"UI Demo / 交互 Demo 缺少：{keyword}")

    html = section_body(text, "HTML 展示文件")
    for keyword in ["wheelwise-report.html", "展示层", "Markdown"]:
        if keyword not in html:
            problems.append(f"HTML 展示文件缺少：{keyword}")

    outro = section_body(text, "最终建议与下一步行动")
    for keyword in ["一句话判断", "7 天", "14 天", "30 天"]:
        if keyword not in outro:
            problems.append(f"最终建议与下一步行动缺少：{keyword}")
    if not re.search(r"go/no-go|Go/no-go|继续/停止|推进/停止", outro):
        problems.append("最终建议与下一步行动缺少 go/no-go 或继续/停止条件")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a WheelWise Markdown report.")
    parser.add_argument("report", type=Path, help="Path to wheelwise-report*.md")
    parser.add_argument(
        "--skip-filename",
        action="store_true",
        help="Validate structure only, useful for shared templates.",
    )
    args = parser.parse_args()

    problems = validate_report(args.report, skip_filename=args.skip_filename)
    if problems:
        print(f"FAIL {args.report}")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"PASS {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
