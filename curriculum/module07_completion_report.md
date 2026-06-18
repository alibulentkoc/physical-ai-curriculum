---
title: "Module 7 — Completion Report (Trajectory Generation and Motion Planning)"
module: 7
status: COMPLETE — paused at module completion
decisions: [D-061, D-062, D-063, D-064, D-065]
date: 2026-06
---

# Module 7 — Completion Report

> **EXECUTIVE SUMMARY**
>
> - **Module:** 7 — Trajectory Generation and Motion Planning. **COMPLETE** across four installments (A–D) and a midpoint assessment; decisions **D-061** (launch) through **D-065** (capstone).
> - **Status:** Fully built and in the repo; `mkdocs build --strict` passes at **229 lesson pages**. **Paused at Module 7 completion** — no further installment reviews within this module.
> - **Totals:** **8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 flagship demos · 32 quizzes · 33 coaches' answer keys · 1 midpoint assessment.** Every notebook passes Restart & Run All ("All checks passed."); every SVG is XML-valid; every quiz is interactive HTML (5 MC + 3 short, MathJax, no browser storage); all demos are self-contained, accessible, and storage-free.
> - **Capstone workflow & deliverable:** the complete robotics workflow **Goal → Path → Trajectory → Validation → Execution** (produced by the actions **Plan → Parameterize → Validate → Execute**) yields the **reference trajectory layer** — `reference(t) → (q_d, q̇_d, q̈_d, info)` with metadata — consumed by Module 8. It is the deliberate bookend to Module 6's `velocity_layer`.
> - **Pedagogical arc:** from *"what is a trajectory?"* (path vs timing, smoothness) to a *validated reference layer for a complete task* (the greenhouse harvest cycle), taught motion-first / feasibility-first / planning-intuitively throughout.
> - **Boundaries held end to end:** no feedback control, no dynamics, no actuator control (all Module 8); the module produces and validates an **open-loop reference**, never tracks it.
> - **Next:** Module 8 — Feedback Control, which builds the tracker that consumes this reference layer.

---

## 1. Scope and structure

Module 7 turns a task ("move the gripper there, around the obstacles") into a validated,
executable **reference trajectory**. It was delivered in four installments plus a midpoint
assessment, each paused for architect review:

- **Installment A (Units 1–2, L01–L08; D-062):** foundations — path vs trajectory and smoothness
  (U1); polynomial time scaling and the smooth-vs-fast trade (U2). Demo at L07.
- **Installment B (Units 3–4 + midpoint, L09–L16; D-063):** joint-space trajectories (U3);
  Cartesian-space trajectories — straight-line, orientation/SLERP, screw motion (U4); the
  Module 7 midpoint assessment.
- **Installment C (Units 5–6, L17–L24; D-064):** feasibility — limits, time scaling,
  fastest-feasible timing, whole-trajectory checks (U5); motion planning — configuration space,
  collision checking, RRT, smoothing (U6). Demos at L17 and L21.
- **Installment D (Units 7–8, L25–L32; D-065):** trajectory quality, validation, tracking
  prerequisites, reference representation (U7); the capstone workflow and the reference
  trajectory layer (U8). Flagship Trajectory Studio demo at L29.

## 2. The eight units (one line each)

1. **Foundations of Trajectories** — path (geometry) vs trajectory (timing); smoothness as continuity.
2. **Time Scaling and Motion Profiles** — cubic/quintic time scaling; trapezoidal/S-curve; the jerk (smooth-vs-fast) trade.
3. **Joint-Space Trajectories** — per-joint polynomials, synchronization to the bottleneck joint, via-points, C² spline blending.
4. **Cartesian-Space Trajectories** — straight-line tool motion (interpolate-then-IK), orientation by SLERP, unified screw motion.
5. **Feasibility: Velocity, Acceleration, and Limits** — why a trajectory is impossible, slowing down (time scaling), fastest feasible timing, whole-trajectory checks.
6. **Motion Planning and Collision Awareness** — configuration space, collision checking, RRT, smoothing → Obstacle → Constraint → Safe Path → Feasible Trajectory.
7. **Trajectory Quality, Validation, and Tracking Prerequisites** — quality metrics, the validation suite, the reference's tracking prerequisites and the M7/M8 boundary, reference representation.
8. **Capstone: Plan → Parameterize → Validate → Execute** — the complete workflow, plan-then-time, the reference trajectory layer, the greenhouse harvest cycle, and the bridge to Module 8.

## 3. The teaching approach that held throughout

Three corrections, requested at launch and reaffirmed at each review, held across all 32 lessons:

- **Motion-first.** Every lesson leads with the motion the robot makes (or the experience of it)
  before the mathematics — the path before the polynomial, the impossibility before the limit,
  the robot-as-a-point picture before configuration-space formalism.
