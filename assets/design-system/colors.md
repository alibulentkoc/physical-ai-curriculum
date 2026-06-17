# Colors

> The curriculum palette. Use these tokens in every SVG, diagram, interactive, and the MkDocs theme. Colour is never the sole carrier of meaning — always pair with a label.

## Core palette

| Token | Hex | Use |
|---|---|---|
| Ink | `#0f172a` | primary text, strong strokes |
| Slate | `#334155` | secondary strokes, arrows |
| Muted | `#64748b` | captions, secondary labels |
| Line | `#e2e8f0` | borders, dividers |
| Soft | `#f8fafc` | panel / surface backgrounds |
| White | `#ffffff` | base background |

## Semantic / role colors

| Token | Hex | Meaning (consistent curriculum-wide) |
|---|---|---|
| Perceive | `#0ea5e9` (sky) | perception / sensing stage |
| Reason | `#8b5cf6` (violet) | reasoning / decision stage |
| Act | `#10b981` (emerald) | action / actuation stage |
| Accent | `#0d9488` (teal) | primary brand accent, links, headings |
| Correct | `#15803d` on `#dcfce7` | correct / success / "good" |
| Error | `#b91c1c` on `#fee2e2` | error / incorrect / "bad" |
| Info | `#1d4ed8` on `#eff6ff` | neutral info / model answers |
| Fruit | `#e11d48` (rose) | the tomato / target object |

## Rules

- The three loop stages **always** map to the same colours (perceive=sky, reason=violet, act=emerald).
- Correct/error use the green/red pairs above, always with text and never red/green alone (colour-blind safety).
- The MkDocs Material theme uses **teal** primary / **green** accent to match `Accent`/`Act`.
- Keep contrast ≥ WCAG AA for text on its background.
