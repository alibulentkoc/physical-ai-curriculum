# Answer Key — Lesson 6.2: Joint Limits and Feasible Solutions

**Coaches only.** Formative.

1. **Feasible iff** — every joint angle lies within its [min, max] limits.
2. **After filtering the two solutions** — you may have one, both, or no feasible solutions.
3. **Limits shrink the effective workspace** — True.
4. **'No feasible solution' meaning (short).** The target is unreachable for *this arm's limits*, even if inside the annulus — report failure and possibly reposition.

**Challenge rubric.** Full credit: e.g. L1=0.4, L2=0.3, target (0.5,0), limits θ₂ ∈ [−150°,0°] make elbow-up (θ₂=−90°) feasible and elbow-down (θ₂=+90°) infeasible — the reverse of the worked example; this shows you can't hard-code one elbow preference, because limits decide per target which elbow survives. Partial: gives a limit set without checking both solutions against it.
