---
module: 8
unit: 2
lesson: 1
type: answer_key
title: "Answer Key — Proportional Control: Correction Proportional to Error"
audience: coaches
---

# Answer Key 2.1 — Proportional Control: Correction Proportional to Error

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** u = Kp·e.

**Q2 — B.** P-only leaves a steady-state offset ≈ load/Kp.

**Q3 — B.** Higher Kp → smaller offset and faster response.

**Q4 — B.** At e=0 the command is 0, which can't hold against the load.

**Q5 — B.** Very high Kp → overshoot/oscillation.

---

**Q6 — model answer.** With u = Kp·e, the command is proportional to the error. To hold the joint against a constant load, the controller must produce a constant nonzero command. But the only way Kp·e is nonzero is if e itself is nonzero. So at equilibrium the error settles to exactly the value whose proportional command balances the load: e_ss ≈ load/Kp. If the error reached zero, the command would vanish and the load would push the joint back, recreating an error — so a residual offset is structurally required by proportional-only control.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Larger Kp makes the controller respond harder to a given error: the response is faster and the steady-state offset (≈ load/Kp) is smaller. But too large a Kp makes the loop overshoot and oscillate, and on a lightly-damped plant it drives the response toward marginal stability (sustained ringing) or instability. Smaller Kp is gentle and stable but slow with a large offset. So Kp is a balance: enough to be responsive and keep the offset small, not so much that the system rings or goes unstable — which is exactly why integral and derivative terms are added rather than just cranking Kp.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The steady-state error is e_ss = q_d − q = 1.0 − 0.8 = 0.2. For proportional-only control under a constant load, e_ss ≈ load/Kp, so 0.2 ≈ 2/Kp, giving Kp ≈ 10. The reasoning: at equilibrium the proportional command Kp·e_ss must balance the load, so Kp·0.2 = 2 → Kp = 10. This also shows how to shrink the offset — doubling Kp to 20 would roughly halve the offset to 0.1 — though raising Kp indefinitely eventually causes overshoot, which is why integral action is the cleaner cure for the offset.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Believing P control can zero the steady-state error under load (it can't).
- Thinking more Kp is always better (it eventually causes oscillation/instability).
- Confusing the offset (steady-state) with transient overshoot.
