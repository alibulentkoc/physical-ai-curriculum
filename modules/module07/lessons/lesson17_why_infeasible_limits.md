---
module: 07
unit: 05
lesson: 5.1
title: "Why a Trajectory Can Be Infeasible: Velocity and Acceleration Limits"
core_idea: "A geometrically valid trajectory can still be impossible to execute: every motor has a top speed and a top acceleration, and a trajectory that demands more than the hardware can deliver is infeasible. Feasibility is a physical limit check, separate from smoothness and from reaching the goal."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L2.3 — Cubic vs quintic time scaling"
  - "M7 L3.2 — Synchronizing joints (peak speed scales with displacement)"
learning_objectives:
  - "Explain why a smooth, goal-reaching trajectory can still be physically infeasible."
  - "Identify velocity and acceleration limits as the hardware constraints feasibility must respect."
  - "Use the Limit Explorer to see a trajectory's peaks cross the limit lines as the duration shrinks."
---

# Lesson 5.1 — Why a Trajectory Can Be Infeasible: Velocity and Acceleration Limits

> Units 1–4 built trajectories that are smooth and reach the goal. This unit asks a blunt physical question the math hasn't yet: *can the robot actually do it?* A motor has a top speed and a top acceleration. Ask for more and the motion is **infeasible** — no matter how pretty the curve. We lead by *watching* a trajectory's peaks cross the limit lines.

---

## 1. Why This Matters
A trajectory can be perfectly smooth ($C^2$), reach exactly the right goal, and still be **impossible** — because the hardware can't move that fast or change speed that quickly. Every joint motor has a **maximum velocity** (it physically can't spin faster) and a **maximum acceleration** (limited by available torque, which we treat here only as a number, not as dynamics). A trajectory that commands a joint past either limit will not be tracked: the motor saturates, the arm lags the plan, and the carefully designed smooth motion falls apart — or the controller rejects the command outright.

So feasibility is a **third, independent question**, alongside "is it smooth?" and "does it reach the goal?" This lesson makes that question concrete and *visible*: the flagship Limit Explorer shows a trajectory's peak speed and peak acceleration as horizontal bars against the limit lines, and lets you shrink the duration until they cross — the moment the motion becomes infeasible. Understanding *why* a trajectory can be impossible, before any fix, is the foundation of the whole unit.

## 2. Physical Intuition
You can plan to walk across a room in half a second. The *plan* is fine — start here, end there, smooth. But your legs have a top speed; below some duration, the plan demands a sprint you physically cannot perform. The plan didn't become "wrong"; it became **infeasible** — it asks for motion the body can't deliver. Give yourself more time and it's easy again.

Robot joints are the same. A move from one angle to another over a duration $T$ implies a peak speed and a peak acceleration. Squeeze $T$ smaller and those peaks grow — eventually past what the motor can do. The trajectory's *shape* (the smooth quintic) never changed; only the *timing* pushed it past the hardware. Feasibility is about whether the demanded peaks fit under the hardware ceilings. When they don't, the robot simply can't follow the plan — the first thing to *see* is exactly that overshoot of the limit line.

## 3. Mathematical Foundations
Take a synchronized rest-to-rest move (Unit 3) with displacement $\Delta q_i$ per joint over a common duration $T$, timed by a quintic. From the quintic's shape, each joint's **peak speed** and **peak acceleration** are

$$\dot q_{i,\max} = \frac{15}{8}\,\frac{|\Delta q_i|}{T},\qquad
  \ddot q_{i,\max} = \frac{10}{\sqrt 3}\,\frac{|\Delta q_i|}{T^2}.$$

The hardware imposes ceilings $\dot q_{\lim}$ and $\ddot q_{\lim}$. The trajectory is **feasible** iff **every** joint satisfies both:

$$\dot q_{i,\max} \le \dot q_{\lim} \quad\text{and}\quad \ddot q_{i,\max} \le \ddot q_{\lim}\quad\text{for all } i.$$

Two things to read off these formulas. First, peaks scale with **displacement** — the largest-$\Delta q$ joint is the first to violate a limit (the bottleneck again). Second, and crucially, peaks scale **inversely with the duration**: velocity as $1/T$, acceleration as $1/T^2$. So shrinking $T$ inflates the peaks (acceleration faster than velocity), and a short-enough duration *always* breaks feasibility. That $1/T$, $1/T^2$ dependence is the lever the next lesson pulls to *fix* infeasibility.

