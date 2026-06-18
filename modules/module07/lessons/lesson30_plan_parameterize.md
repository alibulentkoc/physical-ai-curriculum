---
module: 07
unit: 08
lesson: 8.2
title: "Plan and Parameterize: From Task to Timed Trajectory"
core_idea: "The first half of the workflow turns a task into a timed trajectory in two decoupled steps: PLAN a collision-free geometric path (RRT + smoothing), then PARAMETERIZE it by assigning a time scaling that respects velocity and acceleration limits. Plan answers 'what route?'; parameterize answers 'how fast along it?' — kept separate by design."
estimated_time: "45 min"
difficulty: "Advanced"
prerequisites:
  - "M7 L6.4 — Safe path to feasible trajectory (smoothing + time scaling)"
  - "M7 L5.3 — Fastest feasible timing"
learning_objectives:
  - "Execute the PLAN stage: a collision-free, smoothed path from start to goal."
  - "Execute the PARAMETERIZE stage: assign timing that respects velocity/acceleration limits."
  - "Explain why planning and parameterization are decoupled (plan-then-time)."
---

# Lesson 8.2 — Plan and Parameterize: From Task to Timed Trajectory

> The capstone workflow's first half takes a *task* and produces a *timed trajectory*. It does this in two clean steps: **PLAN** the geometric route (what path?), then **PARAMETERIZE** it with timing (how fast along it?). The two are deliberately separate — plan the shape, then assign the clock. We lead by watching a route appear, then a velocity profile laid onto it.

---

## 1. Why This Matters
Half of motion planning is deciding *where* to go; the other half is deciding *how fast* to go there. The capstone keeps these as two distinct stages — **PLAN** and **PARAMETERIZE** — and the separation is a design choice that pays off everywhere. Planning a collision-free *path* (a pure geometry problem) is hard enough on its own; mixing in timing and limits at the same time (planning velocities and accelerations jointly) is the much harder *kinodynamic* problem, which Module 7 deliberately avoids. By **planning first, then timing** (plan-then-time), each step stays simple, well-understood, and reusable: the planner only worries about avoiding obstacles, and the parameterizer only worries about respecting limits along the fixed route.

This lesson is the first half of the workflow in depth. PLAN uses Unit 6 (RRT + smoothing) to produce a short, collision-free path. PARAMETERIZE uses Units 2–5 (polynomial/spline timing + time scaling to the limits) to turn that path into a trajectory with feed-forward velocity and acceleration. The output is a *timed trajectory* ready for validation (next lesson). For the harvester, this is "find a clear route around the canopy, then time it so the wrist motor isn't overdriven" — two questions, answered in order.

## 2. Physical Intuition
Plan a road trip in two steps. First, with a map, you trace the **route** — which roads, which turns, avoiding the closed bridge. You're not thinking about speed yet, just the path on the map. Second, you decide the **schedule** — how fast to drive each segment, where the speed limits are, when to slow for the winding part. The route came first and stands on its own; the schedule is layered onto it afterward. You'd never try to figure out the exact speed for every meter *while* also discovering the route — you'd lose track of both. Separating them keeps each manageable.

Robot motion is the same. PLAN traces the route through configuration space, avoiding the C-obstacles — pure geometry, no clocks. PARAMETERIZE then lays a timing onto that fixed route: assign how the robot moves along the path over time so that no joint exceeds its speed or acceleration limit. Route first, schedule second. The harvester first finds a clear path around the fruit cluster, then decides the gentle timing to traverse it — and because the route is already fixed, timing it is just the feasibility/time-scaling work of Unit 5.

## 3. Mathematical Foundations
**PLAN (geometry).** Given start $\mathbf q_{\text{start}}$ and goal $\mathbf q_{\text{goal}}$ (from the task, via IK of the tool poses) and the obstacle, produce a collision-free path:

1. **RRT** (6.3) finds a raw collision-free path $\mathbf q^{(0)},\dots,\mathbf q^{(M)}$ in $\mathcal C_{\text{free}}$.
2. **Shortcut smoothing** (6.4) shortens it to a few waypoints $\mathbf w_0,\dots,\mathbf w_m$, still collision-free.

The output is **pure geometry** — an ordered list of configurations, no timing. (If smoothing fits a spline, re-collision-check it, Lesson 6.4.)

**PARAMETERIZE (timing).** Lay a time scaling onto the fixed path so the motion is feasible:

3. **Time each segment.** For each waypoint pair $\mathbf w_k\to\mathbf w_{k+1}$, choose a duration $T_k$ at least the **minimum feasible duration** (5.3): $T_k \ge$ `feasible_duration`$(\mathbf w_k,\mathbf w_{k+1},\dot q_{\lim},\ddot q_{\lim})$, so the segment's peak speed/acceleration fit the limits.
4. **Build the trajectory.** Join the segments with a polynomial/spline time scaling (Units 2–3) — here rest-to-rest quintics per segment (C², feed-forward $\dot{\mathbf q},\ddot{\mathbf q}$ available), giving $\mathbf q(t)$ over $[0,\sum_k T_k]$.

