---
module: 08
unit: 07
lesson: 7.2
title: "The Periodic Control Loop: Running at a Fixed Rate"
core_idea: "An embedded controller does not run continuously — it runs as a periodic task: every control period it senses the state, computes a command, and actuates, then waits for the next period. The control period (and its reciprocal, the control rate) is the loop's heartbeat. Within each period there is a timing budget: sense + compute + actuate must fit. At a well-chosen fixed rate the periodic loop tracks the reference faithfully; the period is how the continuous control law of Units 1–5 is actually executed on real hardware."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M8 L7.1 — What real-time means (deadlines, worst case)"
  - "M8 L6.3 — Control rate and loop delay"
learning_objectives:
  - "Describe the inner loop as a periodic task: sense → compute → actuate, every period."
  - "Define control period and control rate and the within-period timing budget."
  - "Explain the period as the execution of the continuous control law on hardware."
  - "Show that a well-chosen fixed-rate loop tracks the reference."
---

# Lesson 7.2 — The Periodic Control Loop: Running at a Fixed Rate

> A controller on real hardware is not a continuous mathematical function; it is a **periodic task**. A timer fires, the loop reads the sensors, computes the command, sends it to the actuator, and then sleeps until the timer fires again. The interval between firings is the **control period** $T_c$; its reciprocal $1/T_c$ is the **control rate**. This periodic heartbeat is how everything you built in Units 1–5 — the PID law, the feedforward, the actuator command — actually runs. This lesson makes the heartbeat explicit and shows that at a well-chosen fixed rate, the periodic loop tracks the reference just as the continuous picture promised.

---

## 1. Why This Matters
Every line of control logic you've written assumes "now I have the state, now I compute, now I command." On hardware, those steps happen at discrete, evenly spaced moments — once per control period — not continuously. Understanding the loop as periodic is what lets you reason about whether it will work on a real target: how fast it must run, how much computation fits in a period, and how the period relates to the loop delay that Unit 6 showed is dangerous. Without this picture, the control law floats in the abstract; with it, you can put it on a microcontroller and trust it.

This lesson is the constructive heart of Unit 7: 7.1 defined the timing *requirement* (bounded worst case); here we define the *structure* that meets it (a fixed-rate periodic loop) and show it works. The hazards that disturb the structure follow in 7.3, and the target it runs on in 7.4.

## 2. Physical Intuition
Think of a drummer keeping time. Every beat, on the beat, they strike — sense the music, decide, hit — then wait for the next beat. The tempo is fixed; the work for each beat must fit between beats. If the tempo is right and each strike fits its slot, the rhythm is steady and the music holds together. The drummer doesn't play continuously; they play *periodically*, and the regularity is what makes it work.

The control loop is the drummer of the robot. Each control period it strikes once: read the joint, compute the command, drive the actuator. The control rate is the tempo. A fast tempo (high rate) means fresh corrections and tight tracking, but each beat's work must still fit the shorter slot. A slow tempo (low rate) gives the work more room but stales the corrections — and Unit 6 showed too slow destabilises. The art is choosing a tempo that is fast enough for tight, stable control and slow enough that the per-period work reliably fits. Then the loop, like a steady drummer, holds the trajectory.

## 3. Mathematical Foundations
The inner loop is a **periodic task** executing, every period $T_c$, the steps:

1. **Sense** — read the measured state $(q, \dot q)$.
2. **Compute** — evaluate the control law: feedforward (from the M7 reference sample) + PID feedback → requested command; pass it through the actuator → delivered effort (Unit 5).
3. **Actuate** — send the delivered command to the actuator.

then sleep until the next period. The **control rate** is $f_c = 1/T_c$ (e.g., $T_c = 1\text{ ms} \Rightarrow f_c = 1\text{ kHz}$). Within each period there is a **timing budget**: the sum of sense + compute + actuate times must be $\le T_c$ (the worst-case version of this is the real-time requirement of 7.1).

Conceptually, the periodic loop is how the continuous control law is *executed*: instead of acting at every instant, the controller acts at the sample instants $t = 0, T_c, 2T_c, \dots$ and holds its command between them. We keep this **qualitative** — "run the same control law every period, holding the command in between" — and deliberately do **not** invoke discrete-time/sampling theory (the $z$-transform, difference equations, sampled-data stability), which is the formal tool for analysing sampled control and is out of scope. The intuition from Unit 6 suffices: a high enough rate makes the held-between-samples staleness negligible, so the periodic loop behaves like the continuous one; too low a rate adds destabilising delay.

