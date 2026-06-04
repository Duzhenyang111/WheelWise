# Workflow Modes

All workflows start and end through `using-wheelwise`. It owns route selection, artifact creation, Gate decisions, evidence discipline, pre-review state mapping, and final synthesis.

## Common Artifact Baseline

Every selected route must create:

```text
wheelwise-report-<idea-slug>/
  report.md
```

Use `wheelwise-report/` when no idea slug can be inferred.

`report.md` is the minimum source of truth for every workflow. Other artifacts are produced only when the selected route needs them.

## Mode 1: 快速判断

Use when the user wants a fast product pre-review answer.

Default internal flow:

```text
idea-intake -> Gate0 Evidence Intake -> surface-strategy -> feasibility-review: early-screening -> report.md
```

Minimum `report.md` sections:

- 想法摘要
- 预评审状态
- 核心判断
- 关键假设
- 证据缺口
- 下一步建议

Do not create `index.html`, `prototype.html`, `assets/`, `project-state.md`, or `evidence-board.md` unless the quick judgment pauses at Gate0, requires resumable state, or the user explicitly requests extra artifacts.

## Mode 2: 专项评估

Use when the user asks one focused product decision question.

Possible route intents:

- `Pre-MVP Decision`
- `Build/Buy/Reuse Planner`
- `Idea-to-Validation Board`
- `Codex-ready Product Brief`
- focused market, customer, commercialization, risk, surface, technical, visual, or demo planning

Minimum `report.md` sections:

- 专项问题
- 预评审状态
- 结论
- 决策理由
- 证据分类
- 风险与假设
- 下一步行动

Only generate route-specific extra files when needed:

- Use `evidence-board.md` when multiple evidence sources, contradictions, or current research findings must be preserved.
- Use `project-state.md` when the route needs resumable Gate state or continuity across later WheelWise runs.
- Use `assets/`, `index.html`, or `prototype.html` only when the user asks for visuals, web presentation, or an interactive demo.

## Mode 3: 完整预评审

Use when the user asks for a finished WheelWise pre-review package, complete evaluation, stakeholder-ready report, web visualization, or interactive prototype.

Default full package:

```text
wheelwise-report-<idea-slug>/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
```

Full workflow:

```text
Phase 0 Intake:
idea-intake -> Gate0 Evidence Intake -> surface-strategy -> feasibility-review: early-screening

Gate1:
stop if impossible/not recommended; otherwise continue automatically

Phase 1 Discovery:
market-research -> customer-discovery -> reuse-evaluator -> optional technical spike -> evidence-board

Phase 2 Synthesis:
product-strategy -> commercialization -> risk-review -> feasibility-review: full-review -> review-board synthesis -> comparable scorecard

Gate2:
Go maps to 可进入原型验证 or 可进入最小可行产品实验 and continues automatically.
Pivot / Need More Evidence / Kill / Park map to 建议转向后再评审 / 需要补充关键证据 / 建议放弃 / 建议暂缓 or 仅作为参考 and ask user when needed.

Phase 3 Delivery:
technical-planning -> visual-brief -> ui-demo or simulator -> report-visualization -> execution-plan

Final package:
report.md -> index.html -> prototype.html -> assets/
```

Read `final-output-contract.md` and `../../shared/references/output-quality-bar.md` only for this mode or when the user explicitly asks for the same artifact depth.

## Gate-Driven Workflow

### Gate0

Gate0 is a single Evidence Intake step. It returns `Ready`, `Need Basic Input`, or `Field Data Required`.

Ask only when basic routing information is insufficient. Allowed Gate0 questions:

- 面向谁？
- 你想先验证，还是直接做最小可行产品？
- 时间、预算或技术栈限制是什么？

When first-hand data is required, return a dynamic checklist based on the detected idea-type combination and pause with a resumable `Field Data Required` state. If a report folder already exists or must be created for this run, write the pause into `report.md`; create `project-state.md` only when the pause must be resumed later.

### Gate1

Uses `feasibility-review: early-screening`.

- Cannot continue / not recommended now: write the stop reason into `report.md` and end.
- Can continue: continue according to the selected route.

### Gate2

Uses `feasibility-review: full-review`.

- `Go`: map to `可进入原型验证` or `可进入最小可行产品实验`; continue automatically only when the selected route requires Delivery.
- `Pivot`: map to `建议转向后再评审`; ask whether to pivot to the recommended direction.
- `Need More Evidence`: map to `需要补充关键证据`; ask whether to run the recommended research or validation.
- `Kill`: map to `建议放弃`; ask only if the user wants an alternative direction or stop.
- `Park`: map to `建议暂缓` or `仅作为参考`; ask whether to park or change constraints.

## Pre-Review States

Use exactly one:

- 可进入原型验证
- 可进入最小可行产品实验
- 需要补充关键证据
- 建议转向后再评审
- 建议暂缓
- 建议放弃
- 仅作为参考

Every `report.md` must include the selected state, confidence, supporting evidence or assumptions, opposing evidence or risks, evidence gaps, and next action.

## Full Report Rules

Full reports must be Chinese pre-review packages, not dumps of internal skill sections. They must include review-board viewpoints, facts/assumptions/inferences/evidence gaps, options considered and rejected, decision dependencies, validation experiments, comparable scorecard, visual explanation, prototype or simulator, and state-appropriate execution or validation plan.

`index.html` is a report visualization layer sourced from `report.md`. `prototype.html` is a separate product-surface simulation or validation tool.
