---
name: using-wheelwise
description: Use when evaluating, shaping, or planning a product idea with WheelWise, especially when the user wants MVP scope, delivery surface choice, feasibility, build/buy/reuse/fork/reference decisions, risk review, or a Codex-ready execution plan.
---

# Using WheelWise

WheelWise turns a raw product idea into a decision-backed execution plan. Keep the main flow small, route to internal skills deliberately, and synthesize the final answer yourself.

## Core Discipline

1. Start with `idea-intake` unless the user already supplied a complete product brief.
2. Run `surface-strategy` before architecture or reuse decisions. Delivery surface changes validation, reuse options, and execution path.
3. Run `feasibility-review` before detailed planning. Use one verdict: Build MVP, Validate First, Pause, or Reject.
4. Run `reuse-evaluator` for each important product module. Every module needs one decision: Build, Buy, Reuse, Fork, or Reference.
5. Run `risk-review` when decisions touch license, privacy, security, compliance, dependency, market, or execution risk.
6. Run `execution-plan` only after the idea, surface, feasibility, reuse decisions, and risks are coherent.
7. Use `parallel-research` only for complex research or independent review. Treat subagent findings as evidence; final judgment belongs to this skill.

## Route Selection

Read `references/routing-map.md` when the user request is narrow or ambiguous.
Read `references/workflow-modes.md` to choose short workflow, core workflow, or research-heavy workflow.
Read `references/final-output-contract.md` before producing the final WheelWise report.

## Default Core Workflow

```text
Idea
-> idea-intake
-> surface-strategy
-> feasibility-review
-> reuse-evaluator
-> risk-review
-> execution-plan
-> New Product Brief
```

## Output Rules

- Prefer clear decisions over broad option lists.
- Keep implementation surface visible throughout: website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, or automation tool.
- Do not invent market facts. If current competitor, pricing, license, or repository health data matters, browse or mark as needing research.
- Do not copy external skill content. External skills belong in `../../shared/references/external-skills.md` as references or optional dependencies.
- Use `risk-review` consistently for risk work. Do not create alternate risk skill names.
- Final output should follow `../../shared/templates/new-product-brief.md` unless the user asked for a narrower artifact.
