---
module: 8
unit: 3
lesson: 2
type: answer_key
title: "Answer Key — The Shape of a Response: Rise, Overshoot, and Settling"
audience: coaches
---

# Answer Key 3.2 — The Shape of a Response: Rise, Overshoot, and Settling

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Rise time: 10–90% climb time (speed).

**Q2 — B.** Overshoot: peak past target / span (aggressiveness).

**Q3 — B.** Settling time: last exit from the ±band around target.

**Q4 — B.** Steady-state error: residual offset after settling (precision).

**Q5 — B.** Faster rise usually means more overshoot / longer settling.

---

**Q6 — model answer.** Rise time: how long to climb from 10% to 90% of the step — the response's speed. Overshoot (%): how far the response sails past the target relative to the step size — its aggressiveness/under-damping. Settling time: the last moment the response leaves a small band (e.g. ±2%) around the target — when the ringing effectively stops. Steady-state error: the residual gap between target and final value once settled — the response's precision. Together they convert a subjective 'looks good/bad' into a measurable specification you can tune toward and test against.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Making a response faster generally means correcting more aggressively, which gives the joint more momentum as it approaches the target — so it tends to sail further past (more overshoot) and then take longer to ring down (longer settling). Rise time and overshoot pull against each other. Specifying only rise time is dangerous because you can hit a fast rise while badly overshooting and oscillating — technically 'fast' but unusable for a task that can't tolerate overshoot (a welding head, a surgical tool). A sound spec constrains all four metrics together so speed isn't bought at the cost of an unacceptable shape.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The 3%-overshoot joint is better. A camera gimbal slewing to a target must arrive and hold steady so the image is sharp; 35% overshoot means it sails well past the aim point and rings back, blurring the shot and lengthening the settling time before the image is usable. With equal rise time, the low-overshoot response reaches and holds the target with minimal excursion, giving a clean, quickly-usable image. This shows that rise time alone doesn't decide quality — for this task overshoot (and the settling it implies) is the deciding metric, and less is decisively better.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Confusing overshoot (transient) with steady-state error (permanent).
- Optimising rise time alone and breeding overshoot.
- Quoting 'settled' without stating the band, or metrics without the step.
