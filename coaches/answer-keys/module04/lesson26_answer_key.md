# Answer Key — Lesson 7.2: The Reachable Workspace

**Coaches only.** Formative.

1. **Reachable workspace is** — the set of all gripper positions over the joint ranges (image of FK).
2. **Planar 2-link outer radius** — L1 + L2 (inner |L1 − L2|).
3. **Joint limits make the real workspace smaller than the idealized annulus** — True.
4. **Target at radius 0.05 reachable? (short)** No — inside the inner radius |L1−L2| = 0.1, below the minimum reach.

**Challenge rubric.** Full credit: restricting θ2 ∈ [0°,150°] removes the configurations that reach the full inner/outer extremes in some directions, carving the complete annulus down to a partial lune/region; joint limits make the real workspace a strict subset of the idealized annulus because not every (radius, angle) is attainable. Partial: states the region shrinks without explaining why limits exclude points.
