---
name: visual-brief
description: Use when WheelWise must create image-level visual explanation assets for a product brief, including concept visuals, decision maps, MVP roadmaps, module maps, architecture diagrams, demo mockups, validation funnels, or visual report placement.
---

# Visual Brief

Create visual explanations that make the recommendation easier to understand. Do not rely on Mermaid as the primary medium; Mermaid is a fallback for simple diagrams only. For V2.5 final output, write visual results so they can be inserted into the Chinese Markdown report's `视觉说明` section.

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
7. If an image asset exists, include a Markdown image reference such as:

```markdown
![产品概念图](./assets/visual-brief.png)
```

## Output Shape

```text
Visual title:
Type:
Explains:
Why it helps:
Image prompt or production method:
Placement in report:
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
Markdown 图片引用：
```
