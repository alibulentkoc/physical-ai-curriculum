---
module: 8
unit: 5
lesson: 3
type: answer_key
title: "Answer Key — Deadband, Stiction, and Why Integral Wins the Last Millimetre"
audience: coaches
---

# Answer Key 5.3 — Deadband, Stiction, and Why Integral Wins the Last Millimetre

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** block small commands until a breakaway threshold is crossed

**Q2 — B.** their commands shrink to nothing exactly when the error (and its rate) are small

**Q3 — B.** it accumulates the small persistent error until the command crosses the threshold

**Q4 — B.** (load + deadband) / Kp

**Q5 — B.** shrinks the residual but never erases it, and adds jitter/overshoot elsewhere

---

**Q6 — model answer.** Derivative action responds to the rate of change of the error. When the joint is stalled by deadband or stiction, it isn't moving and the error isn't changing, so the error rate is essentially zero and the derivative term contributes nothing. Derivative is useful for damping motion, not for breaking a static stall — that needs a term that keeps building command while the joint sits still, which is the integral.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** While the joint sits stuck with a small residual error, the integral term keeps accumulating that error over time: e_i grows steadily even though e is small. Eventually the integral contribution K_i·e_i lifts the total command past the actuator's deadband and the joint's stiction breakaway threshold, the joint lurches forward, and the error collapses toward zero. The integrator is the only term that treats 'small but persistent' as a reason to keep pushing, which is exactly what the final approach requires.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The only difference between the runs is the integral term, yet it converts a permanent 0.44-rad miss into a near-perfect landing — more than two orders of magnitude better. PD's proportional command shrinks below the deadband/breakaway as the joint nears the target, so it freezes short; the integrator accumulates the residual until it crosses the threshold and finishes the move. The deadband and stiction never changed; integral action is what makes the last millimetre reachable.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Raising Kp to fix a stall — it shrinks but never erases the residual, and adds jitter/overshoot.
- Expecting derivative action to help at a stall (the error rate is ~zero when stuck).
- Forgetting the load — under load P settles off-target by ≈ (load + deadband)/Kp.
