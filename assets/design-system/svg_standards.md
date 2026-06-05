# SVG Standards

> How every SVG asset is authored, so diagrams are consistent, accessible, scalable, and reviewable in version control.

## Structure

- Root: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H" role="img" aria-label="...">`.
- Set `viewBox`; do **not** hard-code root `width`/`height` (let it scale; size at the embed point).
- Keep a small, sane coordinate space (e.g. 760×360 for wide diagrams, 420×400 for square scenes).
- Group related elements; comment non-obvious geometry.

## Accessibility

- Mandatory `role="img"` + `aria-label` (or a `<title>` child) summarizing the figure for screen readers.
- Never encode meaning in colour alone — every coloured element also carries a text label.
- Maintain AA contrast for text.

## Style

- Colours: design-system tokens only (`colors.md`). Stage colours fixed (perceive/reason/act).
- Type: `typography.md` scale; system sans-serif `font-family` on the root.
- Strokes: 2–2.5 px for primary, 1.5 px for secondary; rounded corners `rx≈12–14` on panels.
- Arrows: define one `<marker>` and reuse; solid = primary flow, dashed = feedback/return.
- Backgrounds: transparent or `Soft` (`#f8fafc`); avoid full-bleed white blocks that fight the page.

## Naming & location

- Authored SVGs live in `assets/diagrams/`, named `mNN-lN-slug.svg` (module, lesson, slug).
- A copy is placed in `site_src/assets/` for the site to serve (until single-source sync is adopted).

## Encoding gotchas

- Use XML entities for `&`, `<`, `>`, arrows (`&#8594;` for →) inside text nodes.
- Keep text as real `<text>` (selectable, accessible), not paths.

## Review checklist

- [ ] `viewBox` set, no fixed root size
- [ ] `role="img"` + `aria-label`
- [ ] palette + type tokens only
- [ ] labels on all meaningful elements
- [ ] legible at 320 px wide
