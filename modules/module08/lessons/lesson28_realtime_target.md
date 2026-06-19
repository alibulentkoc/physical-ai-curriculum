---
module: 08
unit: 07
lesson: 7.4
title: "Running the Inner Loop on a Real-Time Target"
core_idea: "The conclusion of Unit 7: the inner control loop belongs on a real-time target — a place (a microcontroller, a real-time thread, dedicated hardware) where its timing is protected, deterministic, and low-jitter, so the rate you designed for is the rate you actually get. The same control logic on a best-effort target (an ordinary thread sharing a general-purpose computer) jitters, overruns, and goes unstable. Meanwhile the outer layers (planning, perception, supervision) run on best-effort compute and tolerate loose timing. This split — real-time inner loop, best-effort outer layers — is the architecture the ROS 2 control stack of Unit 8 will host."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M8 L7.3 — Jitter, overruns, missed deadlines"
  - "M8 L6.4 — A data-flow architecture layered by timing"
learning_objectives:
  - "Describe a real-time target and why the inner loop runs there."
  - "Contrast a real-time target with a best-effort target for the inner loop."
  - "Place the inner loop and outer layers on the right targets (timing split)."
  - "Bridge Unit 7 (real-time) to Unit 8 (the ROS 2 control stack)."
---

# Lesson 7.4 — Running the Inner Loop on a Real-Time Target

> Unit 7 has built to a single architectural decision. The inner control loop has a hard real-time requirement (7.1), runs as a periodic task (7.2), and is destabilised by jitter and missed deadlines (7.3). The conclusion: run it on a **real-time target** — a microcontroller, a real-time thread with a high fixed priority, or dedicated motion-control hardware — where its timing is protected from interference and is therefore deterministic and low-jitter. Put the *same* control logic on a **best-effort target** (an ordinary process sharing a general-purpose computer) and it jitters, overruns, and oscillates. The slower outer layers, by contrast, are happy on best-effort compute. This is the timing split of Lesson 6.4 made concrete — and it is exactly the structure the ROS 2 stack of Unit 8 will host.

---

## 1. Why This Matters
This lesson answers "where does the controller actually run?" — the practical question every robot builder must settle. Getting it wrong is a classic failure: a well-tuned controller put in the wrong place (a normal thread on a busy computer) becomes a jittery, deadline-missing loop and oscillates, and no amount of re-tuning fixes it because the problem is the target, not the gains. Getting it right — a real-time target for the inner loop, best-effort compute for everything slower — is what makes a robot both responsive and capable. It also closes Unit 7 and opens Unit 8: the architecture you settle here is the node/topic stack you'll implement in ROS 2.

## 2. Physical Intuition
A real-time target is a dedicated, undistracted place to do the timing-critical work. Think of an orchestra's conductor versus the stagehands. The conductor must keep time with absolute reliability — every beat, undistracted, because the whole ensemble locks to it; you give the conductor one job and protect it. The stagehands do heavy, important work (moving sets, managing lights) but on loose timing — a few seconds early or late is fine. You would never hand the conductor a set to carry mid-performance; the timing-critical role must stay protected.

The inner control loop is the conductor: it must tick on time, every period, so you give it a target whose only job is to run that loop, free from interruption. The outer layers — planning a path, processing a camera frame, supervising the task — are the stagehands: heavy and important, but tolerant of loose timing, so they run on ordinary best-effort compute. Mixing the two — running the conductor's loop in the same distractible place as the stagehands' work — is exactly what produces the jitter and missed deadlines of 7.3. Keep them apart, on targets matched to their timing needs, and both do their jobs.

## 3. Mathematical Foundations
There is little new math here — the content is architectural, resting on Units 6 and 7. Define two kinds of execution target:

- **Real-time target:** timing is protected and predictable — a microcontroller running only the loop, a real-time OS thread at high fixed priority, or dedicated motion-control hardware. Low jitter, no preemption by lower-priority work, bounded worst case. The inner loop runs here so that the rate it was designed for (7.2) is the rate it actually achieves, with the worst-case timing bounded (7.1).
- **Best-effort target:** an ordinary process/thread on a general-purpose OS, scheduled fairly with everything else. Good average throughput, but it jitters and can be preempted — the hazards of 7.3. The outer layers run here.

The placement rule follows from 6.4's timing split: **latency-critical → real-time target; latency-tolerant → best-effort target.** The inner feedback loop is latency-critical (delay inside it destabilises, 6.3), so it goes on the real-time target. Planning, perception, and supervision are latency-tolerant (they set references at lower rates that the inner loop tracks between updates), so they go on best-effort compute. We keep this **qualitative** — no formal real-time-systems machinery (RTOS scheduling proofs, priority-assignment theorems) beyond the placement principle.

