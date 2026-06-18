---
module: 07
unit: 07
lesson: 7.2
title: "Validating a Trajectory: The Complete Check"
core_idea: "Before a trajectory runs, it must pass a complete validation suite: endpoints correct, continuity (C0/C1/C2), within velocity and acceleration limits, collision-free along the whole path, and reachable throughout. Validation is a single gate that aggregates every check from Units 5-6 into one pass/fail verdict on the reference."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L5.4 — Whole-trajectory feasibility checks"
  - "M7 L6.2 — Collision checking along a path"
learning_objectives:
  - "Assemble the complete validation suite a reference trajectory must pass."
  - "Run validation as one aggregated pass/fail gate and interpret a failed check."
  - "Explain why validation is the safety gate between planning and execution."
---

# Lesson 7.2 — Validating a Trajectory: The Complete Check

> Lesson 7.1 ranked good trajectories; this lesson is the gate that decides whether a trajectory is allowed to run **at all**. Validation gathers every check from Units 5–6 — continuity, limits, collisions, reachability, correct endpoints — into one suite that returns a single verdict. We lead by *running the gauntlet* on a reference and reading which gate, if any, it fails.

---

## 1. Why This Matters
A trajectory that looks fine can still be wrong in one specific way — a momentary limit violation, a link that clips an obstacle between waypoints, an endpoint that's slightly off, a discontinuity at a segment join. Running such a trajectory risks a fault or a crash. So before execution there is a mandatory step: **validation** — a complete, automated check that the reference satisfies *every* requirement, everywhere along its length, returning a clear pass/fail.

This is the safety gate between *planning* (Units 5–6 produced a candidate) and *execution* (Unit 8 runs it). It aggregates the individual checks you already know — the feasibility checks of Lesson 5.4 and the collision check of Lesson 6.2 — plus continuity and endpoint checks, into one suite with one verdict. A "valid" reference is safe to hand off and run; an invalid one is rejected with the specific failing gate named, so it can be fixed (re-plan, re-time, re-smooth). For the harvester, validation is what stands between a planned motion and the arm actually moving near the canopy — nothing runs unvalidated.

## 2. Physical Intuition
Think of a pre-flight checklist. Before a plane leaves the gate, the crew doesn't *feel* whether it's ready — they run a fixed list: fuel, controls, instruments, doors, weight-and-balance. Every item must pass; one failed item grounds the flight, and the checklist tells you exactly which one. The checklist doesn't make the plane fly; it certifies that flying is safe.

Trajectory validation is the robot's pre-flight checklist. Item by item: do the endpoints match the requested start and goal? Is the motion continuous (no teleport, no instantaneous velocity jump)? Does every joint stay within its speed and acceleration limits at every instant? Is the whole arm clear of obstacles along the entire path? Is every configuration reachable? Each item is a check you've met before; validation simply runs them all and gives one answer — *valid* (cleared to run) or *invalid* (grounded, with the failing item named). It certifies safety; it doesn't move the robot.

## 3. Mathematical Foundations
Validation samples the reference $\mathbf q(t)$ densely (a fine time grid, Lesson 5.4) and tests a fixed suite of predicates. The reference is **valid** iff **all** pass:

1. **Endpoints match:** $\mathbf q(0)=\mathbf q_{\text{start}}$ and $\mathbf q(T)=\mathbf q_{\text{goal}}$ (within tolerance) — it actually performs the requested task.
2. **Boundary rest (for rest-to-rest):** $\dot{\mathbf q}(0)=\dot{\mathbf q}(T)=\mathbf 0$ and $\ddot{\mathbf q}(0)=\ddot{\mathbf q}(T)=\mathbf 0$ — starts and ends at rest with no jolt.
3. **Continuity:** $\mathbf q(t)$ is $C^0$ (no position jump), $\dot{\mathbf q}$ is $C^0$ ($C^1$ in position — no velocity jump), and ideally $\ddot{\mathbf q}$ continuous ($C^2$) — no discontinuous leaps at any sample or segment join.
4. **Velocity limit:** $\max_{t,i}|\dot q_i(t)|\le \dot q_{\lim}$ (Lesson 5.1).
5. **Acceleration limit:** $\max_{t,i}|\ddot q_i(t)|\le \ddot q_{\lim}$ (Lesson 5.1).
6. **Collision-free:** the whole arm clears every obstacle at every sampled configuration (Lesson 6.2).
7. **Reachable:** every configuration is finite and valid, and (for Cartesian intent) every tool point lies in the workspace annulus (Lesson 5.4).

