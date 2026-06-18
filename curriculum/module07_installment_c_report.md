---
title: "Module 7 — Installment C Completion Report (Units 5–6 + 2 Demos)"
module: 7
installment: C
decision: D-064
status: delivered — paused at milestone for architect review
date: 2026-06
---

# Module 7 — Installment C Completion Report

> **EXECUTIVE SUMMARY**
>
> - **Module:** 7 — Trajectory Generation and Motion Planning · **Installment C** (Units 5–6 + 2 flagship demos) · decision **D-064**.
> - **Status:** Delivered and in the repo; `mkdocs build --strict` passes at **221 lesson pages**. **Paused at the Installment C milestone** for architect review (not auto-proceeding to Installment D).
> - **What was built:** 8 lessons (L17–L24), 8 SVGs (m07-l17..l24), 8 notebooks (all "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short) + 8 coaches' answer keys, and **2 flagship demos** — L17 *Velocity & Acceleration Limit Explorer* and L21 *Configuration Space & Obstacle Visualizer*. The shared engine was extended with verified feasibility and motion-planning utilities (a canonical RRT scenario was locked and solves across seeds).
> - **Key educational achievement:** feasibility and planning taught **physical-intuition-first**, reaching the architect's objective chain **Obstacle → Constraint → Safe Path → Feasible Trajectory** before any algorithm details — students first understand *why* a trajectory can be impossible, *why* slowing down fixes it, and *why* an obstacle becomes a forbidden region, then meet limits, time scaling, configuration space, collision checking, RRT, and smoothing.
> - **Architect review focus:** (1) is the feasibility-first treatment of Unit 5 at the right depth; (2) is configuration space presented as a *way to understand constraints* (robot = point, obstacle = region) rather than abstract math; (3) does the Obstacle → Constraint → Safe Path → Feasible Trajectory chain land before algorithm detail; (4) confirmation the boundaries held (basic RRT only; no optimization/kinodynamic planning, no feedback, no dynamics).
> - **Next:** Installment D — Units 7 (Trajectory Quality, Validation, and Tracking Prerequisites) and 8 (Capstone: Plan → Parameterize → Validate → Execute), completing Module 7 [**D-065**], **on the architect's go-ahead**.

---

## 1. Scope and approach

Installment C delivers the two "can we actually run it, and around what?" units of Module 7.
Following the architect's guidance, every lesson **leads with physical feasibility** — the
learner first grasps why a motion is impossible, or why an obstacle blocks the way, and only
then meets the formal tools (limits, time scaling, configuration space, planning).

- **Unit 5 — Feasibility: Velocity, Acceleration, and Limits (L17–L20):** why a smooth,
  goal-reaching trajectory can still be impossible (5.1, with the Limit Explorer demo); how
  *slowing down* — uniform time scaling — always fixes speed/acceleration infeasibility while
  leaving the path unchanged (5.2); the *fastest feasible* timing that saturates the limits
  (5.3, trapezoidal/triangular, explicitly **not** formal time-optimal optimization); and the
  *whole-trajectory* check across joint limits, velocity, acceleration, and reachability, with
  the **timing-fixable vs geometric** triage (5.4).
- **Unit 6 — Motion Planning and Collision Awareness (L21–L24):** obstacles become
  *forbidden regions* in **configuration space** (6.1, with the C-space Visualizer demo —
  robot as a point, obstacle as a region); the **collision-checking** primitive that decides
  if a configuration is safe, with dense path sampling and tunneling (6.2); finding a safe
  path with **RRT** — sample, nearest, steer, check, connect (6.3, basic RRT only); and turning
  a jagged safe path into a **feasible trajectory** by shortcut smoothing + time scaling (6.4).

The through-line is the architect's objective chain, realized end to end:
**Obstacle → Constraint (C-obstacle / free space) → Safe Path (check, RRT, smooth) →
Feasible Trajectory (time-scale to limits)** — taught as intuition first, algorithm detail second.

## 2. Feasibility-first, then planning (the architect's lead)

Unit 5 never opens with a limit inequality; it opens with the *experience* of impossibility —
planning to cross a room in half a second, a plan whose shape is fine but whose timing the body
can't deliver. Only then does the peak-vs-limit math appear, and immediately the fix: slow down.
Unit 6 never opens with C-space formalism; it opens with the *picture* of an arm dodging a pole
becoming a dot dodging a blob. Configuration space is introduced as the most useful picture in
robotics (robot = point, obstacle = forbidden region), not as an abstract product space, exactly
as directed. Planning stays practical: RRT is "explore a dark cluttered room with small hops,"
and the unit closes by assembling the four-stage pipeline rather than cataloguing algorithms.

## 3. What shipped (artifacts)

| Artifact | Count | Notes |
|---|---|---|
| Lessons (L17–L24) | 8 | 12-section template + AI Learning Companion + Global Learning Support (EN/ES/中文/TR) |
| SVG diagrams (m07-l17..l24) | 8 | engine-faithful curves/grids; role=img + aria-label; XML-validated |
| Notebooks | 8 | embed the engine; all print "All checks passed." under Restart & Run All |
| Flagship demos | 2 | L17 Limit Explorer · L21 Configuration Space & Obstacle Visualizer |
| Quizzes | 8 | 5 MC + 3 short; interactive HTML + MathJax; no browser storage |
| Coaches' answer keys | 8 | per-question rationale + common-misconception notes |

This brings Module 7 to **24 of 32 lessons** and **3 demos** (L07, L17, L21).

### The two demos
- **L17 — Velocity & Acceleration Limit Explorer.** Drag the duration and the displacement;
  the peak-speed and peak-acceleration bars move against their limit lines, turn red when a
  limit is crossed, and the readout reports feasibility and which limit binds (with the minimum
  feasible duration). Makes the 1/T and 1/T² scaling, and the very notion of infeasibility,
  visible and tangible.
- **L21 — Configuration Space & Obstacle Visualizer.** Drag the disk obstacle in the workspace
  and the forbidden region redraws live in the (q1, q2) configuration space; drag the
  configuration point and the arm moves in the workspace, the point reddening when it enters
  the C-obstacle. Makes "robot = point, obstacle = region" concrete and interactive.

Both are self-contained, accessible (role/aria-label/aria-live, keyboard-operable, visible
focus), and use no browser storage.

## 4. Engine and verification

The shared M7 engine was extended with Unit 5–6 utilities, each verified against closed-form
expectations: `quintic_peaks` (peak |v| = 15|Δq|/8T, |a| = (10/√3)|Δq|/T²), `is_feasible` /
`feasible_duration` (minimum common feasible duration), `uniform_time_scale_factors` (1/k,
1/k²), `arm_points2` / `arm_hits_disk` (link-segment-vs-disk geometry), `cspace_grid`
(C-obstacle occupancy), `edge_collision_free` / `path_collision_free` (dense sampling), `rrt`
(basic sampling-based planner), and `shortcut_smooth` / `path_length`. A **canonical Unit-6
scenario** was searched for and locked — disk center (0.5, 0.05), radius 0.06; start tool
(0.45, 0.25) → goal (0.45, −0.25), both elbow-up — for which the direct C-space edge is blocked,
RRT solves 5/5 across seeds, and smoothing shortens the path while keeping it collision-free.
All 8 notebooks pass Restart & Run All; the SVGs are XML-valid and the most complex (l17, l21,
l23) were rendered and visually checked.

## 5. Site generation and strict build

The generator auto-discovered L17–L24 and injected, per lesson, the SVG (after §4), the **demo
iframe** (after §7) for L17 and L21, the notebook tip (after §8), and the quiz (after §9); the
validator passed (every Visual-Explanation page carries an injected figure, no `[Visual:]`
placeholder leaked, Diagram Specification blocks stripped from student pages). Navigation for
Units 5–6 was added to `mkdocs.yml` with "· demo" markers on 5.1 and 6.1. **`mkdocs build
--strict` passes cleanly (exit 0) at 221 lesson pages** (213 + 8); both demo HTML files are
copied into `site_src/demos/module07/` (three demos total).

## 6. Boundaries held

- **No advanced/optimization/kinodynamic planning.** Only **basic RRT** is taught; the
  deliberate **plan-then-time decoupling** (plan a geometric path, *then* time-scale it) is
  stated explicitly as the alternative to kinodynamic planning, which is named as out of scope.
- **No feedback control.** Planning and timing produce an open-loop **reference**; tracking it
  under disturbance is named as Module 8.
- **No dynamics.** Acceleration limits are treated as **given hardware numbers**, never derived
  from torque/inertia; deriving them is explicitly deferred to Module 8.
- **Scope anchored to the launch package** — feasibility (limits, time scaling) and motion
  planning (C-space, collision checking, RRT, smoothing), static obstacle only — and to the
  running planar 2-link arm (L1 = 0.4, L2 = 0.3).

## 7. Module 7 status after Installment C

24 of 32 lessons · 24 notebooks · 24 SVGs · **3 demos** · 24 quizzes · 24 answer keys · 1
midpoint assessment (+ coaches' key). `mkdocs build --strict` passes at 221 lesson pages.
**Paused at the Installment C milestone** for architect review.

## 8. Next

Installment D — Units 7 (Trajectory Quality, Validation, and Tracking Prerequisites) and 8
(Capstone: Plan → Parameterize → Validate → Execute) — completes Module 7 [**D-065**], on the
architect's go-ahead. The optional **hybrid joint+Cartesian trajectory** enhancement (logged at
the midpoint approval) remains earmarked for the Installment D motion-selection framing.
