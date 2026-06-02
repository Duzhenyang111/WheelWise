---
name: visual-brief
description: Use when WheelWise must create image-level visual explanation assets for a product brief, including concept visuals, decision maps, minimum viable product roadmaps, module maps, architecture diagrams, demo mockups, validation funnels, or visual report placement.
---

# Visual Brief

Create visual explanations that make the recommendation easier to understand. Do not depend on AI image generation. For final output, save visual assets under the report folder's `assets/` directory and write visual results into `report.md`, while `report-visualization` decides how those assets appear in `index.html`.

## Visual Types

Use one or more:

- Product concept image.
- Decision map.
- Minimum viable product roadmap.
- Module map.
- Architecture illustration.
- Demo mockup.
- Validation funnel.
- Before/after workflow.
- Stakeholder pitch visual.

## Process

1. Choose visuals that explain the hardest recommendation or tradeoff.
2. For each visual, state the audience and Chinese report placement.
3. Choose the production method before writing a prompt.
4. Explain in Chinese why the visual improves understanding.
5. Apply `../../shared/references/decision-rationale-standard.md` to visual choices.
6. When UI/UX style guidance is needed, reference `../../shared/references/external-skills.md`; do not copy external skill content.
7. For Chinese text-heavy visuals, prefer SVG or HTML/CSS static diagrams saved under `assets/`.
8. Use AI image generation only for no-text or low-text concept scenes, atmosphere, product context, or user scenario visuals.
9. Image prompts must require all text inside the image to be Chinese. If accurate Chinese text is uncertain, generate text-free images and put explanations in `report.md` and `index.html`.
10. Use Mermaid only as the final fallback when SVG/HTML/CSS, existing assets, or image generation are not practical. At least one backup visual must be a decision map, roadmap, or validation funnel, and all node labels must be Chinese.
11. If an image asset exists, include a Markdown image reference such as:

```markdown
![产品概念图](./assets/concept.png)
```

## V4 State Integration

- Read `project-state.md` and `evidence-board.md` before selecting visuals.
- Use visuals to explain the strongest decision path, biggest contradiction, or highest-priority evidence gap.
- Update `project-state.md` with visual assets planned, visual assets created, visual/demo status, and last updated by skill.

## Required Coverage

- At least one visual must explain the main decision path or tradeoff.
- At least one visual for a full report should be a dense product-information asset such as an SVG decision infographic, architecture/data-flow diagram, roadmap, risk matrix, validation board, or module decision map.
- Full reports should include two to three visuals when useful: product concept, decision map, roadmap, validation funnel, module map, or interaction mockup.
- Avoid thin decorative concept art as the only visual. The primary visual must help a reader understand the idea without reading the whole report.
- Each visual must state whether it belongs in source report only, webpage display only, or both.
- All final-report field names must be Chinese. English labels such as `Visual Brief`, `Type`, or `Explains` must not be used as report section headings.
- Final visible output must use the Chinese display vocabulary from `using-wheelwise/references/final-output-contract.md`.

## Output Shape

```text
Visual title:
Type:
Explains:
Why it helps:
Production method:
Image prompt when applicable:
Placement in report:
Placement in webpage display:
Markdown image reference:
无法生成图片时的中文兜底方案:

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

In the final report, use Chinese field names:

```text
视觉标题：
类型：
解释内容：
为什么帮助理解推荐方案：
图片生成 prompt / 制作方法：
放置位置：
网页展示位置：
Markdown 图片引用：
Mermaid 兜底图表：
```
