# WheelWise Implementation Method

> Research date: 2026-06-01  
> Purpose: turn WheelWise from a product concept into a reusable, extensible Build-vs-Buy-vs-Reuse skill system that Codex and other AI agents can use.

## 1. What WheelWise Solves

WheelWise is not a skill pack that tells an AI agent to start coding immediately.

It should be a pre-development product and technical decision system that helps users decide:

- Which modules should be bought as SaaS products or APIs.
- Which modules should reuse mature libraries, templates, or starter kits.
- Which modules are good candidates for forking open-source projects.
- Which modules should only be referenced, not reused directly.
- Which modules are actually worth building from scratch.

The one-line goal:

```text
Turn a product idea into an executable build plan through the fastest, most reliable path with the least wasted engineering effort.
```

## 2. Core Principle

Do not reinvent the wheel unless the wheel itself is the product differentiation.

Common decisions:

| Strategy | When to Use |
| --- | --- |
| Buy | Payments, authentication, email, monitoring, hosting, analytics, support, and other common infrastructure |
| Reuse | UI kits, admin templates, CMS systems, chart libraries, scheduling components, workflow libraries |
| Fork | An open-source project is very close to the target product but needs deep customization |
| Reference | Product experience, architecture, interaction patterns, or data models are useful, but the code or license is unsuitable for direct reuse |
| Build | Core business logic, differentiated workflows, proprietary algorithms, unique user experience |

WheelWise should not plan everything for its own sake. Its value is quickly identifying where engineering time should not be spent.

## 3. Keep Version 1 Small

The first version should not immediately build every specialist role. Start with a tight closed loop implemented as first-class skills:

- `using-wheelwise`
- `idea-intake`
- `surface-strategy`
- `feasibility-review`
- `reuse-evaluator`
- `risk-review`
- `execution-plan`

Add `parallel-research` as a support skeleton, but do not make subagents the default path.

### 3.1 Router

The Router is the entry-point orchestrator.

It decides what the user actually needs instead of always running the full workflow.

It must also classify the intended implementation form early, because a website, web app, mobile app, desktop app, browser extension, API/SaaS, CLI, or automation tool has different validation paths, reuse options, architecture choices, launch channels, and monetization models.

Typical routing:

| User Request | Modules to Call |
| --- | --- |
| "I have a SaaS idea, help me plan it" | Full workflow |
| "Should I build this feature myself?" | Reuse Evaluator + Risk Review |
| "Find open-source alternatives for this" | Reuse Evaluator |
| "Help me scope the MVP" | Idea Intake + Surface Strategy + Feasibility Review |
| "Generate Codex implementation tasks" | Execution Plan |
| "Review architecture risks" | Risk Review |

Key Router outputs:

- Task type.
- Implementation form.
- Skills to call.
- Whether web research is needed.
- Whether the local repository should be inspected.
- Final output format.

### 3.2 Reuse Evaluator

This is the core WheelWise module.

It researches existing solutions and recommends one option for each product module:

- Buy.
- Reuse.
- Fork.
- Reference.
- Build.

It should evaluate:

- SaaS products.
- APIs.
- Open-source repositories.
- Starter kits.
- Boilerplates.
- Libraries.
- Self-hosted tools.
- Common UX and architecture patterns.

The output should not be vague. It should make explicit decisions:

```text
Authentication: Buy, recommend Clerk/Auth0/Supabase Auth.
Payments: Buy, recommend Stripe Checkout.
Admin dashboard: Reuse, recommend shadcn + Tremor or a mature admin template.
Core recommendation algorithm: Build, because it is product differentiation.
```

### 3.3 Product + Architecture Planner

This module turns the product idea into an MVP and technical direction.

It should produce:

- Target users.
- User problems.
- Implementation form and delivery surface.
- MVP scope.
- Feature/module decomposition.
- User stories.
- Acceptance criteria.
- Technical stack recommendation.
- Data model outline.
- API/integration plan.
- Deployment plan.
- Architecture assumptions.

Its job is not to write a beautiful PRD for its own sake. Its job is to connect product choices to engineering consequences.

