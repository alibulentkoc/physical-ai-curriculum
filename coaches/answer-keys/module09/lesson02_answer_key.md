---
module: 9
unit: 1
lesson: 2
type: answer_key
title: "Answer Key — The Six-Stage Workflow"
audience: coaches
---

# Answer Key 1.2 — The Six-Stage Workflow: Data Flow, Interfaces, and Subsystem Ownership

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Perceive → Understand → Plan → Execute → Track → Recover.

**Q2 — B.** Choosing which fruit to pick is the Understand stage (Module 9 selection); seeing fruit is Perceive.

**Q3 — B.** Plan answers "when to be where" and writes the timed reference trajectory `reference(t)`; it does not move the robot.

**Q4 — C.** Recover is the only stage that can revise `current_target` and route the flow backward.

**Q5 — True.** The arrows are the interfaces/contracts; integration makes each postcondition imply the next precondition.

---

**Q6 — model answer.** Execute is owned by Module 6 (velocity) + Module 8 (control). It reads the reference (from Plan) and the current joint configuration `q`, and writes the joint `command` and new `q`, with real forward kinematics keeping the tool position current. It does not choose the fruit (Understand) or plan the timing (Plan).
*Grading: require correct owner(s), the reference/`q` inputs, and the command/`q` outputs.*
