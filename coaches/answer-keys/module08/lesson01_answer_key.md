---
module: 8
unit: 1
lesson: 1
type: answer_key
title: "Answer Key — Why Open-Loop Isn't Enough: The Reference-vs-Reality Gap"
audience: coaches
---

# Answer Key 1.1 — Why Open-Loop Isn't Enough: The Reference-vs-Reality Gap

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Open-loop commands from the plan with no feedback correction.

**Q2 — B.** Unmodeled disturbance/load/friction/model error go uncorrected → drift.

**Q3 — B.** The q_d − q gap is the tracking error.

**Q4 — B.** Feedback measures the actual output and corrects the error.

**Q5 — B.** Module 8 consumes Module 7's reference q_d, q̇_d, q̈_d.

---

**Q6 — model answer.** Open-loop is like driving with your eyes closed after memorizing the road: you execute the planned steering, but you can't see or correct for anything unexpected — a gust of wind, a slope, a heavier load — so you drift off course and the error grows. A real robot joint faces gravity-like load, friction, payload changes, and model error; with no feedback it never notices or corrects the resulting gap, so the actual motion diverges from the reference. Feedback (eyes open) is what lets it measure the real position and steer back onto the reference.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Module 7 hands Module 8 the validated reference trajectory: the desired position q_d(t) plus the feedforward derivatives q̇_d(t) and q̈_d(t), continuous and feasible. Module 8 treats q_d as the target to track and uses the feedforward terms to lead the motion, then adds feedback correction (comparing measured q to q_d) to reject disturbances and follow the reference on the real arm. Module 8 does not re-plan the motion — it makes the robot actually follow the motion Module 7 already decided.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The reference q_d(t) is where the robot should be at each instant; the reality q(t) is where it actually is. On a real plant these differ — the actual motion drifts from the plan because of load, friction, and model error that open-loop execution never corrects. That growing gap is the tracking error, and eliminating it is the entire job of feedback control. The module exists to build the controller that measures this gap and continuously drives it toward zero, turning a planned reference into faithfully executed motion.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking a good enough plan removes the need for feedback (disturbances always remain).
- Confusing the reference (desired) with the actual measured output.
- Believing open-loop 'corrects' anything — it never measures the result.
