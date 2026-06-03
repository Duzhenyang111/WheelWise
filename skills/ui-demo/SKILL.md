---
name: ui-demo
description: Use when WheelWise must plan a complete interactive product demo for a user-visible product or a simulator for API, CLI, automation, or developer-tool products without connecting a real backend.
---

# UI Demo

Plan a complete interactive prototype that helps users try the product concept before backend implementation. Use simulated data, local state, fixtures, localStorage, static JSON, or simulated APIs instead of real backend services. For final output, write prototype results into the Chinese source report's `前端展示与交互原型` section and create or specify `prototype.html`.

For non-digital ideas, `prototype.html` may be a validation tool instead of a product UI: field-data checklist, trial dashboard, cost/gross-margin calculator, supplier/BOM tracker, compliance checklist, pilot-record board, or continue/stop decision panel.

`ui-demo` does not own `index.html`. The report display page is handled by `report-visualization`.

## Demo Rule

- Website, web app, mobile app, desktop app, and browser extension ideas need a clickable front-end demo.
- API or software-service backend ideas need an API playground, request/response explorer, docs preview, workflow simulator, or SDK quickstart simulator.
- CLI/dev tool ideas need a terminal simulator with commands, outputs, errors, config, and success states.
- Automation/workflow ideas need a trigger/action workflow simulator with retry, error, and success paths.
- Local/offline, physical, regulated, supply-chain, or hardware-heavy ideas need a validation workflow prototype when a product UI would be misleading.

In V4.5, no product skips interaction demonstration only because it lacks a traditional graphical UI. API, CLI, automation, backend, data, or developer products must use simulator mode. If the pre-review state is `需要补充关键证据`, `prototype.html` may be a validation simulator instead of a product UI.

## Required Demo Coverage

Include:

- Page or screen structure.
- Core user flow.
- Clickable navigation.
- Forms and validation.
- State changes.
- Simulated data source.
- Loading, empty, error, and success states.
- Responsive layout.
- Component structure.
- Run instructions.
- Demo boundaries: what is simulated and what is not.
- Demo path.
- Prototype path, normally `prototype.html`.

## Design Adaptation

Read `references/ui-ux-pro-max-adaptation.md` when planning prototype style, layout, interaction states, and anti-pattern checks. Borrow the approach of using design intelligence and surface-aware styling, but do not copy external skill content.

Apply `../../shared/references/decision-rationale-standard.md` to demo format, stack, and flow decisions.

## Prototype Spec

Create or specify an interactive prototype page, defaulting to `prototype.html`, for every product surface:

- Website idea: show the actual website UI and its key interactions.
- Web application idea: show the dashboard/workspace flow.
- Mobile app idea: simulate a phone frame with mobile navigation and touch-like interactions.
- Desktop app idea: simulate desktop windows, sidebars, menus, and local-file flows.
- Browser extension idea: simulate popup, options page, and content-script context.
- API/software-service backend idea: simulate an API playground, request builder, response viewer, docs, logs, and keys.
- CLI/developer tool idea: simulate a terminal with commands, outputs, config, errors, and success states.
- Automation/workflow idea: simulate trigger/action builder, run history, retry, error, and success paths.
- Local/offline idea: simulate field observation entry, competitor rows, compliance notes, cost/margin calculator, trial results, and continue/stop status.
- Physical/supply-chain idea: simulate BOM, supplier options, minimum order quantity, lead time, certification status, inventory risk, and pilot order decision.
- Regulated idea: simulate launch-readiness checklist, professional-review items, data/privacy boundary, and go-live prerequisite tracking.

The prototype page must use local simulated data and must explain what is simulated. It is separate from the report display page.

The prototype must include at least one real state transition. Prefer multiple states: loading, empty, error, success, validation failure, pending review, completed, or retry.

## V4 State Integration

- Read `project-state.md` before choosing the demo mode.
- Use delivery surface and Gate2 status to decide whether to create a UI prototype, API playground, CLI simulator, workflow simulator, request explorer, or terminal simulator.
- Use V4.5 pre-review state to decide whether the prototype demonstrates the product concept, validates an evidence gap, or preserves a reference-only learning artifact.
- Use applicability class to decide whether `prototype.html` should be a product UI or a validation tool.
- Update `project-state.md` with prototype status, interaction demo type, interaction demo path, simulated states, backend boundary, and last updated by skill.
- If no prototype is generated in the current run, write a concrete prototype task into `execution-plan`.

## Output Shape

```text
演示类型:
Pre-review state:
Target surface:
Applicability class:
Primary flow:
Pages/screens:
Interactions:
模拟数据和状态:
Loading/empty/error/success states:
Responsive behavior:
Component structure:
演示路径:
Run instructions:
演示限制:
Interactive prototype file:
Interactive prototype role:

Decision rationale:
Decision:
Why chosen:
Why alternatives lose:
Evidence:
Assumptions:
Risks:
兜底方案:
Confidence:
```

In the final report, use Chinese field names:

```text
演示路径：
运行方式：
核心交互：
页面 / 屏幕 / 模拟器面板：
模拟数据说明：
加载 / 空状态 / 错误 / 成功状态：
未接入真实后端的范围：
交互原型文件：
交互原型用途：
```
