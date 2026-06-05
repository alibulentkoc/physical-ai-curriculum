# Typography

> Type conventions for diagrams, interactives, and the site. Goal: legible, consistent, dependency-free.

## Font family

System sans-serif stack (no web-font downloads, renders everywhere):

```
Segoe UI, Helvetica, Arial, sans-serif
```

The MkDocs Material theme uses its default (Roboto); diagrams and interactives use the system stack above so SVGs render identically offline.

## Scale (SVG / diagrams)

| Role | Size | Weight | Color token |
|---|---|---|---|
| Title | 18 px | 700 | Ink |
| Label | 15 px | 600 | Ink |
| Body | 13–14 px | 400–600 | Slate |
| Caption | 12 px | 400 | Muted |

## Scale (interactive HTML)

| Role | Size | Weight |
|---|---|---|
| Question / heading | 14.5–15 px | 600–700 |
| Body / options | 14 px | 400–600 |
| Feedback / notes | 13 px | 400 |
| Helper text | 12 px | 400 |

## Rules

- Numerals in live readouts use tabular figures (`font-variant-numeric: tabular-nums`) so values don't jitter.
- Math is rendered by MathJax (via `pymdownx.arithmatex`) on the site; in SVGs keep math to simple inline text or render as part of the figure.
- One title per figure; sentence case for labels and captions.
- Don't shrink below 12 px in any asset.
