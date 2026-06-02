# WheelWise 中文实施方法

> 调研日期：2026-06-01  
> 目标：把 WheelWise 从一个项目概念，落成一个可复用、可扩展、可被 Codex/AI Agent 调用的 Build-vs-Buy-vs-Reuse 技能系统。

## 1. WheelWise 要解决什么

WheelWise 不是“让 AI 直接开写代码”的技能包。

它应该是一个写代码之前的产品与技术决策系统，帮助用户判断：

- 哪些模块应该购买 SaaS 或 API。
- 哪些模块应该直接复用成熟库、模板、starter kit。
- 哪些模块适合 fork 开源项目后改造。
- 哪些模块只适合参考，不适合直接复用。
- 哪些模块才值得从零自研。

一句话目标：

```text
用最快、最可靠、最低浪费的方式，把一个产品想法变成可执行的开发计划。
```

## 2. 核心原则

不要重复造轮子，除非“轮子本身”就是产品的核心差异化。

常见判断：

| 策略 | 适用场景 |
| --- | --- |
| Buy | 支付、认证、邮件、监控、托管、分析、客服等通用基础设施 |
| Reuse | UI kit、admin template、CMS、图表库、调度组件、工作流库 |
| Fork | 开源项目非常接近目标产品，但需要深度定制 |
| Reference | 产品体验、架构、交互、数据模型值得借鉴，但代码或协议不适合直接用 |
| Build | 核心业务逻辑、差异化工作流、专有算法、独特用户体验 |

WheelWise 的价值不是“什么都规划一遍”，而是快速识别哪里不该浪费工程时间。

## 3. 第一版不要做太大

第一版不要立刻做完整专家矩阵，而是先做一个紧凑闭环，并把每个环节做成一级 skill：

- `using-wheelwise`
- `idea-intake`
- `surface-strategy`
- `feasibility-review`
- `reuse-evaluator`
- `risk-review`
- `execution-plan`

同时加入 `parallel-research` 支持骨架，但不要把子代理作为默认路径。

### 3.1 Router

Router 是入口调度器。

它负责判断用户真正需要什么，而不是默认跑完整流程。

它还必须尽早判断目标实现形态。因为网站、Web App、移动 App、桌面 App、浏览器插件、API/SaaS、CLI、自动化工具的验证路径、可复用方案、技术架构、发布渠道和商业化方式都不一样。

典型路由：

| 用户请求 | 调用模块 |
| --- | --- |
| “我有一个 SaaS idea，帮我规划” | 全流程 |
| “这个功能要不要自己做” | Reuse Evaluator + Risk Review |
| “帮我找开源替代方案” | Reuse Evaluator |
| “帮我定 MVP 范围” | Idea Intake + Surface Strategy + Feasibility Review |
| “帮我生成 Codex 开发任务” | Execution Plan |
| “帮我看架构风险” | Risk Review |

Router 的关键输出：

- 任务类型。
- 实现形态。
- 需要调用的 skill。
- 是否需要联网搜索。
- 是否需要读取本地 repo。
- 最终输出格式。

### 3.2 Reuse Evaluator

这是 WheelWise 最核心的模块。

它负责研究已有解决方案，并对每个功能模块给出建议：

- Buy。
- Reuse。
- Fork。
- Reference。
- Build。

它应该评估：

- SaaS 产品。
- API。
- 开源仓库。
- starter kit。
- boilerplate。
- libraries。
- self-hosted tools。
- 常见 UX / 架构模式。

输出不应该只是“可以考虑 X”，而应该给出明确决策：

```text
认证：Buy，建议 Clerk/Auth0/Supabase Auth。
支付：Buy，建议 Stripe Checkout。
后台管理：Reuse，建议 shadcn + Tremor 或成熟 admin template。
核心推荐算法：Build，因为它是产品差异化。
```

### 3.3 Product + Architecture Planner

这个模块把产品想法变成 MVP 和技术方案。

它应该输出：

- 目标用户。
- 用户问题。
- 实现形态和交付载体。
- MVP 范围。
- 功能模块拆解。
- 用户故事。
- 验收标准。
- 技术栈建议。
- 数据模型草图。
- API / 集成方案。
- 部署方案。
- 架构假设。

它的重点不是写一份漂亮 PRD，而是把产品选择和工程代价绑定在一起。

### 3.4 Engineering Executor

这个模块把前面的判断转成 Codex 能执行的任务。

它应该输出：

- milestone。
- task。
- repo 结构。
- 文件/模块边界。
- 测试策略。
- 验收标准。
- Codex-ready prompt。
- 实施顺序。

好的输出应该像这样：

```text
Milestone 1: 项目骨架和认证

Task 1.1: 初始化 Next.js 项目
Task 1.2: 集成 Supabase Auth
Task 1.3: 添加受保护 dashboard route

验收标准：
- 未登录用户访问 dashboard 会跳转到登录页
- 登录用户可以看到 dashboard shell
- auth guard 有最小测试覆盖
```

## 4. 标准工作流

默认完整流程：

```text
用户想法
-> Router 判断任务类型
-> 判断实现形态
-> 功能模块拆解
-> 已有方案搜索
-> Build / Buy / Reuse / Fork / Reference 决策矩阵
-> MVP 范围
-> 技术架构
-> 风险审查
-> Codex-ready 开发计划
```

但 WheelWise 必须支持短流程。

