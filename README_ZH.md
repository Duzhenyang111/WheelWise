# WheelWise

WheelWise 是一个面向 Codex 的 Superpowers 风格多 skill 包。它把一个原始产品想法转成结构化产品判断、交付形态建议、复用策略、技术路径、视觉资产方案、报告可视化网页、独立交互原型，以及可交给 Codex 执行的计划。

主入口始终是 `using-wheelwise`。用户只需要调用这个 skill；后续由它路由到内部 skill，并负责最终汇总。

```text
Use $using-wheelwise to evaluate this idea: ...
```

英文文档见 [README.md](README.md)。

## WheelWise 解决什么问题

WheelWise 适合在正式开发前使用。它帮助判断一个产品想法应该先验证、直接做最小可行产品、暂停，还是放弃；也会判断哪些模块应该自研、购买、复用、分叉改造，或仅作为参考。

核心流程：

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
14. 生成完整中文报告文件夹。

## V4.1 流程与输出契约

WheelWise V4.1 保持 Superpowers 风格多 skill pack 架构，并升级 skill 流转：`using-wheelwise` 是总控、路由、状态管理、Gate 控制、自检和最终报告汇总者，同时把报告可视化、独立原型和不依赖生图的视觉资产作为交付能力固化下来。

V4 新增两个内部产物：

```text
project-state.md
evidence-board.md
```

`project-state.md` 记录当前阶段、交付形态、Gate 状态、可行性结论、策略摘要、开放问题、假设和最后更新 skill。`evidence-board.md` 汇总市场调研、用户发现、复用评估、技术探针和商业化证据。

最终产物仍然是中文报告文件夹：

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

V4.1 要求 `index.html` 像可视化咨询报告，用卡片、矩阵、时间线、流程图、架构图、风险图、验证看板和行动卡，把报告里的判断、证据、流程、风险、验证、商业化和执行计划讲清楚。它不能只是 Markdown 转 HTML，不能成为第二份报告，不能只是短摘要页，也不能替代原型。

`prototype.html` 必须独立模拟产品交付形态，使用本地模拟数据、可点击控件、输入、状态变化、加载 / 空状态 / 错误 / 成功状态、响应式布局和未接入真实后端说明。接口、命令行、自动化、后端、数据或开发者工具类想法，应使用接口试验台、终端模拟器、请求浏览器或工作流模拟器。

V4 Gate 规则：

- Gate0 只在基础信息不足时询问：面向谁、先验证还是做最小可行产品、时间/预算/技术栈限制。
- Gate1 做早期可行性初筛；不能继续就结束，可以继续就自动进入 Discovery。
- Gate2 做完整评审；`Go` 自动进入 Delivery，`Pivot`、`Need More Evidence`、`Kill`、`Park` 才询问用户。

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
| `using-wheelwise` | 主入口、路由纪律、最终汇总、报告文件夹契约 |
| `idea-intake` | 把原始想法转成结构化产品简报 |
| `surface-strategy` | 判断网站、网页应用、移动应用、桌面应用、浏览器插件、接口/服务、命令行工具或自动化工具等交付形态 |
| `feasibility-review` | 判断构建最小可行产品、先验证、暂停或放弃 |
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
| `execution-plan` | 生成里程碑、任务、测试、验收标准和报告生成任务 |
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

仓库内置 V4.1 canonical 示例：

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

该示例展示 V4.1 报告文件夹契约、内部状态、证据中枢、中文 Markdown 报告、可视化 `index.html`、独立 `prototype.html`，以及不依赖 AI 生图的 SVG 视觉资产。

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

当前插件版本：`4.0.0`。

V4.1 重点包括：

- `using-wheelwise` 成为总控、路由、状态管理、Gate 控制、自检和最终报告汇总者。
- `project-state.md` 作为内部流程状态。
- `evidence-board.md` 作为内部证据中枢。
- Gate0、Gate1、Gate2 流转纪律。
- 正常 `Go` 路径不打断用户。
- Delivery 前先完成基于证据的 Discovery 和 Synthesis。
- 最终仍输出中文报告文件夹：`report.md`、可视化 `index.html`、独立 `prototype.html` 和 `assets/`。
