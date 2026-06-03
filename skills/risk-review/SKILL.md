---
name: risk-review
description: Use when WheelWise must review product, technical, market, license, security, privacy, compliance, dependency, or execution risks before recommending a product build plan.
---

# Risk Review

Review risks after the delivery surface and reuse decisions are known. Use this skill as WheelWise's risk entry point.

In V4.5, risk review acts as the risk-review committee viewpoint for the pre-review board. It must distinguish risks backed by facts from risks based on assumptions, inferences, or evidence gaps.

## Risk Categories

- Market: weak demand, crowded category, unclear buyer, poor distribution.
- Product: vague workflow, low urgency, missing differentiation, excessive MVP scope.
- Technical: hard integrations, data quality, scalability, platform constraints.
- Security/privacy: sensitive data, auth, permissions, regulated workflows.
- License/compliance: copyleft, unclear commercial rights, data residency, app-store rules, China mainland ICP/App filing, business entity, public-security filing, privacy policy, user agreement, payment/tax/invoice, algorithm/generative-AI filing or application registration, and industry permits.
- Dependency: vendor lock-in, abandoned repositories, unstable APIs.
- Execution: team skill gap, timeline mismatch, operational burden.
- Direction: strong counter-evidence, overconfident user assumptions, unconfirmed major pivot, or a recommendation that differs materially from the user's original direction.
- Data sufficiency: conclusion lacks data, first-hand evidence, current sources, or a clear evidence gap.
- Gate0 continuation: missing dynamic supplemental data, stale time-sensitive evidence, unclear resume state, or treating a `Field Data Required` pause as a confident verdict.

## Output Shape

```text
Risk:
Category:
Severity: Low / Medium / High
Likelihood: Low / Medium / High
Evidence:
Data source:
Evidence type:
Evidence classification: 事实 / 假设 / 推断 / 证据缺口
Evidence strength:
Pre-review state impact:
Original assumption:
Supporting evidence:
Opposing evidence:
Evidence gap:
Gate0 Evidence Intake status:
Waiting for supplemental data:
Time-sensitive recheck needed:
Direction shift:
User confirmation needed:
Mitigation:
Owner or decision point:
Validation priority:
```

Surface-specific risk must be included. A browser extension has permission and store-review risk; a mobile app has app-store and device-permission risk; an API/SaaS has uptime, abuse, auth, and observability risk.

## V4 State Integration

- Read `project-state.md` and `evidence-board.md` before risk review.
- Treat unresolved contradictions and high-impact evidence gaps as risks.
- Treat major direction shifts without user confirmation as high-priority risks that block normal Delivery.
- Record compliance and launch prerequisites in the final report, but do not block the workflow by default unless the idea is unsafe or illegal.
- Update `project-state.md` with risk summary, highest-priority risk, mitigation summary, and last updated by skill.
- Feed risks into `feasibility-review: full-review` for Gate2.
- Update `project-state.md` when risk evidence changes pre-review state, review scorecard, or next-stage recommendation.
- If risk evidence is only assumption-led, lower confidence and mark the required validation before build planning.

When risk review changes the verdict, scope, stack, demo, or execution order, apply `../../shared/references/decision-rationale-standard.md`.