如果用户只问“这个功能要不要用开源项目”，就不要输出完整 PRD、UI、roadmap。

实现形态应该影响工作流：

| 形态 | 规划重点 |
| --- | --- |
| 营销网站 | 定位、落地页结构、CMS/内容流程、数据分析、SEO、转化率、上线速度 |
| Web App | 认证、dashboard 流程、数据模型、权限、付费、前后端架构、部署 |
| 移动 App | 平台选择、应用商店限制、onboarding、推送、离线能力、设备 API |
| 桌面 App | 打包、更新、本地存储、系统集成、分发方式、跨平台取舍 |
| 浏览器插件 | 权限、浏览器 API、商店审核、content scripts、隐私、有限 UI 表面 |
| API/SaaS 后端 | API 设计、认证、限流、文档、SDK、可用性、可观测性、按量计费 |
| CLI/开发者工具 | 安装方式、命令设计、本地环境假设、文档、包分发 |
| 自动化/工作流工具 | trigger/action 模型、集成、权限、可靠性、重试和错误处理 |

## 5. 决策矩阵

每个重要模块都应该打分。

| 维度 | 问题 |
| --- | --- |
| MVP 速度 | 哪个方案最快能上线？ |
| 成本 | 直接成本和隐性成本是多少？ |
| 维护负担 | 谁负责长期维护？ |
| 供应商锁定 | 以后替换难不难？ |
| 定制难度 | 能不能满足产品的特殊需求？ |
| 安全风险 | 是否处理敏感数据、权限、支付或身份？ |
| 协议风险 | 是否允许商业使用？是否有 copyleft 影响？ |
| 差异化价值 | 这个模块是不是产品核心竞争力？ |
| 团队能力 | 团队是否能维护和修改？ |
| 长期扩展 | 用户量增长后是否还能支撑？ |
| 交付载体匹配度 | 这个方案是否适合当前形态：网站、App、插件、API、CLI 或自动化？ |

建议规则：

- 高风险、通用、非差异化模块，优先 Buy。
- 成熟稳定、低锁定、可替换模块，优先 Reuse。
- 开源项目接近目标但需要深度定制时，考虑 Fork。
- 法务、协议、架构或质量不适合直接用时，只 Reference。
- 真正形成产品差异化的模块才 Build。

## 6. 现成 Skill 调研

我在技能生态和 GitHub 上查了一轮。结论是：WheelWise 不应该所有子能力都自研，有些模块可以直接套用或参考成熟 skill。

### 6.1 UI/UX：强烈建议套用 UI UX Pro Max

候选：

- GitHub: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Skills: https://skills.sh/nexu-io/open-design/ui-ux-pro-max
- 查询到的安装量：约 947 installs。

为什么适合：

- 不只是单个 `SKILL.md`。
- 仓库包含 `data/`、`scripts/`、`templates/`。
- 有大量设计数据表，比如 colors、typography、icons、ux-guidelines、ui-reasoning、framework stacks。
- 有 Python 脚本，例如 design system 生成和搜索能力。
- 有多平台模板，包括 Codex、Claude、Cursor、Copilot 等。

建议在 WheelWise 中的定位：

```text
WheelWise 不自研完整 UI/UX 知识库。
WheelWise 的 UI/UX Designer 模块调用或借鉴 UI UX Pro Max。
WheelWise 只负责把产品类型、目标用户、功能模块、约束条件传给 UI/UX skill。
```

适合产出：

- 信息架构。
- 页面结构。
- UI 风格方向。
- 设计系统建议。
- 技术栈相关的 UI 实施建议。
- 反模式检查。

### 6.2 产品管理：建议参考 product-on-purpose/pm-skills

候选：

- GitHub: https://github.com/product-on-purpose/pm-skills
- Skills 示例：https://skills.sh/product-on-purpose/pm-skills/deliver-acceptance-criteria
- 查询到的相关技能安装量：`deliver-acceptance-criteria` 约 209 installs，`develop-adr` 约 168 installs。

为什么适合：

- 它是完整产品管理技能库，不是单一 md 文件。
- 仓库包含 `skills/`、`references/`、`commands/`、`docs/`、`_workflows/`、`agents/`、`.codex-plugin/`。
- 每个具体 skill 通常有自己的 `SKILL.md` 和 `references/`。
- 覆盖 PRD、用户故事、验收标准、ADR、竞品分析、市场规模、persona、OKR、仪表盘需求、实验设计等。

WheelWise 可直接参考或套用的模块：

- `deliver-prd`
- `deliver-user-stories`
- `deliver-acceptance-criteria`
- `develop-adr`
- `discover-competitive-analysis`
- `discover-market-sizing`
- `foundation-lean-canvas`
- `foundation-persona`
- `define-prioritization-framework`

建议在 WheelWise 中的定位：

```text
WheelWise 不重复造完整 PM 方法论。
WheelWise 的 Product Planner 可以复用 pm-skills 的 PRD、用户故事、验收标准、ADR 模板。
WheelWise 自己保留 build-vs-buy-vs-reuse 决策层。
```

### 6.3 架构与安全：可以参考 github/awesome-copilot，但不要直接依赖单个 skill

候选：

- GitHub: https://github.com/github/awesome-copilot
- Skills 示例：https://skills.sh/github/awesome-copilot/breakdown-epic-arch
- 查询到的 `breakdown-epic-arch` 安装量：约 8.6K installs。

为什么值得参考：

