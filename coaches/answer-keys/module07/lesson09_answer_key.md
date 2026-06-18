---
module: 7
unit: 3
lesson: 1
type: answer_key
title: "Answer Key — Point-to-Point Joint Moves: Per-Joint Polynomials"
audience: coaches
---

# Answer Key 3.1 — Point-to-Point Joint Moves: Per-Joint Polynomials

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Each joint runs its own time scaling from its start to its goal over a shared duration.

**Q2 — B.** Forward kinematics is nonlinear, so a straight joint-space line maps to a curved tool path.

**Q3 — B.** Peak speed scales with |Δq|; the larger-displacement joint is faster over the same T.

**Q4 — B.** Joint moves are automatically feasible in the joints (smooth bounded polynomial), not necessarily collision-free.

**Q5 — B.** Joint moves suit gross repositioning where the tool path is irrelevant.

---

**Q6 — model answer.** The configuration moves along the straight segment q(t)=q0+(qf−q0)s(t) — a straight line in joint space. The tool position is f(q(t)), and forward kinematics f is nonlinear (it involves sines and cosines of the joint angles). A nonlinear map sends a straight line to a curve, so the tool sweeps a curved path even though every joint moves monotonically and smoothly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Peak speed scales with displacement: ṡmax is the same for both (same T, same profile), so joint 1's peak is twice joint 2's (60° vs 30°). The larger-displacement joint (joint 1) reaches the higher speed and acceleration, so it is the one that will hit a velocity/acceleration limit first — it drives synchronization and feasibility.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Appropriate: gross repositioning of the harvester from stow to a new plant — only the endpoints matter, and the joint move is fast and always joint-feasible. Not appropriate: the final straight approach onto a fruit — the tool must travel a controlled straight path, which a curved joint move can't guarantee; that needs a Cartesian (MoveL) trajectory.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Expecting a straight tool path from a joint move (it's curved).
- Letting joints finish at different times instead of sharing one duration.
- Forgetting the largest-displacement joint sets the peak speeds and hits limits first.
