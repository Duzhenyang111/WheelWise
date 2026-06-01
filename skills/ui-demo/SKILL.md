---
name: ui-demo
description: Use when WheelWise must plan a complete interactive product demo for a user-visible product or a simulator for API, CLI, automation, or developer-tool products without connecting a real backend.
---

# UI Demo

Plan a complete interactive demo that helps users see and test the product concept before backend implementation. Use mock data, local state, fixtures, localStorage, static JSON, or simulated APIs instead of real backend services. For V2.5+ final output, write demo results so they can be inserted into the Chinese Markdown report's `UI Demo / 交互 Demo` section and, when enabled, into `wheelwise-report.html`.

## Demo Rule

- Website, web app, mobile app, desktop app, and browser extension ideas need a clickable front-end demo.
- API/SaaS backend ideas need an API playground, request/response explorer, docs preview, workflow simulator, or SDK quickstart simulator.
- CLI/dev tool ideas need a terminal simulator with commands, outputs, errors, config, and success states.
- Automation/workflow ideas need a trigger/action workflow simulator with retry, error, and success paths.

## Required Demo Coverage

Include:

- Page or screen structure.
- Core user flow.
- Clickable navigation.
- Forms and validation.
- State changes.
- Mock data source.
- Loading, empty, error, and success states.
- Responsive layout.
- Component structure.
- Run instructions.
- Demo boundaries: what is simulated and what is not.
- Demo path.
- HTML display placement when a static report display is generated.

## Design Adaptation

Read `references/ui-ux-pro-max-adaptation.md` when planning visual style or HTML display. Borrow the approach of using design intelligence, anti-pattern checks, and surface-aware styling, but do not copy external skill content.

Apply `../../shared/references/decision-rationale-standard.md` to demo format, stack, and flow decisions.

## HTML Display Spec

When the report needs an HTML companion, specify `wheelwise-report.html` as a static display layer sourced from the Markdown report. The spec must include:

- Cover and core conclusion.
- Decision map and MVP roadmap.
- Visual explanation assets or Mermaid fallback placement.
- Demo slice with the most important screen, simulator, or interaction state.
- Risk and validation section.
- Codex-ready execution plan section.
- Responsive behavior and accessibility expectations.
- Clear note that Markdown remains the source of truth.

If a UI/UX skill is available, it may guide layout, hierarchy, color, typography, and anti-pattern checks. If unavailable, provide a Codex-ready HTML implementation task instead of blocking.

## Output Shape

```text
Demo type:
Target surface:
Primary flow:
Pages/screens:
Interactions:
Mock data and state:
Loading/empty/error/success states:
Responsive behavior:
Component structure:
Demo path:
Run instructions:
Demo limitations:
HTML display file:
HTML display role:

Decision rationale:
Decision:
Why chosen:
Why alternatives lose:
Evidence:
Assumptions:
Risks:
Fallback:
Confidence:
```

In the final report, use Chinese field names:

```text
Demo 路径：
运行方式：
核心交互：
页面 / 屏幕 / 模拟器面板：
mock 数据说明：
loading / empty / error / success 状态：
未接入真实后端的范围：
HTML 展示文件：
HTML 展示用途：
```
