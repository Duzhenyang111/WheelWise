---
name: ui-demo
description: Use when WheelWise must plan a complete interactive product demo for a user-visible product or a simulator for API, CLI, automation, or developer-tool products without connecting a real backend.
---

# UI Demo

Plan a complete interactive demo that helps users see and test the product concept before backend implementation. Use simulated data, local state, fixtures, localStorage, static JSON, or simulated APIs instead of real backend services. For final output, write demo results into the Chinese source report's `交互演示` section and into the report folder's `index.html`.

## Demo Rule

- Website, web app, mobile app, desktop app, and browser extension ideas need a clickable front-end demo.
- API or software-service backend ideas need an API playground, request/response explorer, docs preview, workflow simulator, or SDK quickstart simulator.
- CLI/dev tool ideas need a terminal simulator with commands, outputs, errors, config, and success states.
- Automation/workflow ideas need a trigger/action workflow simulator with retry, error, and success paths.

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
- Webpage display placement when a static report display is generated.

## Design Adaptation

Read `references/ui-ux-pro-max-adaptation.md` when planning visual style or webpage display. Borrow the approach of using design intelligence, anti-pattern checks, and surface-aware styling, but do not copy external skill content.

Apply `../../shared/references/decision-rationale-standard.md` to demo format, stack, and flow decisions.

## Webpage Display Spec

When the report needs a webpage companion, specify `index.html` inside the report folder as a static display layer sourced from `report.md`. The spec must include:

- Cover and core conclusion.
- Decision map and MVP roadmap.
- Visual explanation assets or Mermaid backup placement.
- Interaction slice with the most important screen, simulator, or interaction state.
- Risk and validation section.
- 可交给 Codex 执行的计划 section.
- Responsive behavior and accessibility expectations.
- Clear note that `report.md` remains the source report.

If a UI/UX skill is available, it may guide layout, hierarchy, color, typography, and anti-pattern checks. If unavailable, provide a task that Codex can implement instead of blocking. All visible output text must be Chinese.

## Output Shape

```text
演示类型:
Target surface:
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
Webpage display file:
Webpage display role:

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
网页展示文件：
网页展示用途：
```
