# Answer Key — Lesson 5.4: Lens Distortion (Unit 5 Recap)

**Coaches only.** Formative consolidation.

1. **Forward map** — world → extrinsics → projection → distortion → K → pixel.
2. **Match** — k1,k2,k3 → radial; p1,p2 → tangential; undistortion → recover ideal pinhole point.
3. **Back-projection needs clean geometry** — True.
4. **Why undistort first (short).** Back-projection builds rays from the ideal pinhole model; a distorted pixel yields the wrong ray direction, so undistortion restores correct geometry before back-projection.

**Challenge rubric.** N/A (recap). Confirm the learner places distortion before K and connects undistortion to back-projection.
