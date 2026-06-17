# Answer Key — Lesson 7.3: Closing the Loop: Perceive → Place → Solve

**Coaches only.** Formative.

1. **Pipeline order** — perceive → place → reachability gate → solve → filter → verify → select.
2. **Every output** — a verified/feasible/selected configuration, or a clear failure reason.
3. **Reachability gate before the solver avoids wasted iterations** — True.
4. **Why distinct failure reasons (short).** So the caller can act specifically: re-detect, reposition, or skip, based on which gate failed.

**Challenge rubric.** Full credit: verifying *before* limit-filtering wastes work and could let an FK-passing but limit-violating pose look acceptable until later; selecting *before* verifying could pick a candidate that doesn't actually reach (a stalled numerical solve), committing a wrong pose — so the safe order is gate early (reachability), filter, then verify, then select. Partial: identifies one bad reordering's failure.
