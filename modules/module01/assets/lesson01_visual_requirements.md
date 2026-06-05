---
title: Lesson 1.1 — Visual Asset Requirements
lesson: 1.1
owner: Claude (specification + production + integration); Architect (approval)
note: Gemini removed from workflow; all assets are produced in-repo and renderable.
---

# Lesson 1.1 — Visual Asset Requirements

> The authoritative list of visuals for Lesson 1.1, their specs, and status. All assets are produced directly (SVG / Mermaid / interactive HTML) and live in the repository.

## Asset inventory

| ID | Asset | Type | Format | Status |
|----|-------|------|--------|--------|
| L1-V1 | Perception → Reasoning → Action loop | Diagram | SVG | ✅ Produced (`assets/diagrams/m01-l1-perception-action-loop.svg`) |
| L1-V2 | Software AI vs Physical AI (consequences) | Diagram | SVG | ✅ Produced (`assets/diagrams/m01-l1-software-vs-physical-ai.svg`) |
| L1-V3 | Pixels→frames→angles pipeline | Diagram | Mermaid | ✅ Produced (embedded in `site_src/module01/lesson01.md`) |
| L1-V4 | "Trace the loop" interactive | Interactive | HTML/JS | ✅ Produced (`modules/module01/demos/lesson01_trace_the_loop.html`) |

## Specifications

**Global conventions**
- Vector format (SVG) preferred for diagrams; scalable, editable, version-controllable.
- Palette: perceive = blue (#0ea5e9), reason = violet (#8b5cf6), act = green (#10b981), ink = #0f172a, muted = #64748b.
- Typography: system sans-serif; titles ~18 px, labels ~15 px, captions ~12 px.
- Every figure carries a one-line caption and an alt-text string for accessibility.
- Namespacing: `m01-l1-<slug>.svg`.

### L1-V1 — Perception → Reasoning → Action loop  *(maps to lesson §4)*
- **Objective:** show intelligence in the physical world as a closed loop; each stage speaks a different data "language" (pixels / meters / angles).
- **Scene:** three labeled stages (PERCEIVE, REASON, ACT) with forward arrows and a dashed return arrow ("check & repeat"); greenhouse framing.
- **Labels:** stage names; data type under each; "pixels→meters" and "meters→angles" over the gaps.
- **Animation notes (for an animated version):** one cycle — camera highlights tomato → coordinate readout appears → arm swings → loop pulses to restart.
- **Alt text:** "A closed loop with three boxes — Perceive (pixels), Reason (meters/frames), Act (joint angles) — and a return arrow labeled check and repeat."

### L1-V2 — Software AI vs Physical AI  *(maps to lesson §5)*
- **Objective:** contrast a wrong software output (a bad sentence) with a wrong physical output (a damaged stem / dropped fruit) — i.e. why precision is non-negotiable in Physical AI.
- **Scene:** split panel: left = a screen/chat producing text; right = the greenhouse robot acting on a real tomato, with a "physical consequence" callout.
- **Labels:** "Software AI: wrong → bad output" vs "Physical AI: wrong → physical consequence."
- **Animation notes:** static is sufficient.
- **Alt text:** "Split comparison: software AI errors produce text mistakes; physical AI errors produce real-world consequences."

### L1-V3 — "Trace the loop" poster frame  *(maps to lesson §7 / demo)*
- **Objective:** a representative still of the interactive demo for use in print/MkDocs where the live demo isn't available.
- **Scene:** the greenhouse scene with a tomato selected, showing its position readout and the arm mid-reach.
- **Dependency:** finalize after the interactive demo UI is built (see `demos/lesson01_trace_the_loop_spec.md`).
- **Alt text:** "A greenhouse robot reaching toward a selected tomato, with its position displayed."

## Acceptance criteria
- Renders cleanly at both small (inline, ~320 px wide) and large (full-width) sizes.
- Colorblind-safe; meaning never conveyed by color alone (labels present).
- Matches the conventions above and agrees visually with the notebook's Matplotlib figures.
- Alt text supplied for every asset.
