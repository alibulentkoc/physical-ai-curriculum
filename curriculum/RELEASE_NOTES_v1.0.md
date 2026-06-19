# Release Notes — curriculum-v1.0
*Physical AI Curriculum · first public release · 2026-06*

EXECUTIVE SUMMARY

**Status:** Prepared for tagging as `curriculum-v1.0` (not yet pushed/deployed). The complete ten-module curriculum builds clean and is publication-ready.

**Findings:** This release contains all 10 modules — 80 units, 325 lessons, 50 interactive demos, 326 diagrams, 325 quizzes, 325 answer keys, and 9 midpoint assessments — published as a 325-page MkDocs/Material site that builds under `--strict` with exit 0 and zero broken references.

**Issues:** None blocking. Optional pre-tag hygiene (orphan notebooks, stale flat `site_src` copies) is documented in the release audit report.

**Recommendations:** Tag after the optional cleanup and a final `--strict` rebuild, per the release execution plan.

**Next:** Execute the release execution plan on approval.

---

## What is curriculum-v1.0

The first complete release of the **Physical AI Curriculum** — a ten-module course that builds one complete Physical AI system, one capability at a time, on a single running example: a planar 2-link arm (L₁ = 0.4, L₂ = 0.3) harvesting a row of tomatoes in a greenhouse. The arc:

> **represent → perceive → reach → move → integrate → twin**

## Modules in this release

1. **Mathematical Foundations** — vectors & linear algebra (33 lessons)
2. **Spatial Transformations and SE(3)** — frames & rigid motion (36 lessons)
3. **Camera Geometry and Robotic Perception** — pixels → 3-D (32 lessons)
4. **Forward Kinematics (DH)** — angles → pose (32 lessons)
5. **Inverse Kinematics** — pose → angles (32 lessons)
6. **Jacobians and Differential Motion** — the velocity layer (32 lessons)
7. **Trajectory Generation and Motion Planning** — the reference layer (32 lessons)
8. **Feedback Control and Real-Time Execution (ROS 2)** — the control layer (32 lessons)
9. **System Integration** — the self-healing harvester, `harvest_row` (32 lessons)
10. **Digital Twin Capstone** — mirror/simulate/monitor/predict/adapt; the curriculum close (32 lessons)

## What's included

| Artifact | Count |
|---|---:|
| Modules / Units / Lessons | 10 / 80 / 325 |
| Self-verifying notebooks (per lesson) | 325 |
| Diagrams (SVG) | 326 |
| Interactive demos | 50 |
| Quizzes | 325 |
| Answer keys (+ midpoint keys) | 325 |
| Midpoint assessments | 9 |
| Published site | 325 lesson pages (`mkdocs --strict`, exit 0) |

Every lesson uses a 12-section template with an AI Learning Companion and four-language Global Learning Support (English · Español · 中文 · Türkçe). English is the authoritative source.

## Highlights

- **One connected system, not ten topics** — each module hands a concrete artifact to the next (velocity layer → reference layer → control layer → integrated system → digital twin).
- **Four flagship demos in the capstone modules** (M9: Pipeline Data-Flow Explorer, Motion-Stack Visualizer, Failure-Injection Sandbox, End-to-End Pick-Cycle Player; M10: Twin vs Model vs Simulation, Sim-to-Real Gap Explorer, Lookahead & What-If Explorer, Twin-in-the-Loop Harvest).
- **The synthesis** — "one tomato through ten modules" and the course close make the full pipeline explicit.

## Conventions (version-stable)

Twist ordering ξ = [v; ω]; geometric Jacobian primary; base/world frame primary; manipulability w = ∏σᵢ; damped least squares from the SVD; canonical arm L₁ = 0.4, L₂ = 0.3.

## Scope boundaries (by design)

No formal manipulator dynamics; no advanced control-theory formalism (Laplace/transfer functions/Bode/Nyquist); integration is reading + coordination (no new estimation/diagnosis); the twin uses no machine learning, RL, adaptive control, or optimization. These are the deliberate edges of a foundation, each with a named next course.

## Known notes

- Optional hygiene (non-blocking, tracked in `release_audit_report.md`): 42 orphan duplicate notebooks (M1/M2), 45 stale flat copies in `site_src/`, a stray spec file in M1's demos folder, two engine backups, and sparse `· demo` nav annotations. None affect the rendered site.
- Multilingual publishing is prepared but not enabled in v1.0 (see `translation_strategy.md`); per-lesson AI translation is available today via the Global Learning Support blocks.

## Provenance

Produced across decisions D-001 … D-078 (see `ARCHITECT_DECISIONS.md`); per-module installment and completion reports plus the curriculum completion report are in `curriculum/`.

*Prepared for `curriculum-v1.0`. Tagging and deployment per `release_execution_plan.md`, on approval.*
