---
name: using-wheelwise
description: Use when evaluating, shaping, researching, visualizing, demoing, or planning a product idea with WheelWise, especially when the user wants a routed product decision workflow, evidence-based gates, state tracking, market research, customer discovery, commercialization, feasibility, reuse, technical planning, visuals, demos, risks, or final report generation.
---

# 使用 WheelWise

`using-wheelwise` is the only user-facing entry point. In V4 it acts as controller, router, state manager, Gate controller, self-check owner, and final-report synthesizer.

The final artifact remains a Chinese report folder. V4 adds two internal artifacts:

- `project-state.md`: workflow state and cross-skill memory.
- `evidence-board.md`: evidence ledger for market, customer, reuse, technical-spike, and validation findings.

These internal artifacts guide the workflow but do not replace `report.md`.

## Core Responsibilities

1. Own the full workflow and keep `using-wheelwise` as the single main entry point.
2. Before and after each internal skill, read or update `project-state.md`.
3. During Discovery, create or update `evidence-board.md`.
4. Control Gate0, Gate1, and Gate2 according to the interruption rules.
5. Route to internal skills without exposing internal skill sections as final report headings.
6. Keep decisions explainable through evidence, assumptions, risks, and fallback plans.
7. Run final self-check before returning artifact paths.
8. Return only artifact paths after final report generation.
9. Treat user-provided direction as original assumptions and challenge them with supporting and opposing evidence.

## Internal State Files

Use these templates:

- `../../shared/templates/project-state.md`
- `../../shared/templates/evidence-board.md`

Default internal paths inside a report folder:

```text
wheelwise-report-<idea-slug>/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
```

`project-state.md` fields must cover idea summary, current phase, delivery surface, gate status, feasibility verdict, product strategy summary, reuse decisions summary, technical plan summary, commercialization summary, risk summary, visual/demo status, final report status, open questions, assumptions, and last updated by skill.

`evidence-board.md` must include evidence item, source/origin skill, evidence type, affected decision, strength, confidence, original assumption, supports or opposes, direction shift, user confirmation needed, assumption vs evidence, contradiction, evidence gap, and recommended next action.

## Challenge and Direction Calibration

WheelWise must not simply complete the user's idea. Treat the user's stated target user, problem, delivery surface, product wedge, business model, compliance boundary, and technical path as original assumptions until evidence supports them.

During Discovery and Synthesis:

- Actively gather supporting and opposing evidence.
- Record counter-evidence that weakens the original direction.
- Adjust the recommendation when current evidence supports a better direction.
- Explain why the original direction is weak whenever the recommendation changes.

Direction shift levels:

| Shift | Use when | Gate behavior |
| --- | --- | --- |
| None | Evidence supports the original direction | Continue normally |
| Minor | Recommendation narrows scope, wording, priority, or validation order without changing the core direction | Continue, but explain the adjustment in the report |
| Major | Target user, core problem, delivery surface, product wedge, business model, compliance boundary, or technical feasibility path changes materially | Gate2 must return `Pivot` or `Need More Evidence`; ask the user whether to continue with the new direction or keep the original direction |

If a major shift is recommended but not confirmed by the user, do not enter Delivery except for an explicitly assumption-led artifact that marks the shift as unconfirmed.

## V4 Phase Flow

```text
using-wheelwise
-> read/update project-state.md
-> Phase 0 Intake
   -> idea-intake
   -> Gate0 information sufficiency
   -> surface-strategy
   -> feasibility-review: early-screening
-> Gate1 early screen
   -> stop if cannot continue or not recommended now
   -> continue automatically if viable
-> Phase 1 Discovery
   -> market-research
   -> customer-discovery
   -> reuse-evaluator
   -> technical spike when needed
   -> evidence-board
-> Phase 2 Synthesis
   -> product-strategy
   -> commercialization
   -> risk-review
   -> feasibility-review: full-review
-> Gate2 full review
   -> Go continues automatically
   -> Pivot / Need More Evidence / Kill / Park asks user
-> Phase 3 Delivery
   -> technical-planning
   -> visual-brief
   -> ui-demo or simulator mode
   -> report-visualization
   -> execution-plan
-> final-report
   -> report.md + index.html + prototype.html + assets/
```

## Gate Rules

### Gate0: Information Sufficiency

Ask the user only when basic information is insufficient to route the idea.

Allowed Gate0 questions:

1. 面向谁？
2. 你想先验证，还是直接做最小可行产品？
3. 时间、预算或技术栈限制是什么？

If reasonable assumptions can keep the workflow moving, record assumptions in `project-state.md` and continue.

### Gate1: Early Screen

Gate1 uses `feasibility-review: early-screening`.

- If the idea cannot continue or is not recommended now, output the stop reason and end.
- If the idea can continue, do not ask the user; automatically enter Discovery.
- If the only blocker is Gate0 information, ask the allowed Gate0 questions.

