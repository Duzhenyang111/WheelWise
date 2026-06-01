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

第一版先实现核心闭环。V2 新增 `product-strategy`、`technical-planning`、`visual-brief` 和 `ui-demo` 作为一级 skill。后续仍可继续把完整的 `market-research`、`customer-discovery`、`commercialization` 扩展成一级 skill。

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

WheelWise 可以生成 `wheelwise-report.html` 作为可选静态展示层。Markdown 仍然是事实来源。

HTML 展示应包含：

- 封面。
- 核心结论。
- 决策地图。
- MVP 路线图。
- 视觉说明。
- Demo 截面。
- 风险与验证。
- 执行计划。

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