The verified result: a periodic loop running a feedforward + PID control law at a good fixed rate (a control period of 10 simulation steps) tracks a moving Module 7 reference (a quintic move) to a tiny RMS error and remains stable — the discrete, periodic execution reproduces the continuous design. The loop made one update per period across the move, exactly as a fixed-rate task should.

## 4. Visual Explanation
`[Visual: a timeline divided into equal control periods; in each period a small three-segment bar shows sense → compute → actuate fitting within the period, then an idle gap until the next period; above, the held command is drawn as a stair-step (zero-order hold) that, at a high rate, hugs the smooth continuous command; a label marks the control period T_c and the rate 1/T_c, and a note shows the per-period timing budget sense+compute+actuate ≤ T_c]`

**Diagram Specification**

- **Objective:** show the loop as a periodic sense→compute→actuate task at a fixed rate, with the held command approximating the continuous one.
- **Scene:** a horizontal timeline split into equal periods by tick marks (label one span "$T_c$ — control period", and "$1/T_c$ — control rate"). In each period, a small three-segment bar **sense | compute | actuate** sits at the start, followed by an idle gap; annotate one period "sense + compute + actuate ≤ $T_c$ (timing budget)". Above the timeline, two curves: a smooth continuous command (faint) and the periodic **held** command drawn as a stair-step that closely tracks it; caption "high rate → held command ≈ continuous".
- **Labels:** "control period $T_c$", "control rate $1/T_c$", "sense", "compute", "actuate", "timing budget", "held command (zero-order hold)".
- **Form:** SVG, a period-tick timeline with per-period task bars + a stair-step-vs-smooth command plot. Period ticks muted `#64748b`, sense/compute/actuate segments sky `#0ea5e9`/teal `#0d9488`/emerald `#10b981`, continuous command faint ink, held stair amber `#d97706`.

## 5. Engineering Example
Fixed-rate periodic loops are the universal structure of embedded control. A motor servo loop runs at a fixed rate (often 1–20 kHz) set by a hardware timer; every tick it reads the encoder, runs the controller, and updates the drive. Flight controllers run their inner attitude loop at a fixed high rate, with the outer loops at slower fixed rates. PLCs in industrial automation execute on a fixed "scan cycle." In all of them the same discipline holds: pick the rate from the dynamics and the per-period budget, then run sense→compute→actuate every period, holding the command between updates. The rate is chosen high enough that the held-command staleness is negligible for the loop's dynamics and low enough that the work reliably fits — exactly the trade this lesson frames.

## 6. Worked Example
A periodic loop tracking a move.

- **Setup:** a feedforward + PID control law for a joint under load, run as a periodic task with a control period of 10 simulation steps, tracking a Module 7 quintic reference (0 → 1.2 rad over 2 s).
- **Result:** the loop is stable and tracks to RMS ≈ **0.0007** — essentially perfect — making one control update per period across the move.
- **Reading it:** the discrete, fixed-rate execution of the control law reproduces the continuous design's tracking. The period is fast enough that holding the command between updates costs almost nothing; the loop behaves like the continuous controller you designed in Units 1–5.
- The notebook asserts the periodic loop is stable, tracks with small RMS, and ran as a periodic task (one update per period).

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**The periodic-loop test.** In the notebook you:

1. Run the control law as a periodic task at a good fixed rate and confirm it tracks the reference.
2. Note the number of updates (one per period) — the loop's heartbeat.
3. Recall from Unit 6 that lowering the rate too far adds delay and destabilises — the rate is a design choice bounded below by stability and above by the per-period budget.

## 8. Coding Exercise
*(Companion notebook — uses `track_reference_rt(..., period_steps=...)`, `quintic_reference`, `classify_stability`.)*

In the notebook you:

1. Run a feedforward + PID control law as a periodic loop at a sensible control period and assert it tracks a moving reference with small RMS.
2. Confirm it executed as a periodic task (one update per period).
3. Connect to Unit 6: reason about how far you could lower the rate before the loop delay destabilises it.