Note what feasibility is **not**: it is not smoothness (a $C^2$ quintic can still be infeasible) and not reachability (the goal can be perfectly reachable yet the *timing* impossible). It is its own check. (We treat $\dot q_{\lim}$ and $\ddot q_{\lim}$ as given hardware numbers; deriving the acceleration limit from torques/inertia is **dynamics — Module 8**, deliberately out of scope here.)

The engine computes the peaks with `quintic_peaks(dq, T)` and tests a move with `is_feasible(q0, qf, T, vlim, alim)`.

## 4. Visual Explanation
`[Visual: a trajectory's peak-speed and peak-acceleration bars against horizontal limit lines, shown at a long T (both under) and a short T (both over → infeasible)]`

**Diagram Specification**

- **Objective:** show feasibility as peaks fitting under limit lines, and infeasibility as peaks crossing them when $T$ shrinks.
- **Scene:** two panels. **Left (feasible, long $T$):** two bars — peak speed and peak acceleration — both **below** their dashed limit lines (green). **Right (infeasible, short $T$):** the same bars, now **above** the limit lines (red), with the acceleration bar overshooting more (it grows as $1/T^2$). Small captions give the $1/T$ and $1/T^2$ scaling.
- **Labels:** "$\dot q_{\lim}$", "$\ddot q_{\lim}$" on the limit lines; "feasible" / "infeasible"; "shrink T → peaks grow".
- **Form:** SVG, 2 panels of bars + limit lines. Under-limit emerald `#10b981`, over-limit error `#b91c1c`, limit lines muted dashed.

