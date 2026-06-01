---
name: execution-plan
description: Use when WheelWise must turn a product brief, surface decision, feasibility verdict, reuse matrix, and risk review into Codex-ready milestones, tasks, acceptance criteria, tests, and implementation order.
---

# Execution Plan

Create a plan Codex can execute without rediscovering product decisions.

## Inputs Required

- Idea brief.
- Delivery surface.
- Feasibility verdict.
- MVP scope.
- Build / Buy / Reuse / Fork / Reference matrix.
- Product strategy.
- Technical plan.
- Key risks and mitigations.
- Visual brief.
- UI demo or simulator spec when applicable.

If an input is missing, state the assumption or route back through `using-wheelwise`.

## Plan Requirements

- Milestones in build order.
- Tasks small enough for a coding agent.
- File/module boundaries when a repository exists or stack is known.
- Test strategy per milestone.
- Acceptance criteria that prove behavior, not activity.
- Explicit reuse/vendor integration tasks.
- Explicit visual-brief generation tasks.
- Explicit UI demo or API/CLI/workflow simulator tasks when applicable.
- Validation experiments when the verdict is Validate First.
- Decision rationale for execution order using `../../shared/references/decision-rationale-standard.md`.

## Output Shape

```text
Milestone:
Goal:
Tasks:
Files/modules:
Dependencies:
Tests:
Acceptance criteria:
Codex-ready prompt:
Visual-brief task:
UI demo or simulator task:
Decision rationale:
```
