---
module: 7
unit: 1
lesson: 3
type: answer_key
title: "Answer Key — What Makes a Trajectory 'Good'"
audience: coaches
---

# Answer Key 1.3 — What Makes a Trajectory 'Good'

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Smooth, feasible, safe, efficient.

**Q2 — C.** C² ⇒ continuous acceleration ⇒ continuous force ⇒ no shock loads.

**Q3 — B.** Exceeding a joint limit is a feasibility failure.

**Q4 — B.** Collisions/saturations occur mid-motion; endpoint-only checks miss them.

**Q5 — B.** C⁰ < C¹ < C² < bounded jerk.

---

**Q6 — model answer.** Force is proportional to acceleration (F=ma). If acceleration jumps, force jumps instantly — a shock load. C² continuity means acceleration is continuous, so force changes continuously and no shock (step in force) ever occurs.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A C² motion whose acceleration ramps up very quickly has large (but finite) jerk. It has no force jumps, yet the fast onset of force is felt as a snap. The culprit is unbounded jerk; bounding jerk is the separate finishing requirement on top of C².
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Arguable. Against: it never collides, so geometrically it's clear. For rejection: near a singularity the arm loses motion authority in some direction and following the path may demand very large joint rates (a latent feasibility problem) and poor conditioning — risky if anything perturbs it. Many reviewers reject sustained near-singular passes; rerouting the path to keep σ_min above a band resolves it cleanly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Confusing C¹ and C² — continuous velocity still allows force to jump.
- Optimizing efficiency before the three hard criteria pass.
- Forgetting singularities are a feasibility/safety concern, not just geometry.
