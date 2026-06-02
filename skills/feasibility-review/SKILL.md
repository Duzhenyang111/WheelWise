---
name: feasibility-review
description: Use when WheelWise must screen a product idea early or make a full Go, Pivot, Need More Evidence, Kill, or Park decision before delivery planning.
---

# Feasibility Review

Feasibility review has two V4 modes: `early-screening` and `full-review`.

## Mode Selection

| Mode | Use when | Output |
| --- | --- | --- |
| `early-screening` | Phase 0 after `idea-intake` and `surface-strategy` | Can continue / cannot continue / not recommended now |
| `full-review` | Phase 2 after evidence-board, product strategy, commercialization, and risk review | Go / Pivot / Need More Evidence / Kill / Park |

## Early-Screening

Purpose: quickly detect ideas that are clearly unsafe, impossible, incoherent, or not worth continuing before spending effort on discovery.

Inputs:

- `project-state.md`.
- Idea brief from `idea-intake`.
- Delivery surface from `surface-strategy`.
- Known constraints, open questions, and assumptions.

Score Low / Medium / High:

- Problem urgency.
- Target customer clarity.
- Delivery surface fit.
- Legal, privacy, or compliance burden.
- Basic technical plausibility.
- Time and budget fit.
- Dependency or data-access risk.

Early verdict rules:

| Verdict | Use when |
| --- | --- |
| Can continue | No obvious blocker; enough information exists for discovery |
| Cannot continue | Legally unsafe, technically impossible, incoherent, or missing a real user/problem |
| Not recommended now | Timing, dependency, budget, compliance, or user clarity makes discovery weak |
| Need Basic Input | The only blocker is missing basic user, scope, or constraint information |
| Field Data Required | Local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content/community, or service-heavy idea lacks required first-hand data for a high-confidence assessment |

Gate1 behavior:

- If `Cannot continue` or `Not recommended now`, output the stop reason and end.
- If `Can continue`, do not ask the user; automatically enter Discovery.
- If `Need Basic Input`, return control to `using-wheelwise` so Gate0 Evidence Intake asks only the allowed basic questions.
- If `Field Data Required`, return control to `using-wheelwise` so Gate0 Evidence Intake returns the dynamic supplemental-data checklist, continue thresholds, stop thresholds, and resumable pause state.

Early output shape:

```text
Mode:
Early verdict:
Confidence:
Why:
Main evidence:
Blocking unknowns:
Applicability class:
Gate0 Evidence Intake status:
Required field data:
Why the data is needed:
Continue thresholds:
Stop thresholds:
Gate1 action:
Project-state update:
```

## Full Review

Purpose: decide whether the synthesized product direction should enter Delivery.

Inputs:

- Updated `project-state.md`.
- `evidence-board.md`.
- Product strategy.
- Commercialization summary.
- Risk review.
- Reuse and technical constraints.

Score Low / Medium / High:

- Problem urgency.
- Reachable target customer.
- Evidence strength.
- Willingness to pay or adopt.
- Differentiation.
- Delivery surface fit.
- Technical feasibility.
- Data or integration dependency.
- Legal, privacy, or compliance burden.
- Commercial path.
- Execution path.
- Original direction fit.
- Strength of supporting and opposing evidence.
- Direction shift severity.

Full verdict rules:

| Verdict | Use when |
| --- | --- |
| Go | Evidence, strategy, risk, and execution path are coherent enough to enter Delivery |
| Pivot | Evidence supports a different customer, problem, surface, or wedge |
| Need More Evidence | A high-impact evidence gap blocks a credible delivery plan |
| Kill | The idea is unsafe, implausible, undifferentiated, or lacks a buyer/user after review |
| Park | The idea may be valid, but timing, dependency, regulation, budget, or team fit blocks near-term progress |

Gate2 behavior:

- `Go`: do not ask the user; automatically enter Delivery.
- `Pivot`, `Need More Evidence`, `Kill`, or `Park`: return control to `using-wheelwise` to ask for user confirmation or next direction.
- If target user, core problem, delivery surface, product wedge, business model, compliance boundary, or technical feasibility path changes materially, the verdict cannot be `Go` until the user confirms the new direction.

Full output shape:

```text
Mode:
Full verdict:
Confidence:
Gate2 action:
Why:
Original direction valid:
Why original direction is weak:
Recommended adjustment:
Direction shift:
User confirmation needed:
Evidence summary:
Evidence gaps:
Contradictions:
Validation threshold:
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
Project-state update:
```

## State Rules

- Always write the verdict, confidence, gate action, and rationale back to `project-state.md`.
- Full review must reference `evidence-board.md`; if the board is empty, the verdict cannot be `Go` unless the report is explicitly marked as assumption-led.
- Do not use `Go`, `Pivot`, `Need More Evidence`, `Kill`, or `Park` as final Chinese report section titles; translate and synthesize them into Chinese report content.
