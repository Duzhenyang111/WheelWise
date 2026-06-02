---
name: reuse-evaluator
description: Use when WheelWise must decide whether product modules should be built, bought, reused, forked, or only referenced, including SaaS, APIs, open-source projects, starter kits, templates, libraries, and self-hosted tools.
---

# Reuse Evaluator

This is WheelWise's core moat. For each important product module, recommend one strategy: Build, Buy, Reuse, Fork, or Reference.

## Process

1. Decompose the idea into modules.
2. Mark which modules create product differentiation.
3. Identify existing SaaS/API/open-source/starter-kit/library options when needed.
4. Score fit, maturity, cost, lock-in, customization, license, security, maintenance, and delivery surface fit.
5. Check whether reuse evidence weakens the user's assumed build, buy, reuse, fork, or reference path.
6. Make one decision per module.

## Decision Rules

| Strategy | Prefer when |
| --- | --- |
| Buy | The module is common, high-risk, non-differentiating, and vendors are mature |
| Reuse | A mature library/template solves the need with low lock-in and acceptable customization |
| Fork | An open-source product is close to the desired product but needs deep product changes |
| Reference | Patterns are useful but license, quality, architecture, or fit prevents direct reuse |
| Build | The module is core differentiation or existing options block the product's unique value |

## Required Matrix

```text
Module:
Recommended strategy:
Suggested option(s):
Why:
Why alternatives lose:
Original module assumption:
Supporting evidence:
Opposing evidence:
Why original module path may be weak:
Direction shift:
User confirmation needed:
Evidence:
Assumptions:
Surface fit:
License/security/privacy notes:
Cost and lock-in:
Risks:
Fallback:
Confidence:
```

Read `../../shared/references/build-buy-reuse-vocabulary.md` for shared terminology.
Read `../../shared/references/decision-rationale-standard.md` for decision rationale requirements.

## V4 State Integration

- Read `project-state.md` before module decomposition to preserve the selected delivery surface and current assumptions.
- Write vendor, API, open-source, license, maturity, cost, and lock-in findings into `evidence-board.md` through `evidence-board`.
- Update `project-state.md` with reuse decisions summary and last updated by skill.
- If reuse evidence changes a differentiating module, core dependency, license boundary, or build/buy strategy materially, mark the direction shift and user confirmation need in `evidence-board.md`.
- If a module needs a technical spike before a safe decision, mark the spike as an evidence gap and recommended next action.
