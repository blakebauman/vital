# Impeccable design system integration

Vital's design work uses the **impeccable** design-quality system as its craft layer. Impeccable (by pbakaus, Apache-2.0 — https://github.com/pbakaus/impeccable) gives AI-generated design a shared vocabulary for hierarchy, contrast, and restraint, plus a deterministic detector for AI-slop clichés. Use its concepts to set direction and its checklist to keep every asset from looking generically AI-made.

When the **impeccable** skill/plugin is installed in the project, defer to its commands for execution (see the command map below). When it is not installed, still apply the direction dimensions and the anti-slop checklist manually — they are the principles, not the tooling.

## 1. Register — the first decision

- **brand** — design *is* the product: landing pages, marketing sites, launch pages, brand showcases, campaigns. This is Vital's default, since Vital produces launch and marketing surfaces.
- **product** — design *serves* the product: dashboards, tools, admin, internal apps.

Most Vital deliverables are **brand** register. Name it explicitly before designing; it sets the defaults for every axis below.

## 2. Direction dimensions

Set the visual direction by placing the asset on these axes (derived from impeccable's design vocabulary). State where each lands and why, tied to the brand voice and the ICP.

- **Expressive axis** — `restrained` (muted, system-feeling) → `committed` (distinct palette/type, clear POV, functional hierarchy) → `drenched` (full saturation, full bleed, expressive type). Brand-register launch pages usually want `committed`; `drenched` for high-conviction brand moments.
- **Tone** — `serious` ↔ `neutral` ↔ `playful`. Independent of the expressive axis (a quiet design can be playful; a bold one can be serious). Enterprise skews serious; consumer/SMB can go playful.
- **Density** — `airy` (96px section padding; editorial-led only) / `balanced` (64–72px; brand-register default) / `packed` (40–48px; product or data-dense). Default `balanced` for brand launch pages. Reserve `airy` for genuinely editorial pages — on a multi-section marketing page it reads as empty padding and pushes the CTA below the fold.
- **Distinctiveness** — `familiar` (pattern-matched to category leaders) / `distinctive` (clearly itself, still legible) / `singular` (unmistakable; brand register, strong conviction). Aim for at least `distinctive` — `familiar` is where AI-default slop lives.
- **Audience** — not a slider but a tuple: who, in what context, with what cultural references (e.g. "enterprise procurement, on a 27-inch monitor at 9 a.m." vs "first-time users, mostly mobile, developing markets"). Write a one-line "scene sentence": where, when, and how the design is encountered.
- **Constraints** — hard walls that beat the stated direction: `a11y-first`, `perf-first`, `brand-faithful` (bolder *within* the existing palette, not a rebrand), `RTL-required`, `print-ready`. Honor constraints over expressive ambition.

## 3. Anti-slop checklist (run on every asset)

Reject these AI-design clichés — they are the tells that make design look machine-generated:

- Default/overused fonts (Inter, Arial, system-ui as the display face). Choose a deliberate type pairing.
- Cyan/purple or purple→blue gradients; "SaaS gradient" hero.
- Glassmorphism hero; dark glows; dark-mode-by-reflex when the brand doesn't call for it.
- Pure black (`#000`) or pure gray — tint neutrals toward the brand hue.
- Gray text on colored backgrounds (contrast + slop tell).
- Excessive card nesting; everything-in-a-card layouts.
- Bounce/elastic easing (dated). Use purposeful, restrained motion.
- Side-tab borders and other decorative-only chrome.

If the client has impeccable installed, run the detector to catch these deterministically:

```
npx impeccable detect src/
npx impeccable detect --json .
```

## 4. Impeccable command map (when impeccable is installed)

Defer execution to impeccable's commands rather than hand-rolling design steps. Syntax: `/impeccable <command> [target]`.

| Need | Command |
| --- | --- |
| One-time setup; write PRODUCT.md + DESIGN.md | `/impeccable init` |
| Plan UX/UI before coding | `/impeccable shape` |
| Full shape-then-build with visual iteration | `/impeccable craft` |
| Generate DESIGN.md from existing code | `/impeccable document` |
| Pull reusable components/tokens into a system | `/impeccable extract` |
| UX review: hierarchy, clarity, resonance | `/impeccable critique` |
| Technical checks: a11y, performance, responsive | `/impeccable audit` |
| Final pass, shipping readiness | `/impeccable polish` |
| Amplify / tone down | `/impeccable bolder` · `/impeccable quieter` |
| Strip to essence | `/impeccable distill` |
| Typography: fonts, hierarchy, sizing | `/impeccable typeset` |
| Strategic color | `/impeccable colorize` |
| Spacing and visual rhythm | `/impeccable layout` |
| Purposeful motion | `/impeccable animate` |
| Adapt for devices | `/impeccable adapt` |
| Iterate visual variants in the browser | `/impeccable live` |

Impeccable also reads `PRODUCT.md` (audience, positioning, voice, anti-references) and `DESIGN.md` (colors, type, components, principles), and respects existing design tokens and component libraries — align Vital's brief with those files when they exist.

## 5. How this fits Vital

- Vital's `brand` agent owns positioning-to-messaging; impeccable's `PRODUCT.md` should inherit that voice and positioning.
- Vital's `design` agent sets direction with the dimensions above and produces build-ready specs; impeccable executes the craft when installed, and Adobe Express/Adobe produces the final pixels.
- Impeccable is a companion, not a dependency: Vital's design still works without it, applying these principles by hand. When a client needs a full existing-site redesign, that is impeccable's own domain — hand it off there rather than doing site migration inside Vital.

*Impeccable is an independent open-source project (Apache-2.0). Vital adopts its principles and defers to its tooling when present; it does not vendor or modify impeccable.*
