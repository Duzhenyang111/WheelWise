# Workflow Modes

## V4.5 Controller Mode

All workflows start and end through `using-wheelwise`. It owns routing, `project-state.md`, Gate decisions, evidence arbitration, pre-review state mapping, review-board synthesis, self-checks, and final pre-review package synthesis.

## Short Workflow

Use when the user asks one narrow question.

Steps:

1. Read or create `project-state.md`.
2. Run only the necessary skill.
3. Update state with decision, assumptions, and next action.
4. Return the decision without producing a full final report unless requested.

Examples:

- "Should auth be built or bought?"
- "Is this better as a browser extension or web app?"
- "Can I fork this open-source repo?"

## V4.5 Full Workflow

Use for complete product ideas or when the user asks for a full WheelWise AI product pre-review package.

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
Go maps to 可进入原型验证 or 可进入最小可行产品实验 and continues automatically; Pivot / Need More Evidence / Kill / Park map to 建议转向后再评审 / 需要补充关键证据 / 建议放弃 / 建议暂缓 or 仅作为参考 and ask user when needed

Phase 3 Delivery:
technical-planning -> visual-brief -> ui-demo or simulator -> report-visualization -> execution-plan

Final report:
report.md -> index.html -> prototype.html -> assets/ as one Chinese pre-review package
```

## V4.5 Pre-Review States

Use exactly:

- 可进入原型验证
- 可进入最小可行产品实验
- 需要补充关键证据
- 建议转向后再评审
- 建议暂缓
- 建议放弃
- 仅作为参考

Each full workflow must record the state, next-stage recommendation, confidence, supporting evidence, opposing evidence, evidence gaps, decision dependencies, options rejected, and validation priority.

## Research-Heavy Workflow

Use when competitor facts, pricing, user evidence, channel rules, platform policy, license status, repository health, market trends, or vendor capabilities materially change the answer.

Required:

- Use `../../shared/references/web-research-standard.md`.
- Write evidence into `evidence-board.md`.
- Label key claims as `事实`, `假设`, `推断`, or `证据缺口`.
- Update evidence gaps and contradictions in `project-state.md`.
- Use `parallel-research` only when independent research briefs are useful.

## Gate-Driven Workflow

### Gate0

Gate0 is a single Evidence Intake step. It returns `Ready`, `Need Basic Input`, or `Field Data Required`.

Ask only if basic routing information is insufficient. Allowed questions:

- 面向谁？
- 你想先验证，还是直接做最小可行产品？
- 时间、预算或技术栈限制是什么？

When first-hand data is required, return a dynamic checklist based on the detected idea-type combination and pause with a resumable `Field Data Required` state in `project-state.md`.

### Gate1

Uses `feasibility-review: early-screening`.

- Cannot continue / not recommended now: stop and explain.
- Can continue: enter Discovery automatically.

### Gate2

Uses `feasibility-review: full-review`.

- Go: enter Delivery automatically.
- Pivot / Need More Evidence / Kill / Park: ask the user for direction.
- Map Gate2 verdicts into the V4.5 Chinese pre-review state before Delivery or final report synthesis.

## Demo-Ready Workflow

Use when the user needs something presentable to stakeholders or test users.

Steps:

1. Ensure Phase 2 has passed Gate2, has an explicit V4.5 pre-review state, or is explicitly assumption-led.
2. Run `technical-planning`.
3. Run `visual-brief` for dense explanatory assets.
4. Run `ui-demo` for traditional UI surfaces or simulator mode for API/CLI/automation.
5. Run `report-visualization` for the report visualization layer.
6. Ensure `execution-plan` includes `report.md`, `index.html`, `prototype.html`, asset tasks, evidence-gap validation tasks, and state-appropriate next actions.

## Final Report Workflow

Use when the user asks for a finished WheelWise pre-review package or when a full workflow is complete.

Steps:

1. Read `final-output-contract.md`.
2. Read `project-state.md` and `evidence-board.md`.
3. Use `new-product-brief.md` unless the user explicitly wants a shorter report.
4. Create the report folder: `wheelwise-report/` or `wheelwise-report-<idea-slug>/`.
5. Write `report.md` in progressive Chinese pre-review sections, including `预评审结论`, `评审委员会意见`, `决策记录与选项排除`, and `横向比较评分`.
6. Generate `index.html` as the report visualization layer sourced from `report.md`.
7. Generate or specify `prototype.html` as the independent product prototype or simulator.
8. Include visual assets under `assets/`, or Mermaid as the Chinese-labeled last fallback.
9. Include interaction prototype or simulator details.
10. Run final self-check before responding with artifact paths.