- 仓库规模很大，包含 `skills/`、`agents/`、`instructions/`、`workflows/`、`hooks/`、`docs/` 等。
- 有架构、合规、安全、供应链、代码库理解等方向的 skill。
- 其中一些 skill 只是单个 `SKILL.md`，但整个仓库本身有比较完整的 agent 资产结构。

可参考模块：

- `breakdown-epic-arch`
- `architecture-blueprint-generator`
- `agent-owasp-compliance`
- `agent-supply-chain`
- `acquire-codebase-knowledge`

建议在 WheelWise 中的定位：

```text
架构和安全模块可以参考 awesome-copilot 的结构和检查维度。
但 WheelWise 仍然需要自研自己的 risk-review skill，因为 build/buy/reuse 的风险判断更垂直。
```

### 6.4 Open Source Evaluator：目前没有找到完全匹配的成熟 skill

我查了 open source、security review、technical architecture、project planning、MVP scope 等关键词。

有一些相关候选：

- `shipshitdev/library@open-source-checker`
- `levnikolaevich/claude-code-skills@ln-645-open-source-replacer`
- `kostja94/marketing-skills@open-source-strategy`
- `slavingia/skills@mvp`
- `shipshitdev/library@mvp-architect`

但从 WheelWise 的目标看，它们都不是完全匹配。

WheelWise 需要的是：

```text
按产品模块查找 SaaS/API/OSS/starter kit
-> 比较成熟度、协议、维护活跃度、定制成本、替换成本
-> 给出 Buy / Reuse / Fork / Reference / Build 决策
```

这部分我建议自研，作为 WheelWise 的核心壁垒。

## 7. 我建议的 WheelWise 组合方式

WheelWise 应该采用 Superpowers 那种技能包结构：一个可安装的 skill pack，里面包含多个真正的 skill。

用户通常只需要调用主 skill：

```text
Use WheelWise to evaluate this idea: ...
```

然后主 skill 负责把工作路由到正确的内部 skill。内部模块不应该只是 reference 文件，而应该是一级 skill：每个都有自己的 `SKILL.md`、触发语义、工作流、references 和可选 tools。

建议技能包组成：

| Skill | 作用 |
| --- | --- |
| `using-wheelwise` | 主入口 skill。建立路由规则、流程纪律，并决定调用哪些 WheelWise 内部 skill。 |
| `idea-intake` | 把原始 idea 结构化，整理假设、目标用户、问题、约束、成功标准。 |
| `feasibility-review` | 判断 idea 应该推进、先验证、暂停，还是放弃。 |
| `market-research` | 研究市场类别、竞品、替代方案、用户需求和市场成熟度。 |
| `customer-discovery` | 定义 persona、JTBD、痛点强度、访谈问题和验证实验。 |
| `product-strategy` | 定义定位、差异化、MVP 范围、功能优先级和产品切入点。 |
| `surface-strategy` | 判断 idea 应该以网站、Web App、移动 App、桌面 App、插件、API/SaaS、CLI 或自动化工具的形式交付。 |
| `reuse-evaluator` | WheelWise 核心壁垒。按模块判断 Build / Buy / Reuse / Fork / Reference。 |
| `technical-planning` | 设计技术栈、架构、数据模型、集成、部署和实现路径。 |
| `commercialization` | 规划商业模式、定价、包装、GTM、渠道和早期变现测试。 |
| `risk-review` | 审查 license、安全、隐私、合规、依赖、市场和执行风险。 |
| `parallel-research` | 当 idea 范围较广、风险较高或模块较多时，按需派发子代理做独立研究或复核。 |
| `execution-plan` | 生成 Codex-ready milestones、任务、文件边界、测试和验收标准。 |

## 8. 推荐仓库结构

我建议 WheelWise 采用 Superpowers-style 的多 skill 包结构。

关键点：`skills/` 下面放多个独立 skill。共享 references、tools、templates 可以放在包级别，也可以放在具体 skill 内部。

第一版先实现核心闭环。V2 新增 `product-strategy`、`technical-planning`、`visual-brief` 和 `ui-demo` 作为一级 skill。V2.8 将完整的 `market-research`、`customer-discovery`、`commercialization` 扩展成一级 skill，并加入当前来源调研标准。

```text
wheelwise/
  README.md
  IMPLEMENTATION_METHOD.md
  IMPLEMENTATION_METHOD_ZH.md
  .codex-plugin/
    plugin.json
  skills/
    using-wheelwise/
      SKILL.md
      references/
        routing-map.md
        workflow-modes.md
        final-output-contract.md
    idea-intake/
      SKILL.md
    feasibility-review/
      SKILL.md
    product-strategy/
      SKILL.md
    surface-strategy/
      SKILL.md
    reuse-evaluator/
      SKILL.md
    technical-planning/
      SKILL.md
    risk-review/
      SKILL.md
    visual-brief/
      SKILL.md
    ui-demo/
      SKILL.md
      references/
        ui-ux-pro-max-adaptation.md
    parallel-research/
      SKILL.md
      templates/
        subagent-brief.md
    execution-plan/
      SKILL.md
  shared/
    references/
      build-buy-reuse-vocabulary.md
      decision-rationale-standard.md
      output-quality-bar.md
      external-skills.md
    templates/
      new-product-brief.md
      final-wheelwise-report.md
      visual-brief.md
      ui-demo-spec.md
  examples/
    ai-resume-optimizer.md
```

