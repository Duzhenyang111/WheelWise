---
name: technical-planning
description: Use when WheelWise must turn delivery surface, product strategy, and build/buy/reuse/fork/reference decisions into a recommended stack, architecture, data model outline, integrations, deployment path, and technical risks.
---

# Technical Planning

Connect `reuse-evaluator` to `execution-plan`. The technical plan must honor the module strategy and must not contradict Build / Buy / Reuse / Fork / Reference decisions.

## Inputs

- Delivery surface from `surface-strategy`.
- Product strategy and MVP workflow from `product-strategy`.
- Module decisions from `reuse-evaluator`.
- Known risks from `risk-review` when available.

## Process

1. Restate the delivery surface and MVP workflow.
2. Map each module decision to an implementation path.
3. Recommend a stack that fits the surface and reuse decisions.
4. Outline frontend design, backend design, architecture, data model, integrations, deployment, and observability.
5. Explain the data flow from user action to backend processing to visible result.
6. Call out surface-specific constraints such as mobile store review, browser permissions, API uptime, CLI packaging, or automation retries.
7. Check whether technical feasibility, integration, data access, compliance, or platform constraints weaken the user's original technical path.
8. Apply `../../shared/references/decision-rationale-standard.md` to stack and architecture choices.

## Conflict Check

- If `reuse-evaluator` says Buy auth, do not plan custom auth as the default.
- If `reuse-evaluator` says Reference a repo, do not plan to fork or import it.
- If `reuse-evaluator` says Build a differentiating module, keep that module in the task plan.
- If the selected surface is API/CLI/no traditional UI, plan a playground, terminal simulator, request explorer, or workflow simulator for demo purposes.

## V4 State Integration

- Read `project-state.md` and `evidence-board.md` before planning.
- If a technical spike was marked as needed, either incorporate its finding or keep it as an explicit evidence gap.
- Update `project-state.md` with technical plan summary, technical spike status, integration constraints, and last updated by skill.
- If technical planning changes the delivery surface, compliance boundary, core integration path, or feasibility path materially, return control to Gate2 unless the user already confirmed the shift.
- Do not enter Delivery planning unless Gate2 is `Go`, assumption-led by explicit user request, or the user confirmed a non-Go Gate2 path.

## Output Shape

```text
Recommended stack:
Frontend design:
Backend design:
High-level architecture:
Data model outline:
Data flow:
API and integration boundaries:
Integrations:
Deployment path:
Surface-specific constraints:
Technical risks:
Reuse alignment notes:
Original technical assumptions:
Supporting evidence:
Opposing evidence:
Why original technical path may be weak:
Direction shift:
User confirmation needed:

Decision rationale:
Decision:
Original assumption:
Why chosen:
Why alternatives lose:
Supporting evidence:
Opposing evidence:
Why adjust:
Direction shift:
Evidence:
Assumptions:
Risks:
Fallback:
Confidence:
```
