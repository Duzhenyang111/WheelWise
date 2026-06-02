---
name: idea-intake
description: Use when a raw product idea, feature idea, startup concept, or vague build request must be structured before WheelWise can judge surface, feasibility, reuse options, or execution plan.
---

# Idea Intake

Structure the user's idea into a brief that downstream WheelWise skills can use.

## Capture

Extract or ask for:

- Idea summary.
- Target customer.
- Problem and urgency.
- Current alternatives or workaround.
- Desired outcome.
- Constraints: budget, timeline, team, platform, data, compliance.
- Success metric.
- Assumptions and unknowns.
- User original assumptions: target customer, problem, delivery surface, product wedge, business model, compliance boundary, and technical path.
- Applicability class: digital product, local/offline business, physical product, supply-chain, regulated, platform-dependent, B2B, content/community, or service product.
- Gate0 Evidence Intake candidate status: `Ready`, `Need Basic Input`, or `Field Data Required`.

## Rules

- Preserve uncertainty instead of filling gaps with confident fiction.
- Treat user-provided claims as original assumptions, not validated facts.
- Read `../../shared/references/idea-applicability-standard.md` when the idea may be non-digital, local, offline, physical, regulated, supply-chain, hardware, platform-dependent, B2B, content, community, or service-heavy.
- Ask only for information that changes routing or feasibility.
- Do not ask generic questions when the real blocker is first-hand field data; pass the detected idea-type-specific data needs to `using-wheelwise`.
- For composite ideas, combine applicability classes instead of reducing the idea to one broad category.
- If the user wants momentum, make assumptions explicit and continue.
- Pass a compact idea brief to `surface-strategy`.

## Output Shape

```text
Idea summary:
Target customer:
Problem and urgency:
Current alternatives:
Desired outcome:
Constraints:
Success metric:
User original assumptions:
Applicability class:
Gate0 Evidence Intake status:
Required evidence:
Missing evidence:
Dynamic supplemental-data needs:
Assumptions:
Unknowns:
```
