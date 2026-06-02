# 最终输出契约

WheelWise 的最终产物是一个中文报告文件夹，而不是单个 Markdown 文件。文件夹内必须包含源报告、网页展示文件和图片资源。V4 还可以包含内部状态文件 `project-state.md` 和 `evidence-board.md`，但它们不能替代最终报告。

## 文件夹契约

- 默认目录：`wheelwise-report/`。
- 如果用户提供 idea 名称，使用：`wheelwise-report-<idea-slug>/`。
- 源报告文件：`report.md`。
- 网页展示文件：`index.html`。
- 交互原型文件：`prototype.html` 或等效文件；用户可见产品需要生成或明确规划。
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

报告必须像一份面向读者的产品方案，而不是内部 skill 输出拼接：

```text
报告说明与阅读导览
-> 用户与问题
-> 核心决策与方案
-> 视觉说明与交互演示
-> 商业化、风险与验证
-> 可交给 Codex 执行的计划
-> 最终建议与下一步行动
```

## V4 状态与证据规则

- `project-state.md` 是内部流程状态，记录 idea summary、current phase、delivery surface、gate status、feasibility verdict、product strategy summary、reuse decisions summary、technical plan summary、commercialization summary、risk summary、visual/demo status、final report status、open questions、assumptions 和 last updated by skill。
- `evidence-board.md` 是内部证据中枢，记录 evidence item、source/origin skill、evidence type、affected decision、strength、confidence、assumption vs evidence、contradiction、evidence gap 和 recommended next action。
- 两者都不是最终报告章节名。
- 最终报告必须吸收 evidence-board 的内容，把证据写入 `市场备注`、`用户假设`、`决策解释摘要`、`关键风险` 和 `验证实验`。
- Gate 状态必须与 `project-state.md` 中的 feasibility verdict 一致。

## 必需中文章节

`report.md` 必须包含：

1. 报告说明与阅读导览
2. 项目标题
3. 想法摘要
4. 交付形态
5. 结论：构建最小可行产品 / 先验证 / 暂停 / 放弃
6. 决策解释摘要
7. 目标用户
8. 问题与紧迫性
9. 市场备注
10. 用户假设
11. 差异化
12. 最小可行产品范围
13. 产品策略
14. 自研 / 购买 / 复用 / 分叉改造 / 参考决策
15. 技术实现路径
16. 视觉说明
17. 交互演示
18. 网页展示文件
19. 商业化备注
20. 关键风险
21. 验证实验
22. 可交给 Codex 执行的计划
23. 最终建议与下一步行动

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

- `视觉说明` 必须写入图片资产、图片生成方式或图表兜底方案。
- 有生图能力时，优先把图片保存到 `assets/` 并在源报告中引用，例如 `![产品概念图](./assets/concept.png)`。
- 图片 prompt 必须要求图片内所有文字为中文。如果无法稳定生成正确中文，优先生成无文字图片，并把中文说明放在 `report.md` 和 `index.html`。
- 无法生成图片时，使用 Mermaid 图表兜底；图表节点文字必须中文。
- `交互演示` 必须写入演示路径、运行方式、核心交互、模拟数据说明、加载 / 空状态 / 错误 / 成功状态，以及未接入真实后端的范围。
- `网页展示文件` 必须写入 `index.html`、展示层定位、源报告关系和包含模块。
- `index.html` 是展示层，内容必须来自同一份 `report.md`，不能成为第二套事实来源。
- 没有传统 UI 的产品不能跳过展示；必须通过 API playground、CLI simulator、workflow simulator、request explorer 或 terminal simulator 说明交互。

## 集成规则

- 关键决策解释必须使用 `../../shared/references/decision-rationale-standard.md` 中的中文字段。
- 可交给 Codex 执行的计划必须包含创建报告文件夹、写入 `project-state.md`、写入 `evidence-board.md`、写入 `report.md`、生成 `index.html`、保存图片到 `assets/`、运行产物检查的任务。
- 使用 `../../shared/templates/new-product-brief.md` 生成完整中文报告；短报告才使用 `../../shared/templates/final-wheelwise-report.md`。

## V4 最终自检

最终回复前，`using-wheelwise` 必须确认：

- `project-state.md` 关键字段完整。
- `evidence-board.md` 有证据或明确证据缺口。
- Gate0、Gate1、Gate2 状态与当前阶段一致。
- 关键决策都有解释。
- `visual-brief` 有图片、图片生成说明或兜底图。
- `ui-demo` 或模拟器方案存在。
- `report.md`、`index.html`、`assets/` 满足契约。
- 可见文字中文化。
