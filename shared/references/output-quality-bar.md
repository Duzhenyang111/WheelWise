# WheelWise Output Quality Bar

A WheelWise answer is acceptable only when it:

- Produces a Chinese report folder: `wheelwise-report/` by default or `wheelwise-report-<idea-slug>/` when the idea name is available.
- Includes `report.md`, `index.html`, `assets/`, and at least one image asset.
- Does not substitute a chat summary for the report folder.
- Uses Chinese for report title, section names, table fields, explanations, decision rationales, risks, experiments, and execution-plan prose.
- Uses Chinese for all visible webpage text, image text, chart labels, alt text, and presentation copy.
- Uses Chinese display terms: 自研, 购买, 复用, 分叉改造, 参考, 网页应用, 软件服务, 最小可行产品, 演示, 模拟数据, 兜底方案, 继续 / 停止条件, 可交给 Codex 执行的计划.
- Reads as a progressive report, not a dump of internal skill sections: opening guide, user/problem, decisions/solution, visual/demo, risks/validation, execution plan, and final action advice.
- Includes `报告说明与阅读导览` with report purpose, applicable stage, core conclusion preview, and reading path.
- Includes `最终建议与下一步行动` with one-sentence judgment, 7-day, 14-day, 30-day actions, and continue/stop conditions.
- Does not use English internal module headings such as `Idea Intake`, `Surface Strategy`, `Reuse Evaluator`, `Technical Planning`, `Risk Review`, `UI Demo Scope`, or `MVP Execution Plan`.
- Makes a clear verdict.
- Names the delivery surface.
- Includes market evidence, user evidence, commercialization assumptions, and a source-evidence summary when current facts materially affect the recommendation.
- Includes decision rationale for key decisions in Chinese: 决策是什么, 为什么选择它, 为什么不选替代方案, 证据, 假设, 风险, 兜底方案, 信心等级.
- Separates evidence from assumptions.
- Uses `shared/references/web-research-standard.md` for current market, customer, pricing, channel, policy, vendor, license, or repository facts; if research is unavailable, marks the evidence gap and lowers confidence.
- Avoids copying external skill content.
- Connects `feasibility-review` to `product-strategy`.
- Gives module-level 自研 / 购买 / 复用 / 分叉改造 / 参考 decisions.
- Connects `reuse-evaluator` decisions to `technical-planning` without contradictions.
- Includes image-level visual explanation via `visual-brief` for full reports, written into the `视觉说明` section with image references under `assets/`, or Mermaid 兜底图表 when image generation is unavailable.
- Includes an interactive demo plan or API/CLI/workflow simulator spec when applicable, expressed in Chinese visible text.
- Includes 演示路径, run command when needed, core interactions, simulated data notes, and backend simulation boundary in the `交互演示` section.
- Includes a `网页展示文件` section. If `index.html` is generated, it is listed as a display layer sourced from `report.md`; if not, the report records whether it is recommended or skipped.
- Calls out license, privacy, security, dependency, market, and execution risks where relevant.
- Produces a plan Codex can act on, including visual-brief, demo, report folder creation/update tasks, source report tasks, webpage display tasks, and asset generation tasks.
- Keeps `using-wheelwise` responsible for final synthesis.