The verified contrast, at fixed control gains:

- the inner loop on a **real-time target** (a deterministic periodic loop): **stable**;
- the **same** inner loop on a **best-effort target** (jitter + occasional missed deadlines): **unstable**;
- a **slow outer layer** (updating its reference infrequently, then holding it) feeding a well-timed inner loop: **stable** (RMS ≈ 0.086) — loose outer timing is tolerated.

Same logic, opposite outcomes depending on the target — the architectural point of the unit.

## 4. Visual Explanation
`[Visual: two boxes. The 'real-time target' box (microcontroller / RT thread) contains the fast inner loop — sensor → controller → actuator — ticking on a tight, even grid, labelled 'protected timing, low jitter → stable'. The 'best-effort target' box (general-purpose computer) contains the slow outer layers — planner, perception, supervisor — running at a loose, uneven cadence, labelled 'loose timing OK'. An arrow from the outer box down to the inner box carries 'reference (q_d, q̇_d, q̈_d), updated slowly'. A red 'WRONG' inset shows the inner loop placed in the best-effort box, jittering and oscillating]`

**Diagram Specification**

- **Objective:** show the inner loop on a protected real-time target and the outer layers on best-effort compute, with the reference flowing down.
- **Scene:** two stacked rounded boxes. **Top — best-effort target** (label "general-purpose computer"): three small boxes "planner", "perception", "supervisor" on a loose, uneven cadence strip; tag "loose timing OK (latency-tolerant)". **Bottom — real-time target** (label "microcontroller / RT thread"): the inner loop "sensor → controller → actuator" on a tight even tick strip; tag "protected, low-jitter timing → stable". A bold arrow from top to bottom labelled "reference $q_d,\dot q_d,\ddot q_d$ (slow updates)". A small red inset, lower right: the inner loop drawn *inside* the best-effort box with a wobbly tick strip and a diverging trace, labelled "WRONG: inner loop on best-effort → jitter → unstable".
- **Labels:** "real-time target", "best-effort target", "inner loop (latency-critical)", "outer layers (latency-tolerant)", "reference (slow)", "WRONG placement".
- **Form:** SVG, two stacked target boxes + a wrong-placement inset. Real-time box teal `#0d9488` with emerald tick strip `#10b981`; best-effort box muted `#64748b` with soft uneven strip `#f1f5f9`; reference arrow ink `#0f172a`; wrong inset red `#e11d48`.

## 5. Engineering Example
The split is standard practice. A self-driving stack runs perception and planning on powerful best-effort computers (GPUs, multicore CPUs) at tens of hertz, while the low-level vehicle controllers run on dedicated real-time microcontrollers at high fixed rates. A manipulator runs its joint servo loops on real-time motion-control hardware or a real-time thread, while motion planning and vision run as ordinary ROS 2 nodes on a Linux box. Drones put the attitude loop on a real-time flight controller and the navigation/mission logic on a companion computer. In each case the engineer's decision is the one this lesson formalises: identify the latency-critical inner loop, give it a protected real-time target, and let the heavy, latency-tolerant work run best-effort — then connect them with a reference flowing from slow to fast.

## 6. Worked Example
Right target vs wrong target.

- **Setup:** identical fixed control gains; the inner loop run on each kind of target, plus a slow outer layer.
- **Real-time target (inner loop):** deterministic periodic timing → **stable**.
- **Best-effort target (inner loop):** the same loop with jitter and occasional missed deadlines → **unstable**.
- **Outer layer (slow updates):** an outer layer that refreshes its reference infrequently, then holds it, feeding a well-timed inner loop → **stable**, RMS ≈ **0.086**.
- **Reading it:** placement decides the outcome. The inner loop must be on the protected target; the outer layer's loose timing is harmless. This is 6.4's timing split realised as a hardware/software placement decision.
- The notebook asserts the real-time inner loop is stable, the best-effort inner loop is unstable, and the slow outer layer is tolerated.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**The placement test.** In the notebook you:

1. Run the inner loop with protected, deterministic timing and confirm it is stable.
2. Run the same inner loop with best-effort timing (jitter + missed deadlines) and confirm it is unstable.
3. Run a slow outer layer feeding a well-timed inner loop and confirm loose outer timing is tolerated.
4. Conclude the placement rule: latency-critical → real-time target; latency-tolerant → best-effort.

