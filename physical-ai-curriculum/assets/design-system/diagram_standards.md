# Diagram Standards

> Conventions for *what* diagrams look like and *how* they communicate, across SVG, Mermaid, and interactive forms. Pairs with `svg_standards.md` (authoring) and `colors.md` / `typography.md` (tokens).

## Shared visual language

| Element | Convention |
|---|---|
| Loop stages | Perceive = sky `#0ea5e9`, Reason = violet `#8b5cf6`, Act = emerald `#10b981` |
| Correct / success | green (`#15803d` on `#dcfce7`) |
| Error / incorrect | red (`#b91c1c` on `#fee2e2`) |
| Target object (fruit) | rose `#e11d48` |
| Primary flow | solid arrow |
| Feedback / return | dashed arrow |
| Frames / axes | thin slate lines, labelled with axis + unit |

## When to use which form

- **SVG** — bespoke spatial figures: vectors, frames, dartboards, number lines, scene schematics. Default.
- **Mermaid** — flows, pipelines, taxonomies, state/sequence. Use when the content is a graph and hand-drawing nodes/edges in SVG would be busywork. Rendered on the site via the superfences `mermaid` fence.
- **Interactive HTML** — when manipulation teaches: dragging a vector, adjusting bias/scatter, moving a target, stepping a process. Only where it clearly beats a static figure (see `production_standards.md` §8).

## Mermaid conventions

- Prefer `flowchart LR` for pipelines, `flowchart TD` for taxonomies/trees.
- Label edges where the transition has meaning (e.g. units changing).
- Keep node text short; use `<br/>` for a second line (e.g. data type).
- Dashed edge (`-.->`) for feedback/return, matching the SVG convention.

## Figure hygiene

- One idea per figure; one title; a one-line caption beneath.
- Label every meaningful element; never rely on colour alone.
- Frame in the greenhouse context where natural.
- Match in-notebook Matplotlib plots to these conventions (same colours, labelled axes with units) so static and computed visuals feel like one family.

## Consistency check (per diagram)

- [ ] Uses the shared colour roles
- [ ] Solid vs dashed arrows used correctly
- [ ] Title + caption + labels present
- [ ] Reads without relying on colour
- [ ] Greenhouse framing where relevant
