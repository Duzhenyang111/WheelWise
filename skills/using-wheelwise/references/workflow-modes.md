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
4. Define product strategy and MVP workflow.
5. Decompose modules.
6. Decide Build / Buy / Reuse / Fork / Reference.
7. Create technical plan aligned with reuse decisions.
8. Review risks.
9. Create visual brief.
10. Create UI demo or simulator spec when applicable.
11. Produce Codex-ready execution plan.

## Research-Heavy Workflow

Use when competitor facts, pricing, license status, repository health, or vendor capabilities materially change the answer. Browse current sources when available. Use `parallel-research` only when the work can be split into independent research briefs.

## Demo-Ready Workflow

Use when the user needs something presentable to stakeholders or test users.

Steps:
1. Run core workflow through `technical-planning`.
2. Run `visual-brief` for image-level explanation assets.
3. Run `ui-demo` for user-visible surfaces, or simulator mode for API/CLI/automation.
4. Ensure `execution-plan` includes tasks to generate the visual brief and demo.