- **Feasibility-first (Unit 5).** Students first understand *why* a trajectory can be impossible
  and *why* slowing down fixes it, before any timing mathematics.
- **Planning-intuitively (Unit 6).** Configuration space is presented as a way to *see*
  constraints (robot = point, obstacle = forbidden region), and planning reaches the objective
  chain **Obstacle → Constraint → Safe Path → Feasible Trajectory** before algorithm details.

The architect's Installment-C assessment singled out exactly these — impossibility before limits,
limits before timing math, robot-as-point intuition, and the obstacle→…→trajectory progression —
as holding; Unit 7–8 continued the pattern (quality before validation machinery, the workflow as
the integrating view, the harvest cycle as the concrete payoff).

## 4. The capstone artifact (the Module 8 handoff)

Module 7's purpose culminates in one object: the **reference trajectory layer**, produced by the
complete robotics workflow **Goal → Path → Trajectory → Validation → Execution** (the artifact chain)
— driven by the four actions **Plan → Parameterize → Validate → Execute** — and consumed by Module 8.

- **PLAN** (Unit 6): a collision-free smoothed path. **PARAMETERIZE** (Units 2–5): a timed
  trajectory within the velocity/acceleration limits. **VALIDATE** (Unit 7): the complete suite,
  gating the handoff. **EXECUTE**: discretize and hand off (open-loop within Module 7).
- The layer exposes `reference(t) → (q_d, q̇_d, q̈_d, info)` — the feed-forward triple — plus
  metadata (duration, control rate, validated flag, quality metrics).
- It is the deliberate **bookend** to Module 6's `velocity_layer`: just as Module 6 handed
  Module 7 a clean velocity interface, Module 7 hands Module 8 a clean reference interface:

  **M6 `velocity_layer(q, ξ_d) → q̇`  →  M7 `reference(t) → (q_d, q̇_d, q̈_d)`  →  M8 tracker.**

The greenhouse harvest cycle (L32) demonstrates the whole module producing this layer for a real,
multi-motion task (reach → grasp → retreat), each leg the full workflow, chained at rest into one
validated reference cycle.

## 5. Engine and verification

A single shared engine underpins the module, extended installment by installment and verified at
every step. Unit 7–8 added: `piecewise_quintic` (rest-to-rest C² reference), `sample_reference`
(discretization), `trajectory_metrics` (duration/peak speed/accel/jerk/Cartesian length),
`validate_trajectory` (the 7-check suite), `plan_parameterize` (PLAN+PARAMETERIZE), and the
capstone `reference_trajectory_layer` (PLAN→PARAMETERIZE→VALIDATE → validated `reference(t)`).
The capstone was verified end-to-end on the canonical scenario: validated = True, all seven checks
pass, the reference returns the feed-forward triple, and peaks sit at the binding limit. **All 32
notebooks pass Restart & Run All.**

## 6. The four flagship demos

- **L07 — Polynomial Profile Shaper** (cubic vs quintic endpoints; the smoothness story).
- **L17 — Velocity & Acceleration Limit Explorer** (peaks vs limit lines; feasibility and the
  binding limit).
- **L21 — Configuration Space & Obstacle Visualizer** (drag the obstacle; the forbidden region
  redraws; robot-as-a-point).
- **L29 — Trajectory Studio** (the whole Plan → Parameterize → Validate → Execute workflow on the
  greenhouse arm, stage by stage, ending in the reference signal handed to Module 8).

All four are self-contained, accessible (role/aria-label/aria-live, keyboard, focus styles), and
use no browser storage.

## 7. Boundaries held

Across all 32 lessons the module stayed within its launch scope. It treats acceleration limits as
**given numbers** (never derived from torque/inertia); it plans geometric paths and times them
separately (**plan-then-time, not kinodynamic**); it uses **basic RRT** (no optimization/optimal
planning); and it produces an **open-loop reference** that is validated and handed off but never
tracked. Feedback control, dynamics, and actuator control are named consistently as **Module 8**.
"Execute" means open-loop playback (via the imported Module 6 velocity layer) plus delivery of the
reference — never a control law.

## 8. Status and next

**Module 7 is COMPLETE.** 8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 demos · 32 quizzes ·
33 answer keys · 1 midpoint. `mkdocs build --strict` passes at 229 lesson pages; all tracking files
updated and decisions D-061…D-065 logged. **Paused at module completion — no further installment
reviews within this module.**

**Next:** **Module 8 — Feedback Control**, which builds the tracker that consumes the reference
trajectory layer produced here, adding closed-loop control, dynamics, and actuator control to turn
the validated reference into actual, disturbance-rejecting motion on the real arm.
