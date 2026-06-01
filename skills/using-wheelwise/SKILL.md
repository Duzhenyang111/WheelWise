---
name: using-wheelwise
description: Use when evaluating, shaping, visualizing, demoing, or planning a product idea with WheelWise, especially when the user wants MVP scope, delivery surface choice, feasibility, product strategy, build/buy/reuse/fork/reference decisions, technical planning, visual brief, interactive demo, risk review, or a Codex-ready execution plan.
---

# Using WheelWise

WheelWise turns a raw product idea into an explainable, presentable, demo-ready product plan. The final artifact is a single Chinese Markdown report file, not only a chat summary. Keep the main flow routed through first-class skills, and synthesize the final report yourself.

## Core Discipline

1. Start with `idea-intake` unless the user already supplied a complete product brief.
2. Run `surface-strategy` before architecture or reuse decisions. Delivery surface changes validation, reuse options, and execution path.
3. Run `feasibility-review` before detailed planning. Use one verdict: Build MVP, Validate First, Pause, or Reject.
4. Run `product-strategy` after feasibility. It must inherit the verdict and focus the MVP around the riskiest assumption.
5. Run `reuse-evaluator` for each important product module. Every module needs one decision: Build, Buy, Reuse, Fork, or Reference.
6. Run `technical-planning` after reuse decisions. It must not contradict Build / Buy / Reuse / Fork / Reference choices.
7. Run `risk-review` when decisions touch license, privacy, security, compliance, dependency, market, product, or execution risk.
8. Run `visual-brief` for full reports so the recommendation has image-level visual explanation, not only text or Mermaid.
9. Run `ui-demo` when the product has a user-visible surface. For API, CLI, automation, or developer-tool products, route to a playground, terminal simulator, request explorer, or workflow simulator.
10. Run `execution-plan` only after the idea, surface, feasibility, product strategy, reuse decisions, technical plan, risks, visuals, and demo scope are coherent.
11. Generate or plan one final Chinese Markdown report file. Default path: `wheelwise-report.md`; if the user supplied an idea name, use `wheelwise-report-<idea-slug>.md`.
12. Use `parallel-research` only for complex research or independent review. Treat subagent findings as evidence; final judgment belongs to this skill.

## Route Selection

Read `references/routing-map.md` when the user request is narrow or ambiguous.
Read `references/workflow-modes.md` to choose short workflow, core workflow, or research-heavy workflow.
Read `references/final-output-contract.md` before producing the final WheelWise report file.

## Default Core Workflow

```text
Idea
-> idea-intake
-> surface-strategy
-> feasibility-review
-> product-strategy
-> reuse-evaluator
-> technical-planning
-> risk-review
-> visual-brief
-> ui-demo when applicable
-> execution-plan
-> Chinese Markdown report file
```

## Output Rules

- Prefer clear decisions over broad option lists.
- Apply `../../shared/references/decision-rationale-standard.md` to every key decision: verdict, surface, product strategy, module strategy, technical stack, visual brief, UI demo, commercialization notes, and execution order.
- Final output must be a single Chinese `.md` file. Use `wheelwise-report.md` by default or `wheelwise-report-<idea-slug>.md` when the user provides an idea name.
- The report body must be fully Chinese: title, section names, table fields, explanations, decision rationales, risks, experiments, and execution-plan prose. Product names, technical stacks, code paths, commands, API names, and Build / Buy / Reuse / Fork / Reference labels may remain English.
- Do not only answer with a structured chat summary. In chat, state the report file path and briefly summarize what was written.
- If visual-brief produces images or image prompts, place them in the report's `视觉说明` section. If image assets exist, reference them with Markdown such as `![产品概念图](./assets/visual-brief.png)`.
- If ui-demo produces a demo, place demo path, run command, core interactions, mock data notes, and backend simulation boundary in the report's `UI Demo / 交互 Demo` section.
- Keep implementation surface visible throughout: website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, or automation tool.
- Do not invent market facts. If current competitor, pricing, license, or repository health data matters, browse or mark as needing research.
- Do not copy external skill content. External skills belong in `../../shared/references/external-skills.md` as references or optional dependencies.
- Use `risk-review` consistently for risk work. Do not create alternate risk skill names.
- Final report should follow `../../shared/templates/new-product-brief.md` unless the user explicitly asks for a shorter Chinese report, in which case use `../../shared/templates/final-wheelwise-report.md`.
