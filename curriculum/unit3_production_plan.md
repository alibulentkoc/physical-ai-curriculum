---
title: Unit 3 Production Plan — Coordinate Systems and Reference Frames
status: plan (approved topic map; production not yet started)
authority: architect decision (Unit 3 authorized, intuition-first, frames before transform math)
---

# Unit 3 Production Plan — Coordinate Systems and Reference Frames

> Unit 3 is one of the most important units in the curriculum. The governing idea is physical and must land before any transformation mathematics:
>
> **"The same tomato has different coordinates depending on who is looking."**
>
> This plan covers the topic map, per-lesson asset plan, the three required interactive demo specs, the asset inventory, and production sequencing. It follows the existing production standards (`curriculum/production_standards.md`) and the single-source generator (`tools/generate_site_pages.py`).

## Pedagogical stance (non-negotiable for this unit)

Lead with **physical intuition and visualization**; introduce notation only after the idea is felt. Across the unit: a tomato sits still in the greenhouse while *its coordinates change* as we change whose frame we measure in. No matrices in Unit 3 — frame transformation is taught **conceptually** (offset + rotation as ideas, computed numerically by hand-rolled helpers), saving matrix machinery for a later unit. Every lesson keeps the five-layer flow: physical intuition → visual → math (light) → computation → robotics context.

## Topic map (approved)

| Lesson | Title | Core idea (draft) |
|---|---|---|
| 3.1 | Why Coordinate Frames Matter | A position is meaningless without "relative to what"; frames give the reference. |
| 3.2 | Cartesian Coordinates | A point is an ordered tuple of signed distances along perpendicular axes from an origin. |
| 3.3 | 2D Coordinate Systems | Locate any point in a plane with (x, y); axes, origin, quadrants, units. |
| 3.4 | 3D Coordinate Systems | Add a third axis (z); right-hand convention; (x, y, z) in real space. |
| 3.5 | Local and Global Frames | The same point has different coordinates in world vs robot vs camera frames. |
| 3.6 | Conceptual Frame Transformations | Convert coordinates between frames via offset + rotation — as intuition, not matrices. |
| 3.7 | Robot and Camera Frames | A real pick: world, robot, and camera frames shown together; perception → action across frames. |

## Per-lesson asset plan

Every lesson: canonical markdown (12-section template) + `core_idea` + YAML frontmatter + ≥1 SVG + runnable notebook + interactive quiz + answer key (`coaches/`) + AI Companion + Global Learning Support + MkDocs page via the generator. Demos only where required/where manipulation clearly helps (heavy in this unit by design).

| Lesson | SVG (intuition-first) | Notebook | Quiz | Demo |
|---|---|---|---|---|
| 3.1 | one tomato, two observers reporting different coordinates | plot a point described from two origins | ✓ | optional (SVG may suffice) |
| 3.2 | axes/origin/signed-distance anatomy of a coordinate | build/plot points from coordinates | ✓ | — |
| 3.3 | 2D plane: axes, quadrants, a located point | place & read 2D points; quadrant logic | ✓ | optional |
| 3.4 | 3D axes (right-hand), a point at (x,y,z) | 3D point + distance; right-hand check | ✓ | optional (3D viewer is high-value if time allows) |
| 3.5 | same tomato, three labeled frames, three coordinate readouts | compute one point's coords in 3 frames | ✓ | **REQUIRED — viewpoint switcher** |
| 3.6 | offset + rotation turning one frame's coords into another's | hand-rolled convert_frame() (offset+rotation), no matrices | ✓ | **REQUIRED — conceptual transform** |
| 3.7 | world + robot + camera frames around a reach, simultaneously | full pick: camera→robot→world coordinate flow | ✓ | **REQUIRED — flagship tri-frame pick** |

SVG naming continues the convention: Unit 3 lessons are files `lesson17 … lesson23` → diagrams `m01-l17-* … m01-l23-*`, quizzes `lesson17_quiz.html …`, notebooks `lesson17_* …`. (Module stays 01; Unit 3 is the third unit of Module 1.)

## Required interactive demo specifications

All demos: self-contained HTML + vanilla JS + inline SVG; no dependencies, no browser storage; keyboard-operable; `aria-live` readouts; design-system colors; embedded via the generator at the lesson's "Interactive Demonstration" section with a validated "open in new tab" fallback.

