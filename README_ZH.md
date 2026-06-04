# WheelWise

WheelWise 是一个面向 Codex 的 Superpowers 风格多 skill 包，也是一个 **AI Idea Pre-review Board / AI 产品预评审系统**。它面向产品想法早期阶段，用结构化评审流程把模糊 idea 推进成可判断、可验证、可执行的产品立项方案。它可以按需路由到快速判断、专项评估或完整预评审；每条路线都会生成报告文件夹和 `report.md`，完整预评审才默认生成报告可视化网页、独立交互原型、视觉资产和内部状态文件。

WheelWise 不是正式审批系统，也不替代真实用户调研、真实业务数据、合规审批、法律意见、投资判断或组织决策。它适合在正式评审之前，把模糊 idea 变成可讨论、可验证、可比较、可决策的预评审包。

主入口始终是 `using-wheelwise`。用户只需要调用这个 skill；后续由它路由到内部 skill，并负责最终汇总。

```text
Use $using-wheelwise to evaluate this idea: ...
```

英文文档见 [README.md](README.md)。

## WheelWise 解决什么问题

WheelWise 适合在正式开发、团队评审或最小可行产品投入前使用。它帮助判断一个产品想法应该继续研究、进入原型验证、进入最小可行产品实验、转向后再评审、暂缓、放弃，还是仅作为参考；也会判断哪些模块应该自研、购买、复用、分叉改造，或仅作为参考。

WheelWise 不默认每次运行完整流程。用户请求深度不清楚时，主入口会先确认三种路线之一：

| 路线 | 适合场景 | 默认产物 |
| --- | --- | --- |
| 快速判断 | 判断 idea 是否值得继续 | `wheelwise-report-<idea-slug>/report.md` |
| 专项评估 | 只看 MVP、复用、验证、技术、商业化、风险或执行计划中的一个问题 | `wheelwise-report-<idea-slug>/report.md` |
| 完整预评审 | 需要正式报告、网页展示、交互原型或完整预评审包 | 完整报告文件夹 |

完整预评审核心流程：

1. 结构化原始想法。
2. 判断交付形态。
3. 做可行性判断。
4. 在当前证据会影响判断时，调研市场类别、竞品、替代方案、需求信号和成熟度。
5. 定义用户假设、待办任务、痛点强度、采用阻力和验证实验。
6. 明确产品策略和最小可行产品范围。
7. 按模块评估自研、购买、复用、分叉改造和参考决策。
8. 生成技术实现路径。
9. 规划商业模式、定价、包装、渠道和早期变现测试。
10. 审查产品、市场、技术、隐私、许可、依赖和执行风险。
11. 创建不依赖 AI 生图的视觉说明资产。
12. 为 `index.html` 生成报告可视化解释层。
13. 规划独立交互原型、模拟器、接口试验台、终端预览或工作流预览。
14. 生成完整中文预评审包文件夹。

## V4.5 流程与输出契约

WheelWise V4.5 保持 Superpowers 风格多 skill pack 架构，并升级为 AI 产品预评审系统：`using-wheelwise` 是总控、路由、状态管理、Gate 控制、证据仲裁、评审委员会汇总、自检和最终预评审包汇总者，同时把数据支撑、Gate0 Evidence Intake、按 idea 类型动态生成的第一阶段补充数据清单、证据分类、中文预评审状态、决策记录、横向评分、合规与上线前置项、报告可视化、独立原型和不依赖生图的视觉资产作为交付能力固化下来。

V4 新增两个内部产物：

```text
project-state.md
evidence-board.md
```

`project-state.md` 记录当前阶段、适用性分类、Gate0 Evidence Intake 状态、证据要求状态、补充数据清单版本、恢复说明、交付形态、Gate 状态、可行性结论、预评审状态、下一阶段建议、评审评分、策略摘要、开放问题、假设、关键假设依赖、考虑和排除的选项、合规前置项和最后更新 skill。`evidence-board.md` 汇总市场调研、用户发现、复用评估、技术探针、商业化证据、动态补充数据要求、用户补回的数据、证据分类、决策依赖、排除选项原因、验证优先级和证据缺口。

所有路线的最小产物是中文报告文件夹和 `report.md`：

```text
wheelwise-report-<idea-slug>/
  report.md
```

完整预评审产物是中文预评审包文件夹：

```text
wheelwise-report/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
    concept.png
```

如果有想法名称，可以使用：

```text
wheelwise-report-<idea-slug>/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
```

`report.md` 是事实来源。`index.html` 是来自同一份中文报告的报告可视化解释层。`prototype.html` 是独立交互原型或模拟器。`assets/` 存放生成或选用的视觉资产。

