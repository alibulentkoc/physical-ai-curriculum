---
module: 7
unit: 5
lesson: 2
type: answer_key
title: "Answer Key — Slowing Down to Restore Feasibility: Uniform Time Scaling"
audience: coaches
---

# Answer Key 5.2 — Slowing Down to Restore Feasibility: Uniform Time Scaling

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Uniform time scaling divides velocity by k and acceleration by k².

**Q2 — B.** The path is unchanged; only the clock rescales.

**Q3 — B.** The minimum stretch factor is the larger (binding) of the two requirements.

**Q4 — B.** Reachability is geometric; slowing down can't make an unreachable point reachable.

**Q5 — B.** Per-joint factors break synchronization; use one common factor.

---

**Q6 — model answer.** Playing a motion's video at half speed shows the exact same path — every configuration, in the same order — but everything moves slower: velocities halve and accelerations drop even more. Uniform time scaling is exactly this: replace the clock so the trajectory takes k times as long. The geometry q(s) is unchanged; only s(t) stretches. Velocities scale by 1/k and accelerations by 1/k², so a large enough k brings any speed/acceleration peaks under the limits without touching the path.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Need v₀/k ≤ v_lim and a₀/k² ≤ a_lim, i.e. k ≥ v₀/v_lim (velocity) and k ≥ √(a₀/a_lim) (acceleration); take the larger (binding) one. It always works because as k→∞ both v₀/k and a₀/k² → 0, so any positive limits can be met by slowing enough. This is special to velocity/acceleration limits — it cannot fix a geometric (reachability or joint-angle) violation.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Because it changes nothing about where the robot goes — the path, the approach, the via-points are all identical — it only rescales the clock. So it can't introduce a new collision or miss the target; it just makes the existing, correct motion gentler. For speed/acceleration infeasibility it's guaranteed to work with a single multiply on the time axis (the global feed-rate/override knob), which is why it's the first thing to reach for.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Forgetting acceleration shrinks faster (1/k²) — the binding constraint can be either.
- Thinking slowing down changes the path (it doesn't).
- Trying to fix a reachability problem by slowing down; scaling joints independently.
