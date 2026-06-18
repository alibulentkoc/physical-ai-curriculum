---
module: 8
type: midpoint_assessment
title: "Module 8 Midpoint Assessment — Units 1–4"
covers: "The tracking problem & feedback loop · PID control · stability, response & tuning · tracking the whole arm (feedforward + feedback)"
estimated_time: "60–75 min"
---

# Module 8 — Midpoint Assessment (Units 1–4)

You are halfway through Module 8. The first half built feedback control from experience
upward: from *why open-loop isn't enough* and *what the feedback loop is*, to *PID control*
(proportional, integral, derivative), to *stability, response, and tuning* (recognising and
shaping the response, then setting the gains), to *tracking the whole arm* (per-joint control
and the feedforward + feedback combination that consumes Module 7's full reference). This
assessment checks that arc. Sections A–D mirror the four units; Section E is integrative.
Computational items can be answered with the lesson notebooks.

Throughout, the running arm is the planar 2-link ($L_1=0.4,\ L_2=0.3$) driven against a
simulated plant (integrator + disturbance + saturation), the tracking error is
$e = q_d - q$, and the controller consumes Module 7's reference $(q_d,\ \dot q_d,\ \ddot q_d)$.
No formal control theory (no Laplace, transfer functions, Bode, or Nyquist) is needed or
expected — answer in terms of behaviour, error, and correction.

---

## Section A — The Tracking Problem and the Feedback Loop (Unit 1)

**A1.** In one or two sentences, explain why an **open-loop** controller (running Module 7's
reference blind) drifts off target under load or model error, and what a **closed-loop**
controller does differently.

**A2.** Define the **tracking error** $e$, and name the four parts of a control system and
the one signal that connects the plant's output back to the controller.

**A3.** State the four stages of the feedback loop in order, and say which single stage is
the one thing open-loop control omits.

## Section B — PID Control (Unit 2)

**B1.** Write the three terms of the PID command and say, in a few words, what each term
responds to (the present, the past, the future of the error).

**B2.** Under a constant load $\ell$, pure proportional control settles with a steady-state
offset. State the offset in terms of $\ell$ and $K_p$, explain in one line why it is
*structural* (not a tuning mistake), and name the term that erases it.

**B3.** A joint under load $\ell = 2.0$ is held with proportional gain $K_p = 40$. Compute
the steady-state offset $e_{ss}=\ell/K_p$. Then name one risk of simply raising $K_p$ to
shrink it further, and the derivative term's two jobs (one helpful, one to watch out for).

## Section C — Stability, Response, and Tuning (Unit 3)

**C1.** Name the four step-response metrics and say, in a few words each, what behaviour
each one captures. Then state the central trade between two of them.

**C2.** Define **stable**, **marginal**, and **unstable** by the response envelope, and name
the **three** things that tip a loop toward instability. Explain in one line why *latency* is
as dangerous as excessive gain.

**C3.** State the **P → D → I** tuning workflow in order, saying what each step fixes, and
explain why you should stop at a *good response with margin* rather than tuning to the edge
of oscillation.

## Section D — Tracking the Whole Arm: Feedforward + Feedback (Unit 4)

**D1.** Explain why **feedback-only** tracking of a fast trajectory leaves a *following
error*, and why raising the gains is not a satisfactory cure. Name the two Module 7 signals
feedback ignores.

**D2.** Write the **inverse-model feedforward** command and say which Module 7 signal each
term uses and what it physically supplies. In one line, explain why feedforward (with a good
model) tracks a fast trajectory with almost no lag while feedback cannot.

**D3.** A disturbance hits the arm partway through a move. Explain why **feedforward alone
cannot reject it** but **feedback can**, referring to *where* the disturbance enters (plant
vs reference). Then write the **complete joint tracker** command and state which part handles
the known plan and which handles the unknown.

## Section E — Integrative

**E1.** *(Division of labour.)* In the feedforward + feedback controller, state in one line
each what **feedforward** is responsible for and what **feedback** is responsible for, and
why neither alone is sufficient for a real arm.

**E2.** *(Design.)* You must drive the harvester arm along a fast Module-7 trajectory to a
fruit, accurately and robustly, on a joint whose load is only approximately known and which
occasionally gets bumped. Describe the controller you'd build (the command, per joint), say
which part gives you the speed/accuracy and which gives you the robustness, and name one
thing you'd check during tuning to keep it safely stable.

**E3.** *(Boundary / continuity.)* A teammate says "Module 8's controller and Module 7's
trajectory generator are basically the same thing — both compute where the joint should go."
Correct this using the Module 7 → Module 8 boundary: what does Module 7 produce, what does
Module 8 produce, and what is the name and signature of the controller Module 8 hands to
Module 9?

---

*Submit your work to your coach. The coaches' answer key lives in
`coaches/answer-keys/module08/midpoint_answer_key.md`.*
