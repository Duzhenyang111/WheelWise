# Workflow Modes

## Short Workflow

Use when the user asks one narrow question.

Examples:
- "Should auth be built or bought?"
- "Is this better as a browser extension or web app?"
- "Can I fork this open-source repo?"

Output only the decision, rationale, risks, and next step.

## Core Workflow

Use for most product ideas.

Steps:
1. Structure idea.
2. Choose delivery surface.
3. Review feasibility.
4. Research market category, competitors, substitutes, and current demand signals when they affect the decision.
5. Define customer hypotheses, jobs-to-be-done, pain intensity, and validation experiments.
6. Define product strategy and minimum viable product workflow.
7. Decompose modules.
8. Decide 自研 / 购买 / 复用 / 分叉改造 / 参考.
9. Create technical plan aligned with reuse decisions.
10. Plan commercialization: business model, pricing, packaging, channels, and monetization tests.
11. Review risks.
12. Create visual brief.
13. Create UI demo or simulator spec when applicable.
14. Produce a plan that Codex can execute.
15. Generate or plan the Chinese report folder.
16. Generate or plan `index.html` when a presentation layer helps.

## Research-Heavy Workflow

Use when competitor facts, pricing, user evidence, channel rules, platform policy, license status, repository health, market trends, or vendor capabilities materially change the answer. Browse current sources using `../../shared/references/web-research-standard.md`.

Use:
- `market-research` for category, competitor, substitute, demand, trend, channel, and maturity research.
- `customer-discovery` for personas, jobs-to-be-done, pain evidence, adoption objections, and validation experiments.
- `commercialization` for business model, pricing, packaging, channels, sales motion, and monetization tests.

Use `parallel-research` only when the work can be split into independent research briefs.

## Demo-Ready Workflow

Use when the user needs something presentable to stakeholders or test users.

Steps:
1. Run core workflow through `technical-planning`.
2. Run `visual-brief` for image-level explanation assets.
3. Run `ui-demo` for user-visible surfaces, or simulator mode for API/CLI/automation.
4. Ensure `execution-plan` includes tasks to generate the visual brief, demo, `report.md`, `index.html`, and assets.

## Final Report Workflow

Use when the user asks for a finished WheelWise report or when a full workflow is complete.

Steps:
1. Read `final-output-contract.md`.
2. Use `new-product-brief.md` unless the user explicitly wants a shorter report.
3. Create the report folder: `wheelwise-report/` or `wheelwise-report-<idea-slug>/`.
4. Write `report.md` in progressive Chinese sections, not internal skill-module sections.
5. Generate `index.html` as a display layer sourced from `report.md`.
6. Include image assets under `assets/`, or Mermaid as the Chinese-labeled backup.
7. Include interaction demo details and webpage display rules.
8. Run the folder self-check before responding with artifact paths.
