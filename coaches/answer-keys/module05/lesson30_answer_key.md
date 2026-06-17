# Answer Key — Lesson 8.2: Building the Solver (Analytical + Numerical)

**Coaches only.** Formative.

1. **Analytical branch preferred because** — fast and returns all solutions.
2. **Recover multiple solutions numerically by** — seeding near each expected solution.
3. **solve() returns an unverified, unfiltered candidate list** — True (separate stages).
4. **Why closed form avoids seeding (short).** It enumerates all solutions directly from the formula, never depending on seed choice.

**Challenge rubric.** Full credit: for a 3R arm with four IK solutions, seed near each (e.g. combinations of the two shoulder branches × two elbow branches, or seeds spread across the joint ranges) and dedup; too few seeds miss whole solutions (the solver only returns the nearest to each seed), whereas a closed form returns all four at once with no seeding. Partial: says "use more seeds" without the all-vs-nearest contrast.