## 9. 主 Skill 路由怎么做

`using-wheelwise` 应该像 Superpowers 的主入口 skill 一样：先加载，建立流程，然后决定必须使用哪些专门 skill。

它不应该包含所有领域知识。它应该保持简洁，把工作路由到正确的内部 skill。

路由示例：

```text
用户只有一个模糊 idea
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review

用户问这个 idea 值不值得做
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review
-> reuse-evaluator
-> risk-review

用户问已验证 idea 如何实现
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review
-> reuse-evaluator
-> risk-review
-> execution-plan

用户问大范围市场、竞品或方案调研
-> using-wheelwise
-> parallel-research（当工作可以拆成独立调研时）
-> using-wheelwise 汇总最终判断
```

外部 skill 仍然有用，但它们是参考资源或可选依赖，不是 WheelWise 的结构本身。

示例：

```text
UI/UX 工作可以参考 UI UX Pro Max。
PRD、用户故事、ADR 工作可以参考 pm-skills。
架构和安全检查可以参考 awesome-copilot。
```

但 WheelWise 本身仍然是一个多 skill 包，而不是一个 skill 下面塞很多 markdown 章节。

## 10. 子代理策略

WheelWise 应该支持子代理，但不要默认每次都开子代理。

规则：

```text
默认：主 skill 串行路由。
复杂 idea：按需使用子代理。
高风险判断：需要独立复核。
```

子代理是可选的加速和复核工具，不是默认执行模型。主 `using-wheelwise` skill 仍然负责综合、判断和最终报告。

适合开子代理的场景：

| 模块 | 为什么适合 |
| --- | --- |
| `market-research` | 竞品、替代方案、市场类别和成熟度可以并行调研。 |
| `reuse-evaluator` | SaaS/API/开源方案可以按产品模块独立评估。 |
| `risk-review` | license、安全、隐私、依赖风险适合独立复核。 |
| `commercialization` | 定价、GTM 渠道、包装方式和变现测试可以分开探索。 |
| `technical-planning` | 复杂架构适合让独立视角做一次反方审查。 |

不适合开子代理的场景：

| 模块 | 原因 |
| --- | --- |
| `idea-intake` | 需要直接和用户澄清。 |
| `surface-strategy` | 应该先形成统一交付方向，再进入深入分析。 |
| `product-strategy` | 需要综合市场、用户和实现上下文做整体判断。 |
| `execution-plan` | 最终执行任务必须由主代理统一收敛，避免计划碎片化。 |

`parallel-research` 只在满足以下一个或多个条件时触发：

- idea 涉及多个独立市场、用户群或产品模块。
- 需要比较多个 SaaS/API/开源方案。
- 用户要求快速、广泛调研。
- 决策风险较高，需要独立复核。
- 主代理判断单线程分析可能遗漏重要视角。

子代理输出应该被视为证据，而不是最终决策。`using-wheelwise` 必须综合发现、解决矛盾、说明信心等级，并产出最终建议。

## 11. 第一阶段实施计划

### Phase 1：建立 Superpowers-style 技能包骨架

交付：

- README.md。
- 中文和英文实施方法。
- `.codex-plugin/plugin.json`。
- `skills/using-wheelwise/SKILL.md`。
- 初始内部 skill 目录。
- build-vs-buy 决策矩阵模板。
- 一个完整示例。

### Phase 2：实现主路由 Skill

交付：

- routing map。
- workflow modes。
- final output contract。
- 每个内部 skill 的调用规则。
- 短流程和完整流程的判断规则。

### Phase 3：自研 Reuse Evaluator

这是最重要的阶段。

交付：

- OSS 评估清单。
- SaaS/API 评估清单。
- license 风险基础说明。
- 模块拆解模板。
- GitHub repo 评分脚本雏形。
- 最终推荐格式。

### Phase 4：实现产品与商业化 Skill

交付：

- `idea-intake`
- `feasibility-review`
- `market-research`
- `customer-discovery`
- `product-strategy`
- `surface-strategy`
- `commercialization`

每一个都应该是真正的 skill 文件夹，包含 `SKILL.md` 和它需要的 references/templates。

### Phase 5：实现子代理支持

交付：

- `parallel-research`
- 子代理触发规则。
- research brief 模板。
- synthesis report 模板。
- 子代理复核何时必须、何时可选的规则。

### Phase 6：Codex-ready 输出

交付：

- `technical-planning`
- `risk-review`
- `execution-plan`
- 工程任务模板。
- milestone 模板。
- 验收标准模板。
- 测试策略模板。
- 示例项目的完整 Codex 执行计划。

### Phase 7：真实项目反复测试

用真实产品想法测试 WheelWise：

- AI 简历优化网站。
- 预约系统。
- B2B SaaS dashboard。
- AI agent marketplace。
- 内容管理系统。

每次测试都检查：

- 是否过度自研。
- 是否漏掉成熟替代方案。
- 是否忽略协议风险。
- 是否输出了无法执行的任务。
- 是否给出了明确推荐，而不是模糊建议。

## 12. 最重要的产品边界

WheelWise 的核心不是 UI、PRD、架构图或项目管理。

这些都有现成 skill 可以借力。

WheelWise 真正应该自研的是：

```text
产品模块拆解
+ 现成方案搜索
+ build/buy/reuse/fork/reference 决策
+ 风险审查
+ Codex-ready 开发任务生成
```

