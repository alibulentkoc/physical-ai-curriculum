# Answer Key — Lesson 5.3: Undistortion

**Coaches only.** Formative.

1. **Undistortion produces** — the ideal pinhole point corresponding to a measured distorted pixel.
2. **Why iterative** — the distortion model has no closed-form inverse.
3. **Center ≈ unchanged** — True.
4. **OpenCV functions (short).** cv2.undistortPoints (points → normalized undistorted); cv2.undistort (whole image → pinhole view).

**Challenge rubric.** Full credit: explains that distortion is a polynomial in the unknown (can't simply subtract), and that iteration converges fast because distortion is small and smooth, especially near the center. Partial: states "no closed form" without the convergence reason.
