# Future Roadmap (parked items — do not implement until approved)

## Asset-hardening & audit pass (deferred — after all modules complete)
Run a dedicated audit/fix pass once production is done. Scope:
- SVG embedding (verify every Visual Explanation renders its intended diagram; tighten any cramped/low-contrast layouts)
- HTML demo consistency (uniform controls, readouts, styling; confirm faux-3D viewers render as intended)
- navigation labels (consistency/wording)
- notebook naming (confirm MXX_UYY_LZ_*.ipynb everywhere)
- page-header ("You are here") consistency
Not blocking production; only fix mid-production if a lesson is entirely blocked.

## Asset-hardening backlog — Module 3 Installment C (logged during production)
- `m03-l17-distortion-types.svg`: barrel/pincushion grids are hand-drawn approximations with a minor top-edge artifact on the barrel shape; the straight/bowed/pinched contrast reads correctly but could be regenerated programmatically (apply an actual radial model to a grid) for precision in the hardening pass.
- General: Unit 5–6 faux-3D ray diagrams (`m03-l21`, `m03-l22`, `m03-l24`) use flat 2D ray schematics; could be upgraded to consistent isometric style matching Module 2's faux-3D during hardening.
