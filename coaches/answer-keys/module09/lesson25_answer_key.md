---
module: 9
unit: 7
lesson: 25
type: answer_key
title: "Answer Key — The Orchestrator: Coordination as a Stage"
audience: coaches
---

# Answer Key 7.1 — The Orchestrator: Coordination as a Stage

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A coordinating stage that re-invokes existing layers — it owns no theory.

**Q2 — B.** Sixth stage: Perceive → Understand → Plan → Execute → Track → Recover, closing the loop.

**Q3 — B.** It consumes detection's output — the localised, owner-tagged fault.

**Q4 — B.** A targeted response is an existing layer call re-invoked (re-perceive = model_perception again; retry-execute = execute_reference again).

**Q5 — True.** Recover is a stage (a coordination role), not a layer (a capability with its own theory).

---

**Q6 — model answer.** Plan is a layer: it owns a body of theory (trajectory generation, limit validation) and provides a capability the system otherwise lacks. Recover owns no theory — it cannot perceive, plan, or control; it can only call the stages that do. Its job is the *when* and *which*: when to retry, which stage to re-invoke, when to stop. That is a coordination role (a stage), not a capability (a layer) — the guardrail that keeps recovery from smuggling in new theory.
*Grading: require the no-theory / coordination distinction and a correct contrast with a real layer.*