V4.5 要求 `report.md` 更像真实产品预评审包，包含预评审结论、执行摘要、原始假设、调研方法与证据等级、评审委员会意见、市场吸引力、竞品与替代方案、决策记录与选项排除、横向比较评分、合规与上线前置项、分阶段验证计划、前端展示与交互原型和最终建议。所有重要结论必须标注为事实、假设、推断或证据缺口。

V4.5 要求 `index.html` 像可视化预评审报告，用卡片、矩阵、时间线、流程图、架构图、风险图、验证看板和行动卡，把报告里的预评审状态、评分、判断、证据、流程、风险、验证、商业化、合规和执行或验证计划讲清楚。它不能只是 Markdown 转 HTML，不能成为第二份报告，不能只是短摘要页，也不能替代原型。

`prototype.html` 必须独立模拟产品交付形态，使用本地模拟数据、可点击控件、输入、状态变化、加载 / 空状态 / 错误 / 成功状态、响应式布局和未接入真实后端说明。接口、命令行、自动化、后端、数据或开发者工具类想法，应使用接口试验台、终端模拟器、请求浏览器或工作流模拟器。线下、实体、强监管或供应链类想法可以使用验证数据看板、成本毛利测算器、合规清单、供应链验证面板或试点记录面板。

V4.5 Gate 规则：

- Gate0 使用统一的 Evidence Intake，返回 `Ready`、`Need Basic Input` 或 `Field Data Required`。补充数据清单必须按 idea 类型组合动态生成；用户之后补回数据时，从 Gate0 复核继续。
- Gate1 做早期可行性初筛；不能继续就结束，可以继续就自动进入 Discovery。
- Gate2 做完整评审；`Go` 映射到 `可进入原型验证` 或 `可进入最小可行产品实验` 并自动进入 Delivery，`Pivot`、`Need More Evidence`、`Kill`、`Park` 映射到 `建议转向后再评审`、`需要补充关键证据`、`建议放弃`、`建议暂缓` 或 `仅作为参考`，再按需询问用户。

V4.5 统一预评审状态：

| 状态 | 含义 |
| --- | --- |
| 可进入原型验证 | 证据足够支撑低成本原型或模拟器验证 |
| 可进入最小可行产品实验 | 核心证据、范围、风险和执行路径足够支撑有限实验 |
| 需要补充关键证据 | 高影响证据缺口阻塞可信决策 |
| 建议转向后再评审 | 证据支持不同用户、问题、形态、切入点、商业模式、合规边界或技术路径 |
| 建议暂缓 | 时机、依赖、监管、预算、团队或市场条件暂不适合 |
| 建议放弃 | 不安全、不可行、无差异或缺少可信用户/买方 |
| 仅作为参考 | 可作为学习、模块或横向比较素材，但不建议直接推进 |

生成产物里的所有面向用户可见文字都必须使用中文，包括 Markdown 正文、网页文案、图片内文字、图表标签、图片替代文字、表格字段和报告说明。技术栈、代码标识符、命令、包名、API 名称和文件路径如果是技术引用，可以保留英文。

必须使用的中文展示词：

| 概念 | 中文展示词 |
| --- | --- |
| Build | 自研 |
| Buy | 购买 |
| Reuse | 复用 |
| Fork | 分叉改造 |
| Reference | 参考 |
| Web App | 网页应用 |
| SaaS | 软件服务 |
| MVP | 最小可行产品 |
| Demo | 演示 |
| mock data | 模拟数据 |
| fallback | 兜底方案 |
| go/no-go | 继续 / 停止条件 |
| Codex-ready execution plan | 可交给 Codex 执行的计划 |

## 仓库结构

```text
.codex-plugin/
  plugin.json
skills/
  using-wheelwise/
  idea-intake/
  surface-strategy/
  feasibility-review/
  market-research/
  customer-discovery/
  evidence-board/
  product-strategy/
  reuse-evaluator/
  technical-planning/
  commercialization/
  risk-review/
  visual-brief/
  ui-demo/
  report-visualization/
  execution-plan/
  parallel-research/
shared/
  references/
  templates/
examples/
  community-tool-share/
    project-state.md
    evidence-board.md
    report.md
    index.html
    prototype.html
    assets/
      concept.svg
scripts/
  check_report_contract.py
```

## 内部 Skill

