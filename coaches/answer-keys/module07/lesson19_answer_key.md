---
module: 7
unit: 5
lesson: 3
type: answer_key
title: "Answer Key — The Fastest Feasible Timing: Respecting Velocity and Acceleration Limits"
audience: coaches
---

# Answer Key 5.3 — The Fastest Feasible Timing: Respecting Velocity and Acceleration Limits

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Saturate the limits: ramp at a_max, cruise at v_max, ramp at a_max (trapezoid).

**Q2 — B.** Triangular when D < v_max²/a_max (never reaches v_max).

**Q3 — B.** Trapezoid is faster but only C¹; quintic is smoother but slower.

**Q4 — B.** The bottleneck (slowest) joint's minimum time sets the synchronized duration.

**Q5 — B.** It's the closed-form limit-saturating timing, not formal time-optimal optimization.

---

**Q6 — model answer.** It has three phases: ramp up at the acceleration limit a_max, cruise at the velocity limit v_max, ramp down at a_max. It is fastest because at every instant it saturates a limit — acceleration on the ramps, velocity on the cruise — so no time is wasted moving below the hardware ceilings. The minimum time for a long move is T = D/v_max + v_max/a_max (cruise + ramp). A smoother quintic spends time easing the ends instead of saturating limits, so it's slower.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A move is triangular when it's too short to reach the cruise speed: D < v_max²/a_max. The joint accelerates at a_max to a peak v_p = √(a_max·D), which is below v_max, then immediately decelerates — no cruise phase. The minimum time is T = 2√(D/a_max). Short repositioning moves are commonly triangular.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Fastest-feasible (in scope) is the simple, closed-form timing that saturates per-joint velocity and acceleration limits — the trapezoidal/triangular profile and synchronizing to the bottleneck. Time-optimal trajectory optimization (out of scope) is heavier machinery: optimizing timing along an arbitrary path under coupled constraints, or kinodynamic planning that plans motion and dynamics together. Module 7 deliberately stays with the practical limit-saturating timing and avoids the optimization framework.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Assuming every move reaches v_max (short moves are triangular).
- Calling the quintic 'fastest' (it's smoother but slower).
- Conflating fastest-feasible with time-optimal optimization / kinodynamics (out of scope).
