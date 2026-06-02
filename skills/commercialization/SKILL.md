---
name: commercialization
description: Use when WheelWise must plan business model, pricing, packaging, go-to-market channels, sales motion, early monetization tests, revenue risks, or commercial assumptions using current market and competitor evidence.
---

# Commercialization

Plan how the product could make money and reach early users. Use current web evidence whenever pricing, packaging, channel, platform, policy, or buyer behavior affects the recommendation.

## Required Reference

Read `../../shared/references/web-research-standard.md` before doing current-source research.
Read `../../shared/references/decision-rationale-standard.md` for commercialization decisions.

## Process

1. Restate the product strategy, target customer, delivery surface, and minimum viable product scope.
2. Search current competitor pricing, free/paid boundaries, packaging, channel rules, platform fees, and buyer payment patterns when relevant.
3. Choose one primary business model and one fallback.
4. Define pricing assumptions, package boundaries, acquisition channels, sales motion, activation path, retention loop, and early monetization tests.
5. Define the first 30-day operating cadence: content, outreach, onboarding, customer success, support, and metric review.
6. Identify revenue risks and validation thresholds.
7. Check whether pricing, packaging, channels, platform rules, or buyer behavior support or weaken the user's original commercial assumptions.
8. Apply the decision rationale fields to the recommended commercial path.

## Minimum Search Coverage

When producing a full WheelWise report, current research should cover:

- Competitor or substitute pricing.
- Free tier, trial, usage limit, or paid feature boundaries.
- Acquisition channels and distribution constraints.
- Platform fees, app-store rules, marketplace rules, or payment restrictions when relevant.
- Signals for who pays: individual user, team, company, developer, operator, or sponsor.

If coverage is incomplete, state the evidence gap and reduce confidence.

## Output Shape

```text
Research questions:
Search date:
Recommended business model:
Fallback business model:
Pricing hypothesis:
Packaging:
Free / paid boundary:
Acquisition channels:
Sales motion:
Activation path:
Retention loop:
Operating cadence:
Early monetization tests:
Revenue risks:
Original commercial assumptions:
Supporting evidence:
Opposing evidence:
Why original commercial path may be weak:
Direction shift:
User confirmation needed:

Source evidence:
Source:
Source type:
Key finding:
Evidence strength:
Affected decision:
Supports or opposes:

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

In the final Chinese report, write the results into `商业化备注`, `验证实验`, `关键风险`, and `最终建议与下一步行动` as needed. Do not use `Commercialization` as a report section heading.

## V4 State Integration

- Read `project-state.md` and `evidence-board.md` before choosing the business model.
- Write pricing, packaging, channel, buyer, and monetization evidence into `evidence-board.md` through `evidence-board`.
- Update `project-state.md` with commercialization summary, revenue risks, operating cadence, and last updated by skill.
- If commercial evidence pushes the product toward a different buyer, pricing model, packaging, or channel, mark the direction shift and user confirmation need in `evidence-board.md`.
- If commercialization is mostly assumption-led, mark it as a Gate2 risk.