**Interactive demo (this lesson's flagship):** *Velocity & Acceleration Limit Explorer* — drag the duration $T$ and the displacement, and watch the peak-speed and peak-acceleration readouts move against the limit lines; the panel turns red the instant either peak crosses its limit, and reports which limit (velocity or acceleration) bound first. (Embedded from `modules/module07/demos/lesson17_limit_explorer.html`.)

## 5. Engineering Example
This is exactly the "speed/accel override" and "trajectory not executable" behavior on real robot controllers. When an operator dials a motion too fast, the controller either clamps the commanded speed to the joint limits (silently slowing the move) or flags the program as infeasible. CNC and pick-and-place tuning is largely a feasibility dance: push the cycle time down until a joint saturates, then back off. The harvester is no different — a tempting "snap to the fruit in 0.2 s" plan demands wrist speeds and accelerations the small distal motor can't produce, so the controller would either refuse it or fail to track it, smearing the approach. Recognizing the infeasibility *before* running the move is what this unit teaches.

## 6. Worked Example
A joint must move $\Delta q = 1.2$ rad with limits $\dot q_{\lim}=1.0$ rad/s and $\ddot q_{\lim}=2.0$ rad/s², using a quintic. Check $T=1.5$ s and $T=0.8$ s.

**At $T=1.5$ s:** peak speed $=\tfrac{15}{8}\cdot\tfrac{1.2}{1.5}=1.5$ rad/s — **over** the $1.0$ limit ✗. Peak accel $=\tfrac{10}{\sqrt3}\cdot\tfrac{1.2}{1.5^2}=3.08$ rad/s² — **over** the $2.0$ limit ✗. Infeasible (both bind).

**At $T=0.8$ s:** peaks are larger still ($\dot q_{\max}=2.81$, $\ddot q_{\max}=10.8$) — even more infeasible. Shrinking $T$ made it worse, as expected.

So this move is infeasible at these durations — neither is impossible to *plan*, both are impossible to *execute*. The fix (next lesson) is to go the other way: **lengthen** $T$. The minimum feasible $T$ here turns out to be $2.25$ s (set by acceleration); the notebook finds it and confirms the peaks then sit exactly at the limits.

## 7. Interactive Demonstration
**Use the Limit Explorer (this lesson's demo).** Steps:

1. Start at a long $T$: both bars sit comfortably under the limit lines (green, feasible).
2. Drag $T$ smaller. Watch the **acceleration** bar rise faster than the velocity bar (it grows as $1/T^2$). Note the $T$ at which each first crosses its limit.
3. Increase the displacement: both bars jump up (peaks scale with $\Delta q$) — the larger the move, the longer the minimum feasible time.
4. Keyboard: the duration and displacement sliders are focusable; arrow keys adjust them, and the readout announces "feasible / infeasible" and which limit bound.

The thing to internalize: *the same smooth trajectory is feasible or not purely depending on the timing versus the hardware ceilings.*

## 8. Coding Exercise
*(Snippet / notebook task — uses `quintic_peaks`, `is_feasible`.)*

In the companion notebook:

1. For a rest-to-rest move, compute peak speed and peak acceleration over a range of durations and plot them against the limit lines.
2. Assert that the move is **infeasible** at a short $T$ and **feasible** at a long $T$ (`is_feasible` flips), and identify which limit (velocity or acceleration) is the first to bind as $T$ grows.
3. Confirm numerically that peak speed scales as $1/T$ and peak acceleration as $1/T^2$ (e.g. doubling $T$ halves the speed peak and quarters the acceleration peak).

## 9. Knowledge Check
1. Name the two hardware limits feasibility must respect, and say what each caps.
2. Can a smooth, goal-reaching trajectory be infeasible? Explain.
3. How do peak speed and peak acceleration scale with the duration $T$?
4. Which joint is the first to violate a limit, and why?

## 10. Challenge Problem
A two-joint move has $\Delta q = (1.5, 0.3)$ rad with $\dot q_{\lim}=2$ rad/s and $\ddot q_{\lim}=3$ rad/s². For joint 1, find the minimum duration set by the velocity limit and the minimum set by the acceleration limit, and say which one binds. Then explain why, as the move gets *longer*, the binding constraint can switch from acceleration to velocity (consider how each minimum-duration scales with $\Delta q$). *(This is the foundation of the fastest-feasible timing in Lesson 5.3.)*

## 11. Common Mistakes
- **Confusing feasibility with smoothness.** A $C^2$ quintic can still demand impossible speeds; check the peaks against the limits.
- **Confusing feasibility with reachability.** The goal can be reachable while the *timing* is infeasible — they're separate checks.
- **Forgetting acceleration grows as $1/T^2$.** Acceleration usually binds before velocity at short durations; check both.
- **Treating the acceleration limit as dynamics.** Here it's a given number; deriving it from torque/inertia is Module 8.

## 12. Key Takeaways
- **Feasibility** is a third, independent question: a trajectory can be smooth and reach the goal yet be **impossible** for the hardware.
- The constraints are **velocity** and **acceleration** limits — hardware ceilings every joint must stay under.
- Peaks scale with **displacement** (largest-$\Delta q$ joint binds first) and **inversely with duration**: $\dot q_{\max}\propto 1/T$, $\ddot q_{\max}\propto 1/T^2$.
- Shrinking the duration always eventually breaks feasibility — which is exactly the lever (lengthening $T$) that the next lesson uses to fix it.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain why a smooth, goal-reaching trajectory can still be infeasible, using the 'plan to cross the room in half a second' analogy. Stress velocity vs acceleration limits and the 1/T, 1/T² scaling. Then give me a feasibility check to compute."
- **Practice (generate exercises):** "Give me three rest-to-rest moves (displacement, duration, velocity and acceleration limits). Ask me to compute the peaks and decide feasibility, naming which limit binds. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how real robot controllers handle a too-fast motion command (clamping vs rejecting), and where feasibility tuning shows up in CNC, pick-and-place, or 3D printing."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain trajectory feasibility for a robot: why a smooth, goal-reaching motion can still be infeasible, the velocity and acceleration limits, and how peaks scale with duration (1/T and 1/T²), at a robotics-course level (no dynamics)."
- **Español:** "Explica la factibilidad de una trayectoria para un robot: por qué un movimiento suave que alcanza la meta puede aun así ser infactible, los límites de velocidad y aceleración, y cómo los picos escalan con la duración (1/T y 1/T²), a nivel de curso de robótica (sin dinámica)."
- **中文（简体）：** "用机器人课程的水平，解释轨迹可行性：为何一条平滑且能到达目标的运动仍可能不可行，速度与加速度限制，以及峰值如何随时长缩放（1/T 与 1/T²）（不涉及动力学）。"
- **Türkçe:** "Bir robot için yörünge uygulanabilirliğini açıkla: pürüzsüz ve hedefe ulaşan bir hareketin neden yine de uygulanamaz olabileceğini, hız ve ivme limitlerini ve tepe değerlerin süreyle nasıl ölçeklendiğini (1/T ve 1/T²) robotik dersi düzeyinde anlat (dinamik yok)."

---

*Next lesson: 5.2 — Slowing Down to Restore Feasibility: Uniform Time Scaling (the simplest fix — give the motion more time).*
