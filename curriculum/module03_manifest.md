---
title: Module 3 — Manifest
module: 03
title_full: Camera Geometry and Robotic Perception
status: IN PRODUCTION
theme: Greenhouse Harvesting Robot (continuous with Modules 1–2)
prerequisite: Module 2 (Spatial Transformations and SE(3)) complete
tooling_introduced: OpenCV (alongside NumPy, Matplotlib)
---

# Module 3 — Manifest: Camera Geometry and Robotic Perception

## What this module is

Module 2 ended with a promise: the perception-to-pose pipeline took the tomato's 3D position **as given in the camera frame**, deferring *how the camera produces that 3D coordinate from an image*. **Module 3 keeps that promise.** It answers: **how does a camera turn the world into pixels, and how do we go back from pixels to a 3D position the robot can act on?**

The arc:

- **Module 1:** the math substrate (frames, vectors, matrices).
- **Module 2:** rigid transforms and the camera→robot→world chain (extrinsics), assuming a 3D detection.
- **Module 3:** the camera itself — projection, intrinsics, image formation, distortion — turning a fruit in the world into pixels and a pixel (plus depth) back into a 3D point, which then feeds the Module 2 chain to a world pose.

By the end, a student can explain and compute the **pinhole projection** of a 3D point to a pixel, the role of the **intrinsic matrix K**, **lens distortion** and its correction, and **back-projection** (pixel + depth → 3D point in the camera frame) — then connect that 3D point to the Module 2 extrinsics chain to estimate a fruit's **world position**.

## The one new idea that unlocks the module

Module 2's transforms were all **rigid** (distance-preserving). A camera is different: projection is **not** rigid and **not** invertible on its own — it collapses 3D to 2D, throwing away depth. Module 3's central device is the **pinhole camera model with intrinsics**: a 3D camera-frame point projects to a pixel via $K$; recovering 3D requires **extra information (depth)**. Perception is the art of adding back what projection removed.

## Educational stance (unchanged)

Five-layer flow on every lesson: **Physical Intuition → Visual Understanding → Mathematical Formulation → Computational Implementation → System Integration.** Lead with the physical camera and what it sees; do **not** open with the projection matrix. The greenhouse-harvesting-robot narrative continues — the camera is the robot's eye on the fruit.

## Scope and deferrals

**In scope:** pinhole model, perspective projection, focal length, image/pixel coordinates, principal point, the intrinsic matrix $K$, radial/tangential distortion and undistortion, back-projection with depth, the perception→camera-frame→world bridge (reusing Module 2 extrinsics), and an introduction to **OpenCV** for the computational layer. Detection is treated at the level of "a pixel location (and depth) for the fruit" — enough to estimate position.

**Deferred to later modules:** learned object detection / neural perception, stereo matching algorithms and SfM internals (we may *use* a depth value without deriving it), camera calibration as a full numerical-optimization procedure (we explain what calibration produces and use given intrinsics), and all kinematics/control (Modules 4+).

## Production contract (inherited)

- **Single-source generation:** canonical lessons in `modules/module03/lessons/`; site pages from `tools/generate_site_pages.py` (extend `MODULES`, `MODULE_TITLES`, `UNIT_TITLES`). `mkdocs build --strict` is the gate.
- **Per-lesson deliverables:** 12-section lesson + `core_idea` + YAML frontmatter + ≥1 SVG + runnable notebook (executes headless, ends "All checks passed.") + interactive quiz + answer key in `coaches/answer-keys/module03/` + AI Learning Companion + Global Learning Support. Demos where they add the most (projection is highly demo-friendly).
- **Numbering:** files `modules/module03/lessons/lessonNN_*.md`; diagrams `m03-lNN-*.svg`; quizzes/demos `lessonNN_*`; notebooks `M03_UUU_L*_*.ipynb`. Per-unit recaps; midpoint checkpoint; module mini-project/assessment.
- **Visuals:** 2D image-plane diagrams and faux-3D isometric for the projection geometry; interactive HTML demos for projection/intrinsics/distortion. No heavy 3D engine.
- **New tooling note:** OpenCV is introduced; a short `software_environment` note for Module 3 will accompany first use. Notebooks should degrade gracefully (use NumPy math directly where OpenCV is not essential, so they execute headless).

## Proposed module structure (units)

See `modules/module03/topic_map.md` for the lesson-level map. Proposed units (subject to architect confirmation at installment reviews):

1. **Why Perception** — the camera as the robot's eye; the world→pixels→world problem; what projection keeps and discards.
2. **The Pinhole Camera Model** — image plane, focal length, perspective projection of a 3D point.
3. **Camera Intrinsics** — the intrinsic matrix $K$; focal length in pixels, principal point, pixel coordinates.
4. **Projection in Practice** — projecting 3D camera-frame points to pixels; the projection pipeline; OpenCV introduction.
5. **Lens Distortion** — radial/tangential distortion and undistortion; why straight lines bend and how to fix it.
6. **Back-Projection: Pixels to 3D** — the inverse problem; a pixel is a ray; adding depth recovers a 3D point.
7. **From Pixels to the Robot** — bridge: camera-frame 3D point → (Module 2 extrinsics) → world position of the fruit.
8. **Mini Project: See the Fruit, Place It in the World** — capstone integrating Module 3 perception with the Module 2 transform chain.

## Directories

```
modules/module03/
  README.md
  learning_objectives.md
  topic_map.md
  assessments.md
  lessons/  notebooks/  demos/  quizzes/  assets/
```

## Through-line

Module 2 (extrinsics; detection assumed) → **Module 3 (the camera produces the detection: projection, intrinsics, distortion, back-projection; world-position estimate)** → Module 4+ (kinematics use the estimated target pose).
