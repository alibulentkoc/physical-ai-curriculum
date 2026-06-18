---
module: 7
type: midpoint_assessment_answer_key
title: "Module 7 Midpoint Assessment — Coaches' Answer Key"
audience: coaches
---

# Midpoint Assessment — Coaches' Key (Units 1–4)

Grading philosophy: reward the **motion** explanation first; the algebra supports it.
Give partial credit for correct intuition with minor formula slips. The recurring theme to
listen for: *geometry (path) vs timing (trajectory); smoothness measured by continuity
class; joint-space is simple but curves the tool; Cartesian controls the tool path at a
cost; everything M7 produces is an open-loop reference that M6 executes and M8 will track.*

## Section A
**A1.** A **path** $q(s)$ is pure geometry — the ordered configurations, no clock. A
**trajectory** $q(t)=q(s(t))$ adds the **timing** via $s(t)$: same geometry, now with a
speed schedule. The trajectory carries the timing. *(Unit 1.2.)*
**A2.** Smooth (else bruised fruit / drivetrain shock), feasible (else commands exceed
limits / unreachable), safe (else collision with stems/canopy or loss of control near a
singularity), efficient (else wasted time/distance/energy). *(Unit 1.3.)*
**A3.** Plan the path → parameterize it in time (trajectory) → execute **open-loop** through
the M6 velocity layer → **track** with feedback (Module 8). The M7/M8 boundary is between
execute and track: M7 (through execute) is open-loop; **feedback/tracking is M8**. *(Unit 1.4.)*

## Section B
**B1.** $C^0$: position continuous. $C^1$: position and velocity continuous. $C^2$:
position, velocity, and acceleration continuous. $C^2$ matters because force tracks
acceleration ($F\propto\ddot q$), so continuous acceleration means **no force jumps** (no
shock loads). *(Unit 2.2.)*
**B2.** Cubic → $C^1$ (zero endpoint velocity, but a nonzero endpoint acceleration jump);
quintic → $C^2$ (zero endpoint velocity *and* acceleration). The quintic pays with a
slightly **higher mid-move peak** velocity/acceleration over the same move and time.
*(Unit 2.3.)*
**B3.** Cubic endpoint accel $=1.2\cdot 6/1.5^2 = 1.2\cdot 6/2.25 = 3.2\ \text{rad/s}^2$.
Quintic peak speed $=1.2\cdot 15/(8\cdot1.5)=1.2\cdot 1.25 = 1.5\ \text{rad/s}$. *(Units 2.3.)*

## Section C
**C1.** The configuration moves along the straight segment $q(t)=q_0+(q_f-q_0)s(t)$ — a
straight line in joint space. The tool position is $f(q(t))$, and forward kinematics $f$ is
**nonlinear** (sines/cosines of the joint angles); a nonlinear map sends a straight line to
a curve, so the tool path bows. *(Unit 3.1.)*
**C2.** $T_i^{\min}=15|\Delta q_i|/(8\cdot2)=0.9375\,|\Delta q_i|$ with
$\Delta q=(1.571,0.524,0.785)$ rad → $T_1^{\min}=1.47$ s, $T_2^{\min}=0.49$ s,
$T_3^{\min}=0.74$ s. $T^\star=\max=1.47$ s; **joint 1** is the bottleneck. *(Unit 3.2.)*
**C3.** Stop-at-each runs rest-to-rest segments — it passes through each via-point but the
joint **stops** there (zero velocity); simple but slow and stuttering. Flow-through assigns
nonzero passing velocities so the motion **glides** through. A **cubic spline** through the
via-points is $C^2$ at every seam (continuous position, velocity, acceleration — no
acceleration jump) and the via velocity is **nonzero** (flows through, no stop). *(Units 3.3–3.4.)*

## Section D
**D1.** Recipe: interpolate the tool path $p(t)=p_0+(p_1-p_0)s(t)$ (straight line, smooth
$s(t)$), then solve $q(t)=\text{IK}(p(t))$ at each sample. New failure modes vs a joint move:
(1) a sampled point on the line can be **unreachable** even with reachable endpoints;
(2) the path can pass near a **singularity** where required joint rates blow up; (also accept
IK branch flips). *(Unit 4.1–4.2.)*
**D2.** An IK **branch** is one of the distinct configurations reaching the same tool pose
(elbow-up / elbow-down for the 2R arm). If the per-sample IK **flips** branches midway,
$q(t)$ **jumps** discontinuously (the full inter-branch distance) — a violent
reconfiguration even though the tool path is smooth. Keep consistency by choosing the
solution nearest the previous sample (or fixing the elbow sign). *(Unit 4.2.)*
**D3.** Averaging two rotations gives a non-rotation (it skews/shrinks) because orientation
lives on a curved space. **SLERP** instead slides along the great-circle arc: it is
(i) always a valid rotation, (ii) the **shortest** arc, (iii) **constant angular rate**.
For the planar arm it reduces to **shortest-arc angle interpolation** (wrap the angle
difference into $(-\pi,\pi]$ and interpolate). *(Unit 4.3.)*

## Section E
**E1.** (a) **Joint move** — only the endpoints matter; fast and joint-feasible.
(b) **Cartesian** — the tool must travel straight in, which a curved joint move can't
guarantee. (c) **Cartesian** — the seam is a straight tool path (the product is the path).
*(Units 3.1, 4.1.)*
**E2.** Build a per-joint **cubic spline** (one per joint, sharing the via-times) through
stow → safe via → pre-grasp: it passes through the via-point without stopping and is $C^2$
at the seams (no jolt) — a single smooth joint-space glide. The **final approach** switches
to a **Cartesian straight-line** move (interpolate the tool position + IK per sample, fixed
elbow branch), because the tool must come straight in along the approach direction — a path
constraint a joint move can't promise. Award credit for: spline for flow-through $C^2$ in
joint space, *and* the deliberate switch to Cartesian for the path-controlled approach.
*(Units 3.4, 4.1–4.2.)*
**E3.** The statement is wrong on the **M7/M8 boundary**: correcting the arm back onto the
path when it drifts is **feedback tracking**, which is **Module 8**, not Module 7. The
Module 7 generator produces an **open-loop reference trajectory** $q(t)$; the **Module 6
velocity layer executes it open-loop** (no error correction). M7 *defines* the reference;
M8 will *track* it. *(Unit 1.4 boundary.)*

---

### Common misconceptions to watch for
- Calling the cubic "$C^2$" because it starts/ends at rest — it's only $C^1$ (nonzero
  endpoint acceleration); the quintic is $C^2$.
- Expecting a straight tool path from a joint move (it curves), or a straight joint path
  from a Cartesian move (the joints curve).
- Assuming reachable endpoints imply a reachable straight line between them.
- Forgetting IK branch consistency — a flip is a joint-space jump even on a smooth tool path.
- Attributing feedback/tracking to Module 7; that's the Module 8 job.
