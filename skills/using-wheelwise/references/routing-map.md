# WheelWise Routing Map

WheelWise is one integrated AI product pre-review skill. The five positioning ideas are internal route intents, not separate user-facing skills. Every route returns to `using-wheelwise` for synthesis, evidence discipline, pre-review state mapping, and artifact creation.

## Route Depth

| Depth | Use when | Minimum artifact |
| --- | --- | --- |
| `快速判断` | The user wants to know whether an idea is worth continuing, or asks a vague "帮我看看 / is this good" question | `wheelwise-report-<idea-slug>/report.md` |
| `专项评估` | The user asks one focused question: MVP scope, Build/Buy/Reuse, validation, technical route, commercialization, risk, or Codex execution plan | `wheelwise-report-<idea-slug>/report.md` |
| `完整预评审` | The user asks for complete evaluation, pre-review package, report, web visualization, demo, prototype, or stakeholder-ready delivery | Complete package |

If the requested depth is unclear, ask the fixed three-choice route confirmation question from `../SKILL.md`.

## Internal Route Intents

| Route intent | Default depth | Trigger examples | Internal skills |
| --- | --- | --- | --- |
| `Product Gatekeeper` | `快速判断` | "值不值得做", "帮我看看这个 idea", "is this good?", "should I pursue this?" | `idea-intake` -> Gate0 -> `surface-strategy` -> `feasibility-review: early-screening` |
| `Pre-MVP Decision` | `专项评估` | "MVP 范围", "先做什么", "最小可行产品", "产品策略" | Gate0 as needed -> `surface-strategy` -> `customer-discovery` as needed -> `product-strategy` -> `feasibility-review` as needed |
| `Build/Buy/Reuse Planner` | `专项评估` | "自研还是购买", "复用", "开源替代", "fork", "starter kit", "模块怎么做" | `reuse-evaluator` -> `risk-review`; add `market-research` / `parallel-research` when current vendor, license, repository, or pricing evidence matters |
| `Idea-to-Validation Board` | `专项评估` | "怎么验证", "先做实验", "访谈", "smoke test", "成功/失败标准" | `idea-intake` -> Gate0 -> `customer-discovery` -> `feasibility-review` as needed -> `execution-plan` in validation mode |
| `Codex-ready Product Brief` | `专项评估` | "交给 Codex 执行", "开发计划", "任务拆解", "验收标准" | Ensure enough state/evidence -> `technical-planning` as needed -> `execution-plan` |
| `Full Pre-review Package` | `完整预评审` | "完整评估", "预评审包", "生成报告", "网页展示", "交互原型", "index.html", "prototype.html" | Full workflow from `workflow-modes.md` |

## Request-To-Route Hints

| User request | Route |
| --- | --- |
| Raw idea, vague concept, "is this good?" | `Product Gatekeeper` |
| "Help me plan/build this idea" without asking for full artifacts | Usually `Pre-MVP Decision` or `Codex-ready Product Brief`; ask the route confirmation question if depth is unclear |
| "Which form should this take?" | `Pre-MVP Decision` focused on delivery surface |
| "Research this market" or "Who are the competitors?" | `专项评估`; `market-research` -> optional `evidence-board` |
| "Who is the customer?" or "How should I validate users?" | `Idea-to-Validation Board` |
| "How should this make money?" or "What pricing/GTM should I use?" | `专项评估`; `commercialization`, with research when current pricing/channel facts matter |
| "Should I build this myself?" | `Build/Buy/Reuse Planner` |
| "Find existing tools/open-source alternatives" | `Build/Buy/Reuse Planner` |
| "Define MVP or product strategy" | `Pre-MVP Decision` |
| "Pick stack or architecture" | `专项评估`; `reuse-evaluator` -> `technical-planning` -> `risk-review` |
| "Make this presentable" | `完整预评审` when report/web/prototype is needed; otherwise `专项评估` |
| "Create a clickable demo" | `完整预评审` if demo artifact is requested; otherwise `专项评估` demo plan |
| "Turn this into Codex tasks" | `Codex-ready Product Brief` |
| "Review risks" | `专项评估`; `risk-review` |

## Artifact Rules

- Every route creates `wheelwise-report-<idea-slug>/report.md`, or `wheelwise-report/report.md` when no slug can be inferred.
- `快速判断` and `专项评估` do not create `index.html`, `prototype.html`, or `assets/` unless explicitly requested or needed by the chosen route.
- `project-state.md` and `evidence-board.md` are optional for `快速判断` and `专项评估`; create them only when state continuity, Gate pauses, Discovery evidence, or full synthesis requires them.
- `完整预评审` creates `project-state.md`, `evidence-board.md`, `report.md`, `index.html`, `prototype.html`, and `assets/`.
- If the pre-review state is `需要补充关键证据`, `建议转向后再评审`, `建议暂缓`, `建议放弃`, or `仅作为参考`, route planning toward validation, pivot, pause, stop, or learning-preservation tasks instead of full development tasks.

## Research Rule

Use `../../shared/references/web-research-standard.md` whenever current market, user, pricing, channel, policy, license, vendor, repository, or platform facts materially affect the answer. If current research is unavailable, mark the item as `证据缺口` and lower confidence.
