---
name: risk-review
description: Use when WheelWise must review product, technical, market, license, security, privacy, compliance, dependency, or execution risks before recommending a product build plan.
---

# Risk Review

Review risks after the delivery surface and reuse decisions are known. Use this skill as WheelWise's risk entry point.

## Risk Categories

- Market: weak demand, crowded category, unclear buyer, poor distribution.
- Product: vague workflow, low urgency, missing differentiation, excessive MVP scope.
- Technical: hard integrations, data quality, scalability, platform constraints.
- Security/privacy: sensitive data, auth, permissions, regulated workflows.
- License/compliance: copyleft, unclear commercial rights, data residency, app-store rules.
- Dependency: vendor lock-in, abandoned repositories, unstable APIs.
- Execution: team skill gap, timeline mismatch, operational burden.
- Direction: strong counter-evidence, overconfident user assumptions, unconfirmed major pivot, or a recommendation that differs materially from the user's original direction.

## Output Shape

```text
Risk:
Category:
Severity: Low / Medium / High
Likelihood: Low / Medium / High
Evidence:
Original assumption:
Supporting evidence:
Opposing evidence:
Direction shift:
User confirmation needed:
Mitigation:
Owner or decision point:
```

Surface-specific risk must be included. A browser extension has permission and store-review risk; a mobile app has app-store and device-permission risk; an API/SaaS has uptime, abuse, auth, and observability risk.

## V4 State Integration

- Read `project-state.md` and `evidence-board.md` before risk review.
- Treat unresolved contradictions and high-impact evidence gaps as risks.
- Treat major direction shifts without user confirmation as high-priority risks that block normal Delivery.
- Update `project-state.md` with risk summary, highest-priority risk, mitigation summary, and last updated by skill.
- Feed risks into `feasibility-review: full-review` for Gate2.

When risk review changes the verdict, scope, stack, demo, or execution order, apply `../../shared/references/decision-rationale-standard.md`.
