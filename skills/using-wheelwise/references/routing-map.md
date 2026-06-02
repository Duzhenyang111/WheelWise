# WheelWise Routing Map

All routes return to `using-wheelwise` for state updates, Gate control, and synthesis.

| User request | Route |
| --- | --- |
| Raw idea, vague concept, "is this good?" | `idea-intake` -> Gate0 -> `surface-strategy` -> `feasibility-review: early-screening` |
| "Help me plan/build this idea" | V4 full workflow |
| "Which form should this take?" | `idea-intake` -> Gate0 -> `surface-strategy` |
| "Research this market" or "Who are the competitors?" | `market-research` -> `evidence-board`; optionally `parallel-research` |
| "Who is the customer?" or "How should I validate users?" | `customer-discovery` -> `evidence-board`; add `market-research` when current sources matter |
| "How should this make money?" or "What pricing/GTM should I use?" | `commercialization`; add `market-research` and `evidence-board` when competitor pricing or channels matter |
| "Should I build this myself?" | `reuse-evaluator` -> `evidence-board` -> `risk-review` |
| "Find existing tools/open-source alternatives" | `reuse-evaluator` -> `evidence-board`; optionally `parallel-research` |
| "Is this worth pursuing?" | `idea-intake` -> Gate0 -> `surface-strategy` -> `feasibility-review: early-screening`; full review if evidence exists |
| "Define MVP or product strategy" | Ensure Gate1 passed -> Discovery as needed -> `product-strategy` |
| "Pick stack or architecture" | `reuse-evaluator` -> `evidence-board` -> `technical-planning` -> `risk-review` |
| "Make this presentable" | Ensure Gate2 is Go or assumption-led -> `visual-brief` -> `ui-demo` -> `report-visualization` |
| "Create a clickable demo" | `product-strategy` -> `technical-planning` -> `ui-demo` |
| "Create API/CLI/automation demo" | `technical-planning` -> `ui-demo` simulator mode |
| "Turn this into Codex tasks" | Ensure state and evidence exist -> `execution-plan` |
| "Review risks" | `risk-review`; add `reuse-evaluator` and `evidence-board` if dependency/license risk is central |

## State Rules

- Before each routed skill, read `project-state.md`.
- After each routed skill, update `project-state.md`.
- Discovery outputs must update `evidence-board.md`.
- Final full reports must use `project-state.md` and `evidence-board.md` for synthesis.

## Research Rule

Use `../../shared/references/web-research-standard.md` whenever current market, user, pricing, channel, policy, license, vendor, or repository facts materially affect the answer.
