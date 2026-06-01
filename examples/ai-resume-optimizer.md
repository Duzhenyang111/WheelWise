# Example: AI Resume Optimizer

## Idea Summary

A tool that helps job seekers tailor resumes to specific job descriptions and produce improvement suggestions.

## Delivery Surface

Primary surface: Web app.

Why: Users need accounts, saved resumes, upload history, billing, and repeated workflows. A marketing website can support acquisition, but the product value lives in the authenticated workflow.

## Verdict

Validate First.

Reason: The workflow is technically straightforward, but differentiation and willingness to pay are uncertain in a crowded category.

## Build / Buy / Reuse / Fork / Reference Decisions

| Module | Decision | Suggested option | Rationale | Risk |
| --- | --- | --- | --- | --- |
| Authentication | Buy | Clerk, Auth0, or Supabase Auth | Common non-differentiating infrastructure | Vendor lock-in |
| Payments | Buy | Stripe Checkout | Common high-risk payment workflow | Pricing/package still uncertain |
| Resume parsing | Reuse | Mature document parsing libraries or APIs | Faster MVP; parsing quality matters | Data privacy |
| AI feedback engine | Build | Product-specific prompt/evaluation pipeline | Main differentiation | Quality and trust |
| Admin dashboard | Reuse | Existing admin UI kit/template | Not differentiating | Template bloat |
| Competitor UX | Reference | Study category patterns | Useful patterns but no direct code reuse | Avoid copycat positioning |

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
