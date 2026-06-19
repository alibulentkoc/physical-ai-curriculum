---
module: 09
unit: 07
lesson: 7.1
title: "The Orchestrator: Coordination as a Stage"
core_idea: "Recovery is not a new layer with new theory — it is a coordinator. The orchestrator is the sixth stage of the workflow: it runs the forward path, and when detection localises a fault, it consults a policy and routes a targeted response built entirely from existing layer calls. It adds no estimator, planner, or controller; its only new capability is deciding what to re-invoke and when. Recover closes the loop the workflow opened."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "6.4 — Detection complete (localised fault + owner)"
  - "Units 1–6 — the full forward path and detection"
learning_objectives:
  - "Define the orchestrator as pure coordination, not a new layer."
  - "Describe how Recover consumes the localised fault and owner from detection."
  - "Place Recover as the sixth stage closing the workflow loop."
tags:
  - physical-ai
  - robotics
  - systems-integration
  - orchestration
  - recovery
---

# Lesson 7.1 — The Orchestrator: Coordination as a Stage

> Detection told us *what failed, where, and who owns it*. Now, finally, *how do we respond?* Installment D opens with the answer's shape: not a clever new algorithm, but a coordinator that re-invokes the layers we already have, aimed by the localisation we already produced. Recover is the stage that turns a detected failure into a second chance.

---

## 1. Why This Matters
Everything so far built *toward* this moment, and the temptation is to make recovery grand — a fault-tolerant control law, a re-planning estimator. That temptation is the trap. In an integrated system, recovery is **coordination**: given a localised fault and its owner, decide which existing layer to call again, with what change, and how many times. The orchestrator introduces no new theory because it does not need to — the layers can already perceive, plan, and execute; what was missing was a stage that *decides to do it again, differently, on purpose*. Framing Recover as coordination keeps it honest and keeps Module 9 in the integration lane to the very end.

## 2. Physical Intuition
A flight director, not a new instrument. When a launch hits a hold, mission control does not invent a new rocket — the flight director reads the telemetry, identifies which team owns the issue, and calls "recycle the count" or "scrub." The director's authority is *coordination*: routing the right existing team to act, deciding whether to retry or stand down. The orchestrator is the robot's flight director: it does not fly the rocket (the layers do that), it decides, on a localised fault, who acts and whether to try again.

## 3. Mathematical Foundations
The orchestrator sits atop the detection pipeline as the **sixth stage**, closing the workflow:

$$\text{Perceive} \to \text{Understand} \to \text{Plan} \to \text{Execute} \to \text{Track} \to \boxed{\text{Recover}}.$$

Its logic is a coordination loop, not an algorithm over signals:

1. Run the guarded forward path (`run_pipeline`) — produces a verdict and, on failure, a **localised fault + owner** (Unit 6).
2. If success, done.
3. If a hard failure, look up the fault in a **recovery policy** (Lesson 7.2) keyed by the event, and apply the **targeted response** it names — which is always *an existing layer call re-invoked* (re-perceive = `model_perception` again; retry-execute = `execute_reference` again) or the target advanced.
4. Repeat under a **budget** (Lesson 7.3) so the loop terminates.

The orchestrator's *inputs* are exactly detection's *outputs* — the localised fault and owner. Its *actions* are exactly the existing layers' *entry points*. Nothing in between is new theory; the only novelty is the control flow that connects them. This is why Recover is a *stage* (a coordination role in the workflow), not a *layer* (a capability with its own theory).

## 4. Visual Explanation
`[Visual: the six-stage workflow ring with Recover as the sixth box, fed by detection's "localised fault + owner" arrow; Recover drawn as a router that points back to existing stages (re-perceive → Perceive, retry → Execute) rather than containing new machinery; a label "coordination, not a new layer".]`

**Diagram Specification**
- **Objective:** show Recover as a coordinating sixth stage that re-invokes existing stages.
- **Scene:** the workflow with Recover receiving the localised fault and routing back to Perceive/Execute/etc.
- **Labels:** "localised fault + owner", "re-invoke existing layer", "coordination, not a new layer", "closes the loop".
- **Form:** SVG.

## 5. Engineering Example
The orchestrator on a transient disturbance. The forward path runs; a one-time kick on joint 0 trips `TRACKING_FAILURE` at Track, localised to owner Execute. The orchestrator reads that localisation, looks up the policy (Execute → retry-execute), and re-invokes `execute_reference` — the same controller, the same plan, a fresh run. The kick is gone this time, the run tracks tightly, and Track returns success. The cycle *recovered*: the same layers, re-coordinated. No new control law was written; the orchestrator simply decided to execute again because the fault's owner and nature said a retry could work. That decision is the whole of Recover.

