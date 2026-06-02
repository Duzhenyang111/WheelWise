# Web Research Standard

Use this standard whenever current facts can materially change a WheelWise decision.

## Must Browse When

Browse current sources when the decision depends on:

- Competitor capabilities, positioning, pricing, packaging, or channel motion.
- Market trends, user demand signals, category maturity, or recent platform changes.
- User complaints, reviews, community discussions, workflows, or adoption objections.
- Open-source repository health, license status, release cadence, or maintainership.
- Vendor capabilities, API limits, terms, privacy posture, or integration constraints.
- Channel rules, platform policies, app-store rules, payment restrictions, or compliance obligations.

If browsing is unavailable, state that the evidence is missing and lower confidence. Do not invent facts.

## Minimum Evidence

For market, customer, and commercialization research, collect enough evidence to support the decision:

- Search date.
- Source URL.
- Source type: vendor page, pricing page, documentation, marketplace listing, review site, community thread, public report, repository, regulatory/policy page, or article.
- Key finding.
- Evidence strength: High, Medium, or Low.
- Unknowns or follow-up research needed.

Prefer primary sources for pricing, policies, terms, repository health, and vendor capabilities. Use community or review sources for user pain and adoption signals, but label them as anecdotal unless they are broad and consistent.

## Evidence Hygiene

- Separate source evidence from analysis assumptions.
- Do not claim a market size, competitor count, pricing model, user pain, or channel performance without a source.
- Use recent sources when the fact is likely to change.
- Note contradictory evidence instead of smoothing it away.
- Tie evidence back to the WheelWise decision it affects: feasibility, product strategy, reuse choice, risk, commercialization, validation, or execution order.
- When public web evidence cannot answer a local, offline, physical, regulated, supply-chain, or hardware question, mark the required first-hand data instead of substituting generic market commentary.

## Counter-Evidence Discipline

Treat user-provided claims as original assumptions until evidence supports them. Research must look for evidence that weakens the user's initial direction, not only evidence that supports it.

Actively check for:

- Stronger competitors, substitutes, or existing workflows that make the idea less differentiated.
- Weak user urgency, unclear buyer, low adoption intent, or poor willingness to pay.
- Pricing, channel, platform, policy, compliance, or distribution constraints that make the proposed path unrealistic.
- Vendor, API, open-source, license, repository health, data-access, or technical dependency risks that undermine the technical plan.
- Evidence that supports a different customer, problem, delivery surface, product wedge, business model, compliance boundary, or technical path.

When counter-evidence changes the recommendation, record why the original direction is weak, how much the recommendation shifted, and whether user confirmation is required before continuing.

## Output Fields

Use these fields in research-heavy outputs:

```text
搜索时间：
来源：
来源类型：
关键发现：
证据强度：
影响的决策：
数据来源：
证据类型：
原始假设：
支持 / 反驳：
偏移程度：
是否需要用户确认：
证据缺口：
仍未知：
```