The output is a **timed trajectory**: $\mathbf q(t)$ with $\dot{\mathbf q}(t),\ddot{\mathbf q}(t)$, feasible by construction (each segment timed to its limit). Faster variants use the fastest-feasible (trapezoidal) timing (5.3); smoother variants blend across waypoints (3.4) — the quality trade of Lesson 7.1.

**Why decoupled (plan-then-time).** Planning the path and timing it **separately** keeps each tractable: the planner solves a geometry problem (no derivatives, no limits), the parameterizer solves a timing problem on a fixed curve (closed-form per segment). Planning them **together** — choosing path *and* velocities/accelerations jointly under coupled constraints — is **kinodynamic planning**, which is harder and **out of Module 7's scope** by design. The decoupling is also why time scaling can fix a too-fast trajectory without re-planning (5.2): the path is already fixed and valid.

The engine fuses both steps in `plan_parameterize(q_start, q_goal, center, radius, vlim, alim, rng)` → `(waypoints, seg_T, ref_fn, T_total)` — PLAN (`rrt` + `shortcut_smooth`) then PARAMETERIZE (`feasible_duration` per segment + `piecewise_quintic`).

## 4. Visual Explanation
`[Visual: two-step first half — PLAN (a collision-free smoothed path around the C-obstacle, no timing) then PARAMETERIZE (the same path with a velocity profile / timing assigned, peaks under the limit lines)]`

**Diagram Specification**

- **Objective:** show PLAN producing geometry and PARAMETERIZE laying timing onto it, decoupled.
- **Scene:** **Left (PLAN):** C-space with the C-obstacle and a smoothed collision-free path (waypoints joined by straight segments), captioned "geometry only — no clock". **Right (PARAMETERIZE):** the same path with a small velocity-vs-time profile beside it (peaks under the dashed limit line) and per-segment durations $T_k$ annotated, captioned "timing laid onto the fixed route". An arrow "plan-then-time" between them.
- **Labels:** "PLAN: route (Unit 6)", "PARAMETERIZE: schedule (Units 2–5)", "$T_k \ge$ min feasible", limit line.
- **Form:** SVG, two panels. Path emerald `#10b981`, obstacle error-tint, velocity profile teal, limit dashed.

## 5. Engineering Example
The plan-then-time split is the standard structure of manipulation pipelines. A sampling-based **planner** returns a geometric path; a separate **time-parameterization** module retimes that path to the robot's velocity and acceleration limits (often with the time-optimal-under-limits timing of Lesson 5.3). They're separate modules with a clean interface (the path), which is why you can swap planners or retimers independently and why the same path can be retimed for a faster or gentler run without replanning. Kinodynamic planners that fuse the two exist but are heavier and reserved for cases that truly need them — most manipulation, including the harvester's reach-and-grasp, uses plan-then-time because it's simpler and modular. For the harvester: plan a clear route around the cluster once, then retime it per task (fast empty reposition vs gentle loaded grasp).

## 6. Worked Example
PLAN and PARAMETERIZE a greenhouse reach (disk at $(0.5,0.05)$, $r=0.06$; start tool $(0.45,0.25)$ → goal $(0.45,-0.25)$; limits $\dot q_{\lim}=2$, $\ddot q_{\lim}=4$).

- **PLAN:** RRT finds a collision-free path around the disk (direct route blocked); smoothing reduces it to ~3 waypoints (start, a detour configuration, goal), C-space length dropping (e.g. 3.3 → ~2.2), still collision-free.
- **PARAMETERIZE:** for each of the two segments, compute the minimum feasible duration from the limits; the binding joint sets each $T_k$. Build rest-to-rest quintics per segment → a timed trajectory $\mathbf q(t)$ with continuous $\dot{\mathbf q},\ddot{\mathbf q}$, total duration $\approx2.35$ s, peaks at/under the limits.
- **Result:** a feasible-by-construction timed trajectory, ready for validation. Change the priority to "faster" and re-time with a trapezoid (shorter duration, more jerk) — same path, different schedule, the quality trade of 7.1. The notebook runs `plan_parameterize`, prints the waypoints and per-segment durations, and confirms each segment is within limits.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook; also the first two stages of the Trajectory Studio.)*

**Route, then schedule.** In the notebook you:

