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

## Output Shape

```text
Risk:
Category:
Severity: Low / Medium / High
Likelihood: Low / Medium / High
Evidence:
Mitigation:
Owner or decision point:
```

Surface-specific risk must be included. A browser extension has permission and store-review risk; a mobile app has app-store and device-permission risk; an API/SaaS has uptime, abuse, auth, and observability risk.
