---
module: 09
unit: 08
lesson: 8.1
title: "The Full Pick Cycle: Six Stages as One Loop"
core_idea: "Everything assembles here. The six stages built across Module 9 — Perceive, Understand, Plan, Execute, Track, Recover — compose into one self-healing pick cycle: perceive the scene, choose a target, plan and execute the motion, judge the result, and recover from any fault. Each stage is a wrapped existing layer; the cycle is the coordination that makes them cooperate. One pick, end to end, is the whole module in a single loop."
estimated_time: "50 min"
difficulty: "Advanced"
prerequisites:
  - "7.4 — Recover (the sixth stage)"
  - "Units 1–7 — every stage the cycle composes"
learning_objectives:
  - "Compose the six stages into one self-healing pick cycle."
  - "Trace a single pick through perceive → understand → plan → execute → track → recover."
  - "Explain that the cycle is coordination over wrapped layers, not new theory."
tags:
  - physical-ai
  - robotics
  - systems-integration
  - pick-cycle
---

# Lesson 8.1 — The Full Pick Cycle: Six Stages as One Loop

> For eight units we built the stages one seam at a time. Now they click together. A single pick — see a fruit, decide to take it, plan the reach, drive the motion, check it landed, recover if it didn't — runs all six stages as one loop. This is the moment Module 9 becomes a *system*.

---

## 1. Why This Matters
A robot is not its parts; it is the loop its parts run. Until now we exercised stages in pairs across seams; this lesson closes the full cycle so a single pick flows end to end without human stitching. That composition is the deliverable of the entire module — a perception-to-recovery pipeline where each handoff is explicit and each failure is caught and handled. Seeing one complete, self-healing pick is what proves the integration works: not that any stage is clever, but that all six cooperate.

## 2. Physical Intuition
A surgeon's full procedure, not a single suture. Each skill — diagnosis, incision, repair, closure, recovery — was practised alone, but the operation is the *sequence*, performed as one continuous act with checks between steps and a plan for complications. The competence that matters is running the whole procedure smoothly, adapting when something goes wrong. The pick cycle is the robot's procedure: the six stages performed as one act, with Track as the check and Recover as the response to complications.

## 3. Mathematical Foundations
The pick cycle is the composition of the six stage functions, with Recover closing the loop:

$$\text{detections} \xrightarrow{\text{Understand}} \text{target} \xrightarrow{\text{to\_configuration}} q_{\text{goal}} \xrightarrow{\text{Plan}} \text{reference} \xrightarrow{\text{Execute}} \text{motion} \xrightarrow{\text{Track}} \text{verdict},$$

and on a fault the verdict's localisation feeds Recover, which re-invokes the owning stage. Each arrow is a *wrapped existing layer* — M3 perception, the Understand adapter, M5 IK, M7 planner, M6/M8 control, the Track judge, the orchestrator — and the cycle introduces no new operator. Formally the pick cycle is a function

$$\text{pick}(\text{world}, q_0) \to \{\text{success}, \text{recovered}, \text{n\_attempts}, \ldots\},$$

assembled purely from calls the module already defines. The single new thing is the *control flow*: the order of the stages, the seam contracts between them, and the recovery loop. That is the precise sense in which integration is the lesson — the intelligence is in the composition, not in any component. A healthy pick runs the forward path once; a faulted pick runs Recover and may retry or escalate; either way the cycle terminates with a definite outcome.

## 4. Visual Explanation
`[Visual: the six-stage ring — Perceive → Understand → Plan → Execute → Track → Recover — drawn as one closed loop, a single fruit flowing through it from "detection" to "harvested"; each stage tagged with the wrapped layer it calls (M3, Understand, M5, M7, M6/M8, Track, orchestrator); Recover's feedback arrow closing the ring.]`

**Diagram Specification**
- **Objective:** show the complete pick cycle as one closed loop of wrapped stages.
- **Scene:** the six-stage ring with a fruit flowing through to "harvested", each stage tagged with its layer.
- **Labels:** the six stages, "wrapped layer" tags, "one pick, end to end", "Recover closes the loop".
- **Form:** SVG.

## 5. Engineering Example
One pick of F3, all six stages. Perceive returns detections; Understand dedupes and commits F3 (nearest ripe, reachable); `to_configuration` solves the IK to a goal configuration; Plan validates a smooth reference to it; Execute tracks the reference closed-loop (rms ≈ 0.0001); Track judges the verdict `success`; Recover has nothing to do, so the pick completes `recovered = False` in one attempt. Every call was an existing layer. Now perturb the execution: Execute's verdict turns `failure`, Track localises `TRACKING_FAILURE`, Recover retries, and — if the disturbance was transient — the pick completes `recovered = True` in two attempts. The same loop absorbs the fault without any new machinery.

