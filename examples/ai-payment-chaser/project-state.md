# Project State

`project-state.md` is an internal WheelWise workflow state file. It is not a final report section and must not replace `report.md`.

## Identity

Idea summary: 款到助手是一个面向自由职业者和小型服务商的智能收款提醒工具，帮助用户整理逾期发票、生成礼貌坚定的提醒节奏，并人工确认发送。

Idea slug: ai-payment-chaser

Target customer: 自由职业者、小型服务商、小型代理公司、独立顾问。

Problem and urgency: 用户经常忘记跟进逾期发票，或担心催款伤害客户关系，导致现金流压力。

Current phase: Final report generated

Last updated by skill: using-wheelwise

Last updated reason: V4 示例补充内部状态文件。

## Routing State

Delivery surface: 网页应用

Secondary surfaces: 邮件插件、电子表格导入工具、浏览器插件

Workflow mode: V4 full workflow

Gate status: Gate2 Go

Gate rationale: 痛点真实且可以用轻量网页应用验证，但需要先验证用户是否愿意上传真实或脱敏发票。

Next skill: final-report complete

User input required: No

## Feasibility State

Early-screening verdict: Can continue

Full-review verdict: Go with validation-first delivery

Feasibility confidence: Medium

Stop / continue rationale: 可继续进入交付规划，但首轮应围绕真实发票上传和人工确认提醒验证。

Validation threshold: 10 个目标用户中至少 4 个愿意上传真实或脱敏逾期发票并试用提醒节奏。

## Strategy State

Product strategy summary: 以“关系安全的收款提醒”为核心差异化，先做导入发票、生成提醒计划、人工确认发送、追踪状态。

Minimum viable product scope: 发票导入、逾期看板、提醒草稿、人工确认、发送记录、回款状态。

Differentiation: 不是完整会计系统，而是帮助小团队用可控语气和节奏跟进逾期款。

Product wedge: 小型服务商每周一次的逾期发票跟进工作流。

## Evidence State

Evidence-board path: evidence-board.md

Evidence summary: 小企业逾期付款痛点有公开来源支持，竞品存在说明市场成熟，但差异化需要围绕关系安全和人工可控验证。

Evidence gaps: 目标用户真实上传意愿、付费意愿、邮件发送合规边界。

Contradictions: 现有会计软件已有提醒能力，但用户可能仍需要更细腻的语气和节奏控制。

Assumptions: 早期用户愿意手动导入发票；人工确认比全自动发送更容易建立信任。

## Reuse And Technical State

Reuse decisions summary: 提醒编排自研；邮件、支付、认证和基础托管优先购买或复用成熟服务。

Technical plan summary: 使用网页应用承载看板、规则、提醒草稿和发送记录；后端负责发票、提醒、状态和审计。

Technical spike status: 建议后续验证邮件发送域名、退信、合规和第三方接口限制。

Integration constraints: 先不深度接入 QuickBooks 或 Stripe，优先表格上传和手动确认。

## Commercial And Risk State

Commercialization summary: 免费试用后按月订阅；首轮验证小团队是否愿意为省时间和降低催款尴尬付费。

Risk summary: 信任门槛、数据隐私、竞品替代、邮件送达、付费意愿不确定。

Highest-priority risk: 用户不愿意把客户和发票数据交给新工具。

Mitigation summary: 先支持脱敏上传、人工确认和导出，不接管真实发送。

## Visual And Demo State

Visual/demo status: Done

Visual assets planned: 产品决策图、流程看板、提醒节奏说明。

Visual assets created: assets/concept.svg

Interaction demo type: 网页应用原型

Interaction demo path: prototype.html

## Final Report State

Final report status: Done

Report folder: examples/ai-payment-chaser/

Source report path: report.md

Web display path: index.html

Prototype path: prototype.html

Assets path: assets/

Self-check status: Passed for example folder

## Open Items

Open questions: 用户真实上传意愿、邮件发送合规、付费阈值。

Blocking unknowns: 无阻塞报告生成的问题；仍需真实用户验证。

Recommended next action: 按报告中的 7 天行动计划招募 10 个目标用户做发票上传和提醒草稿测试。
