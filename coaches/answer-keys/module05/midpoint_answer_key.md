# Midpoint Answer Key — Module 5 (Inverse Kinematics)

**Coaches only.** Formative readiness checkpoint after Unit 4. Not graded. Use $L_1 = 0.4,\ L_2 = 0.3$ for Part B.

---

## Part A — Concept checks

1. **Inverse problem as an equation.** Find $\boldsymbol\theta$ such that $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$ (or, position-only, $f(\boldsymbol\theta) = \mathbf p_{\text{desired}}$). Forward kinematics *evaluates* the function (plug in $\boldsymbol\theta$, read the pose — always one answer); inverse kinematics *solves* the equation for $\boldsymbol\theta$ (nonlinear, possibly 0/1/many answers).

2. **Nonlinearity and the three cases.** Joint angles enter through sine and cosine, so the equations are nonlinear. For the planar 2-link arm with reach $r = \sqrt{x^2+y^2}$: **0 solutions** when $r > L_1+L_2$ or $r < |L_1-L_2|$ (outside the annulus); **1 solution** when $r = L_1+L_2$ (arm straight) or $r = |L_1-L_2|$ (fully folded) — the boundary; **2 solutions** when $|L_1-L_2| < r < L_1+L_2$ (elbow-up / elbow-down).

3. **Reachable workspace.** The set of poses the arm can produce — the image of the forward map over the joint ranges. A target is solvable **iff** it lies in the workspace, so checking reachability first turns "no solution" into a clean, expected answer instead of a solver failure.

4. **atan2 vs arctan.** `atan2(y, x)` uses the signs of both components to return a quadrant-correct angle in $(-180°, 180°]$; `arctan(y/x)` only spans $(-90°, 90°)$ and loses the quadrant (and is undefined at $x=0$). Disagreement example: $(-0.5, 0.5)$ → `atan2` $= 135°$, `arctan` $= -45°$. (Any second/third-quadrant target is acceptable.)

5. **Decoupling.** Splitting the inverse problem into a position sub-problem (place the wrist center with the arm) and an orientation sub-problem (set the gripper orientation with the wrist). It is possible when the arm has a **spherical wrist** — its last three axes intersect at a point, so the wrist rotates the gripper in place without moving the wrist center.

## Part B — Build and apply

6. **(0.6, 0.0) reachable?** $r = 0.6$; annulus is $|0.4-0.3| = 0.1 \le r \le 0.7 = 0.4+0.3$. Since $0.1 \le 0.6 \le 0.7$, **reachable**.

7. **Closed form for (0.6, 0.0).** $\cos\theta_2 = \dfrac{0.36 - 0.16 - 0.09}{2(0.4)(0.3)} = \dfrac{0.11}{0.24} = 0.4583$ → $\theta_2 = \pm 62.72°$.
   - Elbow-down ($\theta_2 = +62.72°$): $\theta_1 = \operatorname{atan2}(0,0.6) - \operatorname{atan2}(0.3\sin62.72°,\ 0.4+0.3\cos62.72°) = -\operatorname{atan2}(0.2666, 0.5375) = -26.39°$. → $(-26.39°, +62.72°)$.
   - Elbow-up ($\theta_2 = -62.72°$): by symmetry $(+26.39°, -62.72°)$.

   Full credit: **both** pairs. Accept ±0.1° rounding.

8. **FK verification (elbow-down).** $x = 0.4\cos(-26.39°) + 0.3\cos(36.33°) = 0.3583 + 0.2417 = 0.600$; $y = 0.4\sin(-26.39°) + 0.3\sin(36.33°) = -0.1778 + 0.1777 \approx 0.000$. Lands on $(0.6, 0)$. ✓ (Either solution is acceptable.)

9. **Solution counts.**
   - $(0.7, 0.0)$: $r = 0.7 = L_1+L_2$ → **1** (outer boundary, arm straight).
   - $(0.3, 0.0)$: $r = 0.3$; inner radius $|L_1-L_2| = 0.1$, so $0.1 < 0.3 < 0.7$ → **2** (strictly inside). *(The "inner radius" prompt is to make them check it — $0.3$ clears it.)*
   - $(0.9, 0.0)$: $r = 0.9 > 0.7$ → **0** (beyond reach).

10. **Jacobian (2×2).**
$$J = \begin{bmatrix} -L_1\sin\theta_1 - L_2\sin(\theta_1+\theta_2) & -L_2\sin(\theta_1+\theta_2) \\ L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) & L_2\cos(\theta_1+\theta_2)\end{bmatrix}.$$
   Column 1 = how the gripper moves for a small change in $\theta_1$; column 2 = how it moves for a small change in $\theta_2$ (each column is $\partial\mathbf p/\partial\theta_j$).

## Part C — Reasoning

11. **3-link redundancy.** A planar 3-link arm has 3 joint angles for 2 position constraints — one extra degree of freedom. So for a reachable point there is a one-parameter **family** of solutions (fix the third joint anywhere and a 2-link sub-problem solves the rest). The 2-link arm has 2 angles for 2 constraints — a determined system with a discrete pair. A positive-dimensional solution family cannot be written by a finite closed-form formula, so (in general) redundant arms have **no closed form** and need numerical methods.

12. **The loop and the Jacobian's role.** Guess–measure–step: from a seed $\boldsymbol\theta_0$, (1) measure error $\mathbf e = \mathbf p_{\text{target}} - f(\boldsymbol\theta)$; (2) solve $\Delta\boldsymbol\theta = J^{+}\mathbf e$; (3) step $\boldsymbol\theta \mathrel{+}= \alpha\Delta\boldsymbol\theta$; (4) stop when $\|\mathbf e\| < \texttt{tol}$. The **seed** sets which solution is found (the nearest) and whether it converges; the **step size $\alpha$** trades speed against stability (too large overshoots the local linear map); the **tolerance** sets the accuracy. In Module 5 the Jacobian is used **only** as the solver's local linear map ($\Delta\mathbf p \approx J\Delta\boldsymbol\theta$). Its velocity interpretation, differential motion, manipulability, singularity theory, and SVD analysis are **deferred to Module 6** and should not be expected here.

---

## Scoring guidance

- **Ready for Units 5–8:** correct on Q1–Q3 (problem/reachability/counts), Q6–Q8 (closed form, both solutions, FK check), and Q12 (loop + Jacobian role). These are the load-bearing skills.
- **Remediation pointers:** A-section shaky → Unit 1; Q7/Q8 shaky → Lesson 3.1 (+ 3.2 for `atan2`); Q10–Q12 shaky → Lessons 4.2–4.3.
- **Common partial-credit cases:** giving only one of the two solutions in Q7 (revisit the ± in 3.1); using `arctan` and getting a wrong quadrant in Q4/Q7 (revisit 3.2); importing velocity/singularity ideas into Q12 (out of scope until Module 6).
