---
module: 8
unit: 1
lesson: 3
type: answer_key
title: "Answer Key — The Feedback Loop: Sense → Compare → Correct → Actuate"
audience: coaches
---

# Answer Key 1.3 — The Feedback Loop: Sense → Compare → Correct → Actuate

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Sense → compare → correct → actuate.

**Q2 — B.** The summing junction forms e = q_d − q.

**Q3 — B.** Feedback rejects disturbances it was never told about.

**Q4 — B.** A closed loop recovers toward the reference after a disturbance.

**Q5 — D.** Actuate is the stage that drives the plant and moves the joint.

---

**Q6 — model answer.** Sense: a sensor measures the actual joint angle q. Compare: a summing junction subtracts q from the desired q_d to form the error e = q_d − q. Correct: the controller turns that error into a command u (e.g. u = Kp·e for proportional). Actuate: the command drives the plant (the joint), producing new motion and a new q. That q is sensed again, closing the loop, so the cycle repeats continuously and the error is driven toward zero — and any disturbance that perturbs q is automatically sensed and corrected.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because feedback acts on the measured outcome, not on a model of the disturbance. Whatever the cause — a gust, a payload, friction, a modeling error — its effect shows up as a change in the measured q, which changes the error e, which the controller immediately acts to correct. The loop doesn't need to know what caused the deviation; it only needs to see the deviation. That is the fundamental advantage over open-loop, which, blind to the actual output, cannot respond to anything it wasn't told about in advance.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Open-loop executes its precomputed command regardless of what happens; a disturbance knocks the joint off course and it stays off — the error from the kick persists to the end because nothing measures or corrects it. Closed-loop senses the resulting error the instant the kick perturbs q, the controller generates a corrective command, and the joint is driven back toward the reference, recovering to the target. The kick produces a transient bump in the closed-loop response but it settles back; in open-loop it produces a permanent offset.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking feedback needs a model of the disturbance (it acts on the measured effect).
- Omitting the compare stage — without forming the error there is nothing to correct.
- Believing open-loop can recover from a disturbance (it cannot).
