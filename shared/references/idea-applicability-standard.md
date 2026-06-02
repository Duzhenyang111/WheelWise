# Idea Applicability Standard

WheelWise is primarily a pre-build validation system for digital products, software products, internet services, automation tools, developer tools, and ideas that can be explained through a web display or prototype.

For offline, physical, local, regulated, supply-chain, hardware, or professional-service ideas, WheelWise should not pretend to be a full industry consultant. It should classify the idea, request the missing evidence early, and provide a limited assessment only when enough data exists.

## Applicability Classes

Use one or more classes:

- Digital product: SaaS, web app, mobile app, browser extension, API, CLI, automation, AI tool, developer tool, content tool.
- Local / offline business: stall, store, school-area business, community service, local life service, event, pop-up, field sales.
- Physical product / hardware: manufactured goods, devices, inventory-heavy goods, certification-heavy products.
- Supply-chain business: sourcing, warehousing, logistics, fulfillment, minimum-order, after-sales, distributor, import/export.
- Regulated product: food, education, medical, finance, insurance, recruitment, minors, personal information, location data, content distribution, payments, AI, algorithmic recommendation.
- Platform-dependent product: WeChat, app store, marketplace, Shopify, Chrome extension store, social platform, payment platform, API ecosystem.
- B2B / enterprise product: buyer and user differ, procurement, contract, integration, security review, pilot customer.
- Content / community / service product: content supply, creator operations, retention, moderation, monetization, customer success.

## Gate0 Evidence Intake

Run this intake after `idea-intake` and before normal Discovery. It is the single Gate0 entrance for both basic routing information and external or first-hand evidence needs.

Gate0 returns exactly one status:

- `Ready`: the idea has enough basic routing information and enough evidence to continue.
- `Need Basic Input`: the only blocker is missing basic routing information. Ask at most three necessary questions: target customer, validation vs MVP intent, and constraints.
- `Field Data Required`: the idea needs first-hand field, market, compliance, supply-chain, hardware, platform, B2B, content/community, or service data before any high-confidence verdict.

If basic input and first-hand data are both missing, ask the fewest basic questions required for routing and include the Phase 1 supplemental-data checklist in the same Gate0 response. Do not split this into two Gate0 interruptions.

If the idea is local, offline, physical, regulated, supply-chain, hardware-heavy, platform-dependent, B2B, content/community, or service-heavy and the user has not provided enough first-hand data, do not produce a high-confidence verdict. Return a dynamic `补充数据清单` generated from the detected idea-type combination.

The checklist must include:

- Applicability class.
- Why each data group is needed.
- Required data.
- Collection method.
- Minimum sample.
- Continue threshold.
- Stop threshold.
- Compliance items to confirm.

Never return a generic checklist when the idea has a specific type. Composite ideas combine checklist modules. For example, "sell one-yuan turkey noodles beside a Nanchang middle school" combines local/offline business, physical food sales, minors context, and geography-heavy constraints.

## Resumable Gate0 Pause

When Gate0 returns `Field Data Required`, write the pause into `project-state.md`:

- Gate0 intake status: `Field Data Required`.
- Waiting for supplemental data: yes.
- Supplemental data checklist version.
- Resume from phase: `Gate0 Evidence Intake`.
- Resume instruction: the user can reply later with collected data and WheelWise must rerun Gate0 before continuing.
- Last user supplemental data received.

When the user later provides data, record it in `evidence-board.md` as user-provided or first-hand field data, compare it against the continue and stop thresholds, then rerun Gate0 Evidence Intake. If a long time has passed, keep first-hand user data but refresh or mark stale market, competitor, regulation, and platform-rule evidence as needing re-check.

## Required Data By Class

Local / offline business:

- Location: city, district, exact point, allowed operating area, time window.
- Foot traffic: count target-user flow during peak windows for 2-3 days.
- Competitors: nearby sellers, categories, prices, queue length, stability.
- Purchase behavior: observed purchase rate among a counted sample.
- Compliance: owner, school, property, city management, market regulation, food safety, health certificate, stall permission.
- Unit economics: materials, packaging, utilities, transport, labor, loss, expected price, gross margin.
- Pilot data: 1-3 day trial sales if legally allowed, including sales, gross profit, complaints, and enforcement interruptions.

Physical / hardware / supply-chain:

- BOM or unit cost, prototype cost, supplier options, minimum order quantity, lead time, certification, inventory risk, returns, warranty, logistics, after-sales.

Regulated product:

- Jurisdiction, user type, sensitive data, industry category, license or filing requirements, professional review owner, privacy/security obligations, platform review path.

Platform-dependent product:

- Platform rules, API access, review requirements, fee model, distribution limits, account risk, dependency fallback.

B2B / enterprise:

- Buyer, user, budget owner, procurement path, sales cycle, pilot customer, integration and security review burden.

Content / community / service:

- Content supply, creator or operator effort, acquisition channel, activation, retention, moderation, monetization, service capacity.

## China Compliance Reminder

Compliance does not block the default WheelWise flow, but it must appear in the final report when relevant. Treat these as launch prerequisites or professional-review items, not legal conclusions.

For China mainland internet or commercial products, check whether the idea may involve:

- Business entity: company or individual industrial/commercial household before formal commercial operation, invoicing, contracts, hiring, or platform entry.
- ICP filing or telecom value-added license: websites, domains, servers, and internet information services.
- App filing: mobile apps providing internet information services in China mainland.
- Mini-program, app-store, or marketplace review.
- Public security network filing where applicable.
- Privacy policy, user agreement, personal information protection, sensitive personal information, minors' information, data security, cross-border data.
- Payments, advertising, membership, commission, marketplace transaction, invoices, taxation.
- AI / algorithm / generated content: algorithm recommendation filing, generative AI service filing or application registration, model/provider status, content safety.
- Industry license or special review: food, education, medical, finance, insurance, recruitment, maps/location, live streaming, social/content, minors.

When compliance status is unknown, the final report may still continue, but it must say formal launch requires confirmation. Do not write that the product can directly launch.

Useful official-source starting points:

- Market entity registration: `https://app.www.gov.cn/govdata/gov/202108/24/475109/article.html`
- Non-commercial internet information service filing: `https://wap.miit.gov.cn/zcfg/xxtxl/art/2024/art_7e48434c08c24131b4b7eecfca5b2b6c.html`
- MIIT filing service page: `https://ythzxfw.miit.gov.cn/bssx/alx/dxhhlw/art/2025/art_88c400fc83904008bcf5b11bc08ec18f.html`
- Generative AI service rules: `https://www.gov.cn/zhengce/zhengceku/202307/content_6891752.htm`

Use current official or high-confidence sources for any concrete compliance statement. If no source is checked, mark the item as pending confirmation.

## Evidence Rule

Every conclusion must be backed by source evidence, user-provided data, first-hand field data, prototype observation, technical spike, or an explicit evidence gap. If no data supports a conclusion, label it as an assumption and lower confidence.
