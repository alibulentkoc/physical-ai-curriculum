---
title: Module 2 — Midpoint Assessment Key (instructor only)
position: After Unit 5
---

# Module 2 — Midpoint Assessment Key (instructor only)

## Part A — Concept checks
1. A $2\times2$ matrix fixes the origin ($M\mathbf{0}=\mathbf{0}$), so it can't translate; frame changes need translation. The homogeneous "1" gives a last column whose entries are added (multiplied by the 1), making translation a matrix.
2. **Rigid** = preserves all distances and angles (no stretch/shear). Robot motion is rigid because arms/bases move objects without deforming them.
3. Orientation = upper-left $3\times3$ rotation block; position = last column $(t_x,t_y,t_z)$; bottom row $= [0\ 0\ 0\ 1]$.
4. Matrix multiplication is non-commutative; e.g. "rotate 90° then move (3,0)" lands at (3,0) but "move then rotate" lands at (0,3).
5. camera→world $= T_{world\leftarrow arm}\,T_{arm\leftarrow cam}$; inverse (world→camera) $= T_{arm\leftarrow cam}^{-1}\,T_{world\leftarrow arm}^{-1}$.

## Part B — Build and apply
6. $\begin{bmatrix}0&-1&2\\1&0&1\\0&0&1\end{bmatrix}$.
7. Apply to $(1,0)$: $(0\cdot1-1\cdot0+2,\ 1\cdot1+0\cdot0+1)=(2,2)$. Rigidity: distance from $(2,1)$ [image of origin] to $(2,2)$ is 1, matching the original origin-to-$(1,0)$ distance of 1.
8. $\begin{bmatrix}1&0&0&0.4\\0&1&0&0.3\\0&0&1&0.9\\0&0&0&1\end{bmatrix}$; rolling $90°$ about $z$ replaces the upper-left block with $R_z(90°)$, translation column unchanged.
9. The point (w=1) picks up the translation; the direction (w=0) does not, because the translation column is multiplied by $w$.

## Part C — Compose and invert
10. Step by step: $T_1(1,0)=(0,1)$, then $T_2(0,1)=(2,1)$. Product $T_2T_1$ applied to $(1,0)=(2,1)$. Match. ✓
11. $T_1 T_2$ applied to $(1,0)$: translate→$(3,0)$, rotate→$(0,3)$ — different. The **translation column** of the product differs.
12. world→camera $= T_{arm\leftarrow cam}^{-1}\,T_{world\leftarrow arm}^{-1}$ applied to the world goal; undo the **last-applied** edge first (the world→arm edge), i.e. $(T_2T_1)^{-1}=T_1^{-1}T_2^{-1}$.

## Part D — Reasoning
13. Likely causes: (a) **wrong composition order** (e.g. swapped mount/pose product) — check by recomputing in physical order; (b) **missing/incorrect inverse** when bringing a world goal into the arm frame — check $T^{-1}T=I$; also a non-rigid block sneaking into a rotation slot. 
14. The two paths should compose to the same transform; disagreement means inconsistent edge data — a miscalibrated or stale transform somewhere on one path.

**Scoring stance:** readiness, not points. The decisive signals are correct **order** in composition and correct **inverse** usage (Part C). Strong Parts A–B but weak Part C → revisit Unit 5 before Units 6–8.
