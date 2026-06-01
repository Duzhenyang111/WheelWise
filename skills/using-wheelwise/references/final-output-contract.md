# Final Output Contract

WheelWise final output is a Chinese Markdown report file. A static HTML display file may also be generated, but it is only a presentation layer sourced from the Markdown report.

## File Contract

- Primary file: `wheelwise-report.md`.
- If the user provides an idea name, use `wheelwise-report-<idea-slug>.md`.
- Optional display file: `wheelwise-report.html`.
- The report body must be fully Chinese.
- Titles, section names, table fields, decision explanations, risk notes, validation experiments, and execution-plan prose must be Chinese.
- Product names, technical stacks, code paths, commands, API names, and Build / Buy / Reuse / Fork / Reference labels may remain English.
- The chat response after generation should only state the Markdown path, the HTML path if created, and a short completion note. Do not substitute a chat summary for the file.

## Progressive Report Order

The report must read like a finished product brief, not a concatenation of skill outputs:

```text
报告说明与阅读导览
-> 用户与问题
-> 核心决策与方案
-> 视觉说明与交互 Demo
-> 商业化、风险与验证
-> Codex-ready 执行计划
-> 最终建议与下一步行动
```

Do not use internal skill names as section headings. Forbidden headings include `Idea Intake`, `Surface Strategy`, `Feasibility Review`, `Product Strategy`, `Reuse Evaluator`, `Technical Planning`, `Risk Review`, `UI Demo Scope`, and `MVP Execution Plan`.

## Required Chinese Sections

The core New Product Brief must include the original 20 sections plus the required opening, HTML display record, and ending action section:

1. 报告说明与阅读导览
2. 项目标题
3. 想法摘要
4. 交付形态
5. 结论：构建 MVP / 先验证 / 暂停 / 放弃
6. 决策解释摘要
7. 目标用户
8. 问题与紧迫性
9. 市场备注
10. 用户假设
11. 差异化
12. MVP 范围
13. 产品策略
14. Build / Buy / Reuse / Fork / Reference 决策
15. 技术实现路径
16. 视觉说明
17. UI Demo / 交互 Demo
18. HTML 展示文件
19. 商业化备注
20. 关键风险
21. 验证实验
22. Codex-ready 执行计划
23. 最终建议与下一步行动

## Opening and Ending

`报告说明与阅读导览` must include:

- 报告目的。
- 适用阶段。
- 核心结论预览。
- 阅读方式。

`最终建议与下一步行动` must include:

- 一句话判断。
- 7 天行动。
- 14 天行动。
- 30 天行动。
- go/no-go or 继续/停止条件。

## Visual and Demo Rules

- Visual brief images, image prompts, or production methods must be written into `视觉说明`.
- Prefer real image assets when image generation is available. Existing assets must be referenced with Markdown, for example `![产品概念图](./assets/visual-brief.png)`.
- If image generation is unavailable, include a Mermaid fallback in `视觉说明`; at least one decision map, MVP roadmap, or validation funnel is required.
- UI demo output must be written into `UI Demo / 交互 Demo`, including demo path, run command, core interactions, mock data notes, loading/empty/error/success states, and backend simulation boundary.
- API, CLI, automation, or developer-tool products must use an API playground, terminal simulator, request explorer, workflow simulator, or comparable non-backend demo surface.

## HTML Display Rules

- `wheelwise-report.html` is optional but recommended when the idea benefits from visual presentation.
- The HTML file is not the source of truth. It must be derived from the same Chinese Markdown report.
- If UI UX Pro Max or another UI/UX skill is available, it may be used as design intelligence only. Do not copy external skill content.
- The HTML display should include cover, core conclusion, decision map, MVP roadmap, visual explanation, demo section, risk and validation, and execution plan.
- If no HTML is generated, the report must still include `HTML 展示文件` and state whether it is planned, skipped, or recommended next.

## Integration Rules

- Decision rationales must use Chinese field names from `../../shared/references/decision-rationale-standard.md`.
- The Codex-ready plan must include tasks to generate or update the Markdown report file.
- If HTML is generated or recommended, the Codex-ready plan must include a task to generate or update `wheelwise-report.html`.

Use `../../shared/templates/new-product-brief.md` for the full Chinese report.
