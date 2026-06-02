# Evidence Board

`evidence-board.md` is an internal WheelWise evidence ledger. It is not a final report section. Its findings should be synthesized into Chinese report sections such as `市场备注`, `用户假设`, `决策解释摘要`, `关键风险`, and `验证实验`.

## Summary

Idea summary: 款到助手帮助小型服务商整理逾期发票并生成可人工确认的收款提醒节奏。

Report folder: examples/ai-payment-chaser/

Last updated by skill: evidence-board

Evidence coverage: 市场痛点、竞品存在、用户假设、复用策略、商业化假设均已覆盖；真实用户上传和付费意愿仍需验证。

Highest-confidence evidence: 逾期发票和现金流压力是小企业常见问题，且现有会计和收款工具提供提醒或自动化功能。

Highest-impact evidence gap: 目标用户是否愿意把真实或脱敏发票交给新工具处理。

Key contradiction: 现有工具已有提醒能力，但款到助手假设用户仍需要更细腻、关系安全、人工可控的提醒体验。

Recommended next action: 进行 10 人用户验证，测试真实发票上传、提醒草稿接受度和付费意愿。

## Evidence Items

| Evidence item | Source / origin skill | Evidence type | Affected decision | Strength | Confidence | Assumption vs evidence | Contradiction | Evidence gap | Recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 小企业存在逾期发票和现金流压力 | market-research | Market source | Feasibility | High | Medium | Evidence | 无 | 需要更新来源日期和地区覆盖 | 保留为市场备注并在真实调研中复核 |
| Chaser、QuickBooks、Stripe、HoneyBook 等工具存在提醒或收款能力 | market-research | Competitor or substitute | Differentiation | High | Medium | Evidence | 竞品成熟会压缩差异化 | 需要比较最新定价和功能边界 | 用关系安全和人工可控做验证切口 |
| 小型服务商担心催款影响客户关系 | customer-discovery | Customer source | Product strategy | Medium | Medium | Assumption supported by directional evidence | 需要真实访谈确认 | 缺少直接访谈 | 访谈 10 个目标用户 |
| 提醒编排是核心差异化，应自研 | reuse-evaluator | Expert judgment | Reuse decision | Medium | Medium | Assumption | 无 | 需要原型测试提醒质量 | 用 prototype.html 测试草稿接受度 |
| 邮件发送和支付能力不应首轮自研 | reuse-evaluator | Vendor or API capability | Technical plan | High | Medium | Evidence and judgment | 供应商锁定 | 需要检查发送限制 | 技术探针验证邮件服务边界 |
| 免费试用后月订阅更易理解 | commercialization | Pricing or packaging | Commercialization | Medium | Low | Assumption | 用户可能不愿为小工具付费 | 缺少价格访谈 | 做价格敏感度访谈 |

## Decision Coverage

| Decision | Supporting evidence | Opposing evidence | Evidence gap | Confidence | Next action |
| --- | --- | --- | --- | --- | --- |
| 先验证 | 痛点存在，竞品存在说明市场有需求 | 竞品已有提醒功能 | 用户真实上传和付费意愿 | Medium | 先跑 10 人验证 |
| 网页应用 | 看板、状态、发送记录需要持久化 | 插件更贴近日常工作流 | 用户是否接受网页登录 | Medium | 首轮做轻量网页应用 |
| 自研提醒编排 | 差异化在语气、节奏和人工确认 | 提醒质量可能难超过通用模型 | 需要原型反馈 | Medium | 用模拟数据测试提醒草稿 |

## Evidence Gaps

| Gap | Why it matters | Affected phase | Suggested research or validation |
| --- | --- | --- | --- |
| 用户是否愿意上传发票 | 决定产品是否能进入真实工作流 | Gate2 / Delivery | 招募 10 个目标用户测试真实或脱敏发票 |
| 付费意愿 | 决定商业化路径 | Synthesis | 访谈价格阈值和替代成本 |
| 邮件发送合规与送达 | 决定技术方案和风险 | Delivery | 技术探针验证域名、退信、退订和发送限制 |

## Contradictions

| Contradiction | Sources or origin skills | Possible explanation | How to resolve |
| --- | --- | --- | --- |
| 竞品已有提醒功能，但仍建议验证款到助手 | market-research / product-strategy | 现有提醒可能偏机械，用户需要关系安全和人工可控 | 用原型测试用户是否觉得差异化有价值 |

## Assumptions To Carry Forward

| Assumption | Owner skill | Why acceptable now | When to revisit |
| --- | --- | --- | --- |
| 人工确认会提高信任 | product-strategy | 首轮可低成本验证 | 原型测试后 |
| 手动导入发票可接受 | technical-planning | 可避免早期复杂集成 | 用户拒绝上传时 |
| 月订阅可行 | commercialization | 小团队易理解 | 价格访谈后 |
