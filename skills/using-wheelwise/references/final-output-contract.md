# 最终输出契约

WheelWise 的最终产物是一个中文报告文件夹，而不是单个 Markdown 文件。文件夹内必须包含源报告、报告可视化网页、独立交互原型和视觉资源。V4 还可以包含内部状态文件 `project-state.md` 和 `evidence-board.md`，但它们不能替代最终报告。

## 文件夹契约

- 默认目录：`wheelwise-report/`。
- 如果用户提供 idea 名称，使用：`wheelwise-report-<idea-slug>/`。
- 源报告文件：`report.md`。
- 报告可视化网页：`index.html`。
- 交互原型文件：`prototype.html` 或等效文件；所有产品都需要生成或明确规划对应交互模拟。
- 图片与静态资源目录：`assets/`。
- 内部状态文件：`project-state.md`。
- 内部证据文件：`evidence-board.md`。
- 图片建议文件名：`concept.png`、`decision-map.png`、`roadmap.png`。
- 最终聊天回复只列出报告文件夹路径、`report.md` 路径和 `index.html` 路径；不要用聊天摘要替代文件。

推荐目录结构：

```text
wheelwise-report-<idea-slug>/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
    concept.png
    decision-map.png
    roadmap.png
```

## 全中文可见文字规则

Markdown、网页、图片内文字、图表标签、图片替代文本、表格字段和报告说明都必须使用中文。

可保留英文的内容仅限技术标识：命令、文件路径、包名、代码标识符、接口名、技术栈名称和不可翻译的产品名。不要把英文作为展示文案。

统一中文替代表达：

| 禁用展示词 | 使用中文 |
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
| mock 数据 | 模拟数据 |
| fallback | 兜底方案 |
| go/no-go | 继续 / 停止条件 |
| Codex-ready 执行计划 | 可交给 Codex 执行的计划 |

禁止使用内部英文 skill 名称作为报告章节，例如 `Idea Intake`、`Surface Strategy`、`Reuse Evaluator`、`Technical Planning`、`Risk Review`、`UI Demo Scope` 和 `MVP Execution Plan`。

## 递进式报告顺序

报告必须像一份面向读者的产品前期调研报告，而不是内部 skill 输出拼接：

```text
报告说明与阅读导览
-> 执行摘要
-> 原始想法与关键假设
-> 调研方法与证据等级
-> 用户、需求、市场、竞品
-> 产品、商业化、合规、风险、验证
-> 技术与复用、前端展示与交互原型
-> 可交给 Codex 执行的计划
-> 最终建议与下一步行动
```

## V4 状态与证据规则

- `project-state.md` 是内部流程状态，记录 idea summary、current phase、delivery surface、gate status、feasibility verdict、product strategy summary、reuse decisions summary、technical plan summary、commercialization summary、risk summary、visual/demo status、final report status、open questions、assumptions 和 last updated by skill。
- `evidence-board.md` 是内部证据中枢，记录 evidence item、source/origin skill、evidence type、affected decision、strength、confidence、original assumption、supports or opposes、direction shift、user confirmation needed、assumption vs evidence、contradiction、evidence gap 和 recommended next action。
- 两者都不是最终报告章节名。
- 最终报告必须吸收 evidence-board 的内容，把证据写入 `市场备注`、`用户假设`、`决策解释摘要`、`关键风险` 和 `验证实验`。
- V4.4 所有结论都必须有数据、证据或明确证据缺口支撑；无证据结论必须降级为假设、需要补充数据或 Need More Evidence。
- Gate0 必须使用统一的 `Gate0 Evidence Intake`。如果暂停在 `Field Data Required`，最终报告必须说明动态补充数据清单、继续/停止阈值、恢复方式，以及用户补充数据后先复核 Gate0。
- Gate 状态必须与 `project-state.md` 中的 feasibility verdict 一致。
- 如果最终建议不同于用户原始方向，报告必须详细说明原始假设、支持证据、反驳证据、为什么原方向不成立或不建议继续、推荐调整方向、偏移程度和用户确认状态。
- 重大偏移必须有 Gate2 用户确认记录；如果未确认，只能标记为假设驱动或待确认方向，不能当作已批准的交付计划。

## 必需中文章节

`report.md` 必须包含：

1. 报告说明与阅读导览
2. 项目标题
3. 执行摘要
4. 原始想法与关键假设
5. 调研方法与证据等级
6. 目标用户与使用场景
7. 问题痛点与需求强度
8. 市场吸引力与机会窗口
9. 竞品与替代方案分析
10. 原始方向校准
11. 产品定位与差异化
12. 最小可行产品范围
13. 商业模式与获客假设
14. 合规与上线前置项
15. 关键风险与不确定性
16. 分阶段验证计划
17. 技术与复用方案
18. 前端展示与交互原型
19. 可交给 Codex 执行的计划
20. 最终建议与下一步行动

