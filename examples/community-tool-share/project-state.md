# Project State

`project-state.md` is an internal WheelWise workflow state file. It is not a final report section and must not replace `report.md`.

## Identity

Idea summary: 邻里工具共享管家是一个社区工具借用网页应用，帮助居民把电钻、梯子、露营灯等低频工具登记、预约、押金、归还提醒和信用记录集中管理。

Idea slug: community-tool-share

Target customer: 小区业委会、社区运营者、共享空间管理员，以及愿意共享低频工具的居民。

Problem and urgency: 居民偶尔需要工具但不想购买；邻里私下借用缺少记录、押金和归还提醒，容易产生纠纷。

Current phase: Final report generated

Last updated by skill: using-wheelwise

Last updated reason: 生成 V4 示例报告文件夹。

## Routing State

Delivery surface: 网页应用

Secondary surfaces: 微信群表单、社区公告页、移动端小程序

Workflow mode: V4 full workflow

Gate status: Gate2 Go

Gate rationale: 想法可低成本验证，最大不确定性是工具主上架意愿和社区治理规则，而不是基础技术可行性。

Next skill: final-report complete

User input required: No

## Feasibility State

Early-screening verdict: Can continue

Full-review verdict: Go with validation-first delivery

Feasibility confidence: Medium

Stop / continue rationale: 可以继续做验证型最小可行产品，但首轮必须限制在一个社区和少量工具。

Validation threshold: 三周内至少 20 件工具上架、10 次预约、8 次顺利归还，且管理员每周处理时间低于 2 小时。

## Strategy State

Product strategy summary: 先做一个轻量社区工具目录和预约工作台，验证工具主、借用者和管理员三方是否愿意使用。

Minimum viable product scope: 工具登记、可用时间、预约申请、押金说明、归还提醒、状态记录、管理员审核。

Differentiation: 不是普通二手平台，而是围绕同社区信任、归还提醒和管理员治理的轻量借用闭环。

Product wedge: 一个小区或共享空间里的低频高价值工具借用。

## Evidence State

Evidence-board path: evidence-board.md

Evidence summary: 证据以产品假设和社区场景推理为主，未做联网市场调研；最大证据缺口是居民真实上架意愿和押金接受度。

Evidence gaps: 工具主上架意愿、押金争议、损坏赔偿规则、社区管理员执行负担。

Contradictions: 熟人社区更容易建立信任，但也更容易因为损坏和逾期归还产生尴尬。

Assumptions: 社区内存在足够闲置低频工具；管理员愿意承担轻量审核；押金和信用记录能降低纠纷。

## Reuse And Technical State

Reuse decisions summary: 工具目录和预约状态自研；登录、通知、表单和静态展示可复用成熟组件或服务。

Technical plan summary: 用网页应用承载居民目录和管理员工作台；后端记录工具、预约、押金说明、归还状态和提醒任务。

Technical spike status: 不需要复杂技术探针；需要验证通知渠道和押金规则。

Integration constraints: 首轮不接入真实支付，押金只记录线下规则和确认状态。

## Commercial And Risk State

Commercialization summary: 首轮不向居民收费，面向社区运营者收取轻量工具管理服务费或作为社区服务试点。

Risk summary: 治理成本、损坏纠纷、押金争议、工具安全责任、供需密度不足。

Highest-priority risk: 工具损坏或逾期归还导致信任受损。

Mitigation summary: 首轮限制工具类型、使用押金说明、管理员审核、归还确认和黑名单机制。

## Visual And Demo State

Visual/demo status: Done

Visual assets planned: 产品概念图、借用流程、验证条件说明。

Visual assets created: assets/concept.svg

Interaction demo type: 网页应用原型

Interaction demo path: prototype.html

## Final Report State

Final report status: Done

Report folder: examples/community-tool-share/

Source report path: report.md

Web display path: index.html

Prototype path: prototype.html

Assets path: assets/

Self-check status: Passed

## Open Items

Open questions: 哪些工具适合首批上架；押金是否必须；管理员审核是否可持续；工具损坏责任如何写清楚。

Blocking unknowns: 无阻塞报告生成的问题；真实社区验证前不应扩大开发。

Recommended next action: 找一个小区或共享空间，用 20 件工具跑三周人工辅助试点。