### Demo 3.5 — Frame Viewpoint Switcher  (`lesson21_frames_viewpoint.html`)
- **Concept:** one physical tomato; its *coordinates* differ by frame.
- **Scene:** greenhouse top-down view with a fixed tomato. Three selectable origins/frames: **World** (corner of the greenhouse), **Robot** (mobile base), **Camera** (offset + rotated on the robot).
- **Interaction:** buttons/tabs to switch the active frame; the chosen frame's axes draw at its origin and the live readout shows the tomato's coordinates **in that frame**. The tomato never moves — only the numbers and axes do. Optional: drag the robot base and watch robot/camera coordinates update while world stays fixed.
- **Readout:** "Tomato in {frame} frame: (x, y)" + a one-line reminder that the object hasn't moved.
- **Learning goal:** internalize that coordinates are frame-relative.

### Demo 3.6 — Conceptual Frame Transform  (`lesson22_frame_transform.html`)
- **Concept:** convert a point's coordinates from one frame to another using **offset + rotation**, no matrices.
- **Scene:** two frames (A and B) with B offset and rotated relative to A; a point shown once, with both frames' axes.
- **Interaction:** sliders for B's offset (dx, dy) and rotation angle; live readout shows the point's coordinates in A and in B, plus the plain-language steps ("shift by the offset, then rotate by θ"). A "show the two steps" toggle animates translate-then-rotate conceptually.
- **Readout:** point in A, point in B, and the offset/angle currently applied.
- **Learning goal:** feel that a transform is just "re-describe the same point from a shifted, turned viewpoint."

### Demo 3.7 — Tri-Frame Pick (flagship)  (`lesson23_robot_camera_frames.html`)
- **Concept:** a real pick shown in **world, robot, and camera frames simultaneously**.
- **Scene:** greenhouse with a tomato; the robot base (robot frame) and a camera mounted with an offset+rotation (camera frame); world frame fixed at a corner. Three small linked panels (or one scene with three labeled overlays) each showing the tomato's coordinates in that frame.
- **Interaction:** step through perceive → reason → act: (1) camera "sees" the tomato (camera-frame coords), (2) convert to robot frame, (3) convert to world frame; a "play" button animates the robot approaching, with all three readouts updating live. Drag the tomato or move the robot to see every frame's numbers change in concert (world stays fixed to the room).
- **Readout:** tomato coordinates in all three frames at once, with the active conversion highlighted.
- **Learning goal:** see the perception→action pipeline as a chain of frame conversions — the payoff of the whole unit and the bridge back to Lesson 1.1's pipeline.

## Asset inventory plan (Unit 3 targets)

- **7 lessons** (3.1–3.7), canonical markdown, all with `core_idea` + the two standard sections.
- **≥7 SVGs** (one+ per lesson; 3.5 and 3.7 likely 2 each for multi-frame views).
- **7 notebooks**, each executed headless to "All checks passed."
- **7 interactive quizzes** + **7 answer keys** in `coaches/`.
- **3 required interactive demos** (3.5, 3.6, 3.7); 3.1/3.3/3.4 demos optional if they add value.
- **7 MkDocs pages** via the generator, added to nav under Module 1 (Unit 3).
- Build gate: `mkdocs build --strict` passes; all notebooks execute clean; all embeds + fallback links resolve.

## Production sequencing (recommended)

1. **Intuition core first:** 3.1 → 3.5 (build the "different coordinates" idea and its flagship-adjacent viewpoint demo early, since everything else serves it).
2. **Foundations:** 3.2 → 3.3 → 3.4 (Cartesian → 2D → 3D), straightforward SVG+notebook+quiz.
3. **Transformation intuition:** 3.6 (conceptual transform demo).
4. **Flagship:** 3.7 (tri-frame pick demo) last, as the synthesis.
5. Suggested installments to preserve quality: (A) 3.1–3.4 + the 3.5 viewpoint demo; (B) 3.5–3.7 with the 3.6 and 3.7 demos; then a short Unit 3 recap if the architect wants the Unit-2 pattern repeated.

## Recommendations before production begins

1. **Confirm the "no matrices in Unit 3" boundary** — frames/transforms taught conceptually (offset + rotation, hand-rolled helpers), with matrix form deferred to a later unit. This keeps Unit 3 intuition-first as directed.
2. **Confirm 3D approach for 3.4/3.7** — 3D-in-SVG is faux-3D (isometric). A true interactive 3D viewer (e.g. lightweight canvas) is higher value but more build effort; recommend faux-3D SVG + the interactive frame demos in 2D-with-depth unless the architect wants a 3D engine.
3. **Confirm demo count** — three required demos are heavy but appropriate for this unit; hold optional demos (3.1/3.3/3.4) unless review shows a need, to manage scope.
4. **Naming/numbering** — Unit 3 = files lesson17–lesson23, diagrams m01-l17…l23. Confirm acceptable, or switch to a per-unit asset namespace if preferred.
5. **Recap** — recommend a short Unit 3 recap ("Frames in Physical AI") mirroring 2.10, given Unit 3's importance.