## 9. Knowledge Check
1. What three steps does the periodic loop perform each period?
2. Define control period and control rate, and give the relationship between them.
3. What is the per-period timing budget?
4. In what sense is the period the execution of the continuous control law?

## 10. Challenge Problem
You're choosing a control rate for a joint loop. Explain the two opposing pressures — Unit 6's "too slow destabilises" (a lower bound on the rate) and 7.1/7.2's per-period timing budget (an upper bound on the rate, since faster means less time to finish the work) — and describe how you'd pick a rate between them. Then explain why simply maximising the rate is naive (what happens to the budget and the worst case?), and how the held-command (zero-order-hold) picture justifies treating a high-rate periodic loop as equivalent to the continuous controller you designed. Note explicitly which formal tool would quantify the sampled loop and why it's out of scope here. *(You are turning the rate into a reasoned design choice bounded on both sides.)*

## 11. Common Mistakes
- **Imagining the controller runs continuously.** On hardware it runs once per period and holds the command between.
- **Maximising the rate blindly.** Faster shrinks the per-period budget and stresses the worst case (7.1).
- **Setting the rate too low.** Below a threshold the loop delay destabilises (Unit 6).
- **Reaching for sampled-data theory.** The qualitative "run every period, hold between" picture is the lesson; the $z$-transform is a later course.

## 12. Key Takeaways
- The inner loop is a **periodic task**: every control period $T_c$ it does **sense → compute → actuate**, then waits.
- The **control rate** is $f_c = 1/T_c$; each period has a **timing budget** (sense + compute + actuate ≤ $T_c$).
- The period is how the **continuous control law is executed** on hardware — act at the sample instants, hold the command between; a high enough rate makes this ≈ the continuous controller.
- Verified: a periodic feedforward + PID loop at a good rate tracks a Module 7 reference to RMS ≈ 0.0007. The rate is bounded below by stability (Unit 6) and above by the per-period budget (7.1). Sampled-data formalism is out of scope.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain the periodic control loop using the 'drummer keeping time' analogy: each beat (period) the loop senses, decides, and strikes, then waits; the tempo is the control rate, and each beat's work must fit between beats. Then explain control period vs rate and the per-period budget."
- **Practice (generate exercises):** "Give me a control period and a per-period workload and ask me whether the loop fits its budget, and whether the rate is high enough to avoid the Unit-6 instability. Withhold the answer until I respond."
- **Explore (connect to the real world):** "Give real fixed-rate loops (a 1 kHz servo loop, a flight controller's inner loop, a PLC scan cycle) and ask me to identify the period, rate, and the sense→compute→actuate steps in each."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain the inner control loop as a periodic task (sense → compute → actuate each control period), define control period and rate and the per-period timing budget, and explain the period as the execution of the continuous control law (held between samples) — at a robotics-course level, qualitatively (no discrete-time/sampling theory, no z-transform)."
- **Español:** "Explica el lazo de control interno como una tarea periódica (sentir → calcular → actuar en cada periodo de control), define el periodo y la tasa de control y el presupuesto de tiempo por periodo, y explica el periodo como la ejecución de la ley de control continua (mantenida entre muestras) — a nivel de curso de robótica, cualitativamente (sin teoría de tiempo discreto/muestreo, sin transformada z)."
- **中文（简体）：** "把内部控制回路解释为一个周期任务（每个控制周期：感知 → 计算 → 执行），定义控制周期与控制频率以及每周期的时间预算，并把'周期'解释为连续控制律的执行（在采样之间保持指令）——达到机器人课程水平，定性说明（不涉及离散时间/采样理论，不涉及 z 变换）。"
- **Türkçe:** "İç denetim döngüsünü periyodik bir görev olarak açıkla (her denetim periyodunda algıla → hesapla → uygula), denetim periyodu ile hızını ve periyot başına zaman bütçesini tanımla ve periyodu sürekli denetim yasasının yürütülmesi olarak açıkla (örnekler arasında komut tutulur) — robotik dersi düzeyinde, niteliksel olarak (ayrık-zaman/örnekleme teorisi yok, z-dönüşümü yok)."

---

*Next: Lesson 7.3 — Jitter, Overruns, and Missed Deadlines.*
