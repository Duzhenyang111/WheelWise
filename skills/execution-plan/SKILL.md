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
- Key risks and mitigations.

If an input is missing, state the assumption or route back through `using-wheelwise`.

## Plan Requirements

- Milestones in build order.
- Tasks small enough for a coding agent.
- File/module boundaries when a repository exists or stack is known.
- Test strategy per milestone.
- Acceptance criteria that prove behavior, not activity.
- Explicit reuse/vendor integration tasks.
- Validation experiments when the verdict is Validate First.

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
```
