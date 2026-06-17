# Answer Key — Lesson 7.2: From a Fruit's Grasp Pose to a Target Configuration

**Coaches only.** Formative.

1. **IK target frame** — the arm's base frame.
2. **Camera → base** — p_base = T_base^cam · p_cam.
3. **Grasp pose adds approach orientation** — True.
4. **Three things that must align (short).** Frames (everything in/transformed to the base frame), units (consistent metres), tolerances (perception + transform error below the grasp tolerance).

**Challenge rubric.** Full credit: combine errors in quadrature, √(3² + 2²) ≈ 3.6 mm, which is below the 4 mm tolerance — so it *usually* succeeds but with little margin; pushes the point that effort should go to the largest error source (perception, 3 mm) since reducing it shrinks the combined error most. Partial: adds errors without comparing to tolerance or identifying where to improve.
