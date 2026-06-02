# Decision Rationale Standard

Every key WheelWise decision must explain the decision, not only state it.

In the final WheelWise report, use Chinese field names:

```text
决策是什么：
原始假设是什么：
为什么选择它：
为什么不选替代方案：
数据来源：
证据类型：
证据强度：
哪些证据支持：
哪些证据反驳：
证据缺口：
为什么需要调整：
偏移程度：
证据：
假设：
风险：
兜底方案：
信心等级：
```

Use this structure for verdict, delivery surface, product strategy, module strategy, technical stack, visual brief, UI demo, commercialization notes, and execution order:

```text
Decision:
Original assumption:
Why chosen:
Why alternatives lose:
Data source:
Evidence type:
Evidence strength:
Supporting evidence:
Opposing evidence:
Evidence gap:
Why adjust:
Direction shift:
Evidence:
Assumptions:
Risks:
Fallback:
Confidence:
```

Guidelines:

- Evidence can be user-provided facts, repository inspection, current web research, known platform constraints, or explicit analysis.
- Every conclusion must be backed by user-provided data, first-hand field data, current-source evidence, prototype observation, technical spike, or an explicit evidence gap.
- Assumptions must be labeled when evidence is missing.
- Confidence must be High, Medium, or Low.
- Fallback should name the next-best option or the validation step that changes the decision.
- If a decision depends on current vendor, competitor, license, or repository facts, verify with current sources or mark the evidence gap.
- If the recommendation differs from the user's original direction, explain why the original direction is weak or not recommended.
- Direction shift must be `None`, `Minor`, or `Major`. Major shifts require Gate2 user confirmation before Delivery.
- If a conclusion has no supporting data, do not present it as a conclusion; mark it as an assumption or `Need More Evidence`.
