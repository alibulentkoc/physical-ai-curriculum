# Module 5 — Inverse Kinematics · Completion Report

**Status:** ✅ COMPLETE (D-056) · 5th of 10 modules signed off
**Build:** `mkdocs build --strict` PASS — **165 pages**, exit 0, validator clean
**Theme:** Greenhouse Harvesting Robot · **Running example:** planar 2-link arm, L1 = 0.4 m, L2 = 0.3 m

---

## 1. What the module teaches

Inverse kinematics turns a desired gripper pose into joint angles — the reverse of Module 4's forward map. The module states the inverse problem (nonlinear; 0/1/many solutions; reachability), solves it in closed form where structure allows and numerically where it doesn't, makes the solver robust against singularities and joint limits, verifies every solution by forward kinematics, and integrates the whole thing with perception into one **Reach-the-Fruit** pipeline.

## 2. Unit-by-unit arc (8 units, 32 lessons)

| Unit | Title | Lessons | Core content |
|---|---|---|---|
| 1 | The Inverse Problem | 01–04 | FK vs IK; nonlinearity; reachability; 0/1/many solutions |
| 2 | IK of One and Two Joints | 05–08 | one-joint by inspection; the 2-link triangle; elbow-up/down (demo 2.3) |
| 3 | Analytical (Closed-Form) IK | 09–12 | boxed 2-link formulas; `atan2` discipline; wrist decoupling |
| 4 | From Geometry to Numerical IK | 13–16 | where closed form runs out; FK Jacobian (local linear map); guess–measure–step · **Midpoint** |
| 5 | Numerical IK in Practice | 17–20 | Newton/pseudoinverse; transpose & damped least squares; convergence/failure (demo 5.1) |
| 6 | Singularities & Solution Selection | 21–24 | singularity **recognition** (det J = 0); joint limits; choosing among solutions (demo 6.1) |
| 7 | Verifying & Connecting to Perception | 25–28 | FK verification (accept/reject); grasp pose → base-frame target; the pipeline |
| 8 | Mini Project: Reach the Fruit | 29–32 | integrated capstone: analytical + numerical, verified, selected, robust (flagship demo 8.1) |

Each unit's `.4` lesson is a recap; the midpoint assessment sits after Unit 4.

## 3. Deliverables (Definition of Done — all met)

| Artifact | Count | Location |
|---|---|---|
| Lesson markdowns (12-section + 2 components) | 32 | `modules/module05/lessons/lesson01..32_*.md` |
| SVG diagrams (XML-valid, embedded §4, accessible) | 32 | `assets/diagrams/m05-l1..l32-*.svg` |
| Notebooks (all "All checks passed.") | 32 | `modules/module05/notebooks/M05_U01..U08_*` |
| Interactive demos | 4 | `modules/module05/demos/` |
| Interactive quizzes (reference renderer) | 32 | `modules/module05/quizzes/lesson01..32_quiz.html` |
| Answer keys (coaches-only) | 32 | `coaches/answer-keys/module05/lesson01..32_answer_key.md` |
| Midpoint assessment + coaches' key | 1 (+key) | `assessments/module05_midpoint_assessment.md` |

**Demos:** `lesson07_two_solution_explorer` (elbow-up/down), `lesson17_convergence_stepper` (Newton step-by-step + error plot), `lesson21_singularity_visualizer` (sweep θ₂, det J → 0, lost direction), and the flagship `lesson29_reach_the_fruit` (drag the fruit, set camera offset + joint limits, watch the full perceive→place→solve→verify→select pipeline run live with a status taxonomy). All demos: design-system CSS vars, accessible SVG, no browser storage; their JS logic mirrors the notebook helpers and FK-verifies.

## 4. Educational boundaries held (as mandated)

- **The Jacobian is solver machinery only** — introduced (Lesson 4.2) and used purely as the numerical solver's local linear map. Velocity interpretation, differential motion, manipulability, full singularity theory, and SVD analysis are all **deferred to Module 6** and re-flagged in the wrap-up (Lesson 8.4).
- **Singularities are recognition-only** (Unit 6) — det J = L₁L₂ sin θ₂ = 0 at θ₂ = 0° (arm straight) / 180° (folded), the workspace boundaries; an explicit in-lesson scope note defers the theory.
- **Downstream deferrals respected:** trajectory/motion planning → Module 7; control → Module 8.

## 5. Integration (the capstone)

The Unit 8 "Reach the Fruit" capstone integrates four modules into one coherent workflow, exactly as directed:

> perceive (**M3**) → place in base frame (**M2/M4**: p_base = T_base^cam · p_cam + grasp pose) → reachability gate → solve (**M5**: analytical where possible, numerical where needed) → filter joint limits → verify with FK (**M4/M5**) → select (nearest/safe) → execute θ⋆ — or return a clear status (unreachable / no_solution / verification_failed / no_feasible).

Solve → Verify with FK → Accept/Reject is the spine of Unit 7 and is carried through the capstone in Unit 8.

## 6. Build & verification summary

- `python3 tools/generate_site_pages.py` → 165 pages; generator detects 4 demos (lessons 07/17/21/29) and 32 quizzes.
- `mkdocs build --strict` → PASS, exit 0, no warnings (the red "Material for MkDocs / MkDocs 2.0" banner is an upstream advisory, filtered).
- Full DoD matrix across lessons 01–32 → all pass (12-section/recap, 2 components, SVG in §4, generated site page embeds the m05 diagram, quiz, answer key, demo on 07/17/21/29).
- All 32 Module 5 notebooks re-executed end to end → 32/32 "All checks passed."

## 7. Notes for the record

- **L5.3 status logic:** for the bounded 2-link arm a too-large gain produces *oscillation* (reported `diverged`, gated on reachability) while an unreachable target *plateaus* (reported `max_iter`); the lesson and notebook state this explicitly so the failure-mode taxonomy stays honest.
- Shared notebook helpers accumulated across the module: `fk_two_link`, `jacobian_2link`, `ik_2link_closed`, `ik_newton`, `ik_dls`, `ik_solve`, `det_jacobian_2link`, `feasible_solutions`, `choose_solution`, `verify`, `cam_to_base`, `perceive_place_solve`, `reach_the_fruit`, `norm180`.

## 8. Next

**Module 6 — Differential Kinematics.** The Jacobian reopens as a velocity relationship (ṗ = J θ̇): differential motion, manipulability, full singularity theory, and SVD — precisely Module 5's deferrals. Not yet started; awaiting the architect's Module 6 launch package.

---

*Module 5 paused at completion for architect review. Not pushed to GitHub.*