### 3.4 Engineering Executor

This module turns the previous decisions into Codex-executable work.

It should produce:

- Milestones.
- Tasks.
- Repository structure.
- File/module boundaries.
- Test strategy.
- Acceptance criteria.
- Codex-ready prompts.
- Implementation order.

Good output should look like:

```text
Milestone 1: Project scaffold and authentication

Task 1.1: Initialize the Next.js project
Task 1.2: Integrate Supabase Auth
Task 1.3: Add a protected dashboard route

Acceptance criteria:
- Unauthenticated users are redirected from dashboard to login
- Authenticated users can see the dashboard shell
- The auth guard has minimal test coverage
```

## 4. Standard Workflow

Default full workflow:

```text
User idea
-> Router classifies the request
-> Implementation form classification
-> Feature/module decomposition
-> Existing solution research
-> Build / Buy / Reuse / Fork / Reference decision matrix
-> MVP scope
-> Technical architecture
-> Risk review
-> Codex-ready build plan
```

WheelWise must also support short workflows.

If the user only asks whether a feature should use an open-source project, do not output a full PRD, UI plan, and roadmap.

Implementation form should affect the workflow:

| Form | Planning Emphasis |
| --- | --- |
| Marketing website | Positioning, landing page structure, CMS/content workflow, analytics, SEO, conversion, launch speed |
| Web app | Auth, dashboard flows, data model, permissions, billing, frontend/backend architecture, deployment |
| Mobile app | Platform choice, app store constraints, onboarding, push notifications, offline behavior, device APIs |
| Desktop app | Packaging, updates, local storage, OS integrations, distribution, cross-platform tradeoffs |
| Browser extension | Permissions, browser APIs, store review, content scripts, privacy, limited UI surface |
| API/SaaS backend | API design, auth, rate limits, docs, SDKs, uptime, observability, usage-based pricing |
| CLI/dev tool | Installation, command design, local environment assumptions, docs, package distribution |
| Automation/workflow tool | Trigger/action model, integrations, permissions, reliability, retry/error handling |

## 5. Decision Matrix

Every important module should be scored.

| Criteria | Question |
| --- | --- |
| Time to MVP | Which option can ship fastest? |
| Cost | What are the direct and hidden costs? |
| Maintenance burden | Who maintains it over time? |
| Vendor lock-in | How hard is it to replace later? |
| Customization difficulty | Can it support the product's special requirements? |
| Security risk | Does it handle sensitive data, permissions, payments, or identity? |
| License risk | Is commercial use allowed? Are there copyleft implications? |
| Product differentiation | Is this module core to the product's competitive advantage? |
| Team capability | Can the team operate and modify it? |
| Long-term scalability | Will it still work as usage grows? |
| Delivery surface fit | Does this option fit the chosen form: website, app, extension, API, CLI, or automation? |

Recommended rules:

- Prefer Buy for high-risk, common, non-differentiating modules.
- Prefer Reuse for mature, stable, low-lock-in, replaceable modules.
- Consider Fork when an open-source project is close to the goal but needs deep customization.
- Use Reference when legal, license, architecture, or quality issues make direct reuse unsuitable.
- Build only when the module creates real product differentiation.

## 6. Existing Skill Research

I researched the skills ecosystem and GitHub. The conclusion: WheelWise should not build every sub-capability itself. Some modules can directly reuse or adapt mature skills.

### 6.1 UI/UX: Strongly Reuse UI UX Pro Max

Candidate:

- GitHub: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Skills: https://skills.sh/nexu-io/open-design/ui-ux-pro-max
- Observed install count: about 947 installs.

Why it fits:

- It is not just a single `SKILL.md`.
- The repository contains `data/`, `scripts/`, and `templates/`.
- It includes many design data tables, such as colors, typography, icons, UX guidelines, UI reasoning, and framework stacks.
- It includes Python scripts for design-system generation and search.
- It includes multi-platform templates for Codex, Claude, Cursor, Copilot, and others.

Recommended WheelWise role:

```text
WheelWise should not build a full UI/UX knowledge base from scratch.
WheelWise's UI/UX Designer module should call or adapt UI UX Pro Max.
WheelWise only needs to pass product type, target users, feature modules, and constraints into the UI/UX skill.
```

Best outputs to use:

- Information architecture.
- Page structure.
- UI style direction.
- Design-system recommendation.
- Stack-specific UI implementation guidance.
- Anti-pattern checks.

### 6.2 Product Management: Reference product-on-purpose/pm-skills

Candidate:

- GitHub: https://github.com/product-on-purpose/pm-skills
- Example skill: https://skills.sh/product-on-purpose/pm-skills/deliver-acceptance-criteria
- Observed related install counts: `deliver-acceptance-criteria` about 209 installs, `develop-adr` about 168 installs.

Why it fits:

- It is a full product-management skill library, not a single markdown file.
- The repository contains `skills/`, `references/`, `commands/`, `docs/`, `_workflows/`, `agents/`, and `.codex-plugin/`.
- Each concrete skill usually has its own `SKILL.md` and `references/`.
- It covers PRDs, user stories, acceptance criteria, ADRs, competitive analysis, market sizing, personas, OKRs, dashboard requirements, experiment design, and more.

WheelWise modules that can reference or reuse it:

- `deliver-prd`
- `deliver-user-stories`
- `deliver-acceptance-criteria`
- `develop-adr`
- `discover-competitive-analysis`
- `discover-market-sizing`
- `foundation-lean-canvas`
- `foundation-persona`
- `define-prioritization-framework`

Recommended WheelWise role:

```text
WheelWise should not recreate a full PM methodology.
WheelWise's Product Planner can reuse pm-skills PRD, user story, acceptance criteria, and ADR templates.
WheelWise should keep its own build-vs-buy-vs-reuse decision layer.
```

### 6.3 Architecture and Security: Reference github/awesome-copilot, but Do Not Depend on a Single Skill

Candidate:

- GitHub: https://github.com/github/awesome-copilot
- Example skill: https://skills.sh/github/awesome-copilot/breakdown-epic-arch
- Observed `breakdown-epic-arch` install count: about 8.6K installs.

Why it is useful:

- The repository is large and includes `skills/`, `agents/`, `instructions/`, `workflows/`, `hooks/`, `docs/`, and more.
- It includes skills for architecture, compliance, security, supply chain, and codebase understanding.
- Some individual skills are just a single `SKILL.md`, but the repository itself has a rich agent-asset structure.

Useful references:

- `breakdown-epic-arch`
- `architecture-blueprint-generator`
- `agent-owasp-compliance`
- `agent-supply-chain`
- `acquire-codebase-knowledge`

Recommended WheelWise role:

```text
Architecture and security modules can reference awesome-copilot's structure and checklist dimensions.
WheelWise still needs its own risk-review skill because build/buy/reuse risk evaluation is more specific.
```

### 6.4 Open Source Evaluator: No Fully Matching Mature Skill Found

I searched for open source, security review, technical architecture, project planning, MVP scope, and related terms.

Some related candidates appeared:

- `shipshitdev/library@open-source-checker`
- `levnikolaevich/claude-code-skills@ln-645-open-source-replacer`
- `kostja94/marketing-skills@open-source-strategy`
- `slavingia/skills@mvp`
- `shipshitdev/library@mvp-architect`

But none fully match WheelWise's core purpose.

WheelWise needs:

```text
Search SaaS/API/OSS/starter kits by product module
-> Compare maturity, license, maintenance activity, customization cost, replacement cost
-> Recommend Buy / Reuse / Fork / Reference / Build
```

This should be built in WheelWise as its core moat.

## 7. Recommended WheelWise Composition

WheelWise should follow the Superpowers-style package structure: one installable skill pack that contains multiple real skills.

The user should usually call the main skill only:

```text
Use WheelWise to evaluate this idea: ...
```

The main skill then routes the work to the right internal skills. The internal modules should not be only reference files. They should be first-class skills with their own `SKILL.md`, triggers, workflows, references, and optional tools.

