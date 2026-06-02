---
name: market-research
description: Use when WheelWise must research market category, competitors, substitutes, user demand signals, trends, market maturity, entry barriers, or current market evidence before feasibility, product strategy, reuse, risk, or commercialization decisions.
---

# Market Research

Research the market context behind a product idea. Use current web evidence whenever competitor, trend, pricing, channel, platform, or category facts affect the decision.

## Required Reference

Read `../../shared/references/web-research-standard.md` before doing current-source research.
Read `../../shared/references/idea-applicability-standard.md` when the idea is local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content, community, or service-heavy.

## Process

1. Restate the idea, target user, delivery surface, and research questions.
2. Classify the market category and likely adjacent categories.
3. Search for current evidence when facts may have changed.
4. Cover direct competitors, indirect substitutes, recent market signals, pricing or packaging clues, and distribution channels or platform ecosystem.
5. Separate source evidence from assumptions.
6. Search for counter-evidence that weakens the user's original market, customer, surface, pricing, or channel assumptions.
7. Explain how the findings affect feasibility, product strategy, reuse decisions, risk, and validation.
8. Mark whether findings support or oppose the original direction and whether they imply a minor or major direction shift.
9. If the market is local, offline, physical, supply-chain-heavy, platform-dependent, B2B, content/community, service-heavy, or regulated, identify what cannot be answered by web research and return idea-type-specific first-hand data needs.
10. If Gate0 is waiting for supplemental data, use any newly supplied user data as evidence, compare it with thresholds, and mark time-sensitive market or competitor facts that need refresh.

## Minimum Search Coverage

When producing a full WheelWise report, current research should cover:

- Direct competitors.
- Indirect substitutes and user workarounds.
- Recent demand or trend signals.
- Pricing or packaging clues.
- Distribution channel, marketplace, or platform ecosystem.
- Entry barriers such as regulation, data access, incumbent advantage, or switching cost.

If coverage is incomplete, state the evidence gap and reduce confidence.

## Output Shape

```text
Research questions:
Search date:
Market category:
Adjacent categories:
Applicability class:
Direct competitors:
Indirect substitutes:
User demand signals:
Recent market signals:
Pricing or packaging clues:
Distribution channels:
Market maturity:
Entry barriers:
Opportunity window:
Data sufficiency:
Required supplemental data:
Why supplemental data is needed:
Collection method:
Minimum sample:
Continue thresholds:
Stop thresholds:
Supplemental data checklist version:
Time-sensitive recheck needed:
Original market assumptions:
Supporting evidence:
Opposing evidence:
Why original direction may be weak:
Direction shift:
User confirmation needed:

Source evidence:
Source:
Source type:
Data source:
Key finding:
Evidence strength:
Affected decision:
Supports or opposes:

Analysis assumptions:
Unknowns:
Evidence gaps:
Impact on feasibility:
Impact on product strategy:
Impact on reuse/risk:
Validation implications:
Confidence:
```

In the final Chinese report, write the results into `市场备注`, `决策解释摘要`, `关键风险`, and `验证实验` as needed. Do not use `Market Research` as a report section heading.

## V4 State Integration

- Before research, read `project-state.md` to confirm phase, delivery surface, assumptions, and open questions.
- After research, write each meaningful finding into `evidence-board.md` through `evidence-board`.
- Update `project-state.md` with market evidence summary, evidence gaps, contradictions, and last updated by skill.
- If market evidence supports a different customer, problem, delivery surface, product wedge, business model, or channel, mark the shift in `evidence-board.md` and feed it to Gate2.
- If no current research is possible, record the gap in `evidence-board.md` instead of inventing facts.
