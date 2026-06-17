# Answer Key — Lesson 6.3: Choosing Among Solutions (Nearest, Smooth, Limit-Safe)

**Coaches only.** Formative.

1. **Good default** — nearest to the current pose (least motion, smooth).
2. **Selection cost combines** — motion to current + limit margin + singularity margin.
3. **Arbitrary selection causes elbow flips** — True.
4. **Why greedy nearest can trap the arm (short).** Repeated nearest picks can walk a joint toward its limit until the next pick has no nearby feasible solution, forcing a big flip.

**Challenge rubric.** Full credit: sketch a fruit sequence where each nearest choice nudges θ₁ toward its max; at fruit k the only feasible solution is far (a flip), whereas choosing a slightly-farther solution earlier would have kept margin and avoided the flip — i.e. greedy is locally optimal but globally costly, motivating look-ahead/planning (Module 7). Partial: describes the trap without the "slightly-farther-now-avoids-flip-later" trade-off.
