# WheelWise

WheelWise is a Superpowers-style multi-skill pack for pre-development product and technical decisions.

Call the main skill:

```text
Use $using-wheelwise to evaluate this idea: ...
```

The main skill routes the work through internal skills for idea intake, delivery surface strategy, feasibility review, product strategy, build/buy/reuse/fork/reference analysis, technical planning, risk review, visual brief generation, optional interactive demo planning, optional parallel research, and execution planning.

Version 2.7 keeps the V2 skill-pack architecture and standardizes the final artifact as one complete report folder. The folder contains a Chinese source report, a Chinese static webpage, and image assets.

1. Structure the raw idea.
2. Choose the delivery surface.
3. Judge feasibility.
4. Define product strategy and minimum viable product workflow.
5. Decide whether each module should be built, bought, reused, forked, or used as reference.
6. Produce a technical plan aligned with reuse decisions.
7. Review key risks.
8. Create image-level visual brief recommendations.
9. Plan an interactive UI demo or API/CLI/workflow simulator when applicable.
10. Produce a progressive Chinese Markdown source report: `report.md`.
11. Produce a Chinese static webpage display layer: `index.html`.
12. Save visual assets under `assets/`.

Default final artifact:

```text
wheelwise-report/
  report.md
  index.html
  assets/
```

If the user provides an idea name, WheelWise may use:

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  assets/
```

All user-visible copy in `report.md`, `index.html`, image text, chart labels, alt text, table fields, and report explanations must be Chinese. Technical stacks, code paths, commands, package names, API names, and code identifiers may remain English.

Use Chinese display terms in generated artifacts: 自研, 购买, 复用, 分叉改造, 参考, 网页应用, 软件服务, 最小可行产品, 演示, 模拟数据, 兜底方案, 继续 / 停止条件, 可交给 Codex 执行的计划.

The report must not use internal English module headings such as `Idea Intake` or `Reuse Evaluator`. It should read progressively: report guide, user/problem, decisions, visual/demo, risks/validation, execution plan, and final action advice.

The visual section should include generated image assets when available, or Mermaid as a Chinese-labeled backup when image generation is unavailable. The demo section must include path, run method, core interactions, simulated data, state coverage, and backend boundary.

External skills such as UI UX Pro Max, pm-skills, and awesome-copilot are reference resources or optional dependencies only. WheelWise does not copy their content.
