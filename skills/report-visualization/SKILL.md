---
name: report-visualization
description: Use when WheelWise must turn report.md, project-state.md, evidence-board.md, visual assets, and prototype links into index.html as a complete visual explanation layer for a Chinese product report.
---

# Report Visualization

`report-visualization` owns `index.html`. It turns the source report into a visual explanation layer. It does not write a second source report and it does not create the product prototype.

## Inputs

- Source report: `report.md`.
- Internal state: `project-state.md`.
- Evidence ledger: `evidence-board.md`.
- Visual asset plan and created assets from `visual-brief`.
- Prototype or simulator path from `ui-demo`, normally `prototype.html`.
- Final output contract: `../../skills/using-wheelwise/references/final-output-contract.md`.
- External UI/UX references: `../../shared/references/external-skills.md` when design direction or anti-pattern review is needed.

## Core Rule

`index.html` must help a reader understand the whole report faster. It must reinterpret report substance as visual structures: cards, boards, matrices, timelines, flows, charts, diagrams, and action panels.

Do not make `index.html`:

- A Markdown-to-HTML conversion.
- A second version of `report.md`.
- A short landing page or summary page.
- A product prototype.
- A page whose only visual is one decorative concept image.

## Visualization Mapping

Choose modules according to the report content. Do not hard-code every report into the same layout.

| Report content | Preferred visual expression |
| --- | --- |
| Verdict and confidence | Verdict banner, decision score strip, confidence meter |
| Delivery surface | Surface badge row, surface tradeoff comparison |
| Target customer | Persona cards, segment cards, role map |
| Problem and urgency | Before/after workflow, pain timeline, scenario storyboard |
| Market and alternatives | Competitor matrix, substitute landscape, evidence board |
| User assumptions | Assumption cards, validation priority map |
| Differentiation | Value wedge, comparison matrix, positioning map |
| Minimum viable product scope | In/out board, release cutline, feature priority grid |
| Build/buy/reuse/fork/reference decisions | Module decision graph, dependency map, sourcing matrix |
| Technical path | Architecture diagram, data flow, integration boundary map |
| Commercialization | Pricing cards, channel funnel, monetization hypothesis board |
| Risks | Risk matrix, mitigation board, risk radar |
| Validation experiments | Experiment kanban, validation funnel, evidence gap board |
| Execution plan | 7/14/30 day timeline, milestone roadmap, task swimlanes |
| Final recommendation | Action cards, continue/stop condition panel |

## Required Coverage

For a full report, `index.html` must include:

- Navigation or anchored section index.
- Cover or hero area with project name and core conclusion.
- Verdict banner.
- At least eight substantive visual modules, selected from the mapping above.
- A visible link or callout to `prototype.html` when a prototype exists.
- At least one local asset from `assets/`.
- A report coverage marker or section structure that covers the main report areas: user/problem, decision/solution, visual/prototype, commercialization/risk/validation, execution/next actions.
- Responsive layout for mobile and desktop.
- Chinese visible text, including headings, labels, buttons, alt text, and chart labels.

## Visual Production Rules

- Use `assets/` for generated or selected images, SVGs, diagrams, and static resources.
- Prefer SVG or HTML/CSS for Chinese text-heavy diagrams, module maps, architecture diagrams, roadmaps, decision maps, risk matrices, and validation boards.
- Use AI image generation only for no-text or low-text concept scenes, product mood images, or environmental visuals.
- Use Mermaid only as a final fallback when SVG/HTML/CSS or real assets are not practical.
- If an image model may render Chinese poorly, make the image text-free and place Chinese explanation in HTML and Markdown.

## Prototype Boundary

`index.html` may contain a prototype preview, screenshot, embedded card, or link, but it must not replace `prototype.html`.

`prototype.html` is owned by `ui-demo` and must simulate the product surface with local data and state. `index.html` explains the report; `prototype.html` lets users try the concept.

## Output Shape

```text
网页展示文件:
源报告:
原型入口:
视觉系统:
模块覆盖:
使用资产:
响应式布局:
不是 Markdown 转网页的证据:
未覆盖内容和原因:
自检结果:

Decision rationale:
Decision:
Why chosen:
Why alternatives lose:
Evidence:
Assumptions:
Risks:
兜底方案:
Confidence:
```

In final user-visible report sections, use Chinese field names only:

```text
网页展示文件：
源报告关系：
视觉系统：
展示模块：
原型入口：
使用资产：
响应式说明：
质量自检：
```
