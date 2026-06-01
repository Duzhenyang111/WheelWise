---
name: parallel-research
description: Use when WheelWise faces broad, complex, or high-risk independent research questions that can be split across subagents or independent passes, especially market research, reuse option comparison, license review, security review, or architecture critique.
---

# Parallel Research

Support subagents, but do not use them by default.

## Trigger Conditions

Use parallel research only when one or more are true:

- The idea spans multiple independent markets, users, or product modules.
- Multiple SaaS/API/open-source options need comparison.
- The user asks for broad or fast research.
- A high-risk decision needs independent review.
- A single-threaded analysis may miss important evidence.

## Rules

- Do not use subagents for direct user clarification.
- Do not let subagents decide the final verdict.
- Give each subagent one narrow brief with success criteria.
- Ask for evidence, sources, and uncertainty.
- Synthesize contradictions in `using-wheelwise`.

## Output Shape

```text
Research question:
Why parallelism is justified:
Sub-briefs:
Evidence requested:
Synthesis plan:
Final owner: using-wheelwise
```

Use `templates/subagent-brief.md` when drafting subagent prompts.