这才是它区别于普通产品规划工具和普通 coding agent 的地方。

## 13. V2 升级：可解释、可展示、可交互 Demo 的产品方案

V2 保留 V1 的 Superpowers-style 多 skill pack 架构。`using-wheelwise` 仍然是唯一主入口，新增能力必须作为一级 skill 文件夹加入，而不是塞进一个大型 reference 目录。

V2 把 WheelWise 从“Codex-ready 执行计划”升级为：

```text
可解释的产品决策
+ 图片级视觉说明
+ 可交互 demo 或 simulator 方案
+ Codex-ready 执行计划
```

### 13.1 V2 主流程

```text
idea-intake
-> surface-strategy
-> feasibility-review
-> product-strategy
-> reuse-evaluator
-> technical-planning
-> risk-review
-> visual-brief
-> ui-demo when applicable
-> execution-plan
-> New Product Brief
```

### 13.2 V2 一级 Skill

| Skill | 作用 |
| --- | --- |
| `product-strategy` | 连接 `feasibility-review`，输出 positioning、differentiation、MVP scope、user-facing workflow、feature priority、product wedge 和 validation focus。 |
| `technical-planning` | 连接 `reuse-evaluator`，输出 stack、architecture、data model、integrations、deployment path、surface constraints 和 technical risks，并且不能和模块决策冲突。 |
| `visual-brief` | 生成图片级视觉说明规格，例如产品概念图、决策地图、MVP 路线图、模块地图、架构示意图、demo mockup 和验证漏斗。Mermaid 只能作为 fallback。 |
| `ui-demo` | 用 mock data、local state、fixtures、static JSON、localStorage 或 simulated API 规划完整可交互 demo。API/CLI/自动化产品则输出 playground、terminal simulator、request explorer 或 workflow simulator。 |

### 13.3 决策解释标准

每个关键决策都必须包含：

```text
Decision
Why chosen
Why alternatives lose
Evidence
Assumptions
Risks
Fallback
Confidence
```

适用范围包括 verdict、delivery surface、product strategy、Build / Buy / Reuse / Fork / Reference 决策、technical stack、visual brief、UI demo、commercialization notes 和 execution order。

### 13.4 Visual Brief 规则

`visual-brief` 应该让推荐方案更容易被利益相关者和用户理解。

可输出：

- 产品概念图。
- 决策地图。
- MVP 路线图。
- 模块地图。
- 架构示意图。
- Demo mockup。
- 验证漏斗。

每个 visual 必须包含 title、type、解释内容、为什么有助理解、图片生成 prompt 或制作方法、fallback 和报告放置位置。它可以把 UI UX Pro Max 作为设计智能参考，但不能复制外部 skill 内容。

### 13.5 UI Demo 规则

`ui-demo` 应该为用户可见产品规划一个不依赖真实后端的完整可交互前端 demo。

Demo 必须包含页面/屏幕结构、核心流程、可点击导航、表单、状态变化、mock 数据、loading/empty/error/success 状态、响应式布局、组件结构、运行方式和 demo 边界。

对没有传统 UI 的产品：

- API/SaaS backend：API playground、request/response explorer、docs preview 或 workflow simulator。
- CLI/dev tool：带命令、输出、错误和成功状态的 terminal simulator。
- 自动化/workflow tool：带 run history、retry、error 和 success 状态的 trigger/action simulator。

### 13.6 V2 仓库新增结构

```text
skills/
  product-strategy/
    SKILL.md
  technical-planning/
    SKILL.md
  visual-brief/
    SKILL.md
  ui-demo/
    SKILL.md
    references/
      ui-ux-pro-max-adaptation.md
shared/
  references/
    decision-rationale-standard.md
  templates/
    visual-brief.md
    ui-demo-spec.md
```

### 13.7 V2 最终报告要求

完整 New Product Brief 必须包含：

- Idea summary。
- Delivery surface。
- Verdict。
- Decision rationale summary。
- Target customer。
- Problem and urgency。
- Market notes。
- Customer assumptions。
- Differentiation。
- MVP scope。
- Product strategy。
- Build / Buy / Reuse / Fork / Reference decisions。
- Technical implementation path。
- Visual Brief。
- UI Demo / Interaction Demo。
- Commercialization notes。
- Key risks。
- Validation experiments。
- Codex-ready execution plan。

`execution-plan` 必须包含生成 visual brief 和 UI demo 或 simulator 的任务。

## 14. V2.5 升级：单个全中文 Markdown 报告文件

V2.5 不推翻 V2 架构。`using-wheelwise` 仍然是唯一主入口，`visual-brief`、`ui-demo`、`product-strategy`、`technical-planning` 和 `decision-rationale-standard` 继续作为一级能力保留。

V2.5 只升级最终产物契约：

```text
WheelWise 最终输出 = 一个完整的全中文 Markdown 报告文件
```

默认文件名：

```text
wheelwise-report.md
```

如果用户提供了 idea 名称，可以使用：

```text
wheelwise-report-<idea-slug>.md
```

报告正文必须全中文。专有名词、技术栈、产品名、代码路径、命令、API 名称以及 Build / Buy / Reuse / Fork / Reference 标签可以保留英文。

### 14.1 V2.5 必需报告章节

Markdown 报告必须包含以下中文章节：

