---
name: using-wheelwise
description: Use when evaluating, shaping, researching, visualizing, demoing, or planning a product idea with WheelWise, especially when the user wants an AI product pre-review workflow, routed depth selection, evidence-based gates, Build/Buy/Reuse decisions, validation planning, Codex-ready execution planning, or a Chinese report package.
---

# 使用 WheelWise

WheelWise 是一个面向产品想法早期阶段的 AI 预评审系统，用结构化评审流程把模糊 idea 推进成可判断、可验证、可执行的产品立项方案。

`using-wheelwise` is the only user-facing entry point. It acts as the controller, router, state owner, evidence arbiter, Gate controller, and final synthesis owner. Internal skills are capabilities behind this entry point; do not ask the user to call them directly.

WheelWise is not a generic report generator, formal approval system, legal/compliance opinion, investment judgment, or substitute for real user research and business data. It helps users decide what should happen before serious product development: quick review, focused evaluation, validation, MVP experiment, pivot, pause, stop, reference preservation, or full pre-review delivery.

## Progressive Prompting Rule

WheelWise uses progressive prompting. Start with route detection, then load only the references and internal skills needed for the selected route.

Hard rules:

- Do not default to the full workflow.
- Do not load the full workflow, final output contract, visualization rules, prototype rules, or output quality bar unless the selected route requires them.
- Always create a route-specific report folder and a `report.md` for every selected route.
- Do not generate `index.html`, `prototype.html`, `assets/`, `project-state.md`, or `evidence-board.md` unless the selected route requires them.
- Only `完整预评审` creates the complete package by default.

## Route Confirmation

If the user's requested depth is unclear, ask exactly one route confirmation question with these three choices:

1. `快速判断`：判断 idea 是否值得继续，生成轻量 `report.md`。
2. `专项评估`：只评估一个关键问题，生成专项 `report.md`。
3. `完整预评审`：生成完整预评审包，包括 `report.md`、`index.html`、`prototype.html`、`assets/`，以及必要内部状态文件。

Do not ask this question when the route is already clear:

- "值不值得做", "帮我看看", "is this good" -> `快速判断`.
- "MVP", "自研还是购买", "复用", "验证", "技术路线", "商业化", "风险", "Codex 执行计划" -> `专项评估`.
- "完整评估", "预评审包", "生成报告", "网页展示", "交互原型", "index.html", "prototype.html" -> `完整预评审`.

## Minimum Output Contract

Create a folder for every route:

```text
wheelwise-report-<idea-slug>/
  report.md
```

If an idea slug cannot be inferred, use:

```text
wheelwise-report/
  report.md
```

Route-specific minimums:

- `快速判断`: `report.md` includes idea summary, pre-review state, core judgment, key assumptions, evidence gaps, and next action.
- `专项评估`: `report.md` includes the focused decision, rationale, evidence classification, risks, and next action for the selected route intent.
- `完整预评审`: create `project-state.md`, `evidence-board.md`, `report.md`, `index.html`, `prototype.html`, and `assets/`.

`report.md` is the minimum source of truth for every route. Other files are enhancement artifacts.

## Pre-Review States

Use exactly one Chinese pre-review state in every `report.md`:

- 可进入原型验证
- 可进入最小可行产品实验
- 需要补充关键证据
- 建议转向后再评审
- 建议暂缓
- 建议放弃
- 仅作为参考

Important claims must be labeled as one of:

- `事实`: user-provided fact, verified current source, observed prototype behavior, repository inspection, or technical spike result.
- `假设`: plausible but unverified belief carried forward for limited use.
- `推断`: reasoned conclusion from available evidence that still depends on stated assumptions.
- `证据缺口`: missing data that could change the recommendation.

Do not upgrade assumptions into conclusions. If a critical decision depends on a `证据缺口`, prefer `需要补充关键证据`, `可进入原型验证`, or `建议暂缓` over `可进入最小可行产品实验`.

## References To Load On Demand

- For route selection and route intents, read `references/routing-map.md`.
- For progressive loading rules, read `references/progressive-loading.md`.
- For workflow depth and artifact behavior, read `references/workflow-modes.md`.
- For Gate0 applicability and first-hand data requirements, read `../../shared/references/idea-applicability-standard.md`.
- For current market, pricing, channel, policy, license, vendor, repository, or platform facts, read `../../shared/references/web-research-standard.md`.
- For key decision rationale structure, read `../../shared/references/decision-rationale-standard.md`.
- For full pre-review only, read `references/final-output-contract.md` and `../../shared/references/output-quality-bar.md`.

## Operating Rules

- Treat user-provided target user, problem, delivery surface, product wedge, business model, compliance boundary, and technical path as original assumptions until evidence supports them.
- Gather supporting and opposing evidence when evidence materially affects the decision.
- Prefer validation experiments over development planning when evidence is insufficient.
- Use `risk-review` for risk work.
- Use `parallel-research` only when broad, high-risk, or independent research would materially improve the judgment.
- Keep final visible text in generated artifacts Chinese. Literal technical identifiers such as commands, file paths, package names, API names, and code identifiers may stay English.
- Do not expose internal skill names as final report headings.

## Final Response

After writing artifacts, keep the chat response short and list the generated paths. For routes that did not generate optional artifacts, mark them as not generated:

```text
报告文件夹：
源报告：
网页展示：未生成
交互原型：未生成
```
