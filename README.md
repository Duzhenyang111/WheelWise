# WheelWise

WheelWise is a Superpowers-style multi-skill pack for Codex and an **AI Idea Pre-review Board**. It turns a raw product idea into a Chinese pre-review package with a review state, evidence classification, evidence gaps, decision records, comparable scorecard, delivery-surface recommendation, reuse strategy, technical direction, compliance and launch prerequisites, report visualization layer, independent interaction prototype, and an execution or validation plan that Codex can act on.

WheelWise is not a formal approval system and does not replace real user research, real business data, compliance approval, legal advice, investment judgment, or organization decisions. It helps before formal review: turning vague ideas into discussable, verifiable, comparable, and decision-ready pre-review packages.

The primary entry point is always `using-wheelwise`. Users should call that skill once; it routes the workflow through the internal skills and owns the final synthesis.

```text
Use $using-wheelwise to evaluate this idea: ...
```

Chinese documentation is available in [README_ZH.md](README_ZH.md).

## What WheelWise Does

WheelWise is meant for the stage before serious implementation, team review, or MVP investment starts. It helps decide whether an idea should enter research, prototype validation, bounded MVP experimentation, pivot review, pause, rejection, or reference-only preservation.

Core workflow:

1. Structure the raw idea.
2. Choose the delivery surface.
3. Review feasibility.
4. Research market category, competitors, substitutes, demand signals, and maturity when current evidence matters.
5. Define customer hypotheses, jobs-to-be-done, pain intensity, adoption objections, and validation experiments.
6. Shape product strategy and minimum viable product scope.
7. Evaluate module-level self-build, purchase, reuse, fork, and reference decisions.
8. Produce a technical implementation path.
9. Plan business model, pricing, packaging, channels, and early monetization tests.
10. Review product, market, technical, privacy, license, dependency, and execution risks.
11. Create visual explanation assets without depending on AI image generation.
12. Generate a report visualization layer for `index.html`.
13. Plan an independent interaction prototype, simulator, playground, or workflow preview.
14. Generate a complete Chinese pre-review package folder.

## V4.5 Workflow And Output Contract

WheelWise V4.5 keeps the Superpowers-style multi-skill pack architecture and upgrades the workflow into an AI product pre-review system with controller-managed state, Gate0 Evidence Intake, dynamic supplemental-data checklists, evidence consolidation, evidence classification, Gate decisions, Chinese pre-review states, review-board synthesis, decision records, comparable scorecards, compliance reminders, report visualization, independent prototypes, and visual assets that do not depend on AI image generation.

`using-wheelwise` is the controller, router, state manager, Gate owner, self-check owner, and final-report synthesizer. It reads and updates internal state as the workflow moves across skills.

Internal V4 artifacts:

```text
project-state.md
evidence-board.md
```

`project-state.md` tracks phase, applicability class, Gate0 Evidence Intake status, evidence requirement status, supplemental-data checklist version, resume instruction, delivery surface, Gate status, feasibility verdict, pre-review state, next-stage recommendation, review scorecard, strategy summaries, open questions, assumptions, critical assumption dependencies, options considered/rejected, compliance prerequisites, and last updated skill. `evidence-board.md` consolidates evidence from market research, customer discovery, reuse evaluation, technical spikes, commercialization work, dynamic supplemental data requirements, user-provided supplemental data, claim classification, decision dependencies, rejected option rationale, validation priority, and evidence gaps.

The final artifact is a Chinese pre-review package folder:

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

When an idea slug is available, the folder should be named:

```text
wheelwise-report-<idea-slug>/
  project-state.md
  evidence-board.md
  report.md
  index.html
  prototype.html
  assets/
```

`report.md` is the source of truth. `index.html` is the report visualization layer generated from the same Chinese report. `prototype.html` is the independent interaction prototype or simulator. `assets/` stores generated or selected visuals.

In V4.5, `report.md` must read like a real product pre-review package, with pre-review conclusion, executive summary, original assumptions, research method and evidence levels, review-board viewpoints, market attractiveness, competitors and substitutes, decision records, comparable scorecard, compliance and launch prerequisites, staged validation, frontend display/prototype, and final recommendation. Every important conclusion must be labeled as fact, assumption, inference, or evidence gap.

In V4.5, `index.html` must be a visual consulting-style pre-review layer. It converts the report's review state, scorecard, judgments, evidence, workflows, risks, validation experiments, commercialization notes, compliance reminders, and execution or validation plan into cards, matrices, timelines, flows, architecture diagrams, risk boards, validation boards, and action panels. It must not be a plain Markdown-to-HTML conversion, second report, short landing page, or prototype substitute.

`prototype.html` must simulate the product surface independently with local data, clickable controls, inputs, state changes, loading/empty/error/success states, responsive behavior, and a clear backend boundary. API, CLI, automation, backend, data, and developer-tool ideas use playground, terminal, request explorer, or workflow simulator modes. Offline, physical, regulated, or supply-chain ideas may use validation dashboards, cost/margin calculators, compliance checklists, supplier validation panels, or pilot-record boards.

