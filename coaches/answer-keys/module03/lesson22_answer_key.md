# Answer Key — Lesson 6.2: Adding Depth Recovers a Point

**Coaches only.** Formative.

1. **Camera-frame point** — P_c = Z·(x_n, y_n, 1).
2. **Depth source** — a depth camera, stereo, or known geometry.
3. **Exact inverse once Z known** — True.
4. **P_c for (480,160), f=800, pp (320,240), Z=0.3 (short).** (0.06, −0.03, 0.3).

**Challenge rubric.** Full credit: derives axial Z from range-along-ray ρ via Z = ρ / sqrt(x_n²+y_n²+1), then P_c = Z(x_n,y_n,1); explains that using ρ as Z overestimates depth by the ray-angle factor (error grows with radius). Partial: correct relationship, missing the error explanation.
