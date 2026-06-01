# Example: AI Resume Optimizer

## Idea Summary

A tool that helps job seekers tailor resumes to specific job descriptions and produce improvement suggestions.

## Delivery Surface

Primary surface: Web app.

Why: Users need accounts, saved resumes, upload history, billing, and repeated workflows. A marketing website can support acquisition, but the product value lives in the authenticated workflow.

## Verdict

Validate First.

Reason: The workflow is technically straightforward, but differentiation and willingness to pay are uncertain in a crowded category.

## Decision Rationale Summary

| Decision area | Decision | Why chosen | Why alternatives lose | Evidence | Assumptions | Risks | Fallback | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Verdict | Validate First | Crowded category and unclear willingness to pay | Building full SaaS first risks wasted engineering | Category is visibly crowded; user willingness to pay not proven | Job seekers will try a focused resume workflow | Low differentiation | Concierge validation landing page | Medium |
| Surface | Web app | Users need saved resumes, uploads, history, and billing | Pure website cannot support repeated workflow | Product requires account workflow | Browser is acceptable for resume work | Data privacy | Start with landing page plus form | High |

## Build / Buy / Reuse / Fork / Reference Decisions

| Module | Decision | Suggested option | Rationale | Risk |
| --- | --- | --- | --- | --- |
| Authentication | Buy | Clerk, Auth0, or Supabase Auth | Common non-differentiating infrastructure | Vendor lock-in |
| Payments | Buy | Stripe Checkout | Common high-risk payment workflow | Pricing/package still uncertain |
| Resume parsing | Reuse | Mature document parsing libraries or APIs | Faster MVP; parsing quality matters | Data privacy |
| AI feedback engine | Build | Product-specific prompt/evaluation pipeline | Main differentiation | Quality and trust |
| Admin dashboard | Reuse | Existing admin UI kit/template | Not differentiating | Template bloat |
| Competitor UX | Reference | Study category patterns | Useful patterns but no direct code reuse | Avoid copycat positioning |

## Visual Brief

Recommended visuals:
- Product concept mockup showing resume, job description, and AI feedback side by side.
- Decision map explaining Validate First before full SaaS.
- Validation funnel from visitor to submitted resume to paid pilot.

## UI Demo / Interaction Demo

Demo type: Web app clickable prototype with mock data.

Core flow:
- Landing page.
- Resume upload and job description form.
- Analysis loading state.
- Feedback dashboard.
- Empty/error/success states.

Backend boundary: simulate parsing and AI feedback with static JSON and local state.

## Codex-Ready Execution Plan

Milestone 1: Validation landing page and concierge workflow.

Tasks:
- Build a landing page with job-seeker positioning.
- Add resume and job-description intake form.
- Route submissions to manual review or a lightweight AI draft workflow.
- Track conversion and completion rate.

Acceptance criteria:
- A user can submit a resume and job description.
- The system stores the request or sends it to an operator inbox.
- The team can measure visitor-to-submission conversion.

Demo task:
- Build an interactive mock resume analysis flow with local fixtures, loading state, error state, and sample feedback.

Visual task:
- Generate the concept mockup, validation funnel, and decision map prompts before demo implementation.
