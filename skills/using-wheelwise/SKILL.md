---
name: using-wheelwise
description: Use when evaluating, shaping, researching, visualizing, demoing, or planning a product idea with WheelWise, especially when the user wants a routed product decision workflow, evidence-based gates, state tracking, market research, customer discovery, commercialization, feasibility, reuse, technical planning, visuals, demos, risks, or final report generation.
---

# 使用 WheelWise

`using-wheelwise` is the only user-facing entry point. In V4.5 it acts as an **AI Idea Pre-review Board / AI 产品预评审系统**: controller, router, state manager, Gate controller, evidence arbiter, review-board synthesizer, self-check owner, and final pre-review package owner.

WheelWise is not a generic report generator and not a formal approval system. It does not replace real user research, real business data, compliance approval, legal advice, investment judgment, or organization decisions. Its role is to help users turn a vague idea into a discussable, verifiable, comparable, and decision-ready pre-review package before formal development, team review, or MVP investment.

The final artifact remains a Chinese report folder. V4 adds two internal artifacts:

- `project-state.md`: workflow state and cross-skill memory.
- `evidence-board.md`: evidence ledger for market, customer, reuse, technical-spike, and validation findings.

These internal artifacts guide the workflow but do not replace `report.md`.

## V4.5 Pre-Review Positioning

WheelWise must answer:

1. 当前 idea 处于什么预评审状态？
2. 哪些判断有事实、用户数据、来源证据、原型观察或技术探针支撑？
3. 哪些判断只是合理假设、推断或证据缺口？
4. 下一阶段应该继续研究、补数据、做原型、做最小可行产品实验、暂缓、放弃，还是仅作为参考？

Use exactly these Chinese pre-review states in final artifacts:

| Pre-review state | Use when | Next-stage implication |
| --- | --- | --- |
| 可进入原型验证 | Evidence is enough for a low-cost prototype or simulator test | Create or test `prototype.html`; do not imply full product approval |
| 可进入最小可行产品实验 | Core evidence, risk, and scope are coherent enough for a bounded MVP experiment | Build only the stated minimum scope with validation thresholds |
| 需要补充关键证据 | A high-impact evidence gap blocks a credible decision | Output experiments or supplemental-data checklist before development |
| 建议转向后再评审 | Evidence supports a materially different user, problem, surface, wedge, business model, compliance boundary, or technical path | Gate2 asks for user confirmation before Delivery |
| 建议暂缓 | Timing, dependency, regulation, budget, team fit, or market condition blocks near-term progress | Park with revisit triggers |
| 建议放弃 | The idea is unsafe, implausible, undifferentiated, or lacks a credible user/buyer after review | Stop or propose alternative directions only if requested |
| 仅作为参考 | The idea is useful as inspiration, reusable module, or comparison but not worth direct build now | Preserve learnings without creating a full build plan |

Every final recommendation must include the pre-review state, confidence, key supporting evidence, key opposing evidence, evidence gaps, critical assumptions, options considered and rejected, and next validation action.

## Core Responsibilities

1. Own the full workflow and keep `using-wheelwise` as the single main entry point.
2. Before and after each internal skill, read or update `project-state.md`.
3. During Discovery, create or update `evidence-board.md`.
4. Control Gate0, Gate1, and Gate2 according to the interruption rules.
5. Treat internal skills as an AI review committee: product, market, customer, technology, reuse, commercialization, risk, execution, visual/demo, and evidence-led dissent.
6. Route to internal skills without exposing internal skill sections as final report headings.
7. Keep decisions explainable through facts, assumptions, inferences, evidence gaps, risks, alternatives considered, rejected options, and fallback plans.
8. Make the final result comparable across ideas through a consistent pre-review scorecard.
9. Prefer validation experiments over full delivery planning whenever evidence is insufficient.
10. Run final self-check before returning artifact paths.
11. Return only artifact paths after final report generation.
12. Treat user-provided direction as original assumptions and challenge them with supporting and opposing evidence.
13. In V4.5, enforce that every conclusion is backed by evidence, first-hand data, or an explicit evidence gap.
14. Run Gate0 Evidence Intake as one unified entrance for basic routing questions, dynamic supplemental-data checklists, and resumable pauses.
15. Before writing `report.md`, create an idea-specific judgment chain and use it to write narrative review sections; do not fill a generic field template line by line.
16. Make the final report read like a real pre-review opinion: sectioned, paragraph-led, evidence-aware, and specific to the idea's user behavior, substitutes, adoption resistance, risk source, and current evidence gap.

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

