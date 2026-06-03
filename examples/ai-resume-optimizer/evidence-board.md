# Evidence Board

`evidence-board.md` is an internal WheelWise evidence ledger. It is not a final report section. Its findings should be synthesized into Chinese report sections such as `市场备注`, `用户假设`, `决策解释摘要`, `关键风险`, and `验证实验`.

## Summary

Idea summary: AI 简历优化器

Report folder: examples/ai-resume-optimizer/

Last updated by skill: using-wheelwise

Evidence coverage: product, user, risk, technical, commercialization gaps

Data sufficiency: enough for prototype validation

Pre-review state: 可进入原型验证

Highest-confidence evidence: 简历包含个人信息，隐私边界必须明确。

Highest-impact evidence gap: 付费意愿。

Key contradiction: 需求明确但替代工具强。

Direction shift summary: 完整开发收窄为原型验证。

User confirmation needed: No

Recommended next action: run 5-user prototype test

## Evidence Items

| Evidence item | Source / origin skill | Data source | Evidence type | Evidence classification | Claim type | Affected decision | Decision dependency | Strength | Confidence | Original assumption | Supports or opposes | Direction shift | User confirmation needed | Assumption vs evidence | Contradiction | Evidence gap | Rejected option rationale | Validation priority | Recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 求职者需要简历反馈 | customer-discovery | user hypothesis | Customer source | 推断 | recommendation | Pre-review state | user urgency | Medium | Medium | build full product | Supports | Minor | No | assumption-led | substitutes exist | real interviews | full build lacks evidence | High | interview users |
| 通用工具可替代浅层改写 | market-research | substitute analysis | Competitor or substitute | 事实 | risk | Differentiation | unique workflow | Medium | Medium | AI optimizer is differentiated | Opposes | Minor | No | evidence-led | demand still exists | current competitor pricing | generic optimizer rejected | High | competitor scan |
| 付费意愿未知 | commercialization | missing data | Evidence gap | 证据缺口 | validation requirement | Commercialization | willingness to pay | High | Low | users will pay | Opposes | None | No | gap | none | pricing test | paid plan rejected | High | price smoke test |

## Decision Coverage

| Decision | Original assumption | Options considered | Options rejected | Supporting evidence | Opposing evidence | Critical assumption dependency | Direction shift | User confirmation needed | Evidence gap | Confidence | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pre-review state | full build | full build; prototype; pause | full build | clear workflow | weak paid evidence | user trust | Minor | No | interviews | Medium | prototype validation |

## Evidence Gaps

| Gap | Why it matters | Affected phase | Validation priority | Suggested research or validation |
| --- | --- | --- | --- | --- |
| 付费意愿 | 决定是否进入收费实验 | Gate2 | High | price smoke test |
| 真实用户反馈 | 决定建议是否有差异 | prototype | High | 5 interviews |

## Supplemental Data Requirements

| Applicability class | Why this data is needed | Required data | Collection method | Minimum sample | Continue threshold | Stop threshold | Compliance items to confirm | Checklist version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| digital / personal information | validate user trust | user interviews | prototype test | 5 users | 3 positive | fewer than 2 positive | privacy boundary | V4.5-resume-001 |

## User Supplemental Data Received

| Received data | Source | Received date | Related checklist version | Evidence type | Threshold comparison | Time-sensitive recheck needed | Next Gate0 action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | None | None | V4.5-resume-001 | Evidence gap | Not met | Yes | keep Ready for prototype |

## Contradictions

| Contradiction | Sources or origin skills | Possible explanation | How to resolve |
| --- | --- | --- | --- |
| 需求存在但替代强 | market and customer review | shallow suggestions are commoditized | test explainable workflow |

## Direction Shifts

| Original direction | Recommended direction | Why original direction is weak | Evidence | Shift level | User confirmation status |
| --- | --- | --- | --- | --- | --- |
| full product | prototype validation | paid and differentiation evidence missing | evidence gap | Minor | not required |

## Assumptions To Carry Forward

| Assumption | Owner skill | Why acceptable now | When to revisit |
| --- | --- | --- | --- |
| users will try safe prototype | ui-demo | low-cost validation | after 5 tests |

## Review Scorecard Evidence

| Score dimension | Current score | Evidence classification | Evidence basis | Evidence gap | Next validation |
| --- | --- | --- | --- | --- | --- |
| 用户问题强度 | 4/5 | 推断 | clear job-seeking pain | interviews | user test |
| 证据充分度 | 2/5 | 证据缺口 | no first-hand data | interviews | collect data |
