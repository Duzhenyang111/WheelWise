---
name: using-wheelwise
description: Use when evaluating, shaping, researching, visualizing, demoing, or planning a product idea with WheelWise, especially when the user wants market research, customer discovery, commercialization, MVP scope, delivery surface choice, feasibility, product strategy, build/buy/reuse/fork/reference decisions, technical planning, visual brief, interactive demo, risk review, or a Codex-ready execution plan.
---

# 使用 WheelWise

WheelWise turns a raw product idea into an explainable, presentable product plan. The primary artifact is a Chinese report folder, not a chat summary, a single loose file, or a dump of internal skill outputs. The folder contains `report.md`, `index.html`, and `assets/`.

## Core Discipline

1. Start with `idea-intake` unless the user already supplied a complete product brief.
2. Run `surface-strategy` before architecture or reuse decisions. Delivery surface changes validation, reuse options, and execution path.
3. Run `feasibility-review` before detailed planning. Internally use one verdict: Build MVP, Validate First, Pause, or Reject; in final visible output translate it to Chinese.
4. Run `market-research` for full reports or whenever market category, competitors, substitutes, trends, pricing clues, channels, or current demand signals affect the decision.
5. Run `customer-discovery` for full reports or whenever persona, jobs-to-be-done, pain intensity, workflow adoption, buyer/user distinction, or validation experiments affect the decision.
6. Run `product-strategy` after feasibility and research context. It must inherit the verdict and focus the MVP around the riskiest assumption.
7. Run `reuse-evaluator` for each important product module. Every module needs one internal decision: Build, Buy, Reuse, Fork, or Reference; final visible output must use 自研 / 购买 / 复用 / 分叉改造 / 参考.
8. Run `technical-planning` after reuse decisions. It must not contradict module strategy choices.
9. Run `commercialization` for full reports or whenever business model, pricing, packaging, channels, sales motion, or early monetization tests affect the decision.
10. Run `risk-review` when decisions touch license, privacy, security, compliance, dependency, market, product, commercialization, or execution risk.
11. Run `visual-brief` for full reports so the recommendation has image-level visual explanation, not only text or Mermaid.
12. Run `ui-demo` when the product has a user-visible surface. For API, CLI, automation, or developer-tool products, route internally to a playground, terminal simulator, request explorer, or workflow simulator; final visible output must describe these in Chinese.
13. Run `execution-plan` only after the idea, surface, feasibility, market research, customer discovery, product strategy, reuse decisions, technical plan, commercialization, risks, visuals, and demo scope are coherent.
14. Generate one final report folder. Default path: `wheelwise-report/`; if the user supplied an idea name, use `wheelwise-report-<idea-slug>/`.
15. The folder must contain `report.md`, `index.html`, and `assets/`; images and other static resources must live under `assets/`.
16. Run the final report self-check before responding: Chinese visible text, folder structure, progressive structure, visuals, demo details, webpage rule, detailed intro, detailed outro, and no English skill-module headings.
17. Use `parallel-research` only for complex research or independent review. Treat subagent findings as evidence; final judgment belongs to this skill.

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
-> market-research
-> customer-discovery
-> product-strategy
-> reuse-evaluator
-> technical-planning
-> commercialization
-> risk-review
-> visual-brief
-> ui-demo when applicable
-> execution-plan
-> Chinese report folder
```

## Output Rules

- Prefer clear decisions over broad option lists.
- Apply `../../shared/references/decision-rationale-standard.md` to every key decision: verdict, surface, product strategy, module strategy, technical stack, visual brief, UI demo, commercialization notes, and execution order.
- Primary final output must be a Chinese report folder. Use `wheelwise-report/` by default or `wheelwise-report-<idea-slug>/` when the user provides an idea name.
- Visible text in `report.md`, `index.html`, image text, chart labels, alt text, table fields, explanations, decision rationales, risks, experiments, and execution-plan prose must be Chinese.
- Technical commands, file paths, package names, API names, code identifiers, and technology names may remain English only when they are literal technical identifiers.
- Do not answer with a structured chat summary. After writing artifacts, the chat response should only state the report folder path, `report.md` path, `index.html` path, and a very short completion note.
- Do not use internal skill names as final report sections. Forbidden report headings include `Idea Intake`, `Surface Strategy`, `Feasibility Review`, `Product Strategy`, `Reuse Evaluator`, `Technical Planning`, `Risk Review`, `UI Demo Scope`, and `MVP Execution Plan`.
- The final report must be progressive: `报告说明与阅读导览` -> user/problem -> decision/recommendation -> visual/demo -> risk/validation -> execution plan -> `最终建议与下一步行动`.
- If visual-brief produces images or image prompts, place them in the report's `视觉说明` section. If image assets exist, reference them with Markdown such as `![产品概念图](./assets/concept.png)`.
- Prefer real image assets when image generation is available. If image generation is unavailable, include a Mermaid 兜底图表 in `视觉说明`; all chart labels must be Chinese.
- If image generation cannot reliably render Chinese text, generate images without text and place Chinese explanations in `report.md` and `index.html`.
- If ui-demo produces a demo, place 演示路径、运行方式、核心交互、模拟数据说明、状态覆盖、后端边界 in the report's `交互演示` section.
- Add a `网页展示文件` section. Default path is `index.html`. State that it is a display layer sourced from `report.md` and list the required display modules.
- If UI UX Pro Max or another UI/UX skill is available, it may be used as design intelligence for the webpage display file, visual brief, or demo surface. Do not copy external skill content.
- Keep implementation surface visible throughout: website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, or automation tool.
- Do not invent market, customer, pricing, channel, policy, license, or repository facts. If current facts matter, browse using `../../shared/references/web-research-standard.md` or mark the evidence gap and lower confidence.
- Full reports must include market evidence, user evidence, commercialization assumptions, and a source-evidence summary when current research was needed.
- Do not copy external skill content. External skills belong in `../../shared/references/external-skills.md` as references or optional dependencies.
- Use `risk-review` consistently for risk work. Do not create alternate risk skill names.
- Final report should follow `../../shared/templates/new-product-brief.md` unless the user explicitly asks for a shorter Chinese report, in which case use `../../shared/templates/final-wheelwise-report.md`.

## Final Self-Check

Before sending the final chat response, confirm:

- The report folder is `wheelwise-report/` or `wheelwise-report-<idea-slug>/`.
- The folder contains `report.md`, `index.html`, `assets/`, and at least one image.
- The report includes all required Chinese sections from `references/final-output-contract.md` in progressive order.
- The opening `报告说明与阅读导览` includes report purpose, applicable stage, core conclusion preview, and reading path.
- The ending `最终建议与下一步行动` includes one-sentence judgment, 7-day, 14-day, and 30-day actions, plus 继续 / 停止条件.
- No forbidden English skill-module headings appear as report sections.
- No visible output text contains English display terms such as Build, Buy, Reuse, Fork, Reference, Web App, SaaS, MVP, Demo, mock, fallback, go/no-go, or Codex-ready.
- `视觉说明` contains real Markdown image references under `assets/`, or Mermaid 兜底图表 when image generation is unavailable.
- `交互演示` includes 演示路径、运行方式、核心交互、模拟数据、加载 / 空状态 / 错误 / 成功状态、后端边界。
- `网页展示文件` records `index.html` rules.
- `可交给 Codex 执行的计划` includes tasks to create or update the report folder, source report, webpage display file, and assets.
- Market, customer, and commercialization claims separate source evidence from analysis assumptions, and any current fact that matters has been browsed or marked as an evidence gap.
