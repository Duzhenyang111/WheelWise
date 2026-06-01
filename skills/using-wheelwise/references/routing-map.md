# WheelWise Routing Map

| User request | Route |
| --- | --- |
| Raw idea, vague concept, "is this good?" | `idea-intake` -> `surface-strategy` -> `feasibility-review` |
| "Help me plan/build this idea" | Full core workflow |
| "Which form should this take?" | `idea-intake` -> `surface-strategy` |
| "Research this market" or "Who are the competitors?" | `market-research`; optionally `parallel-research` |
| "Who is the customer?" or "How should I validate users?" | `customer-discovery`; add `market-research` when user evidence needs current sources |
| "How should this make money?" or "What pricing/GTM should I use?" | `commercialization`; add `market-research` when competitor pricing or channels matter |
| "Should I build this myself?" | `reuse-evaluator` -> `risk-review` |
| "Find existing tools/open-source alternatives" | `reuse-evaluator`; optionally `parallel-research` |
| "Is this worth pursuing?" | `idea-intake` -> `surface-strategy` -> `feasibility-review` |
| "Define MVP or product strategy" | `feasibility-review` -> `market-research` when current evidence matters -> `customer-discovery` -> `product-strategy` |
| "Pick stack or architecture" | `reuse-evaluator` -> `technical-planning` -> `risk-review` |
| "Make this presentable" | `visual-brief`; add `ui-demo` and `index.html` display when interaction or presentation helps |
| "Create a clickable demo" | `product-strategy` -> `technical-planning` -> `ui-demo` |
| "Turn this into Codex tasks" | Ensure V2 decisions exist, then `execution-plan` |
| "Review risks" | `risk-review`; add `reuse-evaluator` if dependency/license risk is central |

Always return to `using-wheelwise` for synthesis.

Final full reports must return through `using-wheelwise` for the Chinese report folder contract: `report.md`, `index.html`, and `assets/`.

Use `../../shared/references/web-research-standard.md` whenever current market, user, pricing, channel, policy, license, vendor, or repository facts materially affect the answer.
