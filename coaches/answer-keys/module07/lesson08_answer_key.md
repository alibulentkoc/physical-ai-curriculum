---
module: 7
unit: 2
lesson: 4
type: answer_key
title: "Answer Key — Trapezoidal vs S-Curve Velocity Profiles"
audience: coaches
---

# Answer Key 2.4 — Trapezoidal vs S-Curve Velocity Profiles

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Accelerate at a_max, coast at v_max, decelerate at a_max.

**Q2 — B.** Piecewise-constant acceleration steps at the corners → C¹ with jerk spikes.

**Q3 — B.** An S-curve bounds jerk, buying C² (continuous acceleration).

**Q4 — B.** Short moves never reach v_max → triangular profile.

**Q5 — B.** The trapezoid is time-optimal; the S-curve is slightly slower but C² smooth.

---

**Q6 — model answer.** It uses the maximum allowed acceleration and velocity the whole time, so no profile obeying the same limits can finish sooner — time-optimal. But its acceleration is piecewise-constant and steps at the phase boundaries, so it is only C¹ and produces jerk spikes (not smooth).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** It bounds jerk, so acceleration must ramp rather than step — the velocity corners round into S-shapes and acceleration becomes continuous (C²). The cost is time: the jerk-limited ramps take longer than instantaneous steps, so the S-curve finishes a bit later than the trapezoid.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** If the required average speed D/T is too high, no profile within v_max can cover D in time T — feasibility fails. Something must give: raise v_max/a_max (if the hardware allows), relax T, or shorten D (path). You cannot keep all of D, T, and the limits simultaneously; this is the converse of Unit 5's time-scaling, where we slow down to gain feasibility.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Believing a trapezoid is smooth — it is time-optimal, not smooth.
- Forgetting the triangular (short-move) case.
- Ignoring the S-curve's time cost; mixing up profiles (limits) with polynomials (endpoints).
