---
name: customer-discovery
description: Use when WheelWise must define target customers, personas, jobs-to-be-done, pain intensity, current workflows, adoption objections, interview questions, or validation experiments using user evidence and current web research.
---

# Customer Discovery

Turn market and product assumptions into testable customer hypotheses. Web evidence can inform discovery, but it does not replace real customer interviews.

## Required Reference

Read `../../shared/references/web-research-standard.md` before doing current-source research.
Read `../../shared/references/idea-applicability-standard.md` when first-hand user, field, buyer, adoption, or local demand data may be required.

## Process

1. Restate the idea, delivery surface, target customer, and unknowns.
2. Identify personas, buyer/user distinction, and jobs-to-be-done.
3. Search for current user evidence when pain, workflow, willingness to adopt, or objections affect the recommendation.
4. Prefer reviews, forums, community discussions, Q&A, product comments, public case studies, job descriptions, and workflow descriptions.
5. Separate observed evidence from interview hypotheses.
6. Check whether the evidence supports or weakens the user's stated target customer, pain urgency, workflow, adoption intent, and willingness to pay.
7. Produce interview questions and validation experiments that test the riskiest assumptions.
8. Mark whether the customer direction should be kept, narrowed, changed, or validated before continuing.
9. If the target user, buyer, or purchase behavior depends on local observation, enterprise pilots, field sales, or service delivery, return required first-hand data and thresholds.

## Evidence Rules

- Treat community and review evidence as directional unless repeated across multiple sources.
- Do not invent quotes, reviews, or user complaints.
- Label inferred pain intensity as an assumption unless supported by strong evidence.
- State that real interviews are still required before a confident build decision when user urgency or willingness to pay is uncertain.

## Output Shape

```text
Research questions:
Search date:
Applicability class:
Primary persona:
Secondary personas:
Buyer / decision maker:
Jobs-to-be-done:
Current workflow:
Current alternatives:
Pain intensity:
Adoption objections:
Willingness-to-pay or adoption signals:
Data sufficiency:
Required supplemental data:
Original customer assumptions:
Supporting evidence:
Opposing evidence:
Why original customer direction may be weak:
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
Interview questions:
Validation experiments:
Success threshold:
Failure response:
Impact on feasibility:
Impact on product strategy:
Confidence:
```

In the final Chinese report, write the results into `目标用户`, `问题与紧迫性`, `用户假设`, `验证实验`, and `最终建议与下一步行动` as needed. Do not use `Customer Discovery` as a report section heading.

## V4 State Integration

- Before discovery, read `project-state.md` for current target customer, delivery surface, assumptions, and Gate status.
- Write user evidence, interview hypotheses, adoption objections, and validation thresholds into `evidence-board.md` through `evidence-board`.
- Update `project-state.md` with customer evidence summary, open questions, and last updated by skill.
- If customer evidence supports a different target user, buyer, problem, adoption path, or willingness-to-pay assumption, mark the direction shift and user confirmation need in `evidence-board.md`.
- If the output is assumption-led, mark it clearly so Gate2 can avoid treating it as strong evidence.
