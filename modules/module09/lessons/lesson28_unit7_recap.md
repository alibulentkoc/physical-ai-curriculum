---
module: 09
unit: 07
lesson: 7.4
title: "Unit 7 Recap: Recover"
core_idea: "Unit 7 closed the workflow loop. The orchestrator — pure coordination, not a new layer — consumes detection's localised fault and owner, routes a targeted response built from existing layer calls, and bounds its retries with state across attempts so transient faults recover and persistent ones escalate. The system can now not only detect and localise failure but respond to it. This recap consolidates Recover and sets up Unit 8, where the full self-healing pick cycle is assembled."
estimated_time: "35 min"
difficulty: "Intermediate"
prerequisites:
  - "7.1 — The orchestrator"
  - "7.2 — Targeted responses"
  - "7.3 — Retry limits and state"
learning_objectives:
  - "Reproduce the Recover loop: detect, route by owner, bound retries, escalate."
  - "State why recovery adds no new theory."
  - "Identify what Unit 8 assembles on top of Recover."
tags:
  - physical-ai
  - robotics
  - systems-integration
  - recap
---

# Lesson 7.4 — Unit 7 Recap: Recover

> The workflow loop is closed. The robot can perceive, understand, plan, execute, judge, monitor, detect, localise — and now respond. This recap consolidates the Recover stage and points at Unit 8, where everything assembles into one self-healing pick cycle.

---

## 1. Why This Matters
Recover is the stage that makes the whole module add up to a *working* system rather than a well-instrumented one. Detection without recovery notices failures it cannot fix; recovery without detection acts on guesses. Unit 7 joined them: a coordinator that takes the localised, owned fault and turns it into a targeted, bounded response. Consolidating that — what the orchestrator is, what it routes, and why it terminates — is what lets Unit 8 assemble the full self-healing cycle with confidence that each piece is sound.

