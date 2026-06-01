# WheelWise

WheelWise is a Superpowers-style multi-skill pack for Codex. It turns a raw product idea into a structured product decision, delivery-surface recommendation, reuse strategy, technical direction, visual plan, interaction-demo plan, and an execution plan that Codex can act on.

The primary entry point is always `using-wheelwise`. Users should call that skill once; it routes the workflow through the internal skills and owns the final synthesis.

```text
Use $using-wheelwise to evaluate this idea: ...
```

Chinese documentation is available in [README_ZH.md](README_ZH.md).

## What WheelWise Does

WheelWise is meant for the stage before serious implementation starts. It helps decide what should be built, validated, bought, reused, forked, or only used as reference.

Core workflow:

1. Structure the raw idea.
2. Choose the delivery surface.
3. Review feasibility.
4. Shape product strategy and minimum viable product scope.
5. Evaluate module-level self-build, purchase, reuse, fork, and reference decisions.
6. Produce a technical implementation path.
7. Review product, market, technical, privacy, license, dependency, and execution risks.
8. Create visual explanation assets or a Chinese Mermaid backup.
9. Plan an interaction demo, simulator, playground, or workflow preview when useful.
10. Generate a complete Chinese report folder.

## V2.7 Output Contract

WheelWise V2.7 no longer outputs a loose Markdown file. The final artifact is a report folder:

```text
wheelwise-report/
  report.md
  index.html
  assets/
    concept.png
```

When an idea slug is available, the folder should be named:

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  assets/
```

`report.md` is the source of truth. `index.html` is a static display layer generated from the same Chinese report. `assets/` stores generated or selected visuals.

All user-visible text in generated artifacts must be Chinese, including Markdown body text, webpage copy, image text, chart labels, alt text, table fields, and report explanations. Technical stacks, code identifiers, commands, package names, API names, and file paths may remain English when they are literal technical references.

Required Chinese display vocabulary:

| Concept | Chinese display term |
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

## Skill Pack Structure

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

## Internal Skills

| Skill | Role |
| --- | --- |
| `using-wheelwise` | Main router, workflow discipline, final synthesis, report-folder contract |
| `idea-intake` | Converts a raw idea into a structured brief |
| `surface-strategy` | Chooses website, webpage application, mobile app, desktop app, extension, API/service, CLI, or automation surface |
| `feasibility-review` | Decides whether to build a minimum viable product, validate first, pause, or reject |
| `product-strategy` | Defines positioning, differentiation, product wedge, and minimum viable product scope |
| `reuse-evaluator` | Evaluates self-build, purchase, reuse, fork, and reference choices by module |
| `technical-planning` | Converts decisions into stack, architecture, data, integration, and deployment guidance |
| `risk-review` | Reviews market, product, technical, legal, privacy, license, dependency, and execution risks |
| `visual-brief` | Plans or creates visual assets under `assets/` |
| `ui-demo` | Plans a clickable demo, simulator, playground, terminal preview, or workflow preview |
| `execution-plan` | Produces milestones, tasks, tests, acceptance criteria, and report-generation tasks |
| `parallel-research` | Optional research or independent review support for complex cases |

## How To Use

Use the main skill for full product evaluation:

```text
Use $using-wheelwise to evaluate this idea:
I want to build an AI resume optimizer for job seekers.
```

Use the main skill even for narrower questions so routing stays consistent:

```text
Use $using-wheelwise to decide whether this should be a browser extension or a webpage application.
```

```text
Use $using-wheelwise to evaluate which modules should be self-built, purchased, reused, forked, or used as reference.
```

Expected final chat response should be short and artifact-oriented:

```text
Report folder: wheelwise-report-ai-resume-optimizer/
Source report: wheelwise-report-ai-resume-optimizer/report.md
Web display: wheelwise-report-ai-resume-optimizer/index.html
```

## Example

See the included V2.7 example:

```text
examples/ai-resume-optimizer/
  report.md
  index.html
  assets/
    concept.png
```

The example demonstrates the folder output contract, Chinese Markdown report, Chinese static webpage, and image asset placement.

## Validation

Validate the example report folder:

```powershell
python scripts\check_report_contract.py examples\ai-resume-optimizer --folder --skip-filename
```

Validate the full report templates:

```powershell
python scripts\check_report_contract.py shared\templates\new-product-brief.md --skip-filename
python scripts\check_report_contract.py shared\templates\final-wheelwise-report.md --skip-filename
```

Validate the plugin manifest:

```powershell
python -m json.tool .codex-plugin\plugin.json
python C:\Users\zhenyang.du\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py D:\WheelWise
```

Validate every skill:

```powershell
$env:PYTHONUTF8='1'
Get-ChildItem skills -Directory | ForEach-Object {
  python C:\Users\zhenyang.du\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
}
```

Run whitespace checks before committing:

```powershell
git diff --check
```

## External References

WheelWise may reference external skill ecosystems such as UI UX Pro Max, pm-skills, and awesome-copilot, but it must not copy their content. External resources are recorded in `shared/references/external-skills.md` as optional references only.

## Version

Current plugin version: `0.2.7`.

V2.7 focuses on:

- Report-folder output instead of single-file output.
- `report.md` as source report.
- `index.html` as Chinese webpage display layer.
- `assets/` as the required resource directory.
- Fully Chinese user-visible generated artifacts.
- Stronger contract validation through `scripts/check_report_contract.py`.