The suite returns a dictionary of per-check booleans plus `valid = all(checks)`. A failed check **localizes** the problem and dictates the remedy (Lesson 5.4's triage): velocity/acceleration → re-time (slow down); collision/reachability/joint-limit → re-plan or re-route; continuity/endpoint → fix the trajectory construction (segment joins, boundary conditions).

The engine implements this as `validate_trajectory(ref_fn, T, waypoints, seg_T, vlim, alim, center, radius, q_start, q_goal)`, returning the per-check dict and the overall `valid`. It is a **pure validation** — it computes nothing about forces, energy, or control; it only certifies the reference's geometry and timing. (The piecewise rest-to-rest quintic of the engine makes continuity automatic, since each segment starts and ends at rest; flowing blended trajectories require the continuity check to catch any join discontinuity.)

## 4. Visual Explanation
`[Visual: a reference passing through a validation checklist — endpoints, continuity, velocity, acceleration, collision-free, reachable — each a row that turns green (pass) or red (fail), with an overall VALID/INVALID verdict]`

**Diagram Specification**

- **Objective:** show validation as a checklist of independent gates with one aggregated verdict.
- **Scene:** a vertical checklist of the seven checks, each a row with a pass (green ✓) or fail (red ✗) marker; one row failed (e.g. "velocity limit ✗ → re-time"), the rest passed. A bold banner at the bottom reads "INVALID — re-time" (or "VALID — cleared to run" in the all-pass variant). A small note maps each failure type to its remedy.
- **Labels:** the seven check names; "VALID / INVALID"; remedy tags (re-time / re-plan / fix construction).
- **Form:** SVG, checklist rows + verdict banner. Pass emerald `#10b981`, fail error `#b91c1c`, verdict bold.

## 5. Engineering Example
Every serious motion system validates before it executes. Robot controllers run a pre-execution check (limits, reachability, sometimes collision against a world model) and refuse programs that fail, naming the offending line. Planning frameworks validate a planned-and-timed trajectory against joint limits, velocity/acceleration bounds, and collision before it's allowed onto the hardware; simulation/digital-twin pipelines validate in a virtual cell first. The pattern is universal: plan, validate, *then* execute — never execute an unvalidated trajectory near people or product. For the harvester, validation against a model of the canopy and the arm's limits is the last automated gate before the reference is handed to execution; a failed gate sends the trajectory back to be re-timed or re-planned, never to the motors.

## 6. Worked Example
Validate a planned-and-timed reference for the canonical obstacle scenario (disk at $(0.5,0.05)$, $r=0.06$; start tool $(0.45,0.25)$ → goal $(0.45,-0.25)$; limits $\dot q_{\lim}=2$, $\ddot q_{\lim}=4$).

- The reference is built by planning (RRT), smoothing, and timing each rest-to-rest segment to its minimum feasible duration (so it sits at the limits).
- Run the suite: **endpoints match** ✓ (q(0)=start, q(T)=goal), **rest-to-rest** ✓, **velocity** ✓ (peak ≤ 2), **acceleration** ✓ (peak = 4, the binding limit), **continuous** ✓ (rest-to-rest joins), **collision-free** ✓ (whole arm clears the disk at every sample), **reachable** ✓ (all configs valid). Overall: **VALID — cleared to run.**
- Now break it: shrink one segment's duration below its minimum. The **velocity/acceleration** check now fails; `valid` flips to False, the failing gate is named, and the remedy is "re-time." Restore the duration and it validates again. The notebook runs both the passing and the deliberately-broken case.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Run the gauntlet.** In the notebook you:

1. Build a valid reference and run `validate_trajectory` — confirm every check passes and the verdict is `valid`.
2. Introduce a single defect (too-short timing → limit violation; or a configuration that clips the obstacle) and confirm exactly that check fails while `valid` flips to False.
3. Read the per-check dictionary to localize the failure and name the correct remedy (re-time vs re-plan).

## 8. Coding Exercise
*(Snippet / notebook task — uses `validate_trajectory`, `piecewise_quintic`, `feasible_duration`.)*

In the companion notebook:

1. Build a valid reference and assert `validate_trajectory(...)['valid']` is True with **every** sub-check True.
2. Create a defective reference (e.g. one segment timed below `feasible_duration`) and assert `valid` is False with the **velocity or acceleration** check False — and that the collision/reachability checks remain True (the failure is localized).
3. Create a second defect that collides (route a segment through the obstacle) and assert the **collision_free** check is the one that fails.

## 9. Knowledge Check
1. List the checks in the complete validation suite.
2. What is the overall verdict, and how is it computed from the individual checks?
3. Why does validation localize a failure to a specific check, and how does that help?
4. Why is validation the gate between planning and execution?

## 10. Challenge Problem
A reference passes velocity, acceleration, collision, and reachability checks but **fails continuity** at one segment join (a velocity jump). Explain what construction choice likely caused it (think about how segments are joined) and how to fix it without changing the path. Then argue why a continuity failure is dangerous even though every individual configuration is feasible and collision-free — i.e. why the controller would struggle with a velocity discontinuity. *(Validation catches problems no single-point check would.)*

## 11. Common Mistakes
- **Validating only the endpoints.** Interior violations (a momentary limit breach, a mid-path collision) require dense sampling.
- **Treating a single failed check as total failure without localizing.** The failing check names the remedy (re-time vs re-plan vs fix construction).
- **Skipping continuity.** A trajectory can be feasible and collision-free yet have a velocity jump at a join — validation must catch it.
- **Executing an unvalidated trajectory.** Validation is mandatory before handoff; planning success is not validation.

## 12. Key Takeaways
- **Validation** aggregates every check — endpoints, rest, continuity, velocity, acceleration, collision-free, reachable — into **one pass/fail verdict** on the reference.
- It samples **densely** and is `valid = all(checks)`; a failed check **localizes** the problem and dictates the remedy.
- It is the **safety gate between planning and execution** — nothing runs unvalidated.
- It is **pure validation** of geometry and timing — no forces, energy, or control (those are Module 8).

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain trajectory validation using the 'pre-flight checklist' analogy. List the checks (endpoints, continuity, velocity, acceleration, collision-free, reachable) and stress the single aggregated verdict. Then give me a reference to validate."
- **Practice (generate exercises):** "Give me three references each with one defect. Ask me which validation check fails and what the remedy is (re-time / re-plan / fix construction). Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how real robot controllers and planning frameworks validate trajectories before execution, and why 'plan, validate, then execute' is universal."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain the complete validation suite for a robot reference trajectory: endpoints, continuity, velocity/acceleration limits, collision-free, and reachability, aggregated into one pass/fail verdict, at a robotics-course level (pure validation, no dynamics or control)."
- **Español:** "Explica la suite completa de validación para una trayectoria de referencia de robot: extremos, continuidad, límites de velocidad/aceleración, ausencia de colisiones y alcanzabilidad, agregadas en un único veredicto aprobado/reprobado, a nivel de curso de robótica (validación pura, sin dinámica ni control)."
- **中文（简体）：** "用机器人课程的水平（纯验证，不涉及动力学或控制），解释机器人参考轨迹的完整验证套件：端点、连续性、速度/加速度限制、无碰撞和可达性，汇总成一个通过/不通过的结论。"
- **Türkçe:** "Bir robot referans yörüngesi için tam doğrulama paketini açıkla: uç noktalar, süreklilik, hız/ivme limitleri, çarpışmasızlık ve erişilebilirlik — tek bir geçti/kaldı kararında toplanır — robotik dersi düzeyinde (saf doğrulama, dinamik veya kontrol yok)."

---

*Next lesson: 7.3 — Tracking Prerequisites: What the Reference Must Provide (the boundary to Module 8).*
