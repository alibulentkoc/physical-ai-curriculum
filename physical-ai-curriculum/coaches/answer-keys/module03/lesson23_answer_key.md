# Answer Key — Lesson 6.3: Back-Projection in Code

**Coaches only.** Formative.

1. **Many depth pixels yield** — a point cloud.
2. **Invalid depths (Z≤0/NaN)** — filtered out before deprojecting.
3. **Round-trip recovers the pixel** — True.
4. **12-px reprojection error causes (short).** Any two of: wrong K, depth/color misalignment, distortion not removed before deprojecting.

**Challenge rubric.** Full credit: lists wrong K, depth/color misalignment, and un-removed distortion, with a sensible check order (verify K first, then alignment, then distortion). Partial: lists causes without order.
