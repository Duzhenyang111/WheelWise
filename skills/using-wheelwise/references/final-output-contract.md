# Final Output Contract

WheelWise final output is one Chinese Markdown report file, not only a structured chat answer.

## File Contract

- Default filename: `wheelwise-report.md`.
- If the user provides an idea name, use `wheelwise-report-<idea-slug>.md`.
- The report body must be fully Chinese.
- Titles, section names, table fields, decision explanations, risk notes, validation experiments, and execution-plan prose must be Chinese.
- Product names, technical stacks, code paths, commands, API names, and Build / Buy / Reuse / Fork / Reference labels may remain English.
- The chat response after generation should state the report path and a brief completion summary. Do not substitute a chat summary for the file.

## Required Chinese Sections

The report must include:

1. 项目标题
2. 想法摘要
3. 交付形态
4. 结论：构建 MVP / 先验证 / 暂停 / 放弃
5. 决策解释摘要
6. 目标用户
7. 问题与紧迫性
8. 市场备注
9. 用户假设
10. 差异化
11. MVP 范围
12. 产品策略
13. Build / Buy / Reuse / Fork / Reference 决策
14. 技术实现路径
15. 视觉说明
16. UI Demo / 交互 Demo
17. 商业化备注
18. 关键风险
19. 验证实验
20. Codex-ready 执行计划

## Integration Rules

- Decision rationales must use Chinese field names from `../../shared/references/decision-rationale-standard.md`.
- Visual brief images, image prompts, or production methods must be written into `视觉说明`.
- Existing image assets must be referenced with Markdown, for example `![产品概念图](./assets/visual-brief.png)`.
- UI demo output must be written into `UI Demo / 交互 Demo`, including demo path, run command, core interactions, mock data notes, and backend simulation boundary.
- The Codex-ready plan must include tasks to generate or update this Markdown report file.

Use `../../shared/templates/new-product-brief.md` for the full Chinese report.
