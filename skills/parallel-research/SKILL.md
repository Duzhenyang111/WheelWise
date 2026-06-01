---
name: parallel-research
description: Use when WheelWise faces broad, complex, or high-risk independent research questions that can be split across subagents or independent passes, especially market research, customer discovery evidence, commercialization research, reuse option comparison, license review, security review, or architecture critique.
---

# Parallel Research

Support subagents, but do not use them by default.

## Trigger Conditions

Use parallel research only when one or more are true:

- The idea spans multiple independent markets, users, or product modules.
- Multiple SaaS/API/open-source options need comparison.
- Market, customer, or commercialization research can be split by competitor set, user segment, channel, pricing model, or geography.
- The user asks for broad or fast research.
- A high-risk decision needs independent review.
- A single-threaded analysis may miss important evidence.

## Rules

- Do not use subagents for direct user clarification.
- Do not let subagents decide the final verdict.
- Give each subagent one narrow brief with success criteria.
- Ask for evidence, sources, and uncertainty.
- Use `../../shared/references/web-research-standard.md` for briefs that depend on current market, customer, pricing, channel, policy, vendor, or repository facts.
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