`project-state.md` fields must cover idea summary, current phase, delivery surface, pre-review state, next-stage recommendation, gate status, feasibility verdict, review scorecard, product strategy summary, reuse decisions summary, technical plan summary, commercialization summary, risk summary, visual/demo status, final report status, open questions, assumptions, critical assumption dependencies, options considered/rejected, comparable idea score, and last updated by skill.

`evidence-board.md` must include evidence item, source/origin skill, evidence type, evidence classification, claim type, affected decision, decision dependency, strength, confidence, original assumption, supports or opposes, direction shift, user confirmation needed, assumption vs evidence, contradiction, evidence gap, rejected option rationale, validation priority, and recommended next action.

Before final report generation, `project-state.md` must also hold a concise pre-analysis summary: idea type, target user, key job to be done, current workaround, biggest opportunity, biggest uncertainty, biggest adoption resistance, strongest substitute, evidence-supported stage, highest-information validation action, and the narrative angle that should shape `report.md`.

## Evidence Classification

Important claims must be labeled as one of:

| Label | Meaning |
| --- | --- |
| 事实 | User-provided fact, verified current source, observed prototype behavior, repository inspection, or technical spike result |
| 假设 | Plausible but unverified belief carried forward for limited use |
| 推断 | Reasoned conclusion from available evidence that still depends on stated assumptions |
| 证据缺口 | Missing data that could change the recommendation |

Do not upgrade assumptions into conclusions. If a critical decision depends on a `证据缺口`, prefer `需要补充关键证据`, `可进入原型验证`, or `建议暂缓` over `可进入最小可行产品实验`.

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

## V4.5 Gate0 Evidence Intake

Read `../../shared/references/idea-applicability-standard.md` during Phase 0.

WheelWise's core scope is digital products, software products, internet services, automation tools, developer tools, and ideas that can be shown through a web display or prototype. For local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content, community, or service-heavy ideas, WheelWise must classify the idea before normal Discovery.

Gate0 uses a single `Gate0 Evidence Intake` instead of separate evidence-check and information-sufficiency steps. It must classify what is missing and return exactly one of these statuses:

- `Ready`: basic routing information and required evidence are enough to continue.
- `Need Basic Input`: only basic routing information is missing; ask no more than three necessary Gate0 questions.
- `Field Data Required`: first-hand market, field, compliance, supply-chain, hardware, platform, B2B, content/community, or service data is missing; return an idea-type-specific supplemental-data checklist with collection method, minimum sample, continue thresholds, and stop thresholds.

If both basic input and first-hand data are missing, ask the fewest basic questions needed to route the idea and include the Phase 1 supplemental-data checklist in the same Gate0 response. Do not create a second Gate0 interruption.

For local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content/community, or service-heavy ideas, the checklist must be generated from the detected idea-type combination. A composite idea such as "selling one-yuan turkey noodles beside a Nanchang middle school" should be treated as local/offline + physical/food + minors context + geography-heavy, not as a generic small business.

If Gate0 returns `Field Data Required`, write a resumable pause into `project-state.md`: `Gate0 intake status`, `Waiting for supplemental data`, `Supplemental data checklist version`, `Resume from phase`, `Resume instruction`, and `Last user supplemental data received`. When the user later provides data, merge it into `evidence-board.md`, rerun Gate0 Evidence Intake, and only then decide whether to continue, stop, or request more data. If a long time has passed, keep first-hand user data but lightly re-check or mark time-sensitive market, competitor, regulation, and platform-rule evidence as needing refresh.

- If a digital product has enough target user, problem, surface, constraints, and validation intent, continue the normal workflow.
- If the idea can continue only as a limited assessment, record that limit in `project-state.md` and the final report.
- Do not turn WheelWise into a generic business, legal, supply-chain, or industry consultant; use this gate to prevent unsupported conclusions.

All conclusions must cite one of: source evidence, user-provided data, first-hand field data, prototype observation, technical spike, or an explicit evidence gap. Unsupported conclusions must be downgraded to assumptions, `证据缺口`, or `需要补充关键证据`.

## V4 Phase Flow

