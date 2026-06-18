---
module: 8
unit: 6
lesson: 1
type: answer_key
title: "Answer Key — The Robot as a Nervous System: The Loop as Messages"
audience: coaches
---

# Answer Key 6.1 — The Robot as a Nervous System: The Loop as Messages

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** separate sensor, controller, and actuator subsystems that exchange messages

**Q2 — B.** the message it carries takes transit and processing time

**Q3 — B.** the sum of the per-hop transit/processing times

**Q4 — B.** giving it a physical source — communication between subsystems takes time

**Q5 — B.** an analogy for 'distributed and delayed', not a model of computation

---

**Q6 — model answer.** A sensor measures the joint and publishes that reading as a message to the controller; the message takes time to travel (a hop). The controller receives it, computes a command, and publishes that command as a message to the actuator — another hop. The actuator receives the command and drives the joint; the joint moves and is sensed again on a feedback hop, closing the loop. Sense, compare, correct, actuate are no longer instantaneous steps in one place but messages crossing gaps between subsystems, each costing time.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The loop latency is the sum of the per-hop times: 1 + 1 + 1 = 3 ms. It means the measurement the controller acts on is about 3 ms old by the time its correction takes effect — the state has aged by the full loop latency in transit and processing. Nothing in the control math changed, but the controller is always reacting to slightly stale information, which is exactly the delay that Lesson 6.3 will show can destabilise the loop.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The analogy: a robot's loop is like a nervous system — sensors (senses) send signals over nerves to a controller (brain), which sends commands over nerves to actuators (muscles), and every signal takes time, so the loop is distributed and delayed. It breaks down in at least two ways: a robot's messages are discrete packets on named channels rather than continuous biochemical impulses, and the controller is a fixed-rate program rather than a plastic biological network with engineered, largely knowable timing. The analogy builds intuition for 'distributed and delayed', not a model of how the robot computes.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Drawing the loop as instantaneous — the arrows are real messages that take time.
- Forgetting the measurement is already old (by the loop latency) when the controller acts.
- Over-trusting the nervous-system analogy as a model of how the controller computes.
