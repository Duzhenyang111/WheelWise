# Evidence Board

`evidence-board.md` is an internal WheelWise evidence ledger. It is not a final report section. Its findings should be synthesized into Chinese report sections such as `市场备注`, `用户假设`, `决策解释摘要`, `关键风险`, and `验证实验`.

## Summary

Idea summary: AI 付款跟进助手

Report folder: examples/ai-payment-chaser/

Last updated by skill: using-wheelwise

Evidence coverage: product, risk, technical, commercialization gaps

Data sufficiency: insufficient for build

Pre-review state: 需要补充关键证据

Highest-confidence evidence: automatic payment reminders may carry relationship and compliance risk.

Highest-impact evidence gap: willingness to use human-reviewed reminder drafts.

Key contradiction: cashflow pain may exist, but automation may be rejected.

Direction shift summary: automatic product shifted to evidence-gathering validation board.

User confirmation needed: No

Recommended next action: interview 5 teams

## Evidence Items

| Evidence item | Source / origin skill | Data source | Evidence type | Evidence classification | Claim type | Affected decision | Decision dependency | Strength | Confidence | Original assumption | Supports or opposes | Direction shift | User confirmation needed | Assumption vs evidence | Contradiction | Evidence gap | Rejected option rationale | Validation priority | Recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 小团队可能有回款提醒痛点 | customer-discovery | hypothesis | Customer source | 推断 | recommendation | Pre-review state | user urgency | Medium | Medium | build automated tool | Supports | Major | No | assumption-led | automation risk | workflow interviews | full build rejected | High | interview teams |
| 自动催付存在关系风险 | risk-review | risk analysis | Risk | 推断 | risk | Risk | trust | High | Medium | automate reminders | Opposes | Major | No | inference | cashflow need | compliance review | automatic sending rejected | High | compliance checklist |
| 付费意愿未知 | commercialization | missing data | Evidence gap | 证据缺口 | validation requirement | Commercialization | buyer budget | High | Low | teams will pay | Opposes | None | No | gap | none | price test | paid plan rejected | Medium | price interview |

## Decision Coverage

| Decision | Original assumption | Options considered | Options rejected | Supporting evidence | Opposing evidence | Critical assumption dependency | Direction shift | User confirmation needed | Evidence gap | Confidence | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pre-review state | automated tool | build; prototype; evidence-gathering | build | plausible cashflow pain | trust/compliance gaps | trust | Major | No | interviews | Low | collect evidence |

## Evidence Gaps

| Gap | Why it matters | Affected phase | Validation priority | Suggested research or validation |
| --- | --- | --- | --- | --- |
| 用户是否接受提醒草稿 | 决定是否可做产品 | Gate2 | High | 5 team interviews |
| 合规边界 | 阻止上线误判 | Risk | High | compliance checklist |

## Supplemental Data Requirements

| Applicability class | Why this data is needed | Required data | Collection method | Minimum sample | Continue threshold | Stop threshold | Compliance items to confirm | Checklist version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B2B finance operations | sensitive workflow | workflow interviews | interviews | 5 teams | 3 willing | fewer than 2 willing | privacy, messaging, payment | V4.5-payment-001 |

## User Supplemental Data Received

| Received data | Source | Received date | Related checklist version | Evidence type | Threshold comparison | Time-sensitive recheck needed | Next Gate0 action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | None | None | V4.5-payment-001 | Evidence gap | Not met | Yes | pause for evidence |

## Contradictions

| Contradiction | Sources or origin skills | Possible explanation | How to resolve |
| --- | --- | --- | --- |
| Need exists but automation risky | customer and risk review | customer relationship sensitivity | human-reviewed draft test |

## Direction Shifts

| Original direction | Recommended direction | Why original direction is weak | Evidence | Shift level | User confirmation status |
| --- | --- | --- | --- | --- | --- |
| automated payment chaser | evidence-gathering dashboard | trust and compliance gaps | risk and gaps | Major | not needed for evidence tasks |

## Assumptions To Carry Forward

| Assumption | Owner skill | Why acceptable now | When to revisit |
| --- | --- | --- | --- |
| teams will discuss workflow | customer-discovery | interviews are low risk | after interviews |

## Review Scorecard Evidence

| Score dimension | Current score | Evidence classification | Evidence basis | Evidence gap | Next validation |
| --- | --- | --- | --- | --- | --- |
| 证据充分度 | 1/5 | 证据缺口 | no interviews | workflow data | interview |
| 风险可控性 | 2/5 | 推断 | sensitive reminders | compliance | checklist |
