---
name: design-brief
description: >
  Use this skill to set visual direction and produce launch creative — art
  direction, creative briefs, landing pages, decks, social and ad graphics,
  and asset kits, built to hand off in Adobe Express and the Adobe suite.
  Triggers include "design brief", "landing page", "launch graphics", "make
  my deck look good", "social creative", "art direction", or "visual identity
  for launch".
allowed-tools: Read, Write
metadata:
  version: "0.1.0"
---

Set a visual direction, then produce concrete, buildable creative for the launch. Pull the message and voice from brand's work. The client has Adobe Express and the wider Adobe suite, so every deliverable must be reproducible in those tools — a spec the client cannot rebuild is a failed deliverable.

**Design-quality layer (impeccable).** Use the impeccable design system as the craft layer for every asset — see `references/impeccable.md`. Set direction with its dimensions (register, expressive axis, tone, density, distinctiveness, audience, constraints), and run its anti-slop checklist on everything so nothing looks generically AI-generated (no default Inter/system display faces, no cyan/purple gradients, no glassmorphism hero, tint neutrals, restrained motion). When the impeccable skill/plugin is installed in the client's project, defer execution to its commands (`/impeccable init | shape | craft | critique | audit | polish | typeset | colorize | layout`) and its detector (`npx impeccable detect`). When it is not installed, apply the same principles by hand. Impeccable is a companion, not a Vital dependency; for a full existing-site redesign, hand off to impeccable's own domain rather than doing site migration inside Vital.

Match the visual register to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise reads polished, restrained, and trustworthy (plus procurement/security one-pagers and ROI visuals); mid-market is modern and confident; small business is bold, fast to grasp, and conversion-focused.

## 1. Art direction

Define the visual system once, then apply it everywhere:

- **Type** — a heading and body pairing (name specific fonts available in Adobe Fonts / Express).
- **Color** — a small palette with exact hex values, and the light/dark logic.
- **Layout** — the grid and spacing feel; how much room the message gets.
- **Imagery** — the style (photography, illustration, 3D, screenshots, generative via Firefly) and the mood.
- **Feel** — three adjectives the visuals should evoke, tied to the brand voice.

Place the asset on the impeccable direction dimensions (register — usually `brand` for launch surfaces; expressive axis; tone; density — default `balanced`; distinctiveness — aim past `familiar`; audience tuple; constraints) and write a one-line scene sentence. See `references/impeccable.md`.

If a dataviz or chart is part of any asset, read the `dataviz` skill before choosing chart colors and forms.

## 2. Asset spec

For each requested asset, write a brief the client can execute in Adobe Express: purpose, channel, exact dimensions, copy blocks (headline, subhead, CTA), color and font choices, imagery direction, and export format. Common specs:

- Social: 1080×1080 (feed), 1080×1920 (story/reel), 1200×630 (OG/link preview).
- Deck: 16:9, 1920×1080 per slide.
- Ads: match the platform's required sizes; state them.

## 3. Adobe production directions

Give step-followable directions: which Express template type to start from, how to set the Brand Kit (logo, colors, fonts), what to change, and how to export. Route heavier work to the right tool — Photoshop (compositing/retouch), Illustrator (vector/logo), InDesign (multi-page), Premiere/After Effects (video), Firefly (generative imagery). Always leave the client able to reproduce and edit the asset themselves.

## 4. Produce what you can here

- **Landing page** — deliver a single self-contained HTML file (inline CSS/JS), on-brand, ready to hand off or preview.
- **Deck** — use the pptx skill to build the actual slides.
- **Static graphics** — provide the exact Express build spec; generate a mockup or reference image only to illustrate direction.

## Output

Deliver the art-direction summary (with the impeccable direction dimensions named) plus a build-ready brief (or produced asset) for each item, with Adobe Express/Adobe directions, exact dimensions, and export formats. Run the anti-slop checklist before shipping any asset. Keep every asset within one visual system. Deliver files with SendUserFile; for a landing page or reusable tracker, consider persisting it as an artifact. Save the art direction to the project.

## Additional resources

- **`references/impeccable.md`** — the impeccable design-quality layer: register/expressive/tone/density/distinctiveness/audience/constraint dimensions, the anti-slop checklist, and the `/impeccable` command map (defer to it when impeccable is installed; apply the principles by hand when it is not).
