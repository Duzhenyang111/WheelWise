# UI UX Pro Max Adaptation for WheelWise

UI UX Pro Max is a design-intelligence reference for WheelWise `ui-demo`, `visual-brief`, and optional `wheelwise-report.html` display work. Use it as inspiration for systematic design choices, not as copied content.

## WheelWise Adaptation

For each demo, define:

- Product surface: website, web app, mobile, desktop, extension, API playground, CLI simulator, or workflow simulator.
- Audience: buyer, end user, developer, operator, or internal reviewer.
- Design intent: utilitarian, analytical, editorial, playful, premium, technical, or trust-heavy.
- Visual system: color role, typography role, spacing density, component language, icon use, and data-display style.
- Interaction model: navigation, forms, feedback, state transitions, and recovery paths.
- Anti-pattern checks: unclear hierarchy, fake static screens, missing states, one-note palette, poor mobile fit, inaccessible contrast, or demo flows that hide the core value.
- HTML report display: cover, core conclusion, decision map, MVP roadmap, visual explanation, demo slice, risk/validation, and execution-plan sections sourced from the Markdown report.

## Surface Guidance

| Surface | Demo emphasis |
| --- | --- |
| Marketing website | Conversion path, proof points, lead capture, responsive content |
| Web app | Auth shell, dashboard, workflow, data states, billing or settings when relevant |
| Mobile app | Onboarding, tab/navigation model, device-specific moments, offline or push states |
| Desktop app | Workspace layout, local file flows, preferences, update or import/export states |
| Browser extension | Popup/options/content-script context, permissions, privacy messaging |
| API/SaaS | Request builder, response viewer, docs, logs, usage limits, keys as mock artifacts |
| CLI/dev tool | Terminal simulator, command help, config, errors, success output |
| Automation tool | Trigger/action builder, run history, retries, error handling |

## Output Expectations

The demo should be believable enough for validation: a user can click through the core flow, see realistic data, encounter states, and understand what backend work remains.

For `wheelwise-report.html`, the design should make the report easier to present, not create a second source of truth. The HTML must preserve the Chinese conclusions and decisions from the Markdown report.