Recommended skill pack composition:

| Skill | Role |
| --- | --- |
| `using-wheelwise` | Main entry skill. Establishes routing, required workflow discipline, and when to call other WheelWise skills. |
| `idea-intake` | Structures the raw idea, assumptions, target user, problem, constraints, and success criteria. |
| `feasibility-review` | Judges whether the idea is worth pursuing, validating first, pausing, or rejecting. |
| `market-research` | Researches market category, competitors, substitutes, user demand, and maturity. |
| `customer-discovery` | Defines personas, jobs-to-be-done, pain intensity, interview questions, and validation experiments. |
| `product-strategy` | Defines positioning, differentiation, MVP scope, feature priority, and product wedge. |
| `surface-strategy` | Decides whether the idea should ship as a website, web app, mobile app, desktop app, extension, API/SaaS, CLI, or automation tool. |
| `reuse-evaluator` | Core WheelWise moat. Decides Build / Buy / Reuse / Fork / Reference per module. |
| `technical-planning` | Designs stack, architecture, data model, integrations, deployment, and implementation path. |
| `commercialization` | Plans business model, pricing, packaging, GTM, channels, and early monetization tests. |
| `risk-review` | Reviews license, security, privacy, compliance, dependency, market, and execution risks. |
| `parallel-research` | Optionally dispatches subagents for independent research or review when the idea is broad, high-risk, or module-heavy. |
| `execution-plan` | Produces Codex-ready milestones, tasks, file boundaries, tests, and acceptance criteria. |

## 8. Recommended Repository Structure

WheelWise should use a Superpowers-style multi-skill package structure.

The important design point: `skills/` contains multiple independent skills. Shared references, tools, and templates can live at the package level or inside individual skill folders when they are specific to one skill.

Version 1 implemented the core closed loop. Version 2 adds `product-strategy`, `technical-planning`, `visual-brief`, and `ui-demo` as first-class skills. Future versions can still add full `market-research`, `customer-discovery`, and `commercialization` skills.

```text
wheelwise/
  README.md
  IMPLEMENTATION_METHOD.md
  IMPLEMENTATION_METHOD_ZH.md
  .codex-plugin/
    plugin.json
  skills/
    using-wheelwise/
      SKILL.md
      references/
        routing-map.md
        workflow-modes.md
        final-output-contract.md
    idea-intake/
      SKILL.md
    feasibility-review/
      SKILL.md
    product-strategy/
      SKILL.md
    surface-strategy/
      SKILL.md
    reuse-evaluator/
      SKILL.md
    technical-planning/
      SKILL.md
    risk-review/
      SKILL.md
    visual-brief/
      SKILL.md
    ui-demo/
      SKILL.md
      references/
        ui-ux-pro-max-adaptation.md
    parallel-research/
      SKILL.md
      templates/
        subagent-brief.md
    execution-plan/
      SKILL.md
  shared/
    references/
      build-buy-reuse-vocabulary.md
      decision-rationale-standard.md
      output-quality-bar.md
      external-skills.md
    templates/
      new-product-brief.md
      final-wheelwise-report.md
      visual-brief.md
      ui-demo-spec.md
  examples/
    ai-resume-optimizer.md
```

## 9. How Main-Skill Routing Works

`using-wheelwise` should work like the main Superpowers entry skill: it loads first, establishes the process, and decides which specialized skills must be used.

It should not contain all domain knowledge. It should stay small and point to the right internal skill.

Example routing:

```text
User has only a vague idea
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review

User asks whether an idea is worth building
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review
-> reuse-evaluator
-> risk-review

User asks how to build a validated idea
-> using-wheelwise
-> idea-intake
-> surface-strategy
-> feasibility-review
-> reuse-evaluator
-> risk-review
-> execution-plan

User asks for broad market, competitor, or option research
-> using-wheelwise
-> parallel-research when the work can be split
-> using-wheelwise synthesizes final decision
```

External skills are still useful, but they are references or optional dependencies, not the structure of WheelWise itself.

Examples:

```text
UI/UX work can reference UI UX Pro Max.
PRD/user-story/ADR work can reference pm-skills.
Architecture/security checks can reference awesome-copilot.
```

But WheelWise remains a multi-skill package, not a single skill with internal markdown chapters.

## 10. Subagent Policy

WheelWise should support subagents, but it should not open subagents by default.

Rule:

```text
Default: main skill routes serially.
Complex idea: use subagents when useful.
High-risk decision: require independent review.
```

Subagents are optional acceleration and review tools, not the default execution model. The main `using-wheelwise` skill remains responsible for synthesis, judgment, and the final report.

Good subagent use cases:

| Area | Why Subagents Help |
| --- | --- |
| `market-research` | Competitors, substitutes, categories, and market maturity can be researched in parallel. |
| `reuse-evaluator` | SaaS/API/OSS options can be evaluated independently by product module. |
| `risk-review` | License, security, privacy, and dependency risks benefit from independent review. |
| `commercialization` | Pricing, GTM channels, packaging, and monetization tests can be explored separately. |
| `technical-planning` | Complex architecture can benefit from an independent critique pass. |

Poor subagent use cases:

| Area | Reason |
| --- | --- |
| `idea-intake` | Requires direct clarification with the user. |
| `surface-strategy` | Should establish one shared direction before deeper work starts. |
| `product-strategy` | Requires integrated judgment across market, user, and implementation context. |
| `execution-plan` | Final execution tasks must be unified by the main agent to avoid fragmented plans. |

`parallel-research` should trigger only when one or more conditions are true:

- The idea spans multiple independent markets, user groups, or modules.
- Multiple SaaS/API/open-source options need comparison.
- The user asks for broad or fast research.
- The decision is high-risk and needs independent review.
- The main agent believes single-threaded analysis may miss important perspectives.

Subagent outputs should be treated as evidence, not final decisions. `using-wheelwise` must synthesize the findings, resolve contradictions, state confidence, and produce the final recommendation.

## 11. First Implementation Plan

### Phase 1: Build the Superpowers-Style Skill Pack Skeleton

Deliverables:

- README.md.
- English and Chinese implementation methods.
- `.codex-plugin/plugin.json`.
- `skills/using-wheelwise/SKILL.md`.
- Initial internal skill directories.
- Build-vs-buy decision matrix template.
- One complete example.

### Phase 2: Build the Main Router Skill

Deliverables:

- Routing map.
- Workflow modes.
- Final output contract.
- Rules for when to call each internal skill.
- Rules for short workflow vs full workflow.

### Phase 3: Build the Reuse Evaluator

This is the most important phase.

Deliverables:

- OSS evaluation checklist.
- SaaS/API evaluation checklist.
- License-risk basics.
- Module decomposition template.
- Initial GitHub repo scoring script.
- Final recommendation format.

### Phase 4: Build Product and Commercialization Skills

Deliverables:

- `idea-intake`
- `feasibility-review`
- `market-research`
- `customer-discovery`
- `product-strategy`
- `surface-strategy`
- `commercialization`

Each should be a real skill folder with `SKILL.md` and only the references/templates it needs.

### Phase 5: Build Subagent Support

Deliverables:

- `parallel-research`
- Subagent trigger rules.
- Research brief template.
- Synthesis report template.
- Rules for when subagent review is required vs optional.

### Phase 6: Codex-Ready Output

Deliverables:

- `technical-planning`
- `risk-review`
- `execution-plan`
- Engineering task template.
- Milestone template.
- Acceptance criteria template.
- Test strategy template.
- Complete Codex execution plan for an example project.

### Phase 7: Test with Real Product Ideas

Use real product ideas to test WheelWise:

- AI resume optimization website.
- Booking system.
- B2B SaaS dashboard.
- AI agent marketplace.
- Content management system.

Each test should check:

- Whether WheelWise overbuilds.
- Whether it misses mature alternatives.
- Whether it ignores license risks.
- Whether it outputs tasks that cannot be executed.
- Whether it gives clear recommendations instead of vague suggestions.