### Gate2: Full Review

Gate2 uses `feasibility-review: full-review`.

- `Go`: do not ask the user; automatically enter Delivery.
- `Pivot`: ask whether to pivot to the recommended direction.
- `Need More Evidence`: ask whether to run the recommended research or validation.
- `Kill`: ask only if the user wants an alternative direction or stop.
- `Park`: ask whether to park or change constraints.
- Unconfirmed `Major` direction shift: do not use `Go`; ask whether to follow the new evidence-led direction or keep the original direction.

Normal `Go` flow must not be interrupted.

## Phase Details

### Phase 0 Intake

Run:

1. `idea-intake`
2. Gate0 check
3. `surface-strategy`
4. `feasibility-review` in `early-screening` mode

Update `project-state.md` after each step.

### Phase 1 Discovery

Run:

1. `market-research`
2. `customer-discovery`
3. `reuse-evaluator`
4. Optional technical spike when technical feasibility, API limits, integration risk, license risk, or architecture uncertainty could change the verdict
5. `evidence-board`

Write market, customer, reuse, and spike findings into `evidence-board.md`. Summarize evidence coverage, contradictions, and gaps in `project-state.md`.

Discovery must include both support and counter-evidence for the user's original assumptions. If evidence points to a different target user, problem, surface, wedge, business model, compliance boundary, or technical path, mark the shift level in `evidence-board.md`.

### Phase 2 Synthesis

Run:

1. `product-strategy`
2. `commercialization`
3. `risk-review`
4. `feasibility-review` in `full-review` mode

Gate2 decides whether to continue into Delivery automatically or ask the user.

Synthesis must explicitly compare the original direction with the evidence-led recommendation. Major shifts must be routed through Gate2 user confirmation.

### Phase 3 Delivery

Run:

1. `technical-planning`
2. `visual-brief`
3. `ui-demo` for UI products or simulator mode for API, CLI, automation, and developer tools
4. `report-visualization` for `index.html`
5. `execution-plan`

If the product has no traditional UI, do not skip demonstration. Use API playground, CLI simulator, workflow simulator, request explorer, terminal simulator, or automation run simulator.

### Final Report

Generate the Chinese report folder:

```text
report.md
index.html
prototype.html
assets/
```

For user-facing products, also create or specify an interactive prototype such as `prototype.html`.

`report.md` is the source of truth. `index.html` is the report visualization layer: it must convert the report's decisions, evidence, workflows, risks, validation, commercialization, and execution plan into visual modules. `prototype.html` is the separate product-surface simulation owned by `ui-demo`.

`project-state.md` and `evidence-board.md` may live in the folder as internal artifacts, but they are not final report substitutes.

## Output Rules

- Visible text in `report.md`, `index.html`, prototype pages, image text, chart labels, alt text, table fields, explanations, risks, experiments, and execution-plan prose must be Chinese.
- Technical commands, file paths, package names, API names, code identifiers, and technology names may remain English only when they are literal technical identifiers.
- Do not answer with a structured chat summary when final artifacts are requested.
- Do not use internal skill names as final report headings.
- Keep implementation surface visible throughout: website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, automation tool, or hybrid.
- Do not invent current market, customer, pricing, channel, policy, license, vendor, or repository facts. Browse when current facts matter or mark the evidence gap.
- Do not uncritically restate the user's idea as the recommendation. If evidence weakens the user's direction, explain the weakness and adjust the recommendation.
- Use `risk-review` consistently for risk work.
- Use `parallel-research` only for complex research or independent review. Final judgment belongs to `using-wheelwise`.

## Final Self-Check

Before final response, confirm:

- `project-state.md` is complete enough for the phase reached.
- `evidence-board.md` has evidence items or explicit evidence gaps.
- Gate status is consistent with feasibility verdict and phase.
- Key decisions include rationale: decision, why chosen, why alternatives lose, evidence, assumptions, risks, fallback, confidence.
- `visual-brief` produced an image, image prompt, or Mermaid 兜底图表.
- `ui-demo` or simulator output exists for the delivery surface.
- `report-visualization` produced or specified `index.html` as a complete visual explanation layer.
- `report.md`, `index.html`, and `assets/` satisfy the final-output contract.
- `index.html` covers the complete report through visual modules, not a short summary or plain Markdown conversion.
- User-facing products have `prototype.html` or a concrete prototype task, and the prototype is not used as a report display substitute.
- Visible generated text is Chinese.
- Market, customer, reuse, and commercialization evidence is separated from assumptions.
- Original assumptions, supporting evidence, opposing evidence, direction shift level, and user confirmation status are recorded when the recommendation differs from the user's direction.

Final chat response should list only:

```text
报告文件夹：
源报告：
网页展示：
交互原型：
```

If Gate1 stops the workflow, return the stop reason and the current `project-state.md` path. If Gate2 needs user input, ask only the Gate2-specific decision question.
