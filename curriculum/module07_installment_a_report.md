---
title: "Module 7 — Installment A (Units 1–2) — Milestone Report"
module: 07
installment: A
units: [1, 2]
lessons: "L01–L08"
decision: D-061
status: delivered — paused for architect review
date: 2026-06
---

# Module 7 — Installment A Milestone Report

## EXECUTIVE SUMMARY

- **Module:** 7 — Trajectory Generation and Motion Planning
- **Status:** Installment A (Units 1–2, lessons L01–L08) **delivered and verified**; **paused at the milestone for architect review** (no auto-proceed to Installment B).
- **What was built:** 8 lessons (full 12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVG diagrams, 8 runnable notebooks (all "All checks passed." under Restart & Run All), 1 flagship interactive demo (L07 Polynomial Profile Shaper), 8 interactive quizzes (5 MC + 3 short), 8 coaches' answer keys. Generator wired for Module 7; nav added; `mkdocs build --strict` passes at **205 lesson pages** (197 M1–M6 + 8 M7).
- **Key educational achievement:** the **cubic → quintic acceleration-jump demonstration (C¹ → C²)** — shown three independent, numerically-agreeing ways (flagship demo, the m07-l7 SVG, and the L07 notebook/engine): a rest-to-rest cubic leaves a non-zero endpoint acceleration of ±6Δ/T² (3.2 rad/s² for the worked move), while the quintic zeros it for continuous acceleration, paying with higher mid-move peaks.
- **Architect review focus:** (1) the motion-first framing of Unit 1 and the C⁰/C¹/C² + jerk treatment of Unit 2; (2) confirmation that both fences held — **no feedback control, no dynamics**, open-loop execution via the imported M6 velocity layer only; (3) one routine **decision-id reconciliation** to acknowledge (below).
- **Next:** Installment B — Units 3 (Joint-Space Trajectories) and 4 (Cartesian-Space Trajectories) + the midpoint assessment after Unit 4 (**D-062**), on approval.

---

## 1. Decision-id reconciliation (flagged)

The launch package proposed **D-058** for the Module 7 launch, with installments following as D-059…D-062. Those ids were **already consumed by Module 6** (M6 Installments A–D = D-057 / D-058 / D-059 / D-060). To avoid a collision, Module 7 starts at the next free id:

| Installment | Launch-package id | **Actual id used** |
|---|---|---|
| Launch + A (U1–U2) | D-058 | **D-061** |
| B (U3–U4 + midpoint) | D-059 | **D-062** |
| C (U5–U6) | D-060 | **D-063** |
| D (U7–U8 + capstone) | D-061 | **D-064** |

This is recorded in `ARCHITECT_DECISIONS.md` under **D-061**. No content impact; the §1 "proposed decision id" line of the launch package is superseded by this mapping. Flagging per protocol; no action required beyond acknowledgement.

## 2. What was delivered

**Unit 1 — Motion, Paths, and Trajectories** (motion literacy, taught motion-first)
- **L01 (1.1)** Why smooth, safe, efficient motion matters — jerky vs smooth harvest; the carried-coffee intuition; the same pose can be reached well or badly.
- **L02 (1.2)** Path vs trajectory — geometry q(s) vs timing q(t)=q(s(t)); the hiking-trail/schedule split; one path, many trajectories.
- **L03 (1.3)** What makes a trajectory "good" — the four criteria (smooth, feasible, safe, efficient) and the C⁰/C¹/C² continuity ladder; the four-inspector framing.
- **L04 (1.4)** The motion pipeline — plan → parameterize → execute-open-loop (M6) → track (M8); both fences (no feedback, no dynamics) drawn explicitly.

**Unit 2 — Time Parameterization and Smoothness** (the timing toolkit)
- **L05 (2.1)** s(t) and its derivatives — chain rule q̇ = q′ṡ, q̈ = q′s̈ + q″ṡ², jerk; "at rest" ≠ zero acceleration.
- **L06 (2.2)** Continuity classes C⁰/C¹/C² and why jerk matters — C² ⇒ continuous force ⇒ no shock loads; bounded jerk as the separate finishing requirement.
- **L07 (2.3) [FLAGSHIP DEMO]** Polynomial time scaling: cubic vs quintic — the acceleration-jump result, the C¹→C² upgrade, and the peak-speed price.
- **L08 (2.4)** Trapezoidal vs S-curve velocity profiles — time-optimal-but-C¹ vs jerk-limited-C²; the triangular short-move case; Unit 2 recap and the polynomial-vs-profile decision table.

## 3. Engine

A reusable Module 7 engine is **embedded in each notebook**:
- **M6 base, imported verbatim** (not reimplemented): `dh`, `forward_chain`, `geometric_jacobian`, `Jv_planar`, `fk_xy`, `analyze` (σ/w/κ/singular flags), `dls`, and **`velocity_layer(P, T, q, ξ_d)`** — the velocity layer is the open-loop execution backend.
- **New Unit 1–2 time utilities:** `poly_eval` (pos/vel/acc/jerk), `cubic_coeffs`, `quintic_coeffs`, `trapezoidal_profile`, `s_curve_profile`.

Verified properties: cubic endpoint acceleration = 6Δ/T² (jump) vs quintic = 0 (smooth, C²); S-curve peak jerk bounded by j_max and total time ≥ the time-optimal trapezoid; trapezoidal/S-curve both reach the target distance within velocity and acceleration limits. Running example: planar 2-link arm L₁=0.4, L₂=0.3 (the engine is length-agnostic via the DH parameter table).

## 4. Verification

- **Notebooks:** all 8 execute clean end-to-end via nbclient Restart-and-Run-All (0 failures); each prints "All checks passed." Two checks were corrected during the build to use exact analytic endpoint derivatives rather than noisy boundary finite-differences (L03 linear-rejection via velocity; L06 class detection via `poly_eval`).
- **SVGs:** all 8 XML-valid; `role="img"` + `aria-label` + `viewBox`; no fixed root width; design-system colors. The flagship m07-l7 and the m07-l4 pipeline were visually rasterized and confirmed on-message.
- **Quizzes:** all 8 are self-contained interactive HTML (5 MC + 3 short), MathJax-enabled, no `localStorage`/`sessionStorage`.
- **Answer keys:** all 8 in coaches' format — MC letter + rationale, 3 short model answers + grading notes, and a "Common misconceptions to watch for" section.
- **Site:** generator wired (`"07"` in `MODULES`, module title, all 8 unit titles); run injected SVG/demo/notebook/quiz into every page; the visual-embed validator passed (no missing figure, no `[Visual:]` placeholder leaked). `mkdocs build --strict` **passes clean (exit 0)** at 205 lesson pages.
- **DoD matrix:** all 8 lessons meet every gate (12 sections · SVG · passing notebook · 5 MC + 3 short quiz · answer key · companion blocks · published site page).

## 5. Boundaries held

No feedback/closed-loop control and no dynamics (forces, torques, inertia) appear anywhere in Installment A. "Efficiency" is treated as a geometric/temporal proxy (time, jerk, path length, clearance), never energy. Open-loop execution appears only through the imported M6 velocity layer, used to demonstrate feasibility — never to correct error. The M7-defines-references / M8-tracks-references fence is stated in L04 and will be reinforced in L27 and L32.

## 6. Repository changes

- `modules/module07/lessons/lesson01..08_*.md` (8)
- `modules/module07/notebooks/lesson01..08_*.ipynb` (8)
- `modules/module07/demos/lesson07_polynomial_profile_shaper.html` (1)
- `modules/module07/quizzes/lesson01..08_quiz.html` (8)
- `assets/diagrams/m07-l1..l8-*.svg` (8)
- `coaches/answer-keys/module07/lesson01..08_answer_key.md` (8)
- `tools/generate_site_pages.py` — Module 07 registered (MODULES + module title + 8 unit titles)
- `mkdocs.yml` — Units 1–2 nav added (demo marked on 2.3)
- `curriculum/ARCHITECT_DECISIONS.md` — **D-061** appended (with the reconciliation flag)
- `curriculum/master_progress.md`, `curriculum/PROJECT_STATE.md` — updated to Module 7 IN PRODUCTION (Installment A)
- `site_src/module07/lesson01..08.md` + `site/` — generated; strict build passing

## 7. Milestone

**Installment A is complete and paused for architect review.** On approval, Installment B (Units 3–4 + midpoint assessment, D-062) follows, beginning with L09 (3.1) Point-to-Point Joint Moves: per-joint cubic polynomials — the first application of the Unit 2 timing toolkit, joint by joint.