## 6. Worked Example
Why is Recover a *stage* and not a *layer*? Contrast it with Plan (a layer). Plan owns a body of theory — trajectory generation, limit validation — and produces a capability the system did not otherwise have. Recover owns *no* theory: it cannot perceive, plan, or control; it can only *call* the stages that do. Its job is the *when and which* — when to retry, which stage to re-invoke, when to stop. That is a coordination role, exactly like a workflow's controller-of-controllers. Calling it a "layer" would wrongly imply it adds a new capability; calling it a "stage" correctly places it as the coordinating step that uses the capabilities already present. The distinction is not pedantic — it is the guardrail that keeps recovery from smuggling in new theory.

## 7. Interactive Demonstration
*(Conceptual — fully realised in the Installment-D flagship, the End-to-End Pick-Cycle Player.)*
A pick cycle runs; inject a transient fault and watch the orchestrator detect it, name the owner, and re-invoke the matching stage, the second attempt succeeding — the workflow ring lighting Recover, then looping back to the re-invoked stage. The demonstration shows recovery as routing, not as new machinery.

## 8. Coding Exercise
*(The notebook runs the real orchestrator.)*
Call `recover(world, q_start)` on a healthy setup and assert it succeeds on the first attempt (`recovered = False`, `n_attempts = 1`). Then inject a transient disturbance (`disturbance = lambda a: kick if a == 0 else None`) and assert the orchestrator recovers (`success = True`, `recovered = True`, `n_attempts = 2`) by re-invoking execution. This shows Recover coordinating existing layers without new theory.

## 9. Knowledge Check
*(Formative — unlimited attempts, immediate feedback.)*
Confirm that the orchestrator is coordination not a new layer, that Recover is the sixth stage, that it consumes detection's localised fault and owner, and that its responses are existing layer calls re-invoked.

## 10. Challenge Problem
The orchestrator's inputs are detection's outputs (localised fault + owner) and its actions are the layers' entry points. Argue what would go wrong if you *skipped* detection and let the orchestrator react to a bare pass/fail boolean instead of a localised, owned fault — specifically, how would it decide *which* stage to re-invoke? Use this to explain why the Architect's sequence puts *who owns the fix* immediately before *recover*. Keep the argument about coordination and information flow, not new theory.

## 11. Common Mistakes
- **Treating recovery as a new layer.** It owns no theory; it coordinates existing layers.
- **Reacting to a bare failure.** Without the localised fault and owner, the orchestrator cannot target a response.
- **Inventing fault-tolerant control.** The response is *re-invoking* a layer, not a new control law.
- **Forgetting Recover closes the loop.** It is the sixth stage that turns a detected failure into a second attempt, completing the workflow.

## 12. Key Takeaways
- The **orchestrator** is the sixth stage — **Recover** — and it is *pure coordination*, not a new layer.
- It **consumes detection's output**: the localised fault and its owner.
- Its **responses are existing layer calls re-invoked** (re-perceive, retry-execute) or the target advanced — no new theory.
- Recover is a **stage** (a coordination role), not a **layer** (a capability with its own theory).
- It **closes the workflow loop**, turning a detected failure into a targeted second chance.

---

## AI Learning Companion
Copy any prompt into an AI assistant.

**Tutor prompt** — explain it another way
```
Re-explain Lesson 7.1 by describing the orchestrator as a flight director who coordinates existing teams, not a new piece of hardware.
```
**Practice prompt** — generate more exercises
```
Give me 4 exercises distinguishing a coordination "stage" from a capability "layer" in a robot pipeline, with answers.
```
**Explore prompt** — connect it to the real world
```
Show me how real robot systems implement a recovery/orchestration layer that coordinates existing modules rather than adding new control theory.
```

## Global Learning Support
Need this lesson in another language? Copy a prompt below into an AI assistant. English is the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just completed Lesson 7.1 — The Orchestrator: Coordination as a Stage.
Explain this lesson in Español. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 7.1 — The Orchestrator: Coordination as a Stage.
Explain this lesson in 中文 (Simplified Chinese). Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 7.1 — The Orchestrator: Coordination as a Stage.
Explain this lesson in Türkçe. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 7.2 — Targeted Responses: Matching Action to Owner (the recovery policy).*
