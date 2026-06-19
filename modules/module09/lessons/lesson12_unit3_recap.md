---
module: 09
unit: 03
lesson: 3.4
title: "Unit 3 Recap: Understand → Plan"
core_idea: "Unit 3 opened the second seam. A committed target pose became a goal configuration via Module 5 IK (verified by Module 4 FK), and that configuration became a timed, validated reference via Module 7's planner — all wrapped verbatim, all wired and traced end to end. This recap consolidates the pose → configuration → reference chain and sets up Unit 4, where the reference finally drives real joint motion."
estimated_time: "30 min"
difficulty: "Intermediate"
prerequisites:
  - "3.1 — Pose to configuration"
  - "3.2 — Invoking the planner"
  - "3.3 — Pose to plan, wired end to end"
learning_objectives:
  - "Reproduce the Understand → Plan chain from target pose to validated reference."
  - "State the ownership split: M5/M7 own the math, integration owns the seam decisions."
  - "Identify what the seam hands to Execute next."
tags:
  - physical-ai
  - robotics
  - systems-integration
  - recap
---

# Lesson 3.4 — Unit 3 Recap: Understand → Plan

> Unit 3 turned a point in the greenhouse into a validated plan to reach it. This recap consolidates the two conversions — pose → configuration, configuration → reference — into one mental model and one runnable check, then points at Unit 4, where the reference becomes motion.

---

## 1. Why This Matters
The Understand → Plan seam is the bridge from *deciding* to *moving*. Everything before it was about choosing the right target; everything after it is about executing the plan to reach it. Locking in this seam — how a pose becomes a configuration, how a configuration becomes a reference, and who owns each decision — is what lets Unit 4 focus purely on execution without re-litigating the goal. This recap makes sure the bridge is solid.

## 2. Physical Intuition
Destination, joint bends, schedule. You have the *spot* (the committed pose); you find the *joint bends* that reach it (IK), checking you can actually reach it; then a lower system makes the *schedule* for the motion (the planner). Three moves, and at the end you hold a timed plan that, if executed, lands your hand on the fruit. That held plan is what Unit 4 will run.

## 3. Mathematical Foundations
Unit 3 in three lines:

- **Pose → configuration** (M5 IK, M4 FK verify): $q_{\text{goal}} = \mathrm{IK}(w^\star)$, with `None` ⇒ unreachable and the elbow-up/down ambiguity resolved by policy; FK confirms $\mathrm{FK}(q_{\text{goal}}) = w^\star$.
- **Configuration → reference** (M7, wrapped verbatim): $\texttt{reference}(t) = (q_d, \dot q_d, \ddot q_d, \text{info})$ with a `validated` flag and a `duration`.
- **Ownership:** the kinematics and trajectory math are Modules 5 and 7; integration owns the **calls and the decisions** — which IK branch, what to do on `None` or `validated = False`, and threading $q_{\text{start}}$ across sequential picks.

The seam's output — a validated `reference(t)` — is the precondition for Execute.

## 4. Visual Explanation
`[Visual: the Understand → Plan seam as one bridge — target pose on the left, an "IK + FK verify" pier, a "M7 planner" pier, and a validated reference(t) on the right handed to Execute; small fault tags under each pier (IK→None unreachable; plan→validated False infeasible).]`

**Diagram Specification**
- **Objective:** one image summarising pose → configuration → reference with its two failure points.
- **Scene:** pose → IK/FK → q_goal → M7 → reference(t) → Execute, with the two fault tags.
- **Labels:** "target pose", "q_goal (IK, FK-verified)", "reference(t) (validated)", "→ Execute".
- **Form:** SVG.

## 5. Engineering Example
End to end, the working example you should be able to recite: Understand commits F3 at $(0.447, 0.152)$; IK returns $q_{\text{goal}} = (-0.356, 1.684)$ and FK confirms it; the planner returns a validated reference of duration $\approx 1.13$ s whose endpoint's FK lands on F3. If you can narrate that chain — value, owner, and check at each step — Unit 3 has done its job.

