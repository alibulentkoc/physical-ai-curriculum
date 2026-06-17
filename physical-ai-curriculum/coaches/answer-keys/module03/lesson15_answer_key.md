# Module 3 · Lesson 4.3 — Answer Key (instructor only)
**Q1** the same extrinsics-then-intrinsics pipeline. **Q2 (match)** K=intrinsics; rvec/tvec=pose; distCoeffs=0=ideal pinhole. **Q3 (T/F)** True. **Q4 (short)** wrong principal point in K, or inverse-pose/wrong-frame (or leftover distortion).
**Coding rubric:** by-hand and cv2.projectPoints agree to tolerance (NumPy fallback if no cv2).
