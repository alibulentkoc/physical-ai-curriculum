# Answer Key — Module 4 Midpoint Assessment

**Coaches only.** Formative readiness checkpoint; not graded.

## Part A

1. **Configuration vs pose.** Configuration = the vector of joint variables (joint space); pose = the gripper's position + orientation (task space, $SE(3)$). FK takes **configuration** as input and outputs pose.
2. **Single-valued forward, many-to-one.** A configuration determines exactly one pose (just evaluate the product). But different configurations can produce the same pose — e.g. elbow-up vs elbow-down both reach the same point.
3. **DOF.** A serial arm's DOF equals its number of joints; each joint contributes one DOF.
4. **General product.** $T_0^n(\boldsymbol{\theta}) = T_0^1(\theta_1)T_1^2(\theta_2)\cdots T_{n-1}^n(\theta_n)$. Base→tip because each factor expresses the next frame relative to the previous one; order matters because 3D rotations (and rigid transforms) don't commute.
5. **Reading $T_0^n$.** Position = the translation column (top three rows of the last column); orientation = the upper-left $3\times3$ rotation block. The rotation block's **columns** are the gripper frame's $x, y, z$ axes expressed in the base frame (one is the approach direction).

## Part B

6. **One joint, $L=0.5$, $\theta=120°$.** Position $(0.5\cos120°, 0.5\sin120°) = (-0.25, 0.433)$; orientation $120°$.
7. **Two-link, $(30°,60°)$.** Elbow $(0.4\cos30°,0.4\sin30°)=(0.346,0.2)$; accumulated $90°$; forearm $(0.3\cos90°,0.3\sin90°)=(0,0.3)$. Gripper $(0.346, 0.5)$, orientation $90°$.
8. **Matrix product.** Forming $T_0^1(30°)$ and $T_1^2(60°)$ and multiplying gives a rotation block for $30°+60°=90°$ and translation column $(0.346, 0.5)$ — identical to Q7. (Composition adds the rotation angles and carries the link translations.)
9. **Three-link, $(30°,60°,-30°)$.** Accumulated $\phi_1=30°,\phi_2=90°,\phi_3=60°$. Reaches: $(0.346,0.2)+(0,0.3)+(0.1,0.173)=(0.446,0.673)$; orientation $\phi_3=60°$.
10. **6-DOF.** $T_0^6$ has **six** $SE(3)$ factors. Changing $\theta_6$ generally moves the gripper position (unless the last link length is zero). Changing $\theta_1$ generally affects the orientation too (it rotates the whole downstream chain).

## Part C

11. **Forward easy, inverse hard.** Forward kinematics just *evaluates* a known product of matrices — one pass, always defined, one answer. Inverse kinematics *solves* $T_0^n(\boldsymbol{\theta}) = T_{\text{desired}}$ for $\boldsymbol{\theta}$ — a nonlinear system that may have zero, one, or many solutions, and generally no closed form. (Module 5.)
12. **Redundancy and orientation.** A redundant (≥7-DOF, or task-redundant) arm can hold the gripper at one position while rotating it through a family of configurations — useful to choose an approach angle that avoids the stem and neighboring fruit. Position-only planning would ignore the approach direction and could drive the hand into the plant.

---

*Use as a readiness signal. If a learner stumbles on B/C, point them to Unit 2 (one-joint transform), Unit 3 (chaining as a product), or Unit 4.3 (FK in code) before the DH units.*