1. 项目标题
2. 想法摘要
3. 交付形态
4. 结论：构建 MVP / 先验证 / 暂停 / 放弃
5. 决策解释摘要
6. 目标用户
7. 问题与紧迫性
8. 市场备注
9. 用户假设
10. 差异化
11. MVP 范围
12. 产品策略
13. Build / Buy / Reuse / Fork / Reference 决策
14. 技术实现路径
15. 视觉说明
16. UI Demo / 交互 Demo
17. 商业化备注
18. 关键风险
19. 验证实验
20. Codex-ready 执行计划

### 14.2 中文决策解释

最终报告中的每个关键决策都必须解释：

```text
决策是什么
为什么选择它
为什么不选替代方案
证据
假设
风险
fallback
信心等级
```

适用范围包括 verdict、delivery surface、product strategy、Build / Buy / Reuse / Fork / Reference 决策、technical stack、visual brief、UI demo、commercialization notes 和 execution order。

### 14.3 视觉和 Demo 汇入规则

`visual-brief` 输出必须写入 `视觉说明` 章节。如果有图片资产，用 Markdown 引用：

```markdown
![产品概念图](./assets/visual-brief.png)
```

如果只有 prompt 或制作方法，也必须写在同一章节。

`ui-demo` 输出必须写入 `UI Demo / 交互 Demo` 章节，并包含：

- Demo 路径。
- 运行命令。
- 核心交互。
- mock 数据说明。
- loading / empty / error / success 状态。
- 未接入真实后端的范围。

### 14.4 执行计划要求

`execution-plan` 必须包含生成或更新中文 Markdown 报告文件的任务。最终聊天回复只需要说明报告路径和简短完成摘要，不能用聊天摘要替代报告文件。

## 15. V2.5.1 升级：递进式中文报告与可选 HTML 展示

V2.5.1 基于真实生成结果的问题收紧最终报告契约。要避免的情况是：报告像内部 skill 输出拼接、残留英文模块标题、没有图片或图表、开头过薄、结尾没有具体行动建议。

### 15.1 递进式报告结构

最终 Markdown 报告必须是面向读者的产品方案，而不是内部模块堆叠：

```text
报告说明与阅读导览
-> 用户与问题
-> 决策与推荐方案
-> 视觉说明与交互 Demo
-> 商业化、风险与验证
-> Codex-ready 执行计划
-> 最终建议与下一步行动
```

实际报告章节必须使用中文。不要把 `Idea Intake`、`Surface Strategy`、`Reuse Evaluator`、`Technical Planning`、`Risk Review`、`UI Demo Scope`、`MVP Execution Plan` 等英文内部模块名作为章节标题。

### 15.2 必需开头与结尾

开头 `报告说明与阅读导览` 必须包含：

- 报告目的。
- 适用阶段。
- 核心结论预览。
- 阅读方式。

结尾 `最终建议与下一步行动` 必须包含：

- 一句话判断。
- 7 天行动。
- 14 天行动。
- 30 天行动。
- go/no-go 或继续/停止条件。

### 15.3 视觉优先级

有生图能力时，WheelWise 应优先生成真实图片资产，并在 Markdown 报告中使用普通 Markdown 图片语法引用。

如果没有生图能力，必须降级使用 Mermaid。至少一个 fallback 视觉应是决策地图、MVP 路线图或验证漏斗。

### 15.4 HTML 展示层

WheelWise 可以在报告文件夹内生成 `index.html` 作为静态展示层。`report.md` 仍然是事实来源。

HTML 展示层应该把报告重新设计成网页，而不是简单把 Markdown 标题和表格转成 HTML。它应使用布局、图片、图表、视觉层级和动效，让读者更容易理解报告。

HTML 展示应包含：

- 封面。
- 核心结论。
- 决策地图。
- MVP 路线图。
- 视觉说明。
- 产品或交互预览。
- 风险与验证。
- 执行计划。
- 对报告实质内容的设计化呈现。

如果产品有用户可见界面，WheelWise 还应该创建或指定独立交互原型页，例如 `prototype.html`。网站想法展示网站界面；网页应用展示工作台；移动、桌面、插件、接口、命令行和自动化产品都用 HTML 模拟对应载体。

UI UX Pro Max 或其他 UI/UX skill 可以作为 HTML 展示、视觉说明或 Demo 规划的设计智能参考，但 WheelWise 不能复制外部 skill 内容。

### 15.5 自检与校验

最终回复前，`using-wheelwise` 必须检查：

- 报告文件符合 `wheelwise-report*.md` 命名规则。
- 所有必需中文章节存在，并按递进顺序排列。
- 开头与结尾足够详细。
- 没有禁止的英文 skill 模块标题。
- `视觉说明` 包含图片引用或 Mermaid fallback。
- `UI Demo / 交互 Demo` 包含路径、运行方式、核心交互、mock 数据、状态覆盖和后端边界。
- `HTML 展示文件` 即使本轮不生成 HTML，也要记录 HTML 展示规则。

仓库包含 `scripts/check_report_contract.py`，用于按这些契约规则校验最终报告和模板。

## 16. V2.7 升级：报告文件夹与全中文用户可见产物

V2.7 覆盖 V2.5 的单文件输出规则。最终产物现在是一个完整报告文件夹，而不是孤立的 Markdown 文件。

默认输出：

```text
wheelwise-report/
  report.md
  index.html
  assets/
    concept.png
    decision-map.png
    roadmap.png
```

