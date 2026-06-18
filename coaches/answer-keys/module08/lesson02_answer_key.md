---
module: 8
unit: 1
lesson: 2
type: answer_key
title: "Answer Key — Tracking Error: The Quantity Control Fights"
audience: coaches
---

# Answer Key 1.2 — Tracking Error: The Quantity Control Fights

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** e = q_d − q (desired minus actual).

**Q2 — B.** e > 0 means the joint is below/behind the target.

**Q3 — B.** A sign change of e indicates overshoot (crossed the target).

**Q4 — B.** Steady-state error is the residual after the transient settles.

**Q5 — B.** Control drives the error toward zero.

---

**Q6 — model answer.** Tracking error is e = q_d − q, the signed gap between the desired and actual joint position at each instant. Transient error is the error during the response — large at first as the joint moves toward the target, possibly crossing zero if it overshoots. Steady-state error is the residual error that remains after the transient has settled; ideally zero, but proportional-only control leaves a nonzero steady-state offset under a sustained load. Control works to shrink both, especially driving the steady-state error toward zero.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The sign tells the controller which way to push. If e = q_d − q is positive the joint is below the target and the controller must drive it up; if negative it has overshot and must pull back. A controller that ignored sign couldn't correct in the right direction. The sign also reveals overshoot: when the error flips from positive to negative, the output has crossed past the target, which is the signal the derivative term uses to start braking.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** It tells you the error has a nonzero steady-state value: after the transient dies out, e settles to a constant offset rather than zero. Physically, the proportional command Kp·e must supply the steady force to balance the load, so some error must persist to generate that command — the error can't reach zero or the command would vanish and the load would win. The error-over-time curve therefore starts large, decays through the transient, and levels off at a constant nonzero offset, which is what integral action is later introduced to remove.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Defining error as q − q_d (sign reversed) — convention here is q_d − q.
- Confusing transient error (during the move) with steady-state error (after settling).
- Assuming any error means failure — small bounded error is normal; the goal is to minimize it.
