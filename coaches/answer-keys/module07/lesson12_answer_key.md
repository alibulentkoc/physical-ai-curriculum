---
module: 7
unit: 3
lesson: 4
type: answer_key
title: "Answer Key — Blending for C² Continuity at Via-Points"
audience: coaches
---

# Answer Key 3.4 — Blending for C² Continuity at Via-Points

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — C.** A cubic spline is C²: continuous position, velocity, and acceleration.

**Q2 — B.** It solves a tridiagonal system for the knot second-derivatives.

**Q3 — B.** Natural spline sets zero end acceleration (relaxed ends).

**Q4 — B.** Stop-at-each is the special case where every passing velocity is forced to zero.

**Q5 — B.** Use a clamped spline to fix nonzero end velocities while staying C².

---

**Q6 — model answer.** A cubic spline is a piecewise cubic that passes through every via-point and is constrained so that position, velocity, and acceleration all match across each interior knot (C²). Writing the unknowns as the knot second-derivatives reduces these conditions to one tridiagonal linear system; solving it yields the interior slopes and curvatures that make the whole curve smooth. The result flows through the via-points (nonzero passing velocity) with no velocity kink and no acceleration jump at any seam.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Natural: the end acceleration (second derivative) is set to zero — 'relaxed' ends, suited to an overall rest-to-rest move. Clamped: the end velocities are specified — used when the trajectory must start or finish matching a particular velocity, e.g. handing off to a following Cartesian approach. Both keep the interior C²; they differ only in the two boundary equations, and those propagate inward to give different interior velocities.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Because the velocity (and acceleration) that makes the incoming segment smooth at a via-point must also make the outgoing segment smooth there — the two sides are coupled. Choosing them independently would generally leave a velocity kink or an acceleration jump at the seam. The spline solves all the interior values together (one linear system) so every seam is simultaneously C².
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Hand-picking via velocities independently (they're coupled — let the spline solve them).
- Forgetting per-joint splines must share the same via-times to stay coordinated.
- Reading a smooth C² spline as automatically collision-free (smooth ≠ safe).