如果有 idea slug：

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  assets/
```

`report.md` 是源报告。`index.html` 是来自同一份中文报告的展示层。`assets/` 存放所有生成或选择的图片和静态资源。

### 16.1 全中文可见文字

生成产物中的所有面向用户可见文字必须使用中文：

- Markdown 正文、章节名、表格字段、图片替代文字和图表标签。
- 网页文案、导航标签、按钮、说明文字和图片替代文字。
- 生成图片内的文字，如果图片需要文字。

技术栈、命令、文件路径、包名、API 名称和代码标识符可以保留英文，因为它们是技术引用，不是展示文案。

最终产物使用这些中文展示词：

```text
自研
购买
复用
分叉改造
参考
网页应用
软件服务
最小可行产品
演示
模拟数据
兜底方案
继续 / 停止条件
可交给 Codex 执行的计划
```

如果生图模型无法稳定渲染中文文字，优先生成无文字图片，并把中文说明放在 `report.md` 和 `index.html` 中。

### 16.2 Skill 更新

- `using-wheelwise` 负责最终汇总、路由纪律、文件夹生成规则和全中文可见文字自检。
- `final-output-contract.md` 定义文件夹结构、命名、必需文件、图片规则和校验规则。
- `new-product-brief.md` 和 `final-wheelwise-report.md` 使用 `report.md` 作为源报告，并增加输出文件夹字段。
- `visual-brief` 把图片资产保存到 `assets/`，并要求图片内文字中文，或使用无文字图片。
- `report-visualization` 指定 `index.html` 为报告可视化解释层，`ui-demo` 指定独立的 `prototype.html`；两者都要求可见界面文案中文。
- `execution-plan` 包含创建报告文件夹、写入 `report.md`、生成 `index.html`、保存资产和运行契约检查的任务。

### 16.3 校验

生成产物使用文件夹模式校验：

```text
python scripts/check_report_contract.py wheelwise-report-<idea-slug> --folder
```

示例目录如果故意使用更短目录名，使用 `--skip-filename`：

```text
python scripts/check_report_contract.py examples/ai-resume-optimizer --folder --skip-filename
```

校验器必须拒绝缺少 `report.md`、缺少 `index.html`、缺少 `assets/`、缺少图片资产、Markdown 图片引用失效、HTML 图片引用失效，以及 Markdown 或网页可见文字中出现常见英文展示词的情况。

## 17. V4 升级：总控状态、证据中枢与 Gate 流程

V4 不推翻 Superpowers 风格多 skill pack 架构，而是优化 skill 流转：`using-wheelwise` 升级为总控、路由、状态管理、Gate 控制、自检和最终报告汇总者。当前实现基线是 V4.4。

### 17.1 内部状态

V4 新增两个内部产物：

```text
project-state.md
evidence-board.md
```

`project-state.md` 记录 idea summary、current phase、delivery surface、Gate0 Evidence Intake status、evidence requirement status、supplemental-data checklist version、resume instruction、gate status、feasibility verdict、product strategy summary、reuse decisions summary、technical plan summary、commercialization summary、risk summary、visual/demo status、final report status、open questions、assumptions 和 last updated by skill。

`evidence-board.md` 汇总 `market-research`、`customer-discovery`、`reuse-evaluator`、可选 technical spike、商业化工作、动态补充数据要求和用户补回的数据。字段包括 evidence item、source/origin skill、evidence type、affected decision、strength、confidence、assumption vs evidence、contradiction、evidence gap、threshold comparison、time-sensitive recheck needed 和 recommended next action。

这两个文件是内部流程产物，不替代 `report.md`，也不能作为最终报告章节标题。

### 17.2 V4 流程

```text
using-wheelwise
-> 读取/更新 project-state.md
-> Phase 0 Intake：idea-intake -> Gate0 Evidence Intake -> surface-strategy -> feasibility-review: early-screening
-> Gate1
-> Phase 1 Discovery：market-research + customer-discovery + reuse-evaluator + 可选 technical spike -> evidence-board
-> Phase 2 Synthesis：product-strategy -> commercialization -> risk-review -> feasibility-review: full-review
-> Gate2
-> Phase 3 Delivery：technical-planning -> visual-brief -> ui-demo 或 simulator -> report-visualization -> execution-plan
-> final-report：report.md + index.html + prototype.html + assets/
```

### 17.3 Gate 规则

Gate0 使用统一的 `Gate0 Evidence Intake`，只返回三类状态：

- `Ready`：基础路由信息和证据足够，可以继续。
- `Need Basic Input`：只缺基础路由信息，最多问三个问题：面向谁、先验证还是做最小可行产品、时间/预算/技术栈限制。
- `Field Data Required`：缺实地、市场、合规、供应链、硬件、平台、B2B、内容/社群或服务类一手数据，不能给高信心判断。

如果基础信息和一手数据都缺，Gate0 先问最少基础问题，同时返回第一阶段补充数据清单，不能拆成两次打断。

`Field Data Required` 的清单必须根据 idea 类型组合动态生成，包含适用性分类、为什么需要这些数据、数据项、采集方法、最小样本、继续阈值、停止阈值、合规待确认项和清单版本。`project-state.md` 记录可恢复暂停状态；用户之后补回数据时，`evidence-board.md` 记录这些数据。

Gate1 使用 `feasibility-review: early-screening`：

- 不能继续或不建议现在继续：输出停止理由并结束。
- 可以继续：自动进入 Discovery。

Gate2 使用 `feasibility-review: full-review`：

- `Go`：自动进入 Delivery。
- `Pivot`、`Need More Evidence`、`Kill`、`Park`：询问用户下一步方向。

### 17.4 最终自检

最终报告前，`using-wheelwise` 必须确认：

- `project-state.md` 对当前阶段足够完整；如果 Gate0 暂停，必须包含恢复字段。
- `evidence-board.md` 有证据或明确证据缺口。
- Gate 状态与可行性结论一致。
- 关键决策都有解释。
- 视觉说明有图片、图片生成说明或 Mermaid 兜底图。
- UI 演示或模拟器存在。
- `report.md`、`index.html`、`assets/` 满足契约。
- 生成产物的可见文字中文化。

## 附录 A. V4 保留的 V3 展示能力

V4 保留 V3 的设计化 HTML 展示与独立交互原型要求：

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  prototype.html
  assets/
    concept.svg
```

