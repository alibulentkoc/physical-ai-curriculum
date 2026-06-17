---
title: Unit 4 Production Plan — Matrices as Transformations
status: plan (approved topic map; production not yet started)
authority: architect decision (Unit 4 authorized; "Transformations of Space", not linear algebra)
---

# Unit 4 Production Plan — Matrices as Transformations

> Unit 4 is **not** a linear-algebra unit. It is **"Transformations of Space."** The central idea:
>
> **A matrix is not a table of numbers. A matrix is an action applied to space.**
>
> Students should first *see* rotation, scaling, reflection, and composition as geometric operations, before any algebraic manipulation. This unit cashes in Unit 3's conceptual "offset + rotation" as the compact matrix notation — the bridge was built in 3.6/3.8.

## Pedagogical stance (non-negotiable)

Geometry first, algebra second. Every lesson opens by *doing something to a shape* (the greenhouse object / gripper / fruit cluster) and only then names the matrix that did it. Keep the five-layer flow: physical intuition → visual → math → computation → robotics context. Tie every operation back to the robot: rotation = reorienting the gripper/camera; scaling = unit/zoom changes; reflection = mirrored views/handedness; composition = a real pipeline of moves where **order matters**.

Matrices now appear (Unit 3's no-matrix boundary is lifted), but introduced as *operators on space*, not as arrays to memorize.

## Topic map (approved)

| Lesson | Title | Core idea (draft) |
|---|---|---|
| 4.1 | Matrices as Operators | A matrix is an action on space: feed it a point, get a transformed point. |
| 4.2 | Matrix Addition | Adding matrices = combining/blending corresponding entries; limited geometric meaning vs multiplication. |
| 4.3 | Matrix Multiplication | Applying one transformation after another; the row–column mechanic *is* "apply the operator." |
| 4.4 | Identity Matrix | The "do nothing" operator: apply it and space is unchanged. |
| 4.5 | Rotation Matrices | Turning space about the origin by an angle θ. |
| 4.6 | Scaling Transformations | Stretching/shrinking space along axes. |
| 4.7 | Reflection Transformations | Mirroring space across an axis/line. |
| 4.8 | Composition of Transformations | Chaining scale → rotate → translate; **order matters** (flagship). |

## Per-lesson asset plan

Every lesson: canonical markdown (12-section template) + `core_idea` + frontmatter + ≥1 SVG + runnable notebook + interactive quiz + answer key (`coaches/`) + AI Companion + Global Learning Support + MkDocs page via the generator. Demos where the architect required them (4.4, 4.5, 4.8) and optionally where manipulation clearly helps (4.6, 4.7 are strong demo candidates).

| Lesson | SVG (geometry-first) | Notebook | Quiz | Demo |
|---|---|---|---|---|
| 4.1 | a point/shape going into a "matrix box" and coming out moved | apply a 2x2 to points with NumPy | ✓ | optional |
| 4.2 | entry-wise addition of two small matrices, side by side | add matrices; note it's not composition | ✓ | — |
| 4.3 | "apply A then B" pipeline; row·column highlighted | multiply matrices / apply to points | ✓ | optional |
| 4.4 | object before/after identity — visually unchanged | I·v = v check | ✓ | **REQUIRED — identity = do nothing** |
| 4.5 | object rotated about origin, angle θ marked | rotate points by θ; verify lengths preserved | ✓ | **REQUIRED — rotation slider 0°→360°** |
| 4.6 | object stretched along x and y (sx, sy) | scale points; area scales by sx·sy | ✓ | optional (slider) |
| 4.7 | object mirrored across an axis | reflect points; orientation flips | ✓ | optional (toggle) |
| 4.8 | scale→rotate→translate chain; and the reversed order differing | compose transforms; show order matters | ✓ | **REQUIRED — flagship composition** |

Naming continues the convention: Unit 4 lessons are files `lesson25 … lesson32`, diagrams `m01-l25-* … m01-l32-*`, quizzes `lesson25_quiz.html …`, notebooks `lesson25_* …`. (Module stays 01; Unit 4 is its fourth unit.) A Unit 4 recap (4.9) can follow the established pattern if the architect wants it (recommended, mirroring 2.10 and 3.8).

## Required interactive demo specifications

All demos: self-contained HTML + vanilla JS + inline SVG; no dependencies, no browser storage; keyboard-operable; `aria-live` readouts; design-system colors; embedded via the generator with a validated "open in new tab" fallback. Each shows the **matrix currently applied** alongside the geometry, reinforcing "matrix = the action you're watching."

### Demo 4.4 — Identity = Do Nothing  (`lesson28_identity.html`)
- **Concept:** applying the identity matrix changes nothing.
- **Scene:** a greenhouse object (a small fruit-cluster polygon) with its points listed; the identity matrix shown.
- **Interaction:** an "Apply matrix" button; when applied, the object visibly does not move; the readout shows input points = output points. A toggle to swap in a non-identity matrix briefly, to contrast ("see — that one *does* something; identity doesn't").
- **Learning goal:** internalize identity as the neutral operator (the "1" of transformations).

### Demo 4.5 — Rotation about the Origin  (`lesson29_rotation.html`)
- **Concept:** a rotation matrix turns space about the origin by θ.
- **Scene:** the greenhouse object and the origin; faint original (ghost) outline plus the live rotated object.
- **Interaction:** a single slider θ from **0° → 360°**; the object rotates live; the readout shows the rotation matrix for the current θ and confirms distances from the origin are unchanged (rotation preserves length). Optional: show one point's coordinates updating.
- **Learning goal:** see rotation as a geometric operation first; the matrix is just its description.

### Demo 4.8 — Composition: Order Matters (flagship)  (`lesson32_composition.html`)
- **Concept:** chaining **scale → rotate → translate**, and that **order matters**.
- **Scene:** the greenhouse object with a ghost of the original; the three operations as toggle/sliders (scale factor, rotation angle, translation offset).
- **Interaction:** apply the three in a chosen order and watch the result build up step by step; a prominent control to **swap the order** (e.g. rotate-then-translate vs translate-then-rotate) showing the end results differ; the combined matrix (and the sequence) displayed. A "step" mode animates one operation at a time.
- **Learning goal:** the signature Module-1 insight that composition is ordered — the conceptual seed of kinematic chains in Module 2.

## Asset inventory plan (Unit 4 targets)

- **8 lessons** (4.1–4.8), canonical markdown, all with `core_idea` + the two standard sections; optional **4.9 recap** (recommended).
- **≥8 SVGs** (geometry-first; before/after or ghost-outline style).
- **8 notebooks**, each executed headless to "All checks passed" (NumPy; rotation preserves length, scaling scales area, identity is neutral, composition is order-dependent).
- **8 interactive quizzes** + **8 answer keys** in `coaches/`.
- **3 required demos** (4.4, 4.5, 4.8); 4.6 and 4.7 demos optional (strong candidates).
- **8 MkDocs pages** via the generator, added to a new "Unit 4" nav section under Module 1.
- Build gate: `mkdocs build --strict` passes; all notebooks execute clean; all embeds + fallback links resolve.

## Production sequencing (recommended, geometry-first)

1. **Operator intuition:** 4.1 Matrices as Operators → 4.4 Identity (do-nothing demo) — establish "matrix = action," with the neutral action first.
2. **The signature actions:** 4.5 Rotation (slider demo) → 4.6 Scaling → 4.7 Reflection — the visible geometric operations.
3. **The mechanics, once the geometry is felt:** 4.3 Matrix Multiplication (= apply-then-apply) → 4.2 Matrix Addition (contrast: not composition).
4. **Flagship synthesis:** 4.8 Composition (order-matters demo) last.
5. Suggested installments: (A) 4.1, 4.4, 4.5 (operator + identity + rotation, with their demos); (B) 4.6, 4.7, 4.3, 4.2; (C) 4.8 flagship + optional 4.9 recap. Pause for review between installments as in Unit 3.

## Recommendations before production begins

1. **Confirm geometry-first ordering** (produce 4.1→4.4→4.5 before the multiply/add mechanics), even though the topic-map numbering lists 4.2/4.3 earlier. The lessons stay numbered 4.1–4.8; only the *production* order leads with intuition. Confirm acceptable.
2. **2D first, with a 3D nod.** Keep transformations in 2D for clarity (matches Unit 3's 2D-with-faux-3D approach); mention 3D/homogeneous coordinates only as a forward pointer to Module 2, not as content. Confirm.
3. **Translation within "matrix" transformations.** Pure 2×2 matrices can't translate; 4.8 needs translation. Recommend treating translate as a step in composition *conceptually* (and noting homogeneous coordinates are the Module-2 tool that folds translation into a matrix), rather than introducing 3×3 homogeneous matrices now. Confirm this boundary.
4. **Demo count.** Three required (4.4, 4.5, 4.8) confirmed; produce 4.6/4.7 demos too (cheap, high value) or hold them? Recommend producing at least 4.6 (scaling slider).
5. **Unit 4 recap (4.9).** Recommend yes, mirroring 2.10 and 3.8, to consolidate before Module 2.
6. **Numbering.** Unit 4 = files lesson25–lesson32 (+lesson33 if recap), diagrams m01-l25…l32(/l33). Confirm.
