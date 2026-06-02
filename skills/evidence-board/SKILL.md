---
name: evidence-board
description: Use when WheelWise must consolidate market, customer, reuse, technical-spike, or validation evidence into a shared decision ledger before synthesis, feasibility full review, risk review, or final reporting.
---

# Evidence Board

Maintain the shared evidence ledger for WheelWise. The board is internal state, not a final report section.

## Inputs

- Current `project-state.md`.
- Outputs from `market-research`.
- Outputs from `customer-discovery`.
- Outputs from `reuse-evaluator`.
- Optional outputs from technical spikes, policy checks, license checks, vendor checks, or prototype tests.
- Known assumptions and evidence gaps.

## Process

1. Read `../../shared/templates/evidence-board.md` before creating or updating the board.
2. Convert each research or review finding into one evidence item.
3. Label the origin skill and evidence type.
4. Mark whether the item is source evidence, direct user evidence, expert judgment, prototype observation, assumption, or gap.
5. Tie every item to an affected decision: feasibility, surface, product strategy, reuse, technical plan, commercialization, risk, validation, visual/demo, or execution order.
6. Record contradictions instead of smoothing them over.
7. Record whether the item supports or opposes a user original assumption.
8. Mark direction shift as `None`, `Minor`, or `Major`.
9. Mark whether the shift needs user confirmation before Delivery.
10. Recommend the next action for each weak or missing evidence area.
11. Write a compact evidence summary back into `project-state.md`.

Every full report conclusion must be traceable to the board. If the board lacks evidence for a conclusion, record an explicit evidence gap and lower confidence.

## Evidence Types

Use these categories:

- Market source.
- Customer source.
- User interview.
- Competitor or substitute.
- Pricing or packaging.
- Vendor or API capability.
- Open-source repository.
- License or policy.
- Technical spike.
- Prototype observation.
- Assumption.
- Evidence gap.

## Output Shape

```text
Evidence item:
Source / origin skill:
Data source:
Evidence type:
Affected decision:
Strength:
Confidence:
Original assumption:
Supports or opposes:
Direction shift:
User confirmation needed:
Assumption vs evidence:
Contradiction:
Evidence gap:
Recommended next action:
```

For Gate0 evidence requirements, also record:

```text
Applicability class:
Required data:
Collection method:
Minimum sample:
Continue threshold:
Stop threshold:
```

## Final Report Integration

Do not use `Evidence Board` as a final report section heading. Instead:

- Put market evidence into `市场备注`.
- Put user evidence and assumptions into `用户假设` and `问题与紧迫性`.
- Put decision support into `决策解释摘要`.
- Put contradictions and weak evidence into `关键风险`.
- Put evidence gaps into `验证实验`.
- Put major direction shifts into `决策解释摘要`, `关键风险`, and `最终建议与下一步行动`, including why the original direction is weak.

## Quality Bar

- Every full report should have either evidence items or explicit evidence gaps.
- Every major conclusion in the final report must have supporting evidence or an explicit gap in the board.
- Gate2 cannot return `Go` if the board has unresolved high-impact gaps that affect feasibility, user urgency, legality, or core technical possibility.
- Gate2 cannot return `Go` when a `Major` direction shift requires user confirmation and has not been confirmed.
- Confidence must be lowered when evidence is missing, anecdotal, stale, or contradictory.