## 8. Coding Exercise
*(Companion notebook — uses `track_reference_rt` (deterministic vs jitter+overrun), `track_reference_actuated` with `zoh_reference`, `classify_stability`.)*

In the notebook you:

1. Assert the inner loop is stable on a real-time (deterministic) target.
2. Assert it is unstable on a best-effort (jittery, deadline-missing) target.
3. Assert a slow outer layer feeding a well-timed inner loop is tolerated.
4. State the placement rule and connect it to 6.4.

## 9. Knowledge Check
1. What is a real-time target, and why does the inner loop run there?
2. Contrast a real-time target with a best-effort target.
3. State the placement rule from the timing split (6.4).
4. Why is loose timing acceptable for the outer layers?

## 10. Challenge Problem
You're architecting the compute for a greenhouse-harvesting arm: a joint servo loop, a trajectory planner, a fruit-detection vision system, and a safety supervisor. Assign each to a real-time or best-effort target with a rough rate, and justify each placement using the latency-critical/latency-tolerant distinction (6.4) and the jitter/missed-deadline hazards (7.3). Then explain what goes wrong if the joint loop is placed best-effort, why re-tuning won't save it, and how the reference flows from the slow layers to the fast loop. Finally, preview how Unit 8 hosts all of this as a single ROS 2 node/topic graph while still letting the inner loop run real-time. *(You are producing the compute architecture for the robot and defending every placement.)*

## 11. Common Mistakes
- **Running the inner loop best-effort.** Sharing a general-purpose computer brings jitter and missed deadlines → instability.
- **Re-tuning to fix a placement problem.** The gains aren't the issue; the target is.
- **Demanding real-time everywhere.** The heavy outer work can't run at inner-loop rates and doesn't need to.
- **Confusing 'fast computer' with 'real-time target'.** A fast best-effort computer can still jitter and preempt; predictability is what matters.

## 12. Key Takeaways
- The inner loop runs on a **real-time target** — protected, deterministic, low-jitter timing — so the designed rate is the achieved rate with a bounded worst case.
- The **same loop on a best-effort target** jitters, misses deadlines, and goes unstable; placement, not gains, decides.
- **Placement rule:** latency-critical (inner loop) → real-time target; latency-tolerant (planning, perception, supervision) → best-effort target — Lesson 6.4's timing split realised.
- Verified: real-time inner loop stable, best-effort inner loop unstable, slow outer layer tolerated (RMS ≈ 0.086). This architecture is what the **ROS 2 control stack (Unit 8)** will host.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain the real-time target vs best-effort target using the 'conductor vs stagehands' analogy: the conductor (inner loop) must keep time undistracted on a protected target; the stagehands (outer layers) do heavy work on loose timing. Then state the placement rule."
- **Practice (generate exercises):** "List robot subsystems (joint loop, planner, vision, supervisor) and ask me to place each on a real-time or best-effort target with a rate and a justification. Withhold the answer until I respond."
- **Explore (connect to the real world):** "Describe how a real autonomous system (self-driving car, drone, manipulator) splits compute between real-time controllers and best-effort planning/perception, and ask me to identify which runs where and why."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain why the inner control loop runs on a real-time target (protected, deterministic timing) while outer layers run best-effort, give the placement rule from the timing split, and bridge to the ROS 2 control stack — at a robotics-course level, qualitatively (no formal RTOS scheduling theory)."
- **Español:** "Explica por qué el lazo de control interno se ejecuta en un objetivo de tiempo real (temporización protegida y determinista) mientras las capas externas se ejecutan en best-effort, da la regla de ubicación según la división por temporización, y enlaza con la pila de control de ROS 2 — a nivel de curso de robótica, cualitativamente (sin teoría formal de planificación de RTOS)."
- **中文（简体）：** "解释为什么内部控制回路运行在实时目标上（受保护的、确定性的时序），而外层运行在尽力而为（best-effort）的计算上；给出基于时序分层的放置规则；并桥接到第 8 单元的 ROS 2 控制栈——达到机器人课程水平，定性说明（不涉及形式化 RTOS 调度理论）。"
- **Türkçe:** "İç denetim döngüsünün neden bir gerçek-zamanlı hedefte (korumalı, belirlenimci zamanlama) çalıştığını, dış katmanların ise best-effort çalıştığını açıkla; zamanlama bölünmesinden gelen yerleştirme kuralını ver ve ROS 2 denetim yığınına köprü kur — robotik dersi düzeyinde, niteliksel olarak (resmi RTOS çizelgeleme teorisi yok)."

---

*Next: Lesson 8.1 — The Closed-Loop Control Stack in ROS 2.*