## 2. Physical Intuition
The flight director now has a playbook and a clock. Unit 7.1 cast the orchestrator as a coordinator (the flight director); 7.2 gave it the playbook (route each fault to the owner's action); 7.3 gave it the clock and the count (bounded retries with memory). With all three, the director can handle a hold: identify it, call the right team, and either recycle a few times or scrub — never spin forever. That complete, terminating, targeted response is what Unit 7 delivers.

## 3. Mathematical Foundations
Unit 7 in four lines:

- **Orchestrator** (7.1): Recover is the sixth stage — *coordination, not a new layer*; it consumes detection's localised fault + owner and re-invokes existing layers.
- **Policy** (7.2): a map from fault → targeted response, routed by owner; responses are existing layer calls; retryability encodes the fault's nature (transient vs deterministic).
- **Budget + state** (7.3): a counter across attempts and a cap $N$; three exits — success (recovered), deterministic escalation (immediate), budget-exhaustion escalation (at $N$).
- **No new theory:** every response is `model_perception`/`execute_reference`/target-advance re-invoked; the only additions are control flow and bookkeeping.

The output is a pick cycle that, on a recoverable fault, *recovers*, and on an unrecoverable one, *escalates cleanly* — never loops. That terminating, self-correcting cycle is Unit 8's building block.

## 4. Visual Explanation
`[Visual: the six-stage workflow with Recover closing the loop — detection's localised fault feeding the orchestrator, which routes by owner (policy) through a bounded retry loop (budget + counter) back to the re-invoked stage; a greyed "Unit 8: full self-healing pick cycle" downstream.]`

**Diagram Specification**
- **Objective:** one image consolidating Recover: coordinate, route by owner, bound retries, escalate.
- **Scene:** workflow loop closed by Recover; policy routing + bounded retry; Unit 8 greyed as next.
- **Labels:** "localised fault + owner", "policy (owner→action)", "budget + counter", "recovered / escalated", "Unit 8: full cycle".
- **Form:** SVG.

## 5. Engineering Example
Three pick cycles, one recap line each. Transient disturbance: `TRACKING_FAILURE` at attempt 0 → retry-execute → success at attempt 1 — *recovered*. Persistent disturbance: fails through the budget → *escalates* (`retry-budget-exhausted`), no infinite loop. Blocked goal: `PLAN_INVALID`, deterministic → *escalates immediately* (`skip-target`). Three faults, three terminating outcomes, all from the same orchestrator coordinating the same layers. If you can predict which outcome each fault yields, Unit 7 has done its job.

## 6. Worked Example
Self-test, answered. *Question:* a teammate proposes making the orchestrator "smarter" by adding a small estimator that predicts whether a disturbance will persist, to skip doomed retries. Is this in scope for Module 9? *Answer:* no — that introduces *estimation theory*, which the integration lane excludes. The orchestrator already handles persistence correctly without prediction: it retries a bounded number of times and escalates if the fault persists. The bounded-retry design *is* the integration-appropriate answer to "will it persist?" — try a few times and find out, rather than estimate. Keeping recovery as coordination (re-invoke + budget) rather than prediction (estimate + decide) is the scope discipline Unit 7 models.

## 7. Interactive Demonstration
*(Conceptual — the Installment-D flagship: the End-to-End Pick-Cycle Player.)*
The recap demonstration is the full pick-cycle player: inject any fault, set a budget, and watch the orchestrator detect, route by owner, retry within budget, and either recover or escalate — the workflow loop closing on each attempt. It is all of Unit 7's competence in one interactive cycle.

## 8. Coding Exercise
*(The recap notebook runs the full Recover stage.)*
Exercise all three exits with `recover`: a transient fault that recovers, a persistent fault that escalates at the budget, and a deterministic fault that escalates immediately. Assert the `recovered`/`escalated` flags, the attempt counts, and the escalation reasons. Passing this is your evidence that Recover coordinates, routes, and terminates correctly on the real layers.

## 9. Knowledge Check
*(Formative — unlimited attempts, immediate feedback.)*
Mixed review across Unit 7: the orchestrator as coordination, the owner→action policy, retryable vs deterministic, the budget and the three termination exits, and why recovery adds no new theory.

## 10. Challenge Problem
Unit 8 will run the orchestrator across a *sequence* of picks (a full row). Sketch what additional state the system must carry at the *row* level (beyond a single cycle's retry counter) to harvest a row robustly — e.g. which fruits were picked, which were skipped after escalation, when to stop. Frame it as coordination state, a preview of Unit 8's full-system assembly, not new theory.

## 11. Common Mistakes
- **Calling Recover a new layer.** It coordinates existing layers; it owns no theory.
- **Unbounded recovery.** Without a budget and counter, persistent faults loop; termination is designed in.
- **One response for all faults.** The policy routes by owner; retryability decides retry-or-skip.
- **Adding prediction/estimation.** Bounded retry is the integration answer to persistence — no estimator needed.

## 12. Key Takeaways
- Unit 7 **closed the workflow loop** with **Recover** — pure coordination, the sixth stage.
- The orchestrator **consumes detection's localised fault + owner**, routes a **targeted response** (existing layer calls), and **bounds retries** with cross-attempt state.
- Three terminating exits: **recovered**, **deterministic escalation**, **budget-exhaustion escalation**.
- Recovery adds **no new theory** — only control flow and bookkeeping around existing layers.
- Next, **Unit 8** assembles the full **self-healing pick cycle** across a harvest.

---

## AI Learning Companion
Copy any prompt into an AI assistant.

**Tutor prompt** — explain it another way
```
Quiz me on Unit 7: orchestrator as coordination, the recovery policy, retryable vs deterministic, and the bounded retry exits. Re-explain whatever I miss.
```
**Practice prompt** — generate more exercises
```
Give me 5 mixed-review questions on robot failure recovery: routing by owner, retry budgets, and termination outcomes, with answers.
```
**Explore prompt** — connect it to the real world
```
Show me how real autonomous systems coordinate targeted, bounded recovery from detected failures without adding new control theory.
```

## Global Learning Support
Need this lesson in another language? Copy a prompt below into an AI assistant. English is the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just completed Lesson 7.4 — Unit 7 Recap: Recover.
Explain this lesson in Español. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 7.4 — Unit 7 Recap: Recover.
Explain this lesson in 中文 (Simplified Chinese). Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```
```
I just completed Lesson 7.4 — Unit 7 Recap: Recover.
Explain this lesson in Türkçe. Keep robotics/math terminology in English where appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 8.1 — Assembling the Full System (Unit 8 opens — the self-healing pick cycle, end to end).*
