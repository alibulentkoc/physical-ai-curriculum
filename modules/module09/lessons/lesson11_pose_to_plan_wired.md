---
module: 09
unit: 03
lesson: 3.3
title: "Integration Exercise — Pose to Plan, Wired End to End"
core_idea: "Now we wire the whole Understand → Plan seam in one run: perceive, understand (commit a target), convert the pose to a configuration (M5 IK), invoke the planner (M7), and read the resulting reference — all on the real layers, with a trace at every step. This is the integration exercise: not new theory, but the discipline of connecting verified layers and confirming the contract chain holds end to end."
estimated_time: "50 min"
difficulty: "Intermediate"
prerequisites:
  - "3.1 — Pose to configuration"
  - "3.2 — Invoking the planner"
learning_objectives:
  - "Wire perceive → understand → to_configuration → plan_reference into one runnable chain."
  - "Emit and read a trace across the Understand → Plan seam."
  - "Confirm the contract chain holds: target → configuration → validated reference reaching the target."
tags:
  - physical-ai
  - robotics
  - systems-integration
  - integration-exercise
---

# Lesson 3.3 — Integration Exercise: Pose to Plan, Wired End to End

> Two lessons gave us the two halves of the seam: pose → configuration, and configuration → reference. This lesson connects them — and the perception in front of them — into a single end-to-end run, then reads the trace to confirm every link holds. It is the integration exercise: the parts are built; the work is wiring them and checking the seams.

---

## 1. Why This Matters
Knowing each step in isolation is not the same as running them together. The end-to-end wire is where the seams between IK and the planner, and between perception and IK, actually get tested: does the configuration from IK feed the planner cleanly? Does the planner's reference truly reach the perceived target? This exercise builds the habit of *composing verified layers and reading the trace* — the same habit Unit 1 introduced, now applied across three real layers (M3 perception stand-in, M5 IK, M7 planner). It is also the rehearsal for Unit 4, where the reference flows on into Execute.

## 2. Physical Intuition
A relay handoff practiced in full. Earlier we practiced each exchange alone; now we run the leg start to finish — see the fruit, decide on it, find the joint bends, schedule the motion — and check the baton never dropped. Running the whole leg surfaces timing and fit problems that single-exchange drills hide. If the end-to-end run produces a validated reference whose endpoint lands on the chosen fruit, the seam is sound.

## 3. Mathematical Foundations
The Understand → Plan seam, composed:

$$\text{detections} \xrightarrow{\text{understand}} w^\star \xrightarrow{\text{to\_configuration (M5)}} q_{\text{goal}} \xrightarrow{\text{plan\_reference (M7)}} \texttt{reference}(t).$$

The end-to-end **contract chain** to verify:

