---
name: surface-strategy
description: Use when WheelWise must decide or review the product delivery surface, including website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, automation tool, or hybrid delivery.
---

# Surface Strategy

Choose the implementation form before planning architecture, reuse, validation, or monetization.

## Delivery Surfaces

| Surface | Use when | Planning emphasis |
| --- | --- | --- |
| Marketing website | Value prop, lead capture, content, or conversion is the product front door | Positioning, SEO, analytics, CMS, launch speed |
| Web app | Users need accounts, dashboards, workflows, collaboration, or persistent data | Auth, data model, permissions, billing, deployment |
| Mobile app | Device presence, notifications, camera, location, or app-store distribution matters | Platform choice, onboarding, offline, push, store review |
| Desktop app | Local files, OS integration, heavy compute, or professional workflows matter | Packaging, updates, local storage, cross-platform tradeoffs |
| Browser extension | The product acts inside existing websites or browser context | Permissions, content scripts, privacy, store review |
| API/SaaS | The user experience is integration, automation, or developer consumption | API design, auth, docs, SDKs, uptime, observability |
| CLI | Developers/operators need local command workflows | Install path, command UX, config, package distribution |
| Automation tool | Value comes from triggers, actions, and integrations | Reliability, retry, permissions, integration coverage |
| Local/offline validation tool | The idea is a stall, store, local service, field activity, or physical operation that needs first-hand validation before a product surface | Field data checklist, trial dashboard, cost and margin calculator, compliance checklist |
| Physical/hardware validation tool | The idea depends on manufacturing, supply chain, inventory, certification, or after-sales | BOM, supplier, certification, inventory, pilot, and after-sales validation |

## Decision Rules

- Prefer the lowest-friction surface that can validate the riskiest assumption.
- Pick one primary surface for MVP. Mark secondary surfaces as later unless needed for validation.
- If the idea depends on another product's UI context, consider browser extension or automation first.
- If monetization depends on recurring team workflows, web app or API/SaaS often wins.
- If the user's requested surface is not the best validation surface, explain the counter-evidence and mark direction shift as `Minor` or `Major`.
- A material change from the user's requested surface is a major direction shift and must feed Gate2 user confirmation.
- For non-digital ideas, the recommended first surface may be a validation dashboard or simulator rather than a product UI.

## Output Shape

```text
Primary surface:
Secondary surfaces:
Why this surface:
Why alternatives lose:
Original surface assumption:
Supporting evidence:
Opposing evidence:
Direction shift:
User confirmation needed:
Surface-specific constraints:
Validation implication:
Applicability class:
Evidence requirement:
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
