---
module: 07
unit: 07
lesson: 7.3
title: "Tracking Prerequisites: What the Reference Must Provide"
core_idea: "A trajectory's job is to be followed. For a downstream tracker (Module 8) to follow it well, the reference must provide, at every instant, the desired position, velocity, and acceleration (feed-forward) — continuous, feasible, and densely sampled. Module 7 produces this reference; it does not do the following. The prerequisites define the clean handoff."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L7.2 — Validating a trajectory"
  - "M7 L1.2 — A trajectory is a timed reference"
learning_objectives:
  - "State what a reference must provide for a tracker to follow it: q_d, q̇_d, q̈_d, continuous and feasible."
  - "Explain the Module 7 / Module 8 boundary: producing the reference vs tracking it."
  - "Identify what would make a reference un-trackable, and why."
---

# Lesson 7.3 — Tracking Prerequisites: What the Reference Must Provide

> A trajectory exists to be **followed**. Module 8 will build the tracker that follows it; Module 7's job is to hand that tracker a reference it *can* follow. This lesson defines the prerequisites — exactly what the reference must provide — and draws the bright line between the two modules. We do **not** track here; we specify the clean handoff. This is the boundary lesson.

---

## 1. Why This Matters
Everything in Module 7 — planning, parameterizing, validating — exists to produce one thing: a **reference trajectory** for a tracker to follow. But a tracker can only follow a reference that gives it what it needs, at every instant, in a usable form. If the reference is missing information (no velocity feed-forward), or is infeasible (demands impossible speeds), or has gaps (a discontinuity, too-coarse sampling), then no tracker can follow it well — the failure was upstream, in the reference, not in the tracking.

So this lesson specifies the **prerequisites**: the contract the reference must satisfy so that a downstream tracker can do its job. Concretely, the reference must provide, at each time, the desired **position** (where to be), **velocity** (how fast — the feed-forward that lets a tracker keep up), and **acceleration** (the feed-forward that lets it anticipate) — and it must be continuous, feasible, and sampled finely enough to step through. Crucially, **Module 7 stops exactly here.** We produce and certify this reference; we do **not** build the controller that follows it, compute tracking errors, or command motors. That is Module 8. Naming the prerequisites is what makes the handoff clean — and what keeps Module 7 inside its scope.

## 2. Physical Intuition
Imagine handing sheet music to a musician. Your job (the composer) is to write a score that's *playable*: notes (which pitch — position), timing (how the notes move — velocity), and dynamics/phrasing cues (how to anticipate what's coming — acceleration). If the score is complete and playable, the musician can perform it. But you, the composer, don't play it — the musician does. And if you wrote an unplayable score (notes too fast for any human, a gap mid-bar), no musician could perform it, however skilled; the fault is in the score.

A reference trajectory is the score; the tracker (Module 8) is the musician. Module 7 writes a complete, playable score: at every instant it says where the joint should be (position), how fast it should be moving (velocity), and how its speed should be changing (acceleration) — smoothly, feasibly, finely enough to read. Module 8 performs it — reads the reference and drives the motors to follow it, correcting for disturbances. Module 7 never performs; it only writes a score that *can* be performed. The prerequisites are "what makes the score playable."

## 3. Mathematical Foundations
A **reference trajectory** is a time-indexed signal the tracker consumes. The prerequisites — what it must provide and satisfy — are:

**Provide, at every time $t\in[0,T]$:**
- **Desired position** $\mathbf q_d(t)$ — the configuration to be at.
- **Desired velocity** $\dot{\mathbf q}_d(t)$ — the joint speeds. This is **feed-forward**: it tells the tracker how fast to move so it isn't always lagging, reacting only to error. (How the tracker *uses* it — feed-forward plus error correction — is Module 8.)
- **Desired acceleration** $\ddot{\mathbf q}_d(t)$ — the feed-forward that lets the tracker anticipate changes in speed.

(For Cartesian intent, the equivalent tool-space reference $\mathbf p_d(t)$ may also be carried, but the joint-space $\mathbf q_d,\dot{\mathbf q}_d,\ddot{\mathbf q}_d$ is what a joint tracker needs.)

**Satisfy:**
- **Continuity:** $\mathbf q_d$ is $C^0$, $\dot{\mathbf q}_d$ continuous ($C^1$), ideally $\ddot{\mathbf q}_d$ continuous ($C^2$) — no jumps for the tracker to chase.
- **Feasibility:** within velocity/acceleration limits and collision-free and reachable (Units 5–6; validated in 7.2) — a tracker can't follow what the hardware can't do.
- **Dense sampling at the control rate:** available at a fine enough time grid (the rate the tracker updates), or as a function the tracker can evaluate at any $t$ (Lesson 7.4).