| Skill | 作用 |
| --- | --- |
| `using-wheelwise` | 主入口、Gate 控制、证据仲裁、评审委员会汇总、预评审包契约 |
| `idea-intake` | 把原始想法转成结构化产品简报 |
| `surface-strategy` | 判断网站、网页应用、移动应用、桌面应用、浏览器插件、接口/服务、命令行工具或自动化工具等交付形态 |
| `feasibility-review` | 将可行性结论映射到 V4.5 预评审状态 |
| `market-research` | 调研市场类别、竞品、替代方案、需求信号、趋势、成熟度和进入壁垒 |
| `customer-discovery` | 定义用户画像、待办任务、痛点强度、工作流、采用阻力和验证实验 |
| `evidence-board` | 汇总市场、用户、复用、技术探针和商业化证据，形成内部决策证据台账 |
| `product-strategy` | 定义定位、差异化、产品切入点和最小可行产品范围 |
| `reuse-evaluator` | 按模块评估自研、购买、复用、分叉改造和参考 |
| `technical-planning` | 把决策转成技术栈、架构、数据、集成和部署建议 |
| `commercialization` | 规划商业模式、定价、包装、渠道、销售路径和早期变现测试 |
| `risk-review` | 审查市场、产品、技术、法律、隐私、许可、依赖和执行风险 |
| `visual-brief` | 规划或创建 `assets/` 下的 SVG、HTML/CSS、图片或兜底视觉资产 |
| `ui-demo` | 规划独立可点击原型、模拟器、接口试验台、终端预览或工作流预览 |
| `report-visualization` | 把 `report.md` 转成完整报告可视化解释层 `index.html` |
| `execution-plan` | 按预评审状态生成开发、原型、补证、转向、暂缓、放弃或参考保留任务 |
| `parallel-research` | 为复杂调研或独立复核提供可选支持 |

## 如何使用

完整评估一个产品想法：

```text
Use $using-wheelwise to evaluate this idea:
I want to build an AI resume optimizer for job seekers.
```

即使是较窄的问题，也建议使用主入口，让路由和输出纪律保持一致：

```text
Use $using-wheelwise to decide whether this should be a browser extension or a webpage application.
```

```text
Use $using-wheelwise to evaluate which modules should be self-built, purchased, reused, forked, or used as reference.
```

最终聊天回复应该很短，只给产物路径：

```text
报告文件夹：wheelwise-report-community-tool-share/
源报告：wheelwise-report-community-tool-share/report.md
网页展示：wheelwise-report-community-tool-share/index.html
交互原型：wheelwise-report-community-tool-share/prototype.html
```

## 示例

仓库内置 V4.5 canonical 示例：

```text
examples/community-tool-share/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
    concept.svg
```

这些示例展示 V4.5 预评审包契约、内部状态、证据中枢、中文 Markdown 报告、可视化 `index.html`、独立 `prototype.html`、评分、预评审状态，以及不依赖 AI 生图的视觉资产。

## 校验

校验示例报告文件夹：

```powershell
python scripts\check_report_contract.py examples\community-tool-share --folder --skip-filename --v4
```

校验完整报告模板：

```powershell
python scripts\check_report_contract.py shared\templates\new-product-brief.md --skip-filename
python scripts\check_report_contract.py shared\templates\final-wheelwise-report.md --skip-filename
```

校验插件清单：

```powershell
python -m json.tool .codex-plugin\plugin.json
python C:\Users\zhenyang.du\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py D:\WheelWise
```

校验所有 skill：

```powershell
$env:PYTHONUTF8='1'
Get-ChildItem skills -Directory | ForEach-Object {
  python C:\Users\zhenyang.du\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
}
```

提交前检查空白问题：

```powershell
git diff --check
```

## 外部参考

WheelWise 可以参考 UI UX Pro Max、pm-skills、awesome-copilot 等外部 skill 生态，但不能复制它们的内容。外部资源只作为可选参考记录在 `shared/references/external-skills.md`。

## 版本

当前插件版本：`4.5.0`。

V4.5 重点包括：

- `using-wheelwise` 成为总控、路由、状态管理、Gate 控制、证据仲裁、评审委员会汇总、自检和最终预评审包汇总者。
- `project-state.md` 作为内部流程状态。
- `evidence-board.md` 作为内部证据中枢。
- Gate0、Gate1、Gate2 流转纪律。
- 七个中文预评审状态。
- 事实、假设、推断、证据缺口四类证据意识。
- 决策记录、选项排除、关键假设依赖和横向比较评分。
- 正常 `Go` 路径不打断用户。
- Delivery 前先完成基于证据的 Discovery 和 Synthesis。
- 最终仍输出中文报告文件夹：`report.md`、可视化 `index.html`、独立 `prototype.html` 和 `assets/`。
