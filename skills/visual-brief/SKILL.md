---
name: visual-brief
description: Use when WheelWise must create image-level visual explanation assets for a product brief, including concept visuals, decision maps, MVP roadmaps, module maps, architecture diagrams, demo mockups, validation funnels, or visual report placement.
---

# Visual Brief

Create visual explanations that make the recommendation easier to understand. Do not rely on Mermaid as the primary medium; Mermaid is a fallback for simple diagrams only.

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
2. For each visual, state the audience and report placement.
3. Write an image-generation prompt or concrete production method.
4. Explain why the visual improves understanding.
5. Apply `../../shared/references/decision-rationale-standard.md` to visual choices.
6. When UI/UX style guidance is needed, reference `../../shared/references/external-skills.md`; do not copy external skill content.

## Output Shape

```text
Visual title:
Type:
Explains:
Why it helps:
Image prompt or production method:
Placement in report:
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