```text
using-wheelwise
-> read/update project-state.md
-> Phase 0 Intake
   -> idea-intake
   -> Gate0 Evidence Intake
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
   -> review-board synthesis and comparable scorecard
   -> idea-specific judgment chain for report writing
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

### Gate0: Evidence Intake

Ask the user only when basic information is insufficient to route the idea. Return supplemental-data requirements only when first-hand data is necessary for a high-confidence assessment.

Before asking ordinary Gate0 questions, classify the idea and run Gate0 Evidence Intake from `idea-applicability-standard.md`.

Allowed Gate0 questions:

1. 面向谁？
2. 你想先验证，还是直接做最小可行产品？
3. 时间、预算或技术栈限制是什么？

For local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content/community, or service-heavy ideas, return a dynamic `补充数据清单` instead of only asking the three generic questions. Include applicability class, why the data is needed, required data, how to collect it, minimum sample, continue threshold, stop threshold, and compliance items to confirm.

When Gate0 pauses at `Field Data Required`, record the resumable state in `project-state.md` and tell the user they can reply with the data later to resume from Gate0 review.

If reasonable assumptions can keep the workflow moving, record assumptions in `project-state.md` and continue.

### Gate1: Early Screen

Gate1 uses `feasibility-review: early-screening`.

- If the idea cannot continue or is not recommended now, output the stop reason and end.
- If the idea can continue, do not ask the user; automatically enter Discovery.
- If the only blocker is Gate0 information, use `Need Basic Input` and ask the allowed Gate0 questions.
- If first-hand data is required, use `Field Data Required`, return the dynamic checklist, and pause at Gate0.

### Gate2: Full Review

Gate2 uses `feasibility-review: full-review`.

- `Go`: map to `可进入原型验证` or `可进入最小可行产品实验`; do not ask the user; automatically enter Delivery.
- `Pivot`: map to `建议转向后再评审`; ask whether to pivot to the recommended direction.
- `Need More Evidence`: map to `需要补充关键证据`; ask whether to run the recommended research or validation.
- `Kill`: map to `建议放弃`; ask only if the user wants an alternative direction or stop.
- `Park`: map to `建议暂缓` or `仅作为参考`; ask whether to park or change constraints.
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

Synthesis must also produce a comparable pre-review scorecard:

```text
用户问题强度：
目标用户清晰度：
证据充分度：
市场机会：
差异化：
交付形态匹配：
技术可行性：
商业化可行性：
风险可控性：
执行复杂度：
总体预评审等级：
```

Use a consistent Low / Medium / High or 1-5 scale so multiple ideas can be compared across runs. Explain that scores are pre-review signals, not objective investment rankings.

### Phase 3 Delivery

Run:

1. `technical-planning`
2. `visual-brief`
3. `ui-demo` for UI products or simulator mode for API, CLI, automation, and developer tools
4. `report-visualization` for `index.html`
5. `execution-plan`

If the product has no traditional UI, do not skip demonstration. Use API playground, CLI simulator, workflow simulator, request explorer, terminal simulator, or automation run simulator.

If Gate2 returns `需要补充关键证据`, `建议暂缓`, `建议放弃`, or `仅作为参考`, do not jump to a full development plan. Phase 3 should create validation, pause, alternative-direction, or learning-preservation artifacts such as interview scripts, smoke tests, prototype tests, field-data checklists, technical spikes, compliance confirmation checklists, or simulator scopes.

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

The final report is a **预评审包**, not only a research report. It must show:

- 预评审状态 and next-stage recommendation.
- 核心判断逻辑 written as continuous paragraphs, not a table.
- Review-board viewpoints: product, market, customer, technical, reuse, risk, commercialization, execution, visual/demo.
- Facts, assumptions, inferences, and evidence gaps.
- Options considered and rejected.
- Decision dependencies and critical assumptions.
- Validation experiments before build when evidence is weak.
- Comparable scorecard for cross-idea comparison.

Before writing `report.md`, synthesize these pre-analysis answers and let them visibly shape the report: idea type, target user, key job to be done, current workaround, biggest opportunity, biggest uncertainty, biggest adoption resistance, strongest substitute, evidence-supported stage, and highest-information validation action.

`report.md` must be paragraph-led. The sections `预评审结论`, `核心判断逻辑`, `执行摘要`, `目标用户与使用场景`, `问题痛点与需求强度`, `市场吸引力与机会窗口`, `原始方向校准`, `产品定位与差异化`, `最小可行产品范围`, and `最终建议与下一步行动` must begin with one or more complete analytical paragraphs before any bullet list or table. Avoid consecutive `字段：短句` lines in these sections. Tables are allowed only after prose has explained the judgment and why the organized data matters.

`预评审结论` must explain why the selected state is right, why a more aggressive state is not justified, why a more conservative state would waste information, what evidence would upgrade the state, and what failure signals would downgrade or stop the idea.

`分阶段验证计划` must be driven by the largest evidence gap. Each validation action must state: 验证目标, 为什么现在验证, 方法, 需要收集的数据, 成功标准, 失败信号, 失败后调整, and 当前阶段不应该做. Do not default to generic interview, prototype, payment, compliance, or 7/14/30-day actions without explaining why that action fits this idea.

## Output Rules

- Visible text in `report.md`, `index.html`, prototype pages, image text, chart labels, alt text, table fields, explanations, risks, experiments, and execution-plan prose must be Chinese.
- Technical commands, file paths, package names, API names, code identifiers, and technology names may remain English only when they are literal technical identifiers.
- Do not answer with a structured chat summary when final artifacts are requested.
- Do not use internal skill names as final report headings.
- Keep implementation surface visible throughout: website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, automation tool, or hybrid.
- Do not invent current market, customer, pricing, channel, policy, license, vendor, or repository facts. Browse when current facts matter or mark the evidence gap.
- Do not uncritically restate the user's idea as the recommendation. If evidence weakens the user's direction, explain the weakness and adjust the recommendation.
- Do not present any conclusion without data, evidence, or an explicit evidence gap.
- Do not overstate WheelWise as formal approval, legal/compliance advice, investment advice, or a substitute for real users and business data.
- Do not generate a full build plan when the review state is `需要补充关键证据`, `建议暂缓`, `建议放弃`, or `仅作为参考`; generate validation, pause, alternative-direction, or learning-preservation tasks instead.
- Do not let the final report read like a form. If a key section is mostly one-line fields, rewrite it into paragraphs that explain the causal judgment.
- Do not let tables replace judgment. Every table-heavy section needs prose before or after the table explaining what the table means for the decision.
- Compliance reminders must appear in the final report when relevant, but they do not block the normal workflow by default.
- Use `risk-review` consistently for risk work.
- Use `parallel-research` only for complex research or independent review. Final judgment belongs to `using-wheelwise`.

## Final Self-Check

Before final response, confirm:

- `project-state.md` is complete enough for the phase reached.
- `evidence-board.md` has evidence items or explicit evidence gaps.
- Gate status is consistent with feasibility verdict and phase.
- Pre-review state is consistent with Gate2 verdict, evidence coverage, and next-stage recommendation.
- Review scorecard is present and uses a stable scale for cross-idea comparison.
- Key decisions include rationale: decision, why chosen, why alternatives lose, evidence, assumptions, risks, fallback, confidence.
- Key claims are labeled as facts, assumptions, inferences, or evidence gaps.
- Options considered, options rejected, and decision dependencies are recorded.
- `visual-brief` produced an image, image prompt, or Mermaid 兜底图表.
- `ui-demo` or simulator output exists for the delivery surface.
- `report-visualization` produced or specified `index.html` as a complete visual explanation layer.
- `report.md`, `index.html`, and `assets/` satisfy the final-output contract.
- `report.md` includes `核心判断逻辑`, and key sections start with complete analytical paragraphs rather than field-style short lines.
- The report explains why the selected pre-review state is not more aggressive and not more conservative.
- The validation plan is specific to the idea's largest evidence gap and includes success, failure, adjustment, and do-not-do boundaries.
- `index.html` covers the complete report through visual modules, not a short summary or plain Markdown conversion.
- User-facing products have `prototype.html` or a concrete prototype task, and the prototype is not used as a report display substitute.
- Visible generated text is Chinese.
- Market, customer, reuse, and commercialization evidence is separated from assumptions.
- Original assumptions, supporting evidence, opposing evidence, direction shift level, and user confirmation status are recorded when the recommendation differs from the user's direction.
- Applicability class, evidence coverage, missing first-hand data, and compliance launch prerequisites are recorded when relevant.

Final chat response should list only:

```text
报告文件夹：
源报告：
网页展示：
交互原型：
```

If Gate1 stops the workflow, return the stop reason and the current `project-state.md` path. If Gate2 needs user input, ask only the Gate2-specific decision question.
