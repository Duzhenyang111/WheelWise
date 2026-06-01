# WheelWise

WheelWise 是一个面向 Codex 的 Superpowers 风格多 skill 包。它把一个原始产品想法转成结构化产品判断、交付形态建议、复用策略、技术路径、视觉方案、交互演示方案，以及可交给 Codex 执行的计划。

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
4. 明确产品策略和最小可行产品范围。
5. 按模块评估自研、购买、复用、分叉改造和参考决策。
6. 生成技术实现路径。
7. 审查产品、市场、技术、隐私、许可、依赖和执行风险。
8. 创建视觉说明资产，或使用中文 Mermaid 兜底图表。
9. 规划交互演示、模拟器、接口试验台、终端预览或工作流预览。
10. 生成完整中文报告文件夹。

## V2.7 输出契约

WheelWise V2.7 不再输出散落的 Markdown 单文件。最终产物是一个报告文件夹：

```text
wheelwise-report/
  report.md
  index.html
  assets/
    concept.png
```

如果有想法名称，可以使用：

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  assets/
```

`report.md` 是事实来源。`index.html` 是来自同一份中文报告的静态展示层。`assets/` 存放生成或选用的视觉资产。

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
  product-strategy/
  reuse-evaluator/
  technical-planning/
  risk-review/
  visual-brief/
  ui-demo/
  execution-plan/
  parallel-research/
shared/
  references/
  templates/
examples/
  ai-resume-optimizer/
    report.md
    index.html
    assets/
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
| `product-strategy` | 定义定位、差异化、产品切入点和最小可行产品范围 |
| `reuse-evaluator` | 按模块评估自研、购买、复用、分叉改造和参考 |
| `technical-planning` | 把决策转成技术栈、架构、数据、集成和部署建议 |
| `risk-review` | 审查市场、产品、技术、法律、隐私、许可、依赖和执行风险 |
| `visual-brief` | 规划或创建 `assets/` 下的视觉资产 |
| `ui-demo` | 规划可点击演示、模拟器、接口试验台、终端预览或工作流预览 |
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
报告文件夹：wheelwise-report-ai-resume-optimizer/
源报告：wheelwise-report-ai-resume-optimizer/report.md
网页展示：wheelwise-report-ai-resume-optimizer/index.html
```

## 示例

仓库内置 V2.7 示例：

```text
examples/ai-resume-optimizer/
  report.md
  index.html
  assets/
    concept.png
```

该示例展示报告文件夹契约、中文 Markdown 报告、中文静态网页和图片资产放置方式。

## 校验

校验示例报告文件夹：

```powershell
python scripts\check_report_contract.py examples\ai-resume-optimizer --folder --skip-filename
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

当前插件版本：`0.2.7`。

V2.7 重点包括：

- 用报告文件夹替代单文件输出。
- `report.md` 作为源报告。
- `index.html` 作为中文网页展示层。
- `assets/` 作为必需资源目录。
- 生成产物的用户可见文字全部中文。
- 通过 `scripts/check_report_contract.py` 强化契约校验。