## 6. Worked Example
Self-test, answered. *Question:* the wired seam returns `validated = False`, but IK succeeded and FK confirmed $q_{\text{goal}}$. Where is the fault, and whose decision is the fix? *Answer:* the fault is in **Plan**, not IK or perception — the goal is a valid reachable configuration, but the *trajectory* between start and goal failed validation (e.g. a limit violation at the requested timing, or no collision-free path). The fix is a Plan/Recover decision: relax the timing, replan, or re-select a target. Reaching that conclusion from the trace is the Unit 3 outcome.

## 7. Interactive Demonstration
*(Conceptual — runnable in the notebook.)*
The recap demonstration is one consolidated run: perceive, understand, convert to configuration, plan, and print a five-stamp trace ending in "endpoint = target ✓". Toggle the target out of reach and the trace stops at IK with `None`. It is Unit 3 compressed into a cell you can execute and trust.

## 8. Coding Exercise
*(The recap notebook runs the consolidated chain.)*
In one short notebook: perceive → understand → `to_configuration` → `plan_reference`, and assert the three-link chain (reachable target; FK-verified configuration; validated reference whose endpoint reaches the target). Then assert that an out-of-reach target stops the chain at IK with `None`. Passing this cell is your evidence that the Understand → Plan seam works end to end on the real layers.

## 9. Knowledge Check
*(Formative — unlimited attempts, immediate feedback.)*
Mixed review across Unit 3: the IK seam and FK verification, the planner invocation and `validated`, the wired end-to-end chain, fault localisation, and the ownership split.

## 10. Challenge Problem
Unit 4 will sample `reference(t)` and feed each sample to Module 8's tracking controller, then read back the actual joint state. Predict the one new question Unit 4 must answer that Unit 3 did not (hint: a *plan* assumes perfect execution, but a real controller has tracking error). State which module owns the tracking math and which stage owns *deciding whether the tracking error is acceptable* — previewing the Track stage in Unit 5.

## 11. Common Mistakes
- **Handing a pose to the planner.** Convert to a configuration first (IK), or the planner has no well-posed goal.
- **Trusting an unverified configuration.** Always FK-verify before planning.
- **Executing an unvalidated plan.** `validated = False` is a Recover concern, never silently run.
- **Forgetting to thread $q_{\text{start}}$.** Sequential picks start from where the arm is, not from home.

## 12. Key Takeaways
- The Understand → Plan seam is **pose → configuration → reference**, bridging deciding and moving.
- **Module 5 IK** (FK-verified) and **Module 7's planner** (wrapped verbatim) do the math; integration owns the **calls and decisions**.
- A correct seam yields a **validated `reference(t)`** whose endpoint reaches the target.
- Failures localise cleanly: **`None` at IK** (unreachable) vs. **`validated = False` at Plan** (infeasible).
- Next, Unit 4 samples that reference and drives **real joint motion** — closing the forward path at the midpoint.

---

## AI Learning Companion
Copy any prompt into an AI assistant.

**Tutor prompt** — explain it another way
```
Quiz me on Unit 3: pose→configuration via IK (with FK verify), invoking the planner, and the wired end-to-end seam. Re-explain whatever I miss.
```
**Practice prompt** — generate more exercises
```
Give me 5 mixed-review questions on converting a pose to a configuration, invoking a trajectory planner, and localising a seam failure, with answers.
```
**Explore prompt** — connect it to the real world
```
Show me how a real robot turns a chosen target into a validated motion plan, and where IK and planning sit in that pipeline.
```

## Global Learning Support
Need this lesson in another language? Copy a prompt below into an AI assistant. English is the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just completed Lesson 3.4 — Unit 3 Recap: Understand → Plan.
Explain this lesson in Español. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 3.4 — Unit 3 Recap: Understand → Plan.
Explain this lesson in 中文 (Simplified Chinese). Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 3.4 — Unit 3 Recap: Understand → Plan.
Explain this lesson in Türkçe. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 4.1 — The Motion Stack: reference → velocity → tracking_controller (Unit 4 drives the plan into real joint motion; the midpoint closes at L16).*
