# Evidence Board

`evidence-board.md` is an internal WheelWise evidence ledger. It is not a final report section. Its findings should be synthesized into Chinese report sections such as `市场备注`, `用户假设`, `决策解释摘要`, `关键风险`, and `验证实验`.

## Summary

Idea summary: 社区工具共享平台

Report folder: examples/community-tool-share/

Last updated by skill: using-wheelwise

Evidence coverage: product, local risk, technical, validation

Data sufficiency: enough for bounded experiment

Pre-review state: 可进入最小可行产品实验

Highest-confidence evidence: offline item sharing carries damage and dispute risk.

Highest-impact evidence gap: real supply and demand density.

Key contradiction: local sharing is attractive but operations may be heavy.

Direction shift summary: broad platform narrowed to one-community experiment.

User confirmation needed: No

Recommended next action: run pilot

## Evidence Items

| Evidence item | Source / origin skill | Data source | Evidence type | Evidence classification | Claim type | Affected decision | Decision dependency | Strength | Confidence | Original assumption | Supports or opposes | Direction shift | User confirmation needed | Assumption vs evidence | Contradiction | Evidence gap | Rejected option rationale | Validation priority | Recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 低频工具共享场景具体 | customer-discovery | scenario analysis | Customer source | 推断 | recommendation | Pre-review state | local demand | Medium | Medium | broad platform | Supports | Minor | No | inference | operations risk | real demand | broad platform rejected | High | pilot |
| 损坏纠纷风险存在 | risk-review | risk analysis | Risk | 事实 | risk | Risk | liability | High | High | easy sharing | Opposes | None | No | evidence-led | demand plausible | dispute rate | no-rules option rejected | High | rule test |
| 商业化未知 | commercialization | missing data | Evidence gap | 证据缺口 | validation requirement | Commercialization | fee acceptance | Medium | Low | service fee | Opposes | None | No | gap | none | fee test | fee plan rejected | Low | no-fee pilot |

## Decision Coverage

| Decision | Original assumption | Options considered | Options rejected | Supporting evidence | Opposing evidence | Critical assumption dependency | Direction shift | User confirmation needed | Evidence gap | Confidence | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pre-review state | broad platform | broad platform; community pilot; reference-only | broad platform | clear use case | operation risk | local trust | Minor | No | pilot data | Medium | MVP experiment |

## Evidence Gaps

| Gap | Why it matters | Affected phase | Validation priority | Suggested research or validation |
| --- | --- | --- | --- | --- |
| 供需密度 | 决定是否值得继续 | MVP experiment | High | community inventory and booking pilot |
| 纠纷率 | 决定风险可控性 | Risk | High | return inspection log |

## Supplemental Data Requirements

| Applicability class | Why this data is needed | Required data | Collection method | Minimum sample | Continue threshold | Stop threshold | Compliance items to confirm | Checklist version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| local community | offline fulfillment | supply and booking data | pilot | 20 bookings | low disputes | high disputes | liability, privacy, deposit | V4.5-community-001 |

## User Supplemental Data Received

| Received data | Source | Received date | Related checklist version | Evidence type | Threshold comparison | Time-sensitive recheck needed | Next Gate0 action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | None | None | V4.5-community-001 | Evidence gap | Not met | Yes | continue pilot |

## Contradictions

| Contradiction | Sources or origin skills | Possible explanation | How to resolve |
| --- | --- | --- | --- |
| Useful locally but hard operationally | product and risk review | offline item handling | bounded pilot |

## Direction Shifts

| Original direction | Recommended direction | Why original direction is weak | Evidence | Shift level | User confirmation status |
| --- | --- | --- | --- | --- | --- |
| broad platform | one-community experiment | scale evidence missing | gaps | Minor | not required |

## Assumptions To Carry Forward

| Assumption | Owner skill | Why acceptable now | When to revisit |
| --- | --- | --- | --- |
| residents will participate | product-strategy | pilot can test it | after 30 days |

## Review Scorecard Evidence

| Score dimension | Current score | Evidence classification | Evidence basis | Evidence gap | Next validation |
| --- | --- | --- | --- | --- | --- |
| 交付形态匹配 | 4/5 | 事实 | list and booking are simple | small program rules | prototype |
| 风险可控性 | 3/5 | 推断 | bounded pilot | dispute data | pilot |
