---
name: visual-brief
description: Use when WheelWise must create image-level visual explanation assets for a product brief, including concept visuals, decision maps, MVP roadmaps, module maps, architecture diagrams, demo mockups, validation funnels, or visual report placement.
---

# Visual Brief

Create visual explanations that make the recommendation easier to understand. Do not rely on Mermaid as the primary medium; Mermaid is a fallback only when image generation or real assets are unavailable. For V2.5+ final output, write visual results so they can be inserted into the Chinese Markdown report's `视觉说明` section and, when enabled, the HTML display file.

## Visual Types

Use one or more:

- Product concept image.
- Decision map.
- MVP roadmap.
- Module map.
- Architecture illustration.
- Demo mockup.
- Validation funnel.
- Before/after workflow.
- Stakeholder pitch visual.

## Process

1. Choose visuals that explain the hardest recommendation or tradeoff.
2. For each visual, state the audience and Chinese report placement.
3. Write an image-generation prompt or concrete production method.
4. Explain in Chinese why the visual improves understanding.
5. Apply `../../shared/references/decision-rationale-standard.md` to visual choices.
6. When UI/UX style guidance is needed, reference `../../shared/references/external-skills.md`; do not copy external skill content.
7. If image generation is available, generate or request real image assets and include Markdown references.
8. If image generation is unavailable, create a Mermaid fallback. At least one fallback must be a decision map, MVP roadmap, or validation funnel.
9. If an image asset exists, include a Markdown image reference such as:

```markdown
![产品概念图](./assets/visual-brief.png)
```

## Required Coverage

- At least one visual must explain the main decision path or tradeoff.
- Full reports should include two to three visuals when useful: product concept, decision map, MVP roadmap, validation funnel, module map, or demo mockup.
- Each visual must state whether it belongs in Markdown only, HTML display only, or both.
- All final-report field names must be Chinese. English labels such as `Visual Brief`, `Type`, or `Explains` must not be used as report section headings.

## Output Shape

```text
Visual title:
Type:
Explains:
Why it helps:
Image prompt or production method:
Placement in report:
Placement in HTML display:
Markdown image reference:
Fallback if image generation is unavailable:

Decision rationale:
Decision:
Why chosen:
Why alternatives lose:
Evidence:
Assumptions:
Risks:
Fallback:
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
HTML 展示位置：
Markdown 图片引用：
Mermaid fallback：
```
