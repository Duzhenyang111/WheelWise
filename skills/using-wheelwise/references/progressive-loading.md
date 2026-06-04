# Progressive Loading

WheelWise uses progressive prompting to reduce token use and avoid over-executing the full workflow.

## Loading Order

1. Start with `using-wheelwise/SKILL.md`.
2. If the route is unclear, read `routing-map.md` and ask the fixed three-choice route confirmation question.
3. After selecting a route, read only the references required for that route.
4. Load internal skill files only when that skill is about to be used.
5. Load full package contracts only for `完整预评审` or explicit artifact requests.

## Route-Specific Loading

### 快速判断

Load:

- `routing-map.md` when route detection is needed.
- `workflow-modes.md` for the quick mode contract.
- `../../shared/references/idea-applicability-standard.md` for Gate0.

Usually use:

- `idea-intake`
- `surface-strategy`
- `feasibility-review`

Do not load:

- `final-output-contract.md`
- `../../shared/references/output-quality-bar.md`
- `report-visualization`
- `ui-demo`
- `visual-brief`

### 专项评估

Load:

- `routing-map.md`
- `workflow-modes.md`
- the specific internal skill needed for the selected route intent
- `../../shared/references/decision-rationale-standard.md` for important decisions

Conditionally load:

- `../../shared/references/web-research-standard.md` when current facts matter.
- `../../shared/references/idea-applicability-standard.md` when Gate0, regulated, local/offline, physical, platform, B2B, content/community, supply-chain, or service-heavy applicability matters.
- `evidence-board` only when multiple sources, contradictions, current research, or reusable state must be preserved.
- `project-state.md` template only when resumable state or later continuation is needed.

Do not load full package contracts unless the user asks for complete artifacts.

### 完整预评审

Load:

- `routing-map.md`
- `workflow-modes.md`
- `final-output-contract.md`
- `../../shared/references/output-quality-bar.md`
- `../../shared/references/idea-applicability-standard.md`
- `../../shared/references/web-research-standard.md` when current facts matter
- all internal skill files as they are used in the full workflow

Generate the complete package by default.

## Artifact Loading Discipline

- `report.md` is required for all routes.
- `index.html` rules are loaded only when generating report visualization.
- `prototype.html` rules are loaded only when generating interactive demo, simulator, or validation tool.
- `assets/` rules are loaded only when creating visual assets.
- `project-state.md` and `evidence-board.md` templates are loaded only when those files are generated or updated.

## Evidence Discipline

Even in short routes, classify important claims as `事实`, `假设`, `推断`, or `证据缺口`. If a conclusion needs current market, pricing, platform, license, vendor, or repository facts and they are not checked, mark that point as `证据缺口` and lower confidence.