## 12. Most Important Product Boundary

WheelWise's core is not UI, PRDs, architecture diagrams, or project management.

Existing skills can help with those areas.

What WheelWise should own is:

```text
Product module decomposition
+ existing solution research
+ build/buy/reuse/fork/reference decisions
+ risk review
+ Codex-ready development task generation
```

That is what separates WheelWise from a generic product-planning tool or a generic coding agent.

## 13. Version 2 Upgrade: Explainable, Visual, Demo-Ready Product Plans

V2 preserves the V1 Superpowers-style multi-skill pack architecture. `using-wheelwise` remains the only main entry skill, and new capabilities are added as first-class skill folders instead of being hidden inside one large reference directory.

V2 upgrades WheelWise from "Codex-ready execution plan" to:

```text
Explainable product decision
+ image-level visual brief
+ interactive demo or simulator plan
+ Codex-ready execution plan
```

### 13.1 V2 Main Workflow

```text
idea-intake
-> surface-strategy
-> feasibility-review
-> product-strategy
-> reuse-evaluator
-> technical-planning
-> risk-review
-> visual-brief
-> ui-demo when applicable
-> execution-plan
-> New Product Brief
```

### 13.2 V2 First-Class Skills

| Skill | Role |
| --- | --- |
| `product-strategy` | Connects `feasibility-review` to positioning, differentiation, MVP scope, user-facing workflow, feature priority, product wedge, and validation focus. |
| `technical-planning` | Connects `reuse-evaluator` to stack, architecture, data model, integrations, deployment path, surface constraints, and technical risks without contradicting module decisions. |
| `visual-brief` | Produces image-level visual explanation specs such as concept images, decision maps, MVP roadmaps, module maps, architecture illustrations, demo mockups, and validation funnels. Mermaid is fallback only. |
| `ui-demo` | Produces a full interactive demo spec using mock data, local state, fixtures, static JSON, localStorage, or simulated APIs. For API/CLI/automation products, it specifies a playground, terminal simulator, request explorer, or workflow simulator. |

### 13.3 Decision Rationale Standard

Every key decision must include:

```text
Decision
Why chosen
Why alternatives lose
Evidence
Assumptions
Risks
Fallback
Confidence
```

This applies to verdict, delivery surface, product strategy, Build / Buy / Reuse / Fork / Reference decisions, technical stack, visual brief, UI demo, commercialization notes, and execution order.

### 13.4 Visual Brief Rules

`visual-brief` should make the recommendation easier to explain to stakeholders and users.

Allowed outputs include:

- Product concept image.
- Decision map.
- MVP roadmap.
- Module map.
- Architecture illustration.
- Demo mockup.
- Validation funnel.

Each visual must include title, type, what it explains, why it helps, image prompt or production method, fallback, and report placement. It may reference UI UX Pro Max as design intelligence, but must not copy external skill content.

### 13.5 UI Demo Rules

`ui-demo` should plan a complete interactive front-end demo for user-visible products without requiring a real backend.

The demo must include page or screen structure, core flow, clickable navigation, forms, state changes, mock data, loading/empty/error/success states, responsive behavior, component structure, run instructions, and demo boundaries.

For products without a traditional UI:

- API/SaaS backend: API playground, request/response explorer, docs preview, or workflow simulator.
- CLI/dev tool: terminal simulator with commands, outputs, errors, and success states.
- Automation/workflow tool: trigger/action simulator with run history, retry, error, and success states.

### 13.6 V2 Repository Additions

```text
skills/
  product-strategy/
    SKILL.md
  technical-planning/
    SKILL.md
  visual-brief/
    SKILL.md
  ui-demo/
    SKILL.md
    references/
      ui-ux-pro-max-adaptation.md
shared/
  references/
    decision-rationale-standard.md
  templates/
    visual-brief.md
    ui-demo-spec.md
```

### 13.7 V2 Final Report Requirements

The full New Product Brief must include:

- Idea summary.
- Delivery surface.
- Verdict.
- Decision rationale summary.
- Target customer.
- Problem and urgency.
- Market notes.
- Customer assumptions.
- Differentiation.
- MVP scope.
- Product strategy.
- Build / Buy / Reuse / Fork / Reference decisions.
- Technical implementation path.
- Visual Brief.
- UI Demo / Interaction Demo.
- Commercialization notes.
- Key risks.
- Validation experiments.
- Codex-ready execution plan.

`execution-plan` must include tasks for generating the visual brief and the UI demo or simulator.

## 14. Version 2.5 Upgrade: Single Chinese Markdown Report File

V2.5 does not replace the V2 architecture. `using-wheelwise` remains the only main entry skill, and `visual-brief`, `ui-demo`, `product-strategy`, `technical-planning`, and `decision-rationale-standard` remain first-class capabilities.

The V2.5 change is the final artifact contract:

```text
WheelWise final output = one complete Chinese Markdown report file
```

Default filename:

```text
wheelwise-report.md
```

If the user provides an idea name, WheelWise may use:

```text
wheelwise-report-<idea-slug>.md
```

The report body must be fully Chinese. Product names, technical stacks, code paths, commands, API names, and Build / Buy / Reuse / Fork / Reference labels may remain English.

### 14.1 V2.5 Required Report Sections

The Markdown report must include these Chinese sections:

1. 项目标题
2. 想法摘要
3. 交付形态
4. 结论：构建 MVP / 先验证 / 暂停 / 放弃
5. 决策解释摘要
6. 目标用户
7. 问题与紧迫性
8. 市场备注
9. 用户假设
10. 差异化
11. MVP 范围
12. 产品策略
13. Build / Buy / Reuse / Fork / Reference 决策
14. 技术实现路径
15. 视觉说明
16. UI Demo / 交互 Demo
17. 商业化备注
18. 关键风险
19. 验证实验
20. Codex-ready 执行计划

### 14.2 Chinese Decision Rationale

Every key decision in the final report must explain:

```text
决策是什么
为什么选择它
为什么不选替代方案
证据
假设
风险
fallback
信心等级
```

This applies to verdict, delivery surface, product strategy, Build / Buy / Reuse / Fork / Reference decisions, technical stack, visual brief, UI demo, commercialization notes, and execution order.

### 14.3 Visual and Demo Integration

`visual-brief` outputs must be written into the `视觉说明` section. If image assets exist, reference them with Markdown:

```markdown
![产品概念图](./assets/visual-brief.png)
```

If only prompts or production methods exist, write those prompts or methods in the same section.

`ui-demo` outputs must be written into the `UI Demo / 交互 Demo` section, including:

- Demo path.
- Run command.
- Core interactions.
- Mock data notes.
- Loading / empty / error / success states.
- Scope not connected to a real backend.

### 14.4 Execution Plan Requirement

`execution-plan` must include a task to generate or update the Chinese Markdown report file. The final chat response should state the report path and a brief completion summary, not replace the report with a chat-only summary.

## 15. Version 2.5.1 Upgrade: Progressive Chinese Report and Optional HTML Display

V2.5.1 tightens the final report contract based on real output failures. The problem to prevent is a report that looks like internal skill outputs pasted together, contains English module headings, lacks images or diagrams, and ends without concrete next actions.

### 15.1 Progressive Report Structure

The final Markdown report must be structured as a reader-facing product brief:

```text
Report guide
-> User and problem
-> Decisions and recommended solution
-> Visual explanation and interactive demo
-> Commercialization, risks, and validation
-> Codex-ready execution plan
-> Final recommendation and next actions
```

In the actual report, these sections must be written in Chinese. Do not use headings such as `Idea Intake`, `Surface Strategy`, `Reuse Evaluator`, `Technical Planning`, `Risk Review`, `UI Demo Scope`, or `MVP Execution Plan`.

### 15.2 Required Opening and Ending

The opening section `报告说明与阅读导览` must include:

- Report purpose.
- Applicable stage.
- Core conclusion preview.
- Reading path.

The ending section `最终建议与下一步行动` must include:

