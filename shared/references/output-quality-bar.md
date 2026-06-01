# WheelWise Output Quality Bar

A WheelWise answer is acceptable only when it:

- Produces a single Chinese Markdown report file: `wheelwise-report.md` by default or `wheelwise-report-<idea-slug>.md` when the idea name is available.
- Does not substitute a chat summary for the report file.
- Uses Chinese for report title, section names, table fields, explanations, decision rationales, risks, experiments, and execution-plan prose.
- Reads as a progressive report, not a dump of internal skill sections: opening guide, user/problem, decisions/solution, visual/demo, risks/validation, execution plan, and final action advice.
- Includes `报告说明与阅读导览` with report purpose, applicable stage, core conclusion preview, and reading path.
- Includes `最终建议与下一步行动` with one-sentence judgment, 7-day, 14-day, 30-day actions, and go/no-go or continue/stop conditions.
- Does not use English internal module headings such as `Idea Intake`, `Surface Strategy`, `Reuse Evaluator`, `Technical Planning`, `Risk Review`, `UI Demo Scope`, or `MVP Execution Plan`.
- Makes a clear verdict.
- Names the delivery surface.
- Includes decision rationale for key decisions in Chinese: 决策是什么, 为什么选择它, 为什么不选替代方案, 证据, 假设, 风险, fallback, 信心等级.
- Separates evidence from assumptions.
- Avoids copying external skill content.
- Connects `feasibility-review` to `product-strategy`.
- Gives module-level Build / Buy / Reuse / Fork / Reference decisions.
- Connects `reuse-evaluator` decisions to `technical-planning` without contradictions.
- Includes image-level visual explanation via `visual-brief` for full reports, written into the `视觉说明` section with Markdown image references when assets exist, or Mermaid fallback when image generation is unavailable.
- Includes an interactive UI demo plan or API/CLI/workflow simulator spec when applicable.
- Includes demo path, run command, core interactions, mock data notes, and backend simulation boundary in the `UI Demo / 交互 Demo` section.
- Includes an `HTML 展示文件` section. If `wheelwise-report.html` is generated, it is listed as a display layer sourced from Markdown; if not, the report records whether it is recommended or skipped.
- Calls out license, privacy, security, dependency, market, and execution risks where relevant.
- Produces a plan Codex can act on, including visual-brief, demo, Chinese Markdown report generation/update tasks, and HTML display tasks when enabled.
- Keeps `using-wheelwise` responsible for final synthesis.
