---
module: 8
unit: 8
lesson: 8.2
type: answer_key
title: "Answer Key 8.2 — A Lightweight ROS 2 Tracker Node"
audience: coaches
---

# Answer Key 8.2 — A Lightweight ROS 2 Tracker Node

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** Two subscriptions (reference, measured state) and one publication (command)

*Why:* Two inputs in, one command out, one computation per cycle.

**Q2 — B.** Intelligence

*Why:* The law is the intelligence; the node is the plumbing around it.

**Q3 — B.** Exactly one actuator command

*Why:* One command per state received — the node's contract.

**Q4 — B.** The intelligence stays unit-testable and reusable across nodes/robots

*Why:* Every Module 8 notebook tested the law in isolation for this reason.

**Q5 — B.** N commands

*Why:* One command per state (e.g., 1001 → 1001).

**Q6 — model answer.** The control law is the computation that turns reference + measured state into a command (feedforward + PID + actuator) — the engineering. The node is plumbing: it subscribes to inputs, calls the law once per cycle, and publishes the command. The intelligence stays the same across robots; only the plumbing wiring changes.

**Q7 — model answer.** Because it runs the control law once per control period when a new state arrives. It matters for periodic, real-time execution (Unit 7): one deterministic update per cycle is what keeps the loop's timing and behaviour predictable.

**Q8 — model answer.** Keep the control-law function unchanged (the intelligence) and re-point the node's plumbing: subscribe to that robot's state and reference topics and publish to its command topic. The contract (one command per state) and the law stay the same; only the wiring changes.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Believing a ROS 2 controller needs deep framework expertise; the engineering is the control law.
- Entangling the control law with node code instead of keeping it a separate, testable function.
- Expecting more or fewer commands than states — the node's contract is one command per cycle.