1. Run PLAN: `rrt` + `shortcut_smooth` → a short collision-free path; confirm it's collision-free and the direct route was blocked.
2. Run PARAMETERIZE: time each segment to its minimum feasible duration and build the trajectory; confirm peaks are within limits.
3. Re-parameterize the **same** path with a faster timing and observe only the schedule changes (the route is untouched) — the decoupling in action.

## 8. Coding Exercise
*(Snippet / notebook task — uses `plan_parameterize`, `feasible_duration`, `path_collision_free`.)*

In the companion notebook:

1. Run `plan_parameterize(...)` and assert PLAN produced a **collision-free** smoothed path (waypoints) and PARAMETERIZE produced per-segment durations each $\ge$ `feasible_duration`.
2. Assert the resulting timed trajectory is **within limits** on every segment (peak speed/accel under the limits).
3. Re-parameterize the same waypoints with longer durations and assert the **path is unchanged** while the peaks shrink — demonstrating plan-then-time decoupling.

## 9. Knowledge Check
1. What does PLAN produce, and what does PARAMETERIZE produce?
2. Which earlier-unit tools implement each step?
3. Why are planning and parameterization kept separate (plan-then-time)?
4. What is the harder alternative that fuses them, and is it in scope?

## 10. Challenge Problem
You've planned a clear path and now must parameterize it for two scenarios: a delicate loaded grasp (minimize jerk) and a fast empty reposition (minimize duration). Describe how the *same* planned path is timed differently for each (which timing profile, what changes in duration and jerk), and confirm both remain feasible. Then explain why, if PARAMETERIZE can't make the path feasible by any timing, the problem must be sent back to PLAN — i.e. what kind of infeasibility timing cannot fix (recall Lesson 5.4). *(The decoupling defines which stage owns which failure.)*

## 11. Common Mistakes
- **Mixing timing into planning.** Plan the geometry first; assign timing after — don't solve the kinodynamic problem unless you must.
- **Timing below the minimum feasible duration.** Each segment's $T_k$ must be at least `feasible_duration`, or the trajectory is infeasible.
- **Re-planning to fix a too-fast trajectory.** That's a timing problem — re-parameterize (slow down), don't re-plan.
- **Forgetting to re-check a smoothing spline.** If PARAMETERIZE blends across waypoints with a spline, re-collision-check the curve (6.4).

## 12. Key Takeaways
- The workflow's first half is two decoupled steps: **PLAN** a collision-free geometric path (RRT + smoothing) → **PARAMETERIZE** it with a limit-respecting timing (time scaling + polynomial/spline).
- PLAN answers **"what route?"** (geometry, no clock); PARAMETERIZE answers **"how fast along it?"** (timing on the fixed route).
- **Plan-then-time** keeps each step tractable and reusable; fusing them is **kinodynamic planning**, out of Module 7's scope.
- The output is a **feasible-by-construction timed trajectory**, ready for validation — and the same path can be re-timed for different quality priorities without replanning.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain Plan and Parameterize using the 'road trip: trace the route, then schedule the speeds' analogy. Stress plan-then-time decoupling and that PARAMETERIZE times the fixed route to the limits. Then ask me what each step produces."
- **Practice (generate exercises):** "Give me a planned path and limits, plus two priorities (gentle vs fast). Ask me to parameterize the same path for each and confirm feasibility. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how manipulation pipelines separate the planner from time-parameterization, why that modularity helps, and when kinodynamic (fused) planning is actually needed."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain the Plan and Parameterize stages for a robot motion: PLAN a collision-free smoothed path (RRT + smoothing), then PARAMETERIZE it with a timing that respects velocity/acceleration limits, kept decoupled (plan-then-time, not kinodynamic), at a robotics-course level."
- **Español:** "Explica las etapas Planificar y Parametrizar de un movimiento robótico: PLANIFICAR un camino suavizado libre de colisiones (RRT + suavizado), luego PARAMETRIZARLO con una temporización que respete los límites de velocidad/aceleración, manteniéndolas desacopladas (planificar-luego-temporizar, no kinodinámico), a nivel de curso de robótica."
- **中文（简体）：** "用机器人课程的水平，解释机器人运动的'规划'与'参数化'阶段：先规划一条无碰撞、经平滑的路径（RRT + 平滑），再用满足速度/加速度限制的时序对其参数化，二者解耦（先规划后定时，非运动动力学）。"
- **Türkçe:** "Bir robot hareketinin Planla ve Parametrele aşamalarını açıkla: önce çarpışmasız yumuşatılmış bir yol PLANLA (RRT + yumuşatma), sonra hız/ivme limitlerine uyan bir zamanlama ile PARAMETRELE — ayrık tutularak (önce-planla-sonra-zamanla, kinodinamik değil) — robotik dersi düzeyinde."

---

*Next lesson: 8.3 — Validate and Hand Off: The Reference Trajectory Layer (the second half — certify and package the Module 8 handoff).*
