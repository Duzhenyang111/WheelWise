# Evidence Board

`evidence-board.md` is an internal WheelWise evidence ledger. It is not a final report section. Its findings should be synthesized into Chinese report sections such as `市场备注`, `用户假设`, `决策解释摘要`, `关键风险`, and `验证实验`.

## Summary

Idea summary: 邻里工具共享管家帮助社区登记低频工具、处理预约、归还提醒和信用记录。

Report folder: examples/community-tool-share/

Last updated by skill: evidence-board

Evidence coverage: 当前示例未联网调研，证据以场景推理、产品假设和执行验证设计为主；市场、用户和商业化均明确缺口。

Highest-confidence evidence: 低频工具购买和存放成本高，社区内借用需要记录和归还提醒。

Highest-impact evidence gap: 工具主是否愿意把工具登记给邻居借用，以及押金规则是否被接受。

Key contradiction: 同社区关系有助于信任，但工具损坏和逾期归还也可能让邻里关系更敏感。

Recommended next action: 通过一个社区的三周试点收集真实上架、预约、归还和纠纷数据。

## Evidence Items

| Evidence item | Source / origin skill | Evidence type | Affected decision | Strength | Confidence | Assumption vs evidence | Contradiction | Evidence gap | Recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 低频工具存在购买和存放成本 | idea-intake | Assumption | Feasibility | Medium | Medium | Assumption | 无 | 需要用户访谈确认高频工具类型 | 访谈 10 位居民 |
| 社区借用需要记录、归还提醒和责任边界 | customer-discovery | Assumption | Product strategy | High | Medium | Assumption | 熟人关系可能减少也可能放大纠纷 | 缺少真实纠纷案例 | 试点中记录逾期和损坏情况 |
| 网页应用能承载目录、预约和管理员审核 | surface-strategy | Expert judgment | Delivery surface | High | Medium | Evidence from product reasoning | 移动端更方便但开发更重 | 需要验证居民是否接受网页入口 | 首轮用二维码访问网页 |
| 工具目录和预约状态应自研 | reuse-evaluator | Expert judgment | Reuse decision | Medium | Medium | Assumption | 表单工具也可临时代替 | 需要验证流程复杂度 | 先用轻量自研原型 |
| 首轮不接入真实支付 | technical-planning | Expert judgment | Technical plan | High | High | Evidence from risk reduction | 押金线下处理会增加管理员负担 | 需要试点记录押金争议 | 只记录押金状态和说明 |
| 社区运营者可能是付费方 | commercialization | Assumption | Commercialization | Medium | Low | Assumption | 居民也可能愿意按次支付 | 缺少付费访谈 | 访谈社区管理员 |

## Decision Coverage

| Decision | Supporting evidence | Opposing evidence | Evidence gap | Confidence | Next action |
| --- | --- | --- | --- | --- | --- |
| 先验证 | 可低成本试点，风险主要在治理和采用 | 没有真实社区数据 | 上架意愿和押金接受度 | Medium | 三周试点 |
| 网页应用 | 能快速做目录、预约、审核和状态 | 移动端更方便 | 网页入口接受度 | Medium | 用二维码入口测试 |
| 不接真实支付 | 降低合规和技术复杂度 | 押金线下处理麻烦 | 押金争议数据 | High | 只记录押金确认 |

## Evidence Gaps

| Gap | Why it matters | Affected phase | Suggested research or validation |
| --- | --- | --- | --- |
| 工具主上架意愿 | 决定供给密度 | Discovery / Gate2 | 招募 20 件工具做试点 |
| 借用者预约意愿 | 决定需求强度 | Discovery / Delivery | 三周内观察 10 次预约 |
| 押金和损坏赔偿规则 | 决定风险和信任 | Synthesis / Risk | 试点前让居民阅读并反馈规则 |
| 管理员负担 | 决定商业化和运营可持续性 | Commercialization | 记录每周处理时间 |

## Contradictions

| Contradiction | Sources or origin skills | Possible explanation | How to resolve |
| --- | --- | --- | --- |
| 熟人关系既增加信任，也增加纠纷尴尬 | customer-discovery / risk-review | 借用前信任高，出问题后关系成本更高 | 用押金说明、归还确认和管理员介入降低风险 |

## Assumptions To Carry Forward

| Assumption | Owner skill | Why acceptable now | When to revisit |
| --- | --- | --- | --- |
| 一个社区能凑够 20 件可借工具 | customer-discovery | 首轮试点可快速验证 | 招募不足时 |
| 管理员愿意每周投入少量时间 | commercialization | 社区服务试点可接受 | 每周超过 2 小时时 |
| 网页二维码入口足够方便 | surface-strategy | 避免移动端开发成本 | 居民使用率低时 |
