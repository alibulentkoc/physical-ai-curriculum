---
module: 8
unit: 1
lesson: 4
type: answer_key
title: "Answer Key — Anatomy of a Control System"
audience: coaches
---

# Answer Key 1.4 — Anatomy of a Control System

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Reference, controller, plant, feedback.

**Q2 — B.** The reference comes from Module 7's reference layer.

**Q3 — B.** The plant is the system being controlled (the joint/arm).

**Q4 — B.** Disturbances enter at the plant, perturbing its output.

**Q5 — B.** Removing feedback yields an open-loop system that can't reject disturbances.

---

**Q6 — model answer.** Reference: the desired motion, q_d, q̇_d, q̈_d, supplied by Module 7 — where the arm should be. Controller: computes the correction (the command u) from the error — the 'brain' that decides how hard to drive. Plant: the system being controlled — the greenhouse arm's joint, which turns the command into motion but is also pushed by load and friction. Feedback: the sensor path that measures the actual q and returns it to be compared with q_d. Together they form the loop: reference in, error formed, correction computed, plant actuated, output measured and fed back.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A disturbance enters at the plant, perturbing its output q directly (gravity-like load, friction, a payload). That placement matters because it means the disturbance is not in the reference or the command — the controller doesn't know it's coming. It only discovers it through the feedback path, when the perturbed q changes the measured error. This is exactly why feedback is necessary: the disturbance acts on the plant downstream of the controller, so only by measuring the plant's actual output can the loop detect and reject it.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The feedback path is what carries the actual measured output back to be compared with the reference, creating the error the controller acts on. Without it, the controller computes commands purely from the reference (or feedforward) and never learns what actually happened — that is open-loop execution, which cannot reject disturbances or correct model error. Adding the feedback path closes the loop: the system now responds to reality, not just to the plan. So the feedback path is the defining ingredient that converts a plan-and-hope pipeline into a true control system.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Confusing the controller with the plant (controller decides; plant is controlled).
- Thinking the disturbance enters at the reference or controller (it acts on the plant).
- Forgetting the feedback path is what makes it closed-loop.