**What makes a reference un-trackable** (and is therefore Module 7's responsibility to prevent): missing derivatives (position only, no feed-forward), infeasibility (impossible speeds), discontinuities (velocity jumps), or too-coarse sampling. Each is an upstream defect validation (7.2) is meant to catch.

**The boundary (explicit).** Module 7 *produces* $(\mathbf q_d, \dot{\mathbf q}_d, \ddot{\mathbf q}_d)$ — an **open-loop reference**. It does **not**:
- compute the tracking error $\mathbf q_d - \mathbf q_{\text{actual}}$ or any corrective term (**feedback control — Module 8**);
- model forces, torques, inertia, or motor behavior (**dynamics / actuator control — Module 8+**);
- command motors or close any loop.

The reference is the *input* to the controller, produced and validated here; the controller is built in Module 8. The engine exposes the reference via the layer's `reference(t) → (q_d, qd_d, qdd_d, info)` (Lesson 8.3 packages it) — feed-forward only, no error term, no torque.

## 4. Visual Explanation
`[Visual: the Module 7 / Module 8 boundary — M7 produces a reference (q_d, q̇_d, q̈_d, continuous, feasible) which crosses a clean handoff line into M8's tracker (error correction, motors); the handoff line is labeled 'reference in, tracking out']`

**Diagram Specification**

- **Objective:** show the reference as the handoff and draw the bright M7/M8 line.
- **Scene:** **Left (Module 7):** a box "reference $\mathbf q_d(t),\dot{\mathbf q}_d(t),\ddot{\mathbf q}_d(t)$ — continuous, feasible, validated" emitting three small signal curves (position, velocity, acceleration). A bold vertical **handoff line** labeled "reference in →". **Right (Module 8, greyed/dashed):** a box "tracker: error correction + motor commands" marked "(Module 8 — not built here)". An explicit caption: M7 writes the score; M8 plays it.
- **Labels:** "feed-forward $\dot q_d,\ddot q_d$"; "open-loop reference"; "Module 8: feedback, dynamics, actuators — out of scope".
- **Form:** SVG, two boxes split by the handoff line; M7 side solid/teal, M8 side dashed/muted.

## 5. Engineering Example
This separation is exactly how real motion stacks are layered. A **trajectory generator** (Module 7's role) emits the time-stamped reference — position plus velocity/acceleration feed-forward — at the control rate. A separate **servo/tracking controller** (Module 8's role) consumes that reference each cycle, compares it to the measured state, and computes motor commands to follow it, using the feed-forward terms to stay ahead of error. The interface between them is precisely the reference signal. Standard robot frameworks define this handoff explicitly (a "JointTrajectory" of positions/velocities/accelerations with timestamps is consumed by a trajectory-tracking controller). For the harvester, Module 7 produces the validated reach-and-grasp reference; the (Module 8) controller will track it on the real arm. Keeping the layers separate is what lets the same reference run in simulation and on hardware, and what keeps each layer testable on its own.

## 6. Worked Example
Inspect the reference a validated motion provides (canonical scenario; limits $\dot q_{\lim}=2$, $\ddot q_{\lim}=4$).

- At several times $t$, query the reference: it returns $\mathbf q_d(t)$ (a configuration), $\dot{\mathbf q}_d(t)$ (joint speeds), $\ddot{\mathbf q}_d(t)$ (joint accelerations) — three vectors, the complete feed-forward.
- At the endpoints, $\dot{\mathbf q}_d=\ddot{\mathbf q}_d=\mathbf 0$ (starts/ends at rest); in the interior, the speeds peak below $\dot q_{\lim}$ and the accelerations below $\ddot q_{\lim}$ (feasible, validated in 7.2).
- The reference is **continuous** and available at any $t$ (the layer evaluates it), so a tracker could step it at any control rate.
- **What it does not provide:** any tracking error, corrective gain, torque, or motor command — those don't exist in Module 7. The reference is purely the desired motion. The notebook queries the reference at sample times, confirms it returns the three feed-forward vectors, confirms rest at the ends and feasibility within, and confirms there is **no** error/torque field — the boundary holds.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Inspect the handoff.** In the notebook you:

1. Query the reference at several times and confirm it returns desired position, velocity, and acceleration (the feed-forward triple).
2. Confirm the reference is continuous and feasible (rest at the ends, peaks within limits) — i.e. trackable.
3. Confirm the reference carries **no** tracking error, gain, or torque — Module 7 produces the reference only; tracking is Module 8.

## 8. Coding Exercise
*(Snippet / notebook task — uses the reference from `reference_trajectory_layer`, `sample_reference`.)*

In the companion notebook:

1. From a validated layer, query `reference(t)` at several times and assert it returns desired position, velocity, and acceleration of the right shape.
2. Assert the velocity and acceleration feed-forward are **zero at the endpoints** and **within limits** in the interior (trackable prerequisites met).
3. Assert the reference object exposes only the desired motion (position/velocity/acceleration + info) and **no** error/torque/gain field — verifying the Module 7/8 boundary in code.

## 9. Knowledge Check
1. What must a reference provide, at every instant, for a tracker to follow it?
2. What is feed-forward, and why does it help a tracker keep up?
3. State the Module 7 / Module 8 boundary in one sentence.
4. Name two things that would make a reference un-trackable, and whose responsibility it is to prevent them.

## 10. Challenge Problem
A colleague proposes "simplifying" the reference to carry **only** desired position $\mathbf q_d(t)$, dropping the velocity and acceleration feed-forward, on the grounds that a good tracker can figure out the rest. Explain what the tracker loses without feed-forward (think about lag and anticipation), why this pushes work and error onto Module 8, and why Module 7 should provide the full triple. Then state clearly which parts of "making the robot actually follow it" remain Module 8's job regardless. *(The prerequisites exist so the handoff is clean and the tracker's job is well-posed.)*