- One-sentence judgment.
- 7-day action.
- 14-day action.
- 30-day action.
- go/no-go or continue/stop conditions.

### 15.3 Visual Priority

WheelWise should prioritize real image assets when image generation is available. Generated or existing assets must be referenced from the Markdown report with normal Markdown image syntax.

If image generation is unavailable, WheelWise must fall back to Mermaid. At least one visual fallback must be a decision map, MVP roadmap, or validation funnel.

### 15.4 HTML Display Layer

WheelWise may generate `index.html` inside the report folder as a static display layer. `report.md` remains the source of truth.

The HTML display should include:

- Cover.
- Core conclusion.
- Decision map.
- MVP roadmap.
- Visual explanation.
- Demo section.
- Risk and validation section.
- Execution plan.

UI UX Pro Max or other UI/UX skills may be used as design intelligence for the HTML display, visual brief, or demo plan, but WheelWise must not copy external skill content.

### 15.5 Self-Check and Validation

Before final response, `using-wheelwise` must check:

- The report file follows the `wheelwise-report*.md` naming rule.
- All required Chinese sections exist and appear in progressive order.
- The opening and ending sections are detailed.
- No forbidden English skill-module headings remain.
- `视觉说明` contains an image reference or Mermaid fallback.
- `UI Demo / 交互 Demo` contains path, run method, core interactions, mock data, state coverage, and backend boundary.
- `HTML 展示文件` records the HTML display rule even when HTML generation is skipped.

The repository includes `scripts/check_report_contract.py` to validate final reports and templates against these contract rules.

## 16. Version 2.7 Upgrade: Report Folder and Fully Chinese User-Facing Artifacts

V2.7 supersedes the V2.5 single-file output rule. The final artifact is now a complete report folder, not an isolated Markdown file.

Default output:

```text
wheelwise-report/
  report.md
  index.html
  assets/
    concept.png
    decision-map.png
    roadmap.png
```

When an idea slug is available:

```text
wheelwise-report-<idea-slug>/
  report.md
  index.html
  assets/
```

`report.md` is the source report. `index.html` is the display layer sourced from the same Chinese report. `assets/` stores all generated or selected images and static resources.

### 16.1 Fully Chinese Visible Text

All user-facing visible text in generated artifacts must be Chinese:

- Markdown body, section names, table fields, alt text, and chart labels.
- Webpage copy, navigation labels, buttons, captions, and image alt text.
- Text inside generated images when image text is used.

Technical stacks, commands, file paths, package names, API names, and code identifiers may remain English because they are technical references, not display copy.

Use Chinese display terms in final artifacts:

```text
自研
购买
复用
分叉改造
参考
网页应用
软件服务
最小可行产品
演示
模拟数据
兜底方案
继续 / 停止条件
可交给 Codex 执行的计划
```

If image generation cannot reliably render Chinese text, prefer text-free images and place the Chinese explanation in `report.md` and `index.html`.

### 16.2 Skill Updates

- `using-wheelwise` owns final synthesis, routing discipline, folder creation rules, and Chinese visible-text self-checks.
- `final-output-contract.md` defines the folder structure, naming, required files, image rules, and validation rules.
- `new-product-brief.md` and `final-wheelwise-report.md` use `report.md` as the source report and include an output-folder field.
- `visual-brief` saves image assets under `assets/` and requires Chinese image text or text-free images.
- `ui-demo` specifies `index.html` as the webpage display file and requires all visible interface copy to be Chinese.
- `execution-plan` includes tasks for creating the report folder, writing `report.md`, generating `index.html`, saving assets, and running contract checks.

### 16.3 Validation

Use folder mode for generated outputs:

```text
python scripts/check_report_contract.py wheelwise-report-<idea-slug> --folder
```

Use `--skip-filename` for example folders whose directory name is intentionally shorter:

```text
python scripts/check_report_contract.py examples/ai-resume-optimizer --folder --skip-filename
```

The validator must reject missing `report.md`, missing `index.html`, missing `assets/`, missing image assets, broken Markdown image references, broken HTML image references, and common English display terms in Markdown or webpage visible text.
