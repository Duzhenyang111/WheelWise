# WheelWise

WheelWise is a Superpowers-style multi-skill pack for pre-development product and technical decisions.

Call the main skill:

```text
Use $using-wheelwise to evaluate this idea: ...
```

The main skill routes the work through internal skills for idea intake, delivery surface strategy, feasibility review, product strategy, build/buy/reuse/fork/reference analysis, technical planning, risk review, visual brief generation, optional interactive demo planning, optional parallel research, and Codex-ready execution planning.

Version 2.5+ keeps the V2 skill-pack architecture and standardizes the final artifact as one complete Chinese Markdown report file, with an optional static HTML display file for presentation.

1. Structure the raw idea.
2. Choose the delivery surface.
3. Judge feasibility.
4. Define product strategy and MVP workflow.
5. Decide Build / Buy / Reuse / Fork / Reference by module.
6. Produce a technical plan aligned with reuse decisions.
7. Review key risks.
8. Create image-level visual brief recommendations.
9. Plan an interactive UI demo or API/CLI/workflow simulator when applicable.
10. Produce a single progressive Chinese Markdown report file: `wheelwise-report.md`.
11. Optionally produce `wheelwise-report.html` as a display layer sourced from the Markdown report.

Default final artifact:

```text
wheelwise-report.md
```

If the user provides an idea name, WheelWise may use:

```text
wheelwise-report-<idea-slug>.md
```

The report body must be fully Chinese. Product names, technical stacks, code paths, commands, API names, and Build / Buy / Reuse / Fork / Reference labels may remain English when that is clearer.

The report must not use internal English module headings such as `Idea Intake` or `Reuse Evaluator`. It should read progressively: report guide, user/problem, decisions, visual/demo, risks/validation, execution plan, and final action advice.

The visual section should include generated image assets when available, or Mermaid fallback when image generation is unavailable. The demo section must include path, run method, core interactions, mock data, state coverage, and backend boundary.

External skills such as UI UX Pro Max, pm-skills, and awesome-copilot are reference resources or optional dependencies only. WheelWise does not copy their content.