V4.5 Gate behavior:

- Gate0 uses one Evidence Intake step. It returns `Ready`, `Need Basic Input`, or `Field Data Required`; dynamic supplemental-data checklists are generated from the detected idea-type combination and can resume from Gate0 when the user later provides data.
- Gate1 uses early feasibility screening. If the idea cannot continue, it stops; if it can continue, it automatically enters Discovery.
- Gate2 uses full feasibility review. `Go` maps to `可进入原型验证` or `可进入最小可行产品实验` and continues automatically; `Pivot`, `Need More Evidence`, `Kill`, and `Park` map to `建议转向后再评审`, `需要补充关键证据`, `建议放弃`, `建议暂缓`, or `仅作为参考` and ask the user for direction when needed.

V4.5 pre-review states:

| State | Meaning |
| --- | --- |
| 可进入原型验证 | Enough evidence exists for low-cost prototype or simulator validation |
| 可进入最小可行产品实验 | Evidence, scope, risk, and execution path are coherent enough for a bounded MVP experiment |
| 需要补充关键证据 | A high-impact evidence gap blocks a credible decision |
| 建议转向后再评审 | Evidence supports a materially different direction |
| 建议暂缓 | Timing, dependency, regulation, budget, team fit, or market condition blocks near-term progress |
| 建议放弃 | The idea is unsafe, implausible, undifferentiated, or lacks a credible user/buyer |
| 仅作为参考 | The idea is useful as learning or module reference but not worth direct build now |

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

## Internal Skills

| Skill | Role |
| --- | --- |
| `using-wheelwise` | Main router, Gate owner, evidence arbiter, review-board synthesizer, final pre-review package contract |
| `idea-intake` | Converts a raw idea into a structured brief |
| `surface-strategy` | Chooses website, webpage application, mobile app, desktop app, extension, API/service, CLI, or automation surface |
| `feasibility-review` | Maps feasibility verdicts to V4.5 pre-review states before delivery planning |
| `market-research` | Researches market category, competitors, substitutes, demand signals, trends, maturity, and entry barriers |
| `customer-discovery` | Defines personas, jobs-to-be-done, pain intensity, workflows, adoption objections, and validation experiments |
| `evidence-board` | Consolidates market, customer, reuse, technical-spike, and commercialization evidence into an internal decision ledger |
| `product-strategy` | Defines positioning, differentiation, product wedge, and minimum viable product scope |
| `reuse-evaluator` | Evaluates self-build, purchase, reuse, fork, and reference choices by module |
| `technical-planning` | Converts decisions into stack, architecture, data, integration, and deployment guidance |
| `commercialization` | Plans business model, pricing, packaging, channels, sales motion, and early monetization tests |
| `risk-review` | Reviews market, product, technical, legal, privacy, license, dependency, and execution risks |
| `visual-brief` | Plans or creates explanatory SVG, HTML/CSS, image, or fallback visual assets under `assets/` |
| `ui-demo` | Plans an independent clickable prototype, simulator, playground, terminal preview, or workflow preview |
| `report-visualization` | Turns `report.md` into `index.html` as a complete visual explanation layer |
| `execution-plan` | Produces state-appropriate build, prototype, validation, pivot, pause, stop, or reference-preservation tasks |
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
Report folder: wheelwise-report-community-tool-share/
Source report: wheelwise-report-community-tool-share/report.md
Web display: wheelwise-report-community-tool-share/index.html
Interactive prototype: wheelwise-report-community-tool-share/prototype.html
```

## Example

See the included V4.5-compatible canonical examples:

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

The examples demonstrate the V4.5 pre-review package contract, internal state, evidence board, Chinese Markdown report, visualized `index.html`, independent `prototype.html`, scorecards, review states, and visual assets that do not depend on AI image generation.

## Validation

Validate the example report folder:

```powershell
python scripts\check_report_contract.py examples\community-tool-share --folder --skip-filename --v4
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

Current plugin version: `4.5.0`.

V4.5 focuses on:

- `using-wheelwise` as controller, router, state manager, Gate controller, evidence arbiter, review-board synthesizer, self-check owner, and final pre-review package owner.
- `project-state.md` as internal workflow state.
- `evidence-board.md` as internal evidence ledger.
- Gate0, Gate1, and Gate2 flow discipline.
- Seven Chinese pre-review states.
- Evidence classification: fact, assumption, inference, and evidence gap.
- Decision records, rejected options, critical assumption dependencies, and comparable scorecards.
- Automatic continuation for normal `Go` paths.
- Evidence-based Discovery before Synthesis.
- Final Chinese report folder with `report.md`, visualized `index.html`, independent `prototype.html`, and `assets/`.