## 开头与结尾

`报告说明与阅读导览` 必须包含：

- 报告目的。
- 适用阶段。
- 核心结论预览。
- 阅读方式。

`最终建议与下一步行动` 必须包含：

- 一句话判断。
- 7 天行动。
- 14 天行动。
- 30 天行动。
- 继续 / 停止条件。

## 视觉与网页规则

- `前端展示与交互原型` 必须写入图片资产、图片生成方式或图表兜底方案。
- 视觉资产不依赖 AI 生图。中文密集的信息图、路线图、架构图、模块图、风险图和决策图优先使用 SVG 或 HTML/CSS 静态图。
- AI 生图只适合无文字或少文字的概念图、氛围图和场景图。
- 图片 prompt 必须要求图片内所有文字为中文。如果无法稳定生成正确中文，优先生成无文字图片，并把中文说明放在 `report.md` 和 `index.html`。
- Mermaid 只能作为最后兜底；图表节点文字必须中文。
- 不得把单张装饰性概念图作为唯一视觉资产。至少一个视觉资产必须解释决策、流程、架构、路线、风险或验证。
- `前端展示与交互原型` 必须写入 `index.html`、报告可视化层定位、源报告关系、`prototype.html`、核心交互、模拟数据说明、加载 / 空状态 / 错误 / 成功状态，以及未接入真实后端的范围。
- `index.html` 是报告可视化解释层，内容必须来自同一份 `report.md`，不能成为第二套事实来源。
- `index.html` 必须把报告中的执行摘要、调研方法与证据等级、核心判断、证据、用户、问题、市场吸引力、竞品与替代方案、方案、范围、复用决策、技术路径、商业化、合规与上线前置项、风险、分阶段验证计划、执行计划和最终建议转成视觉结构。
- `index.html` 不能是普通 Markdown 转网页、短摘要页、第二份报告或产品原型。
- `index.html` 应包含导航、封面或核心结论、多个可视化模块、至少一个 `assets/` 本地视觉资产、`prototype.html` 入口和响应式布局。
- `prototype.html` 是独立交互原型、模拟器或验证工具。它不能承担报告展示职责。
- `prototype.html` 必须包含模拟数据、可点击交互、输入或选择、局部状态变化、加载 / 空状态 / 错误 / 成功状态、响应式布局和未接入真实后端范围。对非数字 idea，可展示验证数据看板、成本毛利测算器、合规清单、供应链验证面板或试点记录面板。
- 没有传统 UI 的产品不能跳过展示；必须通过 API playground、CLI simulator、workflow simulator、request explorer 或 terminal simulator 说明交互。

## 集成规则

- 关键决策解释必须使用 `../../shared/references/decision-rationale-standard.md` 中的中文字段，并包含数据来源、证据类型、证据强度、证据缺口和信心等级。
- 适用性分类和补充数据要求必须使用 `../../shared/references/idea-applicability-standard.md`。
- 可交给 Codex 执行的计划必须包含创建报告文件夹、写入 `project-state.md`、写入 `evidence-board.md`、写入 `report.md`、生成 `index.html`、生成 `prototype.html`、保存视觉资产到 `assets/`、运行产物检查的任务。
- 使用 `../../shared/templates/new-product-brief.md` 生成完整中文报告；短报告才使用 `../../shared/templates/final-wheelwise-report.md`。

## V4 最终自检

最终回复前，`using-wheelwise` 必须确认：

- `project-state.md` 关键字段完整。
- `evidence-board.md` 有证据或明确证据缺口。
- Gate0、Gate1、Gate2 状态与当前阶段一致；如 Gate0 等待补充数据，`project-state.md` 必须包含恢复字段。
- 关键决策都有解释。
- `visual-brief` 有图片、图片生成说明或兜底图。
- `ui-demo` 或模拟器方案存在。
- `report-visualization` 或等效步骤已确认 `index.html` 覆盖报告主要内容并不是 Markdown 转网页。
- `report.md`、`index.html`、`assets/` 满足契约。
- `prototype.html` 已生成或有明确任务，且与 `index.html` 职责分离。
- 可见文字中文化。
- 报告没有无批判复述用户想法；若有重大方向偏移，Gate2 用户确认状态已写入报告。
- 报告包含调研方法与证据等级、竞品与替代方案分析、合规与上线前置项、分阶段验证计划；所有结论都有证据或缺口。