1. $w^\star$ is ripe and reachable (Unit 2's postcondition).
2. $q_{\text{goal}} = \mathrm{IK}(w^\star) \neq \text{None}$, and $\mathrm{FK}(q_{\text{goal}}) = w^\star$ (Lesson 3.1).
3. The plan is `validated`, and $\mathrm{FK}(\texttt{reference}(\text{duration})) = w^\star$ (Lesson 3.2).

If all three hold, the seam is correct: the perceived target became a validated motion plan that ends exactly where the fruit is. The exercise asserts each link; a break at any link localises the fault to a stage — the diagnostic skill from Unit 1, now spanning three layers.

## 4. Visual Explanation
`[Visual: a horizontal wired chain — Perceive → Understand → (pose) → IK → (q_goal) → Plan → (reference) — with a trace stamp under each arrow showing the value handed forward, ending in a small plot of reference(t) whose endpoint is annotated "= target pose".]`

**Diagram Specification**
- **Objective:** show the whole seam wired, with the value on every arrow and the end-to-end check.
- **Scene:** perceive → understand → IK → plan, batons labelled (detections, target pose, q_goal, reference), endpoint verified against the target.
- **Labels:** "target pose", "q_goal (IK)", "reference(t) (M7)", "endpoint = target ✓".
- **Form:** SVG.

## 5. Engineering Example
One run, narrated by its trace. Perceive yields detections; Understand commits F3 at $(0.447, 0.152)$. `to_configuration(F3)` returns $q_{\text{goal}} = (-0.356, 1.684)$, and FK confirms it reaches $(0.447, 0.152)$. `plan_reference(q_{\text{start}}, q_{\text{goal}})` returns a `validated` layer of duration $\approx 1.13$ s. Sampling `reference(duration)` and running FK lands on $(0.447, 0.152)$ — the same fruit. Every link checked; the baton travelled from a camera detection to a validated motion plan without a drop. That is a correct Understand → Plan seam.

## 6. Worked Example
Suppose the end-to-end run breaks at link 3: the plan comes back `validated = False`. Localise it using the trace, without opening the planner. Reasoning: links 1 and 2 passed, so the target is reachable and $q_{\text{goal}}$ is a valid configuration that FK confirms. A failed validation with a good goal points to the *plan between start and goal* — for instance, the move violates a velocity/acceleration limit at the requested timing, or (with an obstacle) no collision-free path exists. The fault is in Plan's inputs or constraints, not in IK or perception. The fix is a Plan/Recover concern (relax timing, replan, or re-select). The exercise teaches you to read the trace to that conclusion.

## 7. Interactive Demonstration
*(Conceptual — runnable in the notebook.)*
A single "run the seam" button that prints the trace: `perceive → N detections`, `understand → target F3`, `IK → q_goal (FK err ≈ 0)`, `plan → validated, duration`, `endpoint → matches target`. Flip a switch to push the target out of reach and watch the trace stop at the IK link (`None`), demonstrating fault localisation. The notebook implements exactly this.

## 8. Coding Exercise
*(The notebook runs the full seam on real layers.)*
Wire `model_perception → understand → to_configuration → plan_reference` and assert the three-link contract chain: the committed target is ripe and reachable; IK returns a configuration whose FK matches the target; the plan is validated and its endpoint's FK matches the target. Then break one link (unreachable target) and assert the chain stops at IK with `None`. This is the integration exercise in code.

## 9. Knowledge Check
*(Formative — unlimited attempts, immediate feedback.)*
Confirm the order of the wired chain, the three contract links, how to localise a break to a stage, and the scope fence (wiring verified layers, not adding theory).

## 10. Challenge Problem
Extend the wired seam to plan for **two** targets in sequence: pick F3, then the next-ranked fruit. Identify what must carry over between the two plans (hint: the second plan's $q_{\text{start}}$ is the first plan's $q_{\text{goal}}$, i.e. where the arm ends up) and which stage owns threading that state. Then state one end-to-end check that would catch a bug where the second plan wrongly starts from the home configuration instead of F3's configuration.

## 11. Common Mistakes
- **Testing links only in isolation.** The end-to-end wire is where seam fit is actually verified.
- **Not threading $q_{\text{start}}$.** The next plan starts from where the arm *is*, not from home; mishandling this corrupts sequential picks.
- **Blaming the planner for an IK problem (or vice versa).** Read the trace: a `None` is an IK/reach issue; a `validated = False` with a good goal is a Plan issue.
- **Adding theory.** This is pure wiring of verified layers; no new kinematics or planning is introduced.

## 12. Key Takeaways
- The Understand → Plan seam wires **perceive → understand → to_configuration → plan_reference** into one run.
- A correct run satisfies a **three-link contract chain**: reachable target → FK-verified configuration → validated reference whose endpoint reaches the target.
- Reading the trace **localises any break to a stage** — `None` at IK (unreachable) vs. `validated = False` at Plan (infeasible timing/path).
- Sequential picks must **thread $q_{\text{start}}$** from one plan's endpoint to the next.
- The exercise is composition and verification, not new theory — the core integration skill.

---

## AI Learning Companion
Copy any prompt into an AI assistant.

**Tutor prompt** — explain it another way
```
Re-explain Lesson 3.3 by wiring perception → target selection → inverse kinematics → trajectory planning into one chain and checking each handoff.
```
**Practice prompt** — generate more exercises
```
Give me 4 "run the seam, read the trace, localise the break" exercises for a target → configuration → plan pipeline, with answers.
```
**Explore prompt** — connect it to the real world
```
Show me how real robot software chains perception, IK, and motion planning into one request and how it verifies the result end to end.
```

## Global Learning Support
Need this lesson in another language? Copy a prompt below into an AI assistant. English is the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just completed Lesson 3.3 — Integration Exercise: Pose to Plan, Wired End to End.
Explain this lesson in Español. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 3.3 — Integration Exercise: Pose to Plan, Wired End to End.
Explain this lesson in 中文 (Simplified Chinese). Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 3.3 — Integration Exercise: Pose to Plan, Wired End to End.
Explain this lesson in Türkçe. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 3.4 — Unit 3 Recap (the Understand → Plan seam consolidated, before Unit 4 drives the reference into real joint motion).*
