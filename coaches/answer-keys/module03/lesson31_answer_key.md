# Answer Key — Lesson 8.3: Verifying and Visualizing

**Coaches only.** Project verification.

1. **Re-projection fails but distance holds** — fault in the extrinsics / frame transform.
2. **Re-projection transforms P_w back using** — the inverse, T(cam←world)=T(world←cam)⁻¹.
3. **Passing distance alone ≠ correct** — True.
4. **Best check for wrong depth (short).** Distance preservation — a wrong Z changes the camera-to-fruit distance, breaking the rigid-invariant equality.

**Challenge rubric.** Full credit: defines a health score (e.g., weighted sum or min of normalized check margins), weights re-projection heavily (sub-pixel) since it catches the most faults, and sets a halt threshold (e.g., re-projection > a few px or distance error beyond sensor noise). Partial: reasonable score without justified weighting/threshold.