## 11. Common Mistakes
- **Providing position only.** Without velocity/acceleration feed-forward the tracker lags; provide the full triple.
- **Handing off an infeasible or discontinuous reference.** A tracker can't follow what the hardware can't do or what jumps; validate first (7.2).
- **Doing tracking in Module 7.** Computing error, gains, torques, or motor commands is Module 8 — out of scope here.
- **Blurring the boundary.** The reference is the *input* to the controller; Module 7 produces it, Module 8 consumes it.

## 12. Key Takeaways
- A trajectory exists to be **followed**; the reference must give a tracker, at every instant, the desired **position, velocity, and acceleration** (feed-forward) — continuous, feasible, densely sampled.
- These **prerequisites** define a clean handoff; un-trackable references (missing derivatives, infeasible, discontinuous, too coarse) are upstream defects Module 7 must prevent (validated in 7.2).
- **Module 7 produces the open-loop reference; Module 8 tracks it.** Module 7 does **no** error correction, **no** dynamics, **no** actuator/motor commands.
- The reference is the *input* to the controller — the score, not the performance.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain tracking prerequisites using the 'composer writes a playable score, musician performs it' analogy. Stress that the reference provides position + velocity + acceleration feed-forward, and that Module 7 writes the score while Module 8 performs it. Then ask me what makes a reference un-trackable."
- **Practice (generate exercises):** "Give me four references with one prerequisite missing each (no feed-forward, infeasible, discontinuous, too coarse). Ask me which prerequisite fails and whether it's Module 7's or Module 8's responsibility. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how real motion stacks separate a trajectory generator (emits the reference) from a tracking controller (follows it), and why that interface — the reference signal — is the clean boundary."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain tracking prerequisites for a robot reference trajectory: it must provide desired position, velocity, and acceleration (feed-forward), be continuous, feasible, and densely sampled, and that Module 7 produces the reference while Module 8 tracks it (no feedback/dynamics/actuators in Module 7), at a robotics-course level."
- **Español:** "Explica los prerrequisitos de seguimiento para una trayectoria de referencia de robot: debe proporcionar posición, velocidad y aceleración deseadas (prealimentación), ser continua, factible y muestreada densamente, y que el Módulo 7 produce la referencia mientras el Módulo 8 la sigue (sin realimentación/dinámica/actuadores en el Módulo 7), a nivel de curso de robótica."
- **中文（简体）：** "用机器人课程的水平，解释参考轨迹的跟踪前提：它必须在每一时刻提供期望的位置、速度和加速度（前馈），连续、可行且密集采样；模块7产生参考，模块8进行跟踪（模块7中没有反馈/动力学/执行器）。"
- **Türkçe:** "Bir robot referans yörüngesi için izleme önkoşullarını açıkla: her an istenen konum, hız ve ivmeyi (ileri besleme) sağlamalı, sürekli, uygulanabilir ve yoğun örneklenmiş olmalı; Modül 7 referansı üretir, Modül 8 onu izler (Modül 7'de geri besleme/dinamik/eyleyici yok) — robotik dersi düzeyinde."

---

*Next lesson: 7.4 — Sampling and Representing the Reference: Discretization for Execution (turning the continuous reference into a steppable signal), and the Unit 7 recap.*
