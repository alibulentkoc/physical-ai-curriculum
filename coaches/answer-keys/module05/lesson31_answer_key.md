# Answer Key — Lesson 8.3: Verifying, Selecting, and Handling No-Solution Cases

**Coaches only.** Formative.

1. **Capstone tail** — verify → filter limits → select → θ⋆ (or a status).
2. **Match** — unreachable → target outside workspace; no_feasible → verified but limits exclude all; ok → executable θ⋆ found.
3. **One executable θ⋆ with ok, or None with a reason — never silent, never invalid** — True.
4. **Why distinguish no_solution vs no_feasible (short).** Different remedies: no_solution → re-seed/reposition the solver; no_feasible → reposition the base or relax the task (solutions exist but limits exclude them).

**Challenge rubric.** Full credit: the harvester responds differently — `no_solution` suggests the target is geometrically out of reach or the solver failed (reposition the base, re-seed, or switch step rule), while `no_feasible` means a reachable target with valid solutions that the joint limits forbid (reposition for a better approach, or approach from another row) — so collapsing them loses the right corrective action. Partial: gives the distinction without distinct remedies.
