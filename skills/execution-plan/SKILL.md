---
name: execution-plan
description: Use when WheelWise must turn a product brief, surface decision, feasibility verdict, reuse matrix, risk review, visual brief, demo plan, and final Chinese report folder requirement into executable milestones, tasks, acceptance criteria, tests, and implementation order.
---

# Execution Plan

Create a plan Codex can execute without rediscovering product decisions.

## Inputs Required

- Idea brief.
- Delivery surface.
- Feasibility verdict.
- V4.5 pre-review state.
- Next-stage recommendation.
- Review scorecard and comparable idea score.
- Minimum viable product scope.
- 自研 / 购买 / 复用 / 分叉改造 / 参考 matrix.
- Product strategy.
- Technical plan.
- Key risks and mitigations.
- Evidence coverage, evidence gaps, and required supplemental data.
- Critical assumption dependencies, options considered, options rejected, and validation priority.
- Gate0 Evidence Intake status, supplemental-data checklist version, resume instruction, and whether the workflow is waiting for user supplemental data.
- Compliance and launch prerequisites when relevant.
- Visual brief.
- UI demo or simulator spec when applicable.
- Final Chinese report folder path: `wheelwise-report/` or `wheelwise-report-<idea-slug>/`.
- Internal project state path: `project-state.md`.
- Internal evidence board path: `evidence-board.md`.
- Source report path: `report.md`.
- Webpage display path: `index.html`.
- Interactive prototype path: `prototype.html`.
- Asset directory path: `assets/`.

If an input is missing, state the assumption or route back through `using-wheelwise`.

## Plan Requirements

- Milestones in state-appropriate order.
- Tasks small enough for a coding agent.
- File/module boundaries when a repository exists or stack is known.
- Test strategy per milestone.
- Acceptance criteria that prove behavior, not activity.
- Explicit reuse/vendor integration tasks.
- Explicit visual-brief generation tasks and asset save paths under `assets/`.
- Explicit UI demo or API/CLI/workflow simulator tasks when applicable.
- Explicit task to create or update the final Chinese report folder.
- Explicit task to create or update `project-state.md`.
- Explicit task to create or update `evidence-board.md`.
- Explicit task to generate or update `report.md`.
- Explicit task to generate or update `index.html` as the report visualization layer.
- Explicit task to generate or update `prototype.html` as the independent product prototype or simulator.
- Report contract checks: folder structure, Chinese visible text, required visual assets or fallback, complete prototype details, webpage visualization record, UI quality baseline, and final action advice.
- Validation experiments when the pre-review state is `可进入原型验证` or `需要补充关键证据`.
- Pivot review tasks when the pre-review state is `建议转向后再评审`.
- Pause or revisit-trigger tasks when the pre-review state is `建议暂缓`.
- Stop or alternative-learning tasks when the pre-review state is `建议放弃`.
- Reference-preservation tasks when the pre-review state is `仅作为参考`.
- Supplemental-data tasks when Gate0 Evidence Intake returns `Field Data Required`, including collection method, minimum sample, continue/stop thresholds, compliance items to confirm, and resume-from-Gate0 instruction.
- Compliance reminder tasks for the final report when China mainland launch, App, website, platform, AI, payments, personal information, minors, or regulated industries are involved.
- Decision rationale for execution order using `../../shared/references/decision-rationale-standard.md`.

Do not produce a full build plan when the pre-review state is `需要补充关键证据`, `建议转向后再评审`, `建议暂缓`, `建议放弃`, or `仅作为参考`. Produce validation, pivot, pause, stop, or reference-preservation tasks instead.

## Output Shape

```text
Milestone:
Goal:
Pre-review state:
Plan type:
Tasks:
Files/modules:
Dependencies:
Tests:
Acceptance criteria:
可交给 Codex 执行的提示:
Visual-brief task:
UI demo or simulator task:
Webpage display task:
Interactive prototype task:
Source report task:
Report self-check:
Decision rationale:
```

The source report task must say where `report.md` will be written and must require visible output text to be Chinese. It must also require `报告说明与阅读导览`, `预评审结论`, `评审委员会意见`, `决策记录与选项排除`, `横向比较评分`, `视觉说明`, `交互演示`, `网页展示文件`, and `最终建议与下一步行动`.

The source report task must also require `执行摘要`, `调研方法与证据等级`, `市场吸引力与机会窗口`, `竞品与替代方案分析`, `合规与上线前置项`, `分阶段验证计划`, and `前端展示与交互原型`.

The webpage display task must say that `index.html` is a report visualization layer sourced from `report.md`, not a replacement source of truth or a plain Markdown conversion. It must require visual modules that cover the report's pre-review state, scorecard, conclusion, research method/evidence level, review-board viewpoints, user/problem, decision path, options rejected, market/alternatives, compliance prerequisites, scope, reuse decisions, technical path, commercialization, risks, staged validation plan, execution or validation plan, and final action advice. If no webpage file is created in the current run, include a concrete task for creating it later.

The interactive prototype task must say that `prototype.html` is separate from `index.html` and must simulate the delivery surface with local data, user inputs, clickable interactions, loading/empty/error/success states, responsive behavior, and a clear backend boundary. For non-digital ideas, it may be a validation dashboard, cost/margin calculator, field-data recorder, compliance checklist, supplier tracker, or pilot decision panel. If no prototype is created in the current run, include a concrete task for creating it later.
