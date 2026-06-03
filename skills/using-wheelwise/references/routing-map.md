# WheelWise Routing Map

All routes return to `using-wheelwise` for state updates, Gate control, pre-review state mapping, evidence arbitration, and synthesis.

| User request | Route |
| --- | --- |
| Raw idea, vague concept, "is this good?" | `idea-intake` -> Gate0 -> `surface-strategy` -> `feasibility-review: early-screening` |
| "Help me plan/build this idea" | V4.5 full workflow; if evidence is weak, produce validation tasks instead of a full build plan |
| "Which form should this take?" | `idea-intake` -> Gate0 -> `surface-strategy` |
| "Research this market" or "Who are the competitors?" | `market-research` -> `evidence-board`; optionally `parallel-research` |
| "Who is the customer?" or "How should I validate users?" | `customer-discovery` -> `evidence-board`; add `market-research` when current sources matter |
| "How should this make money?" or "What pricing/GTM should I use?" | `commercialization`; add `market-research` and `evidence-board` when competitor pricing or channels matter |
| "Should I build this myself?" | `reuse-evaluator` -> `evidence-board` -> `risk-review` |
| "Find existing tools/open-source alternatives" | `reuse-evaluator` -> `evidence-board`; optionally `parallel-research` |
| "Is this worth pursuing?" | `idea-intake` -> Gate0 -> `surface-strategy` -> `feasibility-review: early-screening`; full review if evidence exists; return a Chinese pre-review state |
| "Define MVP or product strategy" | Ensure Gate1 passed -> Discovery as needed -> `product-strategy` |
| "Pick stack or architecture" | `reuse-evaluator` -> `evidence-board` -> `technical-planning` -> `risk-review` |
| "Make this presentable" | Ensure Gate2 maps to 可进入原型验证 / 可进入最小可行产品实验 or is explicitly assumption-led -> `visual-brief` -> `ui-demo` -> `report-visualization` |
| "Create a clickable demo" | `product-strategy` -> `technical-planning` -> `ui-demo` |
| "Create API/CLI/automation demo" | `technical-planning` -> `ui-demo` simulator mode |
| "Turn this into Codex tasks" | Ensure state and evidence exist -> `execution-plan` |
| "Review risks" | `risk-review`; add `reuse-evaluator` and `evidence-board` if dependency/license risk is central |

## State Rules

- Before each routed skill, read `project-state.md`.
- After each routed skill, update `project-state.md`.
- Discovery outputs must update `evidence-board.md`.
- Final full reports must use `project-state.md` and `evidence-board.md` for synthesis.
- Final full reports must include V4.5 pre-review state, evidence classification, review-board viewpoints, decision records, and comparable scorecard.
- If the pre-review state is `需要补充关键证据`, `建议转向后再评审`, `建议暂缓`, `建议放弃`, or `仅作为参考`, route `execution-plan` toward validation, pivot, pause, stop, or learning-preservation tasks instead of full development tasks.

## Research Rule

Use `../../shared/references/web-research-standard.md` whenever current market, user, pricing, channel, policy, license, vendor, or repository facts materially affect the answer.
