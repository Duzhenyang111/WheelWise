# WheelWise Output Quality Bar

A WheelWise answer is acceptable only when it:

- Produces a single Chinese Markdown report file: `wheelwise-report.md` by default or `wheelwise-report-<idea-slug>.md` when the idea name is available.
- Does not substitute a chat summary for the report file.
- Uses Chinese for report title, section names, table fields, explanations, decision rationales, risks, experiments, and execution-plan prose.
- Makes a clear verdict.
- Names the delivery surface.
- Includes decision rationale for key decisions in Chinese: 决策是什么, 为什么选择它, 为什么不选替代方案, 证据, 假设, 风险, fallback, 信心等级.
- Separates evidence from assumptions.
- Avoids copying external skill content.
- Connects `feasibility-review` to `product-strategy`.
- Gives module-level Build / Buy / Reuse / Fork / Reference decisions.
- Connects `reuse-evaluator` decisions to `technical-planning` without contradictions.
- Includes image-level visual explanation via `visual-brief` for full reports, written into the `视觉说明` section with image prompts or Markdown image references when assets exist.
- Includes an interactive UI demo plan or API/CLI/workflow simulator spec when applicable.
- Includes demo path, run command, core interactions, mock data notes, and backend simulation boundary in the `UI Demo / 交互 Demo` section.
- Calls out license, privacy, security, dependency, market, and execution risks where relevant.
- Produces a plan Codex can act on, including visual-brief, demo, and Chinese Markdown report generation/update tasks.
- Keeps `using-wheelwise` responsible for final synthesis.
