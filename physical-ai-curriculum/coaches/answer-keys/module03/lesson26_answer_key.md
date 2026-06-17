# Answer Key — Lesson 7.2: Bridging to Module 2 (the extrinsics chain)

**Coaches only.** Formative.

1. **T(world←cam) for arm-mounted camera** — T(world←arm) · T(arm←cam).
2. **T(arm←cam) source** — a one-time hand-eye calibration.
3. **Composition right-to-left** — True.
4. **Worked chain (short).** After arm←cam: (0.06,−0.03,0.4); after world←arm: (1.06, 0.47, 0.4).

**Challenge rubric.** Full credit: for a fixed mast, T(world←cam) is a single calibrated pose (no arm hop); if the mast pans/tilts, T(world←cam) becomes time-varying and must be updated from the mast's joint state. Partial: single-pose answer without the pan/tilt extension.
