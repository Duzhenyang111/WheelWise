# Project State

`project-state.md` is an internal WheelWise workflow state file. It is not a final report section and must not replace `report.md`.

## Identity

Idea summary: AI 简历优化器，帮助求职者根据岗位描述诊断和修改简历。

Idea slug: ai-resume-optimizer

Target customer: 应届生和转岗求职者。

Problem and urgency: 简历与岗位匹配度不清晰，修改频繁。

Current phase: V4.5 pre-review package complete.

Last updated by skill: using-wheelwise

Last updated reason: V4.5 example upgrade.

## Routing State

Delivery surface: 网页应用

Secondary surfaces: 无

Workflow mode: V4.5 full workflow

Applicability class: digital product / personal information

Evidence requirement status: enough for prototype validation

Required supplemental data: 5 位求职者访谈、付费意向测试

Gate0 intake status: Ready

Waiting for supplemental data: No

Supplemental data checklist version: V4.5-resume-001

Resume from phase: Phase 1 Discovery if new data arrives

Resume instruction: Merge user data into evidence-board.md and rerun Gate2 mapping.

Last user supplemental data received: None

Gate status: Gate2 Go mapped to 可进入原型验证

Gate rationale: 需求和形态清晰，但商业化和差异化证据不足。

Next skill: ui-demo validation

User input required: No

## Feasibility State

Early-screening verdict: Can continue

Full-review verdict: Go

Feasibility confidence: Medium

Stop / continue rationale: Continue only into prototype validation.

Validation threshold: 5 位测试者中 3 位认可建议差异。

Pre-review state: 可进入原型验证

Next-stage recommendation: Build clickable prototype and run user tests.

Review scorecard: 用户问题强度 4/5; 目标用户清晰度 4/5; 证据充分度 2/5; 市场机会 3/5; 差异化 3/5; 交付形态匹配 4/5; 技术可行性 4/5; 商业化可行性 2/5; 风险可控性 3/5; 执行复杂度 4/5.

Comparable idea score: Medium

## Pre-Analysis State

Idea type: AI-assisted job-search workflow tool

Key job to be done: Tailor a resume to a target job with understandable revision rationale.

Current workaround: Generic chat tools, friends, templates, recruiting-platform suggestions, or paid resume services.

Biggest opportunity: Job-specific and explainable resume advice that feels more useful than generic rewriting.

Biggest uncertainty: Whether job seekers perceive enough difference to reuse or pay.

Biggest adoption resistance: Resume privacy concerns and fear of generic or misleading suggestions.

Strongest substitute: Generic chat tools.

Evidence-supported stage: Prototype validation.

Highest-information validation action: Job-specific resume suggestion prototype test with target job seekers.

Narrative angle: Clear workflow, crowded substitutes, privacy-sensitive prototype validation.

Report variation notes: Emphasize differentiation from generic rewriting and privacy trust.

## Strategy State

Product strategy summary: 岗位化简历诊断与改写建议。

Minimum viable product scope: 简历输入、岗位输入、匹配评分、建议和风险提示。

Differentiation: 可解释的岗位匹配建议。

Product wedge: 应届生和转岗人群的单岗位简历修改。

## Evidence State

Evidence-board path: evidence-board.md

Evidence summary: 需求为推断，隐私风险为事实，付费意愿为证据缺口。

Evidence coverage: product, user, risk, technical, commercialization gaps

Evidence gaps: real interviews, pricing, current competitors

Highest-impact evidence gap: willingness to pay

Data sufficiency: enough for prototype validation, not full build

Contradictions: demand likely exists but substitutes are strong

Assumptions: users will upload resume text in a safe prototype

Original assumptions: build complete AI resume optimizer

Critical assumption dependencies: user trust, suggestion quality, privacy boundary

Options considered: full build, prototype validation, pause, reference-only

Options rejected: full build

Supporting evidence summary: clear workflow and common job-seeking need

Opposing evidence summary: generic tools can replace shallow suggestions

Direction shift level: Minor

User confirmation status: Not required

Limited assessment boundary: no legal or platform-policy guarantee

## Reuse And Technical State

Reuse decisions summary: reuse model capability, build workflow.

Technical plan summary: static prototype with local simulated data.

Technical spike status: needed for suggestion quality.

Integration constraints: no real backend in prototype.

## Commercial And Risk State

Commercialization summary: pricing unvalidated.

Risk summary: privacy and generic-output risk.

Compliance prerequisites summary: privacy policy and personal information boundary.

Highest-priority risk: resume personal information.

Mitigation summary: local simulation and clear no-upload boundary.

## Visual And Demo State

Visual/demo status: prototype planned and example generated.

Visual assets planned: concept image.

Visual assets created: assets/concept.png

Interaction demo type: webpage prototype

Interaction demo path: prototype.html

## Final Report State

Final report status: complete

Report folder: examples/ai-resume-optimizer/

Source report path: report.md

Web display path: index.html

Prototype path: prototype.html

Assets path: assets/

Self-check status: pending validation script

## Open Items

Open questions: willingness to pay, competitor pricing, privacy requirements

Blocking unknowns: real user evidence

Recommended next action: run prototype validation