`report.md` 仍然是事实来源。`index.html` 是设计化报告展示页，不是普通 Markdown 转换页。它应该使用高信息密度视觉图、图表、卡片、时间线、产品截图或模拟图、动效和清晰视觉层级，帮助小白读者理解可行性、产品价值、实施路径和下一步行动。

`prototype.html` 或等效页面是产品载体模拟页。它应使用本地模拟数据展示目标用户体验：

- 网站：落地页和转化流程。
- 网页应用：仪表盘、工作台、表单、状态变化和核心工作流。
- 移动应用：手机框、移动导航和触控式流程。
- 桌面应用：桌面窗口、本地文件流程、菜单和面板。
- 浏览器插件：弹窗、选项页和网页上下文。
- 接口/后端服务：请求构造器、响应查看器、文档、日志和密钥管理。
- 命令行/开发者工具：终端命令、配置、错误和成功状态。
- 自动化/工作流工具：触发器、动作、运行历史、重试、错误和成功路径。

V4 完整报告还应包含一张高信息密度视觉资产，例如产品决策海报或实施地图。单薄的装饰图不足以支撑完整 WheelWise 报告。

## 附录 B. V4.1 视觉交付架构

V4.1 保持 V4 的产品判断流程不变，重点重新定义最终交付物职责：

```text
report.md       = 源报告和事实来源
index.html      = 完整报告的可视化解释层
prototype.html  = 独立产品原型或模拟器
assets/         = SVG、图片、图表、Mermaid 兜底图和静态视觉资源
```

Phase 3 Delivery 调整为：

```text
technical-planning -> visual-brief -> ui-demo 或 simulator -> report-visualization -> execution-plan
```

`report-visualization` 是新的一级内部 skill。它读取 `report.md`、`project-state.md`、`evidence-board.md`、视觉资产和原型路径，负责创建或规划 `index.html`。该页面必须把报告实质内容转成视觉结构，例如结论横幅、用户卡片、前后流程、市场矩阵、假设卡、范围看板、模块决策图、架构图、商业化漏斗、风险矩阵、验证看板、执行时间线和行动卡。它不能是 Markdown 转网页、第二份报告、短摘要页或原型替代品。

`ui-demo` 现在只负责 `prototype.html` 或等效模拟器。它必须用本地数据、交互控件、状态变化、加载 / 空状态 / 错误 / 成功状态、响应式布局和后端边界说明来模拟目标产品载体。

`visual-brief` 不得依赖 AI 生图。中文密集的信息图应优先使用 SVG 或 HTML/CSS。AI 生图只适合无文字或少文字概念场景。Mermaid 是最后兜底，不是默认方案。

V4 校验器应拒绝缺少 `prototype.html`、缺少导航或视觉模块的薄弱 `index.html`、没有交互和状态变化的原型、失效的本地资产引用、缺少非装饰性资产、用户可见英文展示文案、缺少 Gate0 恢复字段，以及缺少动态补充数据清单字段。

## 附录 C. V4.4 Gate0 Evidence Intake

V4.4 解决的是“询问基础信息”和“返回补充数据要求”之间的歧义。Gate0 现在是一个统一数据入口，而不是两个相邻决策点。

V4.4 行为：

- 数字产品或软件产品，如果目标用户、问题、交付形态、约束和验证意图足够清楚，通常返回 `Ready`。
- “做个 App”这类模糊想法返回 `Need Basic Input`，只问最少路由问题。
- 本地、线下、实体、强监管、供应链、平台依赖、B2B、内容/社群或服务类 idea，如果缺一手证据，返回 `Field Data Required`。
- 复合 idea 要叠加清单模块。例如“南昌中学门口卖一元火鸡面”应识别为本地/线下 + 实体食品 + 未成年人场景 + 地域强相关，Gate0 应要求人流、许可/合规、竞品价格、单份成本、试卖销量、投诉和被中断风险，而不是返回通用市场规模清单。
- 用户之后补回实地数据时，WheelWise 从 Gate0 Evidence Intake 复核继续，把数据写入 `evidence-board.md`，对照继续/停止阈值，并刷新或标记市场、竞品、法规、平台规则等时间敏感证据。

V4.4 计划里的场景例子还没有做成可执行测试。当前已提交的验证覆盖静态契约检查、报告模板检查、Python 语法检查和空白检查。后续可以补脚本化 prompt 场景测试，覆盖 SaaS、南昌学校摆摊、模糊 App、补数据恢复和证据过期复核等案例。
