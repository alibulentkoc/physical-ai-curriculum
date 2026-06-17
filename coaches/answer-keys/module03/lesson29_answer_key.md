# Answer Key — Lesson 8.1: The Project: Pixel to World

**Coaches only.** Project framing.

1. **Mini project produces** — a verified world-frame fruit position.
2. **One acceptance check** — re-projection within ~1 px.
3. **Reference result (1.06,0.47,0.4)** — True.
4. **Three acceptance checks (short).** Re-projection (≤~1px); distance preservation (rigid invariant); workspace plausibility.

**Challenge rubric.** Full credit: proposes a frame check such as verifying the result lies in the world frame by comparing against a known fixed landmark, or asserting the transform was actually applied (e.g., P_w ≠ P_c when extrinsics are non-identity); notes a frame bug yields P_w that re-projects fine (since the bug is post-camera) yet sits in the wrong place — which the distance check can miss if translation magnitudes coincide. Partial: any sensible fourth check.
