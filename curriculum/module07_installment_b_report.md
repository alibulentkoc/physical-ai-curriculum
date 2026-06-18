---
title: "Module 7 — Installment B Completion Report (Units 3–4 + Midpoint)"
module: 7
installment: B
decision: D-063
status: delivered — paused at milestone for architect review
date: 2026-06
---

# Module 7 — Installment B Completion Report

> **EXECUTIVE SUMMARY**
>
> - **Module:** 7 — Trajectory Generation and Motion Planning · **Installment B** (Units 3–4 + midpoint assessment) · decision **D-063**.
> - **Status:** Delivered and in the repo; `mkdocs build --strict` passes at **213 lesson pages**. **Paused at the Installment B milestone** for architect review (not auto-proceeding to Installment C).
> - **What was built:** 8 lessons (L09–L16), 8 SVGs (m07-l9..l16), 8 notebooks (all "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short) + 8 coaches' answer keys, and the **Module 7 midpoint assessment** (after Unit 4) + its coaches' key. **No new flagship demo** (the architect's schedule places demos at L07/L17/L21/L29). The shared engine was extended with verified joint-space and Cartesian-space utilities.
> - **Key educational achievement:** the **joint-space-vs-Cartesian-space** distinction made *visible and motion-first* — students first see that a joint move is straight in joint space but curves the tool, and that Cartesian planning straightens the tool path at a cost — then earn the interpolation math (per-joint polynomials, synchronization, C² via-point splines, IK-per-sample loops, SLERP, screw motion).
> - **Architect review focus:** (1) is the motion-first treatment of Units 3–4 at the right depth; (2) the joint/Cartesian balance (§9.2) and the SLERP-+-screw / light-quaternion choice (§9.3); (3) the midpoint's placement and coverage at the Unit-4 seam; (4) confirmation that the M7/M8 boundary held (reference vs tracking).
> - **Next:** Installment C — Units 5 (Feasibility: Velocity, Acceleration, and Limits) and 6 (Motion Planning and Collision Awareness), with demos at L17 and L21 [D-064], **on the architect's go-ahead**.

---

## 1. Scope and approach

Installment B delivers the two trajectory-construction units of Module 7. Following the
architect's guidance, every lesson **leads with motion** — the learner first sees the path
the robot follows and how a trajectory choice behaves, and only then meets the
interpolation mathematics that produces it.

- **Unit 3 — Joint-Space Trajectories (L09–L12):** the simplest trajectories, built joint
  by joint. Per-joint polynomials (3.1), synchronization where the slowest-limited joint
  sets the pace (3.2), via-points and the stop-vs-flow choice (3.3), and C² cubic-spline
  blending that flows through via-points without stopping or jolting (3.4).
- **Unit 4 — Cartesian-Space Trajectories (L13–L16):** controlling the tool's path in
  space. Why Cartesian / straight-line tool motion (4.1), straight-line position via the
  interpolate-then-IK loop with branch consistency and reachability (4.2), orientation by
  SLERP (4.3), and unified position+orientation by screw motion (4.4, with the Unit 4
  recap).

The through-line: **joint-space is simple and joint-feasible but curves the tool;
Cartesian-space controls the tool path at the cost of computation, reachability, and
singularity risk.** The trajectory is always an open-loop **reference** the M6 velocity
layer executes — feedback/tracking remains Module 8.

## 2. Deliverables (in the repo)

| Artifact | Location | Count |
|---|---|---|
| Lessons (L09–L16) | `modules/module07/lessons/lesson09..16_*.md` | 8 |
| Diagrams (SVG) | `assets/diagrams/m07-l9..l16-*.svg` | 8 |
| Notebooks | `modules/module07/notebooks/lesson09..16_*.ipynb` | 8 |
| Quizzes (5 MC + 3 short) | `modules/module07/quizzes/lesson09..16_quiz.html` | 8 |
| Answer keys (coaches') | `coaches/answer-keys/module07/lesson09..16_answer_key.md` | 8 |
| Midpoint assessment | `assessments/module07_midpoint_assessment.md` | 1 |
| Midpoint coaches' key | `coaches/answer-keys/module07/midpoint_answer_key.md` | 1 |

**No flagship demo** in this installment (architect demo schedule: L07/L17/L21/L29).

## 3. Lesson-by-lesson summary

- **3.1 Point-to-Point Joint Moves: Per-Joint Polynomials** — each joint runs its own
  cubic/quintic over a shared duration; the tool path is *shown* curved while the joint
  path is straight (forward kinematics is nonlinear).
- **3.2 Synchronizing Multiple Joints** — one clock; the synchronizing duration
  $T^\star=\max_i T_i^{\min}$; the slowest-limited joint sets the pace, the rest are
  stretched to arrive together.
- **3.3 Via-Points and Multi-Segment Joint Trajectories** — routing through intermediate
  configurations; the stop-at-each (halts) vs flow-through (glides) contrast seen first.
- **3.4 Blending for C² Continuity at Via-Points** — the cubic spline picks the interior
  velocities/accelerations (one tridiagonal solve) so the whole trajectory flows through
  the via-points $C^2$ — no kinks, no acceleration jumps; natural vs clamped ends.
- **4.1 Why Cartesian Space? Straight-Line Tool Motion** — the same endpoints give a curved
  joint-move tool path vs a straight Cartesian one; the interpolate-then-IK recipe and its
  costs (computation, reachability, singularities).
- **4.2 Position Interpolation and the IK-per-Sample Loop** — sample the line, IK each
  sample; **branch consistency** (no elbow flip) and **per-sample reachability** as the
  feasibility conditions; fail cleanly on an unreachable point.
- **4.3 Orientation Interpolation: SLERP** — why averaging rotations fails; SLERP's
  shortest-arc, constant-rate, always-valid properties; the planar shortest-arc reduction.
  Quaternion algebra kept light (§9.3).
- **4.4 Screw Motion: Unified Position + Orientation Interpolation** — constant-twist
  interpolation $T(s)=T_0\exp(s\log(T_0^{-1}T_1))$; screw vs decoupled (agree at endpoints,
  differ between); Chasles' theorem; Unit 4 recap.

## 4. Engine (extended and verified)

The reusable engine (M6 base imported verbatim + Unit 1–2 time utilities) gained Unit 3–4
utilities, each verified numerically before any lesson, notebook, or figure used it:

- `ik_2link(x,y,L1,L2,elbow)` — closed-form planar 2R IK; FK round-trip residual ~5e-17.
- `joint_traj` / `sample_joint_traj` / `sync_duration` — synchronized per-joint polynomial
  trajectories; e.g. $[0,0]\to[2,0.5]$ at $v_{\max}=1$ gives $T^\star=3.75$ s.
- `cubic_spline_natural` / `eval_spline` — C² natural cubic spline; interpolates the knots
  and keeps the second derivative continuous across via-points.
- `cartesian_line` / `cartesian_traj_ik` — straight-line tool path + IK per sample;
  max perpendicular deviation from the line = 5e-17, every sample FK-verified, raises on an
  unreachable path point.
- `quat_axis_angle` / `slerp` / `slerp_angle` — SLERP; unit-norm throughout, shortest arc
  (170°→−170° → +20° turn).
- `se2` / `screw_interp_se2` — SE(2) screw interpolation; endpoints exact, constant twist.

All 8 notebooks execute end-to-end (Restart & Run All) and print **"All checks passed."**

## 5. Build and validation

- Generator auto-discovered L09–L16 and injected each SVG (after §4), notebook tip
  (after §8), and quiz (after §9). The visual-embed validator passed: every
  Visual-Explanation page carries an injected figure, **no `[Visual:]` placeholder leaked**,
  and the Diagram Specification is stripped from student pages.
- Nav added under "Module 7 — Trajectory Generation and Motion Planning" (Units 3–4; no
  demo markers on L09–L16).
- `mkdocs build --strict` **passes** (clean, exit 0) at **213 lesson pages** (205 + 8).
- Quizzes are self-contained interactive HTML with MathJax and **no browser storage**.

## 6. Educational boundaries (held)

- **No feedback / closed-loop control and no dynamics** anywhere in Installment B. The
  trajectory is an open-loop **reference**; the imported **M6 velocity layer executes it**.
  The midpoint's Section E3 explicitly tests this — "correcting the arm back onto the path"
  is Module 8, not Module 7.
- §9.2 joint/Cartesian balance maintained (one full unit each). §9.3 honored: SLERP and
  screw interpolation **applied**, quaternion algebra kept light. §9.7 demo schedule
  honored: **no demo** in Installment B.
- Running example unchanged: planar 2-link arm $L_1=0.4,\ L_2=0.3$.

## 7. Status and next

**Module 7 after Installment B:** 16 / 32 lessons · 16 notebooks · 16 SVGs · 1 demo ·
16 quizzes · 16 answer keys · 1 midpoint assessment (+ coaches' key). **Paused at the
Installment B milestone for architect review.**

**Next (on go-ahead):** Installment C — Units 5 (Feasibility: Velocity, Acceleration, and
Limits) and 6 (Motion Planning and Collision Awareness), with demos at L17 and L21 [D-064].
