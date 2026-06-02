#!/usr/bin/env python3
"""Validate WheelWise final report structure.

This script checks the concrete failure modes seen in real WheelWise output:
English skill-module headings, missing Chinese report sections, missing visuals,
thin intro/outro, and incomplete UI demo details.
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import re
import struct
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "报告说明与阅读导览",
    "项目标题",
    "想法摘要",
    "交付形态",
    "结论：构建最小可行产品 / 先验证 / 暂停 / 放弃",
    "决策解释摘要",
    "目标用户",
    "问题与紧迫性",
    "市场备注",
    "用户假设",
    "差异化",
    "最小可行产品范围",
    "产品策略",
    "自研 / 购买 / 复用 / 分叉改造 / 参考决策",
    "技术实现路径",
    "视觉说明",
    "交互演示",
    "网页展示文件",
    "商业化备注",
    "关键风险",
    "验证实验",
    "可交给 Codex 执行的计划",
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

BANNED_VISIBLE_TERMS = [
    "Build",
    "Buy",
    "Reuse",
    "Fork",
    "Reference",
    "Web App",
    "SaaS",
    "MVP",
    "Demo",
    "mock",
    "fallback",
    "go/no-go",
    "Codex-ready",
]

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}

PROJECT_STATE_REQUIRED_FIELDS = [
    "Idea summary",
    "Current phase",
    "Delivery surface",
    "Gate status",
    "Feasibility",
    "Product strategy summary",
    "Reuse decisions summary",
    "Technical plan summary",
    "Commercialization summary",
    "Risk summary",
    "Visual/demo status",
    "Final report status",
    "Open questions",
    "Assumptions",
    "Last updated by skill",
]

EVIDENCE_BOARD_REQUIRED_FIELDS = [
    "Evidence item",
    "Source / origin skill",
    "Evidence type",
    "Affected decision",
    "Strength",
    "Confidence",
    "Assumption vs evidence",
    "Contradiction",
    "Evidence gap",
    "Recommended next action",
]


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"style", "script"}:
            self._skip_depth += 1
        for name, value in attrs:
            if name in {"alt", "title", "aria-label"} and value:
                self.parts.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"style", "script"} and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        return "\n".join(part.strip() for part in self.parts if part.strip())


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


def strip_markdown_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]*`", "", text)


def html_visible_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.text()


def find_banned_visible_terms(text: str) -> list[str]:
    found = []
    for term in BANNED_VISIBLE_TERMS:
        if re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", text, re.I):
            found.append(term)
    return sorted(set(found), key=str.lower)


def local_image_refs_from_markdown(text: str) -> list[str]:
    refs = []
    for image_ref in re.findall(r"!\[[^\]]+\]\(([^\)]+)\)", text):
        if not re.match(r"https?://|data:", image_ref):
            refs.append(image_ref)
    return refs


def local_image_refs_from_html(path: Path) -> list[str]:
    refs = re.findall(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", path.read_text(encoding="utf-8"), re.I)
    return [ref for ref in refs if not re.match(r"https?://|data:", ref)]


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as file:
        header = file.read(24)
    if len(header) >= 24 and header.startswith(b"\x89PNG\r\n\x1a\n"):
        return struct.unpack(">II", header[16:24])
    return None


def validate_image_file(path: Path) -> list[str]:
    problems = []
    if not path.exists():
        return [f"图片文件不存在：{path}"]
    if path.stat().st_size <= 0:
        problems.append(f"图片文件为空：{path}")
    if path.suffix.lower() == ".png":
        dimensions = png_dimensions(path)
        if not dimensions or dimensions[0] <= 0 or dimensions[1] <= 0:
            problems.append(f"PNG 图片尺寸无效：{path}")
    return problems


def validate_report(
    path: Path, *, skip_filename: bool = False, check_local_assets: bool = False
) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []

    if not skip_filename and path.name != "report.md" and not re.fullmatch(
        r"wheelwise-report(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?\.md", path.name
    ):
        problems.append(
            "文件名必须是 report.md、wheelwise-report.md 或 wheelwise-report-<idea-slug>.md"
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

    visible_terms = find_banned_visible_terms(strip_markdown_code(text))
    if visible_terms:
        problems.append("Markdown 可见文字包含禁止英文展示词：" + "、".join(visible_terms))

    intro = section_body(text, "报告说明与阅读导览")
    for keyword in ["报告目的", "适用阶段", "核心结论预览", "阅读方式"]:
        if keyword not in intro:
            problems.append(f"报告说明与阅读导览缺少：{keyword}")

    visual = section_body(text, "视觉说明")
    if not re.search(r"!\[[^\]]+\]\([^\)]+\)|```mermaid", visual):
        problems.append("视觉说明必须包含 Markdown 图片引用或 Mermaid 兜底方案")
    elif check_local_assets:
        for image_ref in local_image_refs_from_markdown(visual):
            image_path = (path.parent / image_ref).resolve()
            problems.extend(validate_image_file(image_path))

    demo = section_body(text, "交互演示")
    for keyword in ["演示路径", "运行方式", "核心交互", "模拟数据", "未接入真实后端"]:
        if keyword not in demo:
            problems.append(f"交互演示缺少：{keyword}")

    html = section_body(text, "网页展示文件")
    for keyword in ["index.html", "展示层", "源报告"]:
        if keyword not in html:
            problems.append(f"网页展示文件缺少：{keyword}")
    if check_local_assets and "已生成" in html:
        html_refs = re.findall(r"`([^`]+\.html(?:#[^`]+)?)`|(?<![\w.-])([./\w-]+\.html)(?:#[\w-]+)?", html)
        flattened_refs = [left or right for left, right in html_refs]
        for html_ref in flattened_refs:
            clean_ref = html_ref.split("#", 1)[0]
            if clean_ref.startswith("http://") or clean_ref.startswith("https://"):
                continue
            html_path = (path.parent / clean_ref).resolve()
            if not html_path.exists():
                problems.append(f"网页展示文件标记为已生成，但文件不存在：{html_ref}")

    outro = section_body(text, "最终建议与下一步行动")
    for keyword in ["一句话判断", "7 天", "14 天", "30 天"]:
        if keyword not in outro:
            problems.append(f"最终建议与下一步行动缺少：{keyword}")
    if not re.search(r"继续\s*/\s*停止|推进\s*/\s*停止|继续条件|停止条件", outro):
        problems.append("最终建议与下一步行动缺少继续/停止条件")

    return problems


def normalize_local_ref(ref: str) -> str:
    return ref.replace("\\", "/").removeprefix("./")


def validate_internal_v4_files(folder: Path) -> list[str]:
    problems: list[str] = []
    project_state = folder / "project-state.md"
    evidence_board = folder / "evidence-board.md"

    if not project_state.exists():
        problems.append("V4 报告目录缺少 project-state.md")
    else:
        state_text = project_state.read_text(encoding="utf-8")
        missing_state = [
            field for field in PROJECT_STATE_REQUIRED_FIELDS if field not in state_text
        ]
        if missing_state:
            problems.append("project-state.md 缺少字段：" + "、".join(missing_state))

    if not evidence_board.exists():
        problems.append("V4 报告目录缺少 evidence-board.md")
    else:
        evidence_text = evidence_board.read_text(encoding="utf-8")
        missing_evidence = [
            field for field in EVIDENCE_BOARD_REQUIRED_FIELDS if field not in evidence_text
        ]
        if missing_evidence:
            problems.append("evidence-board.md 缺少字段：" + "、".join(missing_evidence))

    return problems


def validate_folder(
    folder: Path, *, skip_filename: bool = False, v4: bool = False
) -> list[str]:
    problems: list[str] = []
    if not folder.exists() or not folder.is_dir():
        return [f"报告目录不存在：{folder}"]
    if not skip_filename and not re.fullmatch(
        r"wheelwise-report(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?", folder.name
    ):
        problems.append("报告目录名必须是 wheelwise-report 或 wheelwise-report-<idea-slug>")

    report_path = folder / "report.md"
    html_path = folder / "index.html"
    assets_dir = folder / "assets"

    if not report_path.exists():
        problems.append("报告目录缺少 report.md")
    if not html_path.exists():
        problems.append("报告目录缺少 index.html")
    if not assets_dir.exists() or not assets_dir.is_dir():
        problems.append("报告目录缺少 assets/ 目录")

    image_files = []
    if assets_dir.exists() and assets_dir.is_dir():
        image_files = [
            path
            for path in assets_dir.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        ]
        if not image_files:
            problems.append("assets/ 目录至少需要一张图片")
        for image_file in image_files:
            problems.extend(validate_image_file(image_file))

    if report_path.exists():
        problems.extend(
            validate_report(report_path, skip_filename=True, check_local_assets=True)
        )
        report_text = report_path.read_text(encoding="utf-8")
        for image_ref in local_image_refs_from_markdown(report_text):
            if not normalize_local_ref(image_ref).startswith("assets/"):
                problems.append(f"Markdown 图片引用必须指向 assets/：{image_ref}")

    if html_path.exists():
        visible = html_visible_text(html_path)
        html_terms = find_banned_visible_terms(visible)
        if html_terms:
            problems.append("HTML 可见文字包含禁止英文展示词：" + "、".join(html_terms))
        for image_ref in local_image_refs_from_html(html_path):
            clean_ref = image_ref.split("#", 1)[0]
            image_path = (html_path.parent / clean_ref).resolve()
            if not image_path.exists():
                problems.append(f"HTML 图片引用不存在：{image_ref}")
            elif not normalize_local_ref(clean_ref).startswith("assets/"):
                problems.append(f"HTML 图片引用必须指向 assets/：{image_ref}")

    if v4:
        problems.extend(validate_internal_v4_files(folder))

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a WheelWise Markdown report.")
    parser.add_argument("report", type=Path, help="Path to report.md or report folder")
    parser.add_argument(
        "--folder",
        action="store_true",
        help="Validate a WheelWise report folder with report.md, index.html, and assets/.",
    )
    parser.add_argument(
        "--v4",
        action="store_true",
        help="In folder mode, also require V4 internal project-state.md and evidence-board.md.",
    )
    parser.add_argument(
        "--skip-filename",
        action="store_true",
        help="Validate structure only, useful for shared templates.",
    )
    parser.add_argument(
        "--check-local-assets",
        action="store_true",
        help="Also verify local image and generated HTML references exist.",
    )
    args = parser.parse_args()

    if args.folder:
        problems = validate_folder(
            args.report, skip_filename=args.skip_filename, v4=args.v4
        )
    else:
        problems = validate_report(
            args.report,
            skip_filename=args.skip_filename,
            check_local_assets=args.check_local_assets,
        )
    if problems:
        print(f"FAIL {args.report}")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"PASS {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