## 6. Worked Example
Trace what the cycle returns for a healthy pick versus a transiently disturbed one, and identify what differs. Healthy: the forward path runs once, Track passes, `recover` reports `success = True, recovered = False, n_attempts = 1`. Transiently disturbed: the first attempt's Track fails with `TRACKING_FAILURE`, Recover (policy: `retry-execute`, retryable) re-runs Execute, the disturbance has cleared, Track passes, and `recover` reports `success = True, recovered = True, n_attempts = 2`. What differs is *only* the recovery bookkeeping — `recovered` and `n_attempts` — not any stage's internals. The cycle is identical; the loop simply ran Execute twice. This is the signature of integration: the same composed stages, re-sequenced by the orchestrator, handle both the clean and the faulted case.

## 7. Interactive Demonstration
*(Conceptual — the Installment-D flagship: the End-to-End Pick-Cycle Player.)*
Watch a single pick advance stage by stage around the ring, each stage lighting as it runs; toggle a transient disturbance and watch Track fail, Recover retry, and the pick complete on the second pass. The player makes the closed loop and its self-healing visible — the whole module animated as one cycle.

## 8. Coding Exercise
*(The notebook runs the full cycle.)*
Call `recover(world, q_start, target=...)` to run one complete pick and assert it succeeds in one attempt on a healthy setup (`recovered = False`). Then inject a transient disturbance on that pick and assert the full cycle still succeeds via recovery (`recovered = True`, `n_attempts = 2`). This verifies the six stages compose into one self-healing pick.

## 9. Knowledge Check
*(Formative — unlimited attempts, immediate feedback.)*
Confirm the six stages and their order, that each is a wrapped existing layer, that the cycle's only new content is the control flow and seams, and how a healthy pick differs from a recovered one.

## 10. Challenge Problem
The pick cycle composes six stages, each of which can hand off cleanly *or* trip a guard. Count the distinct outcomes of a single pick (success first-try; success after recovery; escalation at each hard-failure stage) and argue that the set is *finite and enumerable* — then explain why that finiteness is exactly what makes the integrated system testable. Keep the argument about composition and outcomes; do not add new stages or theory.

## 11. Common Mistakes
- **Mistaking parts for the system.** The robot is the loop its stages run, not any single stage.
- **Forgetting the seams.** The cycle works because each handoff contract holds; a broken seam breaks the loop.
- **Thinking the loop adds theory.** The only new content is the control flow and seam contracts — every stage is a wrapped layer.
- **Ignoring recovery in the cycle.** A complete pick cycle includes Recover; a forward-only path is not the full system.

## 12. Key Takeaways
- The pick cycle **composes the six stages** — Perceive, Understand, Plan, Execute, Track, Recover — into one self-healing loop.
- Each stage is a **wrapped existing layer**; the cycle's only new content is the **control flow and seam contracts**.
- A **healthy pick** runs the forward path once; a **faulted pick** runs Recover and retries or escalates — both terminate with a definite outcome.
- The difference between a clean and a recovered pick is **only the recovery bookkeeping**, not any stage's internals.
- One complete pick is **the whole module in a single loop** — integration is the lesson.

---

## AI Learning Companion
Copy any prompt into an AI assistant.

**Tutor prompt** — explain it another way
```
Re-explain Lesson 8.1 by walking one fruit through all six stages of the pick cycle as a single continuous procedure, like a surgeon's full operation.
```
**Practice prompt** — generate more exercises
```
Give me 4 exercises tracing a single pick through perceive → understand → plan → execute → track → recover, including one faulted case. With answers.
```
**Explore prompt** — connect it to the real world
```
Show me how a real robot composes perception, planning, control, and recovery into one closed pick-and-place cycle.
```

## Global Learning Support
Need this lesson in another language? Copy a prompt below into an AI assistant. English is the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just completed Lesson 8.1 — The Full Pick Cycle: Six Stages as One Loop.
Explain this lesson in Español. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 8.1 — The Full Pick Cycle: Six Stages as One Loop.
Explain this lesson in 中文 (Simplified Chinese). Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 8.1 — The Full Pick Cycle: Six Stages as One Loop.
Explain this lesson in Türkçe. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 8.2 — Harvesting a Row with Injected Failure (the capstone: the full system, across a whole row).*
