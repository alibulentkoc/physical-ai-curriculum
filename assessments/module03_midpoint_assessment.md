---
title: Module 3 — Midpoint Assessment (Readiness Checkpoint)
position: After Unit 4 (Projection in Practice)
covers: [Unit 1 why perception, Unit 2 pinhole model, Unit 3 camera intrinsics K, Unit 4 full pipeline + OpenCV]
excludes: [lens distortion, back-projection, pixels-to-robot bridge, the mini project]
format: formative readiness checkpoint; unlimited attempts; not graded
---

# Module 3 — Midpoint Assessment (Readiness Checkpoint)

**Placement:** after Unit 4. The first half of Module 3 builds the entire *forward* map — world point to pixel — and makes it runnable and OpenCV-verified. This checkpoint confirms a student can project confidently before the second half *inverts* the map (distortion, back-projection, world-position estimate). It is formative — a readiness signal, not a grade.

**The readiness signal:** given a 3D point, a camera pose, and intrinsics $K$, can the student compute the exact pixel (and judge its validity), and reconcile their result with OpenCV? If yes, they are ready for Units 5–8.

---

## Part A — Concept checks (short answer)

1. Why does a single image give a *direction* (a pixel) rather than a 3D *position*? Use the words "many-to-one" and "depth."
2. State the pinhole projection equation and explain in one sentence what the divide-by-$Z$ does.
3. What does focal length trade off against, and why can't you increase both at once?
4. Write the intrinsic matrix $K$ and name each of its four parameters.
5. Name the two stages of the full projection pipeline and say which one is non-invertible.

## Part B — Build and apply

6. A 5 mm lens sits on a sensor with 0.004 mm pixels. Compute the focal length in pixels.
7. Build $K$ for $f_x=f_y=800$, principal point $(320,240)$. Project the camera-frame point $(0.08, 0.0, 0.4)$ to a pixel.
8. For the same $K$, where does any point of the form $(0,0,Z)$ image, and why?
9. A camera-frame point is $(0.5, 0, 0.4)$ in a $640\times480$ image with the $K$ above. Compute its pixel and classify it (in-frame / out-of-frame / behind camera).
10. A point has $Z = -0.2$ in the camera frame. What is its image, and how should code handle it?

## Part C — Pipeline and OpenCV

11. A world point $(0.06, -0.03, 0.3)$ is seen by a camera at the world origin with no rotation ($T_{\text{cam}\leftarrow\text{world}} = I$), $K$ as above. Compute the pixel through the full pipeline.
12. The same world point is now seen after the camera translates $0.1$ m along its $x$-axis. Which stage of the pipeline changes, and does the intrinsic stage change?
13. You call `cv2.projectPoints(pts, rvec, tvec, K, distCoeffs)`. Match each argument to its role, and state what `distCoeffs = 0` means.
14. Your hand-built projection and OpenCV's disagree by a constant offset. List two likely causes.

---

## Answer key (instructor)

**A1** Forward projection is many-to-one: all 3D points on one ray share a pixel, so depth (and thus position) is lost; the pixel encodes only direction. **A2** $x=fX/Z,\ y=fY/Z$; the divide-by-$Z$ shrinks things with distance (perspective) and discards absolute depth. **A3** Magnification vs field of view; both depend on $f$ oppositely (magnification $\propto f$, FOV $=2\arctan(w/f)$). **A4** $K=[[f_x,0,c_x],[0,f_y,c_y],[0,0,1]]$: $f_x,f_y$ focal length in pixels; $c_x,c_y$ principal point. **A5** Stage 1 extrinsics (rigid, Module 2) and Stage 2 intrinsics ($K$, ÷Z); Stage 2 is non-invertible.

**A6** $5/0.004 = 1250$ px. **A7** $u=800\cdot0.08/0.4+320=160+320=480$; $v=240$ → $(480,240)$. **A8** The principal point $(320,240)$ for any $Z$, since $X/Z=Y/Z=0$. **A9** $u=800\cdot0.5/0.4+320=1000+320=1320$; $1320\ge640$ → out of frame (valid geometry, not captured); $v=240$. **A10** $Z\le0$ → behind the camera, no valid image; code must reject it.

**A11** $\mathbf P_c=(0.06,-0.03,0.3)$; $u=480$, $v=160$ → $(480,160)$. **A12** Stage 1 (extrinsics) changes — the camera-frame coordinates shift; the intrinsic stage ($K$) is unchanged. **A13** `pts`=3D points, `rvec`/`tvec`=camera pose ($R$ via Rodrigues, $\mathbf t$), `K`=intrinsics, `distCoeffs`=lens distortion; `distCoeffs=0` = ideal pinhole (no distortion), matching the hand-built pipeline. **A14** Wrong principal point in $K$, or an inverse-pose / wrong-frame mix-up (or leftover nonzero distortion).

**Readiness:** Parts A–B fluent and at least 3/4 of Part C correct → ready for Units 5–8. Struggles on the pipeline (Q11–12) → revisit Unit 4; struggles on $K$ (Q7–8) → revisit Unit 3.
