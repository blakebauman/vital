# The default launch stack: Cloudflare, free plan first

When a client has no web stack yet, or is weighing one, Vital's default recommendation for the **launch surface** is Cloudflare, starting on the Free plan and upgrading only when a named trigger fires. It covers the landing page, forms, web analytics, tag and consent loading, inbound email, and launch-day traffic protection on one account, and most launches never leave the free tier.

Vital **specifies**; the client's engineers **deploy**. Every recommendation here is a decision and a spec, not a deployment Vital performs.

> **Prices and limits change.** Figures below were checked against Cloudflare's own pages on **2026-11-11**. Before quoting any number to a client, re-check the source page linked in [Sources](#sources) and cite it with the date you checked. Never quote a figure from memory.

## When not to recommend it

Default, not dogma. Recommend something else, and say why, when:

- **The client already runs a working stack.** Moving a working site for a launch is risk without return. Fit Vital's advice to what they have.
- **The app is deeply tied to another platform** (e.g. heavy use of a host's proprietary features). Cloudflare can host the marketing site alone; it does not need to host the product.
- **Enterprise procurement dictates the vendor.** Enterprise clients usually have an approved CDN/WAF already; Vital advises within it.
- **Product analytics is the question.** Cloudflare Web Analytics measures *the site*; it does not do funnels, cohorts, or identified-user product analytics. Pair it with a product analytics tool (see the `measurement` skill), don't substitute it.

## Map: launch need → Cloudflare product → free tier → upgrade trigger

| Launch need | Product | Free tier (as of 2026-11-11) | Upgrade when | Next step and price |
| --- | --- | --- | --- | --- |
| Landing page / marketing site | Workers + Workers Static Assets (preferred over Pages for new sites) | Static asset requests **free and unlimited**; Workers 100,000 requests/day, 10 ms CPU per invocation | Server-side logic exceeds 100k requests/day or needs more CPU | Workers Paid, **$5/month minimum** per account: 10M requests/month included, then $0.30/M |
| Waitlist / signup storage | D1 (SQL) or KV | D1: 5M rows read/day, 100k rows written/day, 5 GB total; KV: 100k reads/day, 1k writes/day | Writes exceed the daily cap on launch day | Workers Paid: D1 50M rows written/month included; KV 1M writes/month included |
| Forms without spam or bots | Turnstile | Up to 20 widgets, **unlimited** challenges; validate tokens server-side | More than 20 widgets or Bot Management needed | Enterprise |
| Uploads, press-kit downloads, media | R2 | 10 GB-month storage, 1M Class A / 10M Class B requests per month, **egress free** | Storage or request volume above the free tier | Pay as you go: $0.015/GB-month |
| Privacy-first web analytics | Cloudflare Web Analytics | Free; works **without** moving DNS or proxying through Cloudflare; Cloudflare states it does not collect visitors' personal data and does not track individuals across sites | Need funnels, cohorts, or identified users | Add a product analytics tool; this layer stays free |
| Third-party tags (pixels, chat widgets) | Zaraz | 1,000,000 events/month on every account | Over 1M events/month | Zaraz Paid: $5/month per additional 1M events |
| Custom-domain inbound email (`press@`, `hello@`) | Email Routing | Free forwarding to verified addresses | Need to *send* from the app | Email Sending requires Workers Paid |
| Launch-day traffic spikes and attacks | CDN cache + DDoS + WAF | **Unmetered DDoS protection** and the Free Managed Ruleset on every plan; 1 rate-limiting rule (by IP, 10 s period) | You need more than one rate limit or longer windows | Pro: 2 rules; Business: 5 rules |
| Queue visitors when the app can't scale | Waiting Room | **Not available** on Free or Pro | The product (not the site) has a hard capacity ceiling | Business: 1 basic room |
| A/B tests on the landing page | Workers (split traffic at the edge) | Within Workers free limits | Test traffic needs more than 100k requests/day | Workers Paid |
| Logs for debugging launch day | Workers Logs | 200,000 events/day, 3-day retention | Need more volume or 7-day retention | Workers Paid: 20M events/month included |

## The plan ladder

Application services plans (per domain), from Cloudflare's plans page on 2026-11-11:

| Plan | Price | What it adds that a launch cares about |
| --- | --- | --- |
| **Free** | $0 | Unmetered DDoS, WAF with Free Managed Ruleset, global CDN, 70 Rules, 1 rate-limiting rule. Community support. No SLA. |
| **Pro** | $20/month billed annually, $25 monthly | Lossless image optimization, 225 Rules, 2 rate-limiting rules, ticket support. No SLA. |
| **Business** | $200/month billed annually, $250 monthly | **100% uptime SLA**, chat support, Waiting Room (1 room), 5 rate-limiting rules, PCI DSS 4.0. |
| **Enterprise** | Custom, billed annually | 24×7 phone support, higher SLA credits, advanced rate limiting, Bot Management, more rooms. |

**Workers Paid** ($5/month minimum per account) is separate from these. It raises compute and storage limits, and is usually the first and only upgrade a small launch needs.

## Default by segment

- **Small business:** Free plan, plus Workers Paid ($5/month) only if the site has server logic that might exceed 100k requests/day. Total infrastructure for the launch is often $0–$5/month. Lead with this in `bootstrapping`: the launch surface should not cost money before revenue.
- **Mid-market:** Free or Pro, plus Workers Paid. Move to Business when a contract or customer requires an uptime SLA, or when the product needs a Waiting Room for a known demand spike.
- **Enterprise:** advise within the client's approved vendor. If Cloudflare is the vendor, Business is the floor for the SLA and chat support; anything beyond that is a contract conversation.

## Launch-day checklist (for `launch-plan` and `/vital:readiness`)

Frame these as checks for the client's engineers, never as work Vital does:

1. The landing page is served as static assets (free, unlimited, cached at the edge), so the page itself cannot fall over.
2. The signup or waitlist path has been load-tested against the expected peak, and its writes fit the storage tier, or Workers Paid is on before launch day.
3. Every public form has Turnstile with **server-side** token validation.
4. One rate-limiting rule protects the most expensive endpoint (signup, trial creation).
5. Web Analytics (and Zaraz, if third-party tags are used) is installed and verified **before** traffic arrives.
6. If the *product* has a hard capacity ceiling, decide in advance between a Business-plan Waiting Room and a waitlist page, rather than discovering the ceiling live.

## Sources

Re-check these before quoting a figure:

- Workers and storage pricing: https://developers.cloudflare.com/workers/platform/pricing/
- Application services plans: https://www.cloudflare.com/plans/network-cdn/
- Turnstile plans: https://developers.cloudflare.com/turnstile/plans/
- Web Analytics: https://developers.cloudflare.com/web-analytics/about/
- Zaraz pricing: https://developers.cloudflare.com/zaraz/pricing-info/
- Email Routing: https://developers.cloudflare.com/email-routing/
- Waiting Room plans: https://developers.cloudflare.com/waiting-room/plans/
- Rate-limiting rules: https://developers.cloudflare.com/waf/rate-limiting-rules/
- Static assets: https://developers.cloudflare.com/workers/static-assets/
