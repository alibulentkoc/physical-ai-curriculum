---
module: 7
type: midpoint_assessment
title: "Module 7 Midpoint Assessment — Units 1–4"
covers: "Motion, paths & trajectories · time parameterization & smoothness · joint-space trajectories · Cartesian-space trajectories"
estimated_time: "60–75 min"
---

# Module 7 — Midpoint Assessment (Units 1–4)

You are halfway through Module 7. The first half built trajectory generation from the
ground up: from *what motion quality means*, to *how to time a motion smoothly*, to
*joint-space trajectories* (per-joint, synchronized, through via-points), to
*Cartesian-space trajectories* (straight-line tool motion, orientation, screw). This
assessment checks that arc. Sections A–D mirror the four units; Section E is integrative.
Computational items can be answered with the lesson notebooks.

Throughout, the running arm is the planar 2-link ($L_1=0.4,\ L_2=0.3$), and the
conventions are: $s\in[0,1]$ is the path parameter, $t$ is time, $T$ the duration.

---

## Section A — Motion, Paths, and Trajectories (Unit 1)

**A1.** Distinguish a **path** $q(s)$ from a **trajectory** $q(t)=q(s(t))$ in one or two
sentences, and state which one carries the *timing* of the motion.

**A2.** Name the four motion-quality criteria from Unit 1 and give a one-line greenhouse
failure that each one, if violated, would produce.

**A3.** State the four stages of the plan → parameterize → execute → track pipeline, and
mark precisely where the Module 7 / Module 8 boundary falls (which stage is open-loop and
which adds feedback).

## Section B — Time Parameterization and Smoothness (Unit 2)

**B1.** Define the continuity classes $C^0$, $C^1$, $C^2$ in terms of which derivatives are
continuous, and explain in one sentence why $C^2$ matters physically (relate it to force).

**B2.** A rest-to-rest **cubic** time scaling has endpoint acceleration $\ddot s(0)=6/T^2$.
A **quintic** has $\ddot s(0)=0$. State the continuity class of each and the price the
quintic pays for its smoother ends.

**B3.** For a rest-to-rest joint move of $\Delta q=1.2$ rad over $T=1.5$ s, compute the
cubic's endpoint acceleration $\ddot q(0)=\Delta q\cdot 6/T^2$ and the quintic's peak speed
$\dot q_{\max}=\Delta q\cdot 15/(8T)$.

## Section C — Joint-Space Trajectories (Unit 3)

**C1.** A joint-space point-to-point move is *straight in joint space but curved in task
space.* Explain why, naming the property of forward kinematics responsible.

**C2.** Three joints have displacements $\Delta q=(90^\circ,30^\circ,45^\circ)$ and a common
velocity limit $\dot q_{\max}=2$ rad/s, moved with quintics. Compute each joint's minimum
time $T_i^{\min}=15|\Delta q_i|/(8\dot q_{\max})$, give the synchronizing duration $T^\star$,
and name the bottleneck joint.

**C3.** Contrast **stop-at-each** and **flow-through** for via-points, and state what a
**cubic spline** through the via-points guarantees about the seams (which continuity class,
and what happens to the via velocity).

## Section D — Cartesian-Space Trajectories (Unit 4)

**D1.** State the **interpolate-then-IK** recipe for a straight-line Cartesian move, and
name two failure modes it introduces that a joint move does not have.

**D2.** Explain **IK branch consistency**: what an IK branch is, and what happens to
$q(t)$ if the branch flips midway along a straight tool path.

**D3.** Why can orientation **not** be interpolated by averaging two rotations, and what
does **SLERP** do instead (name its three defining properties)? State what SLERP reduces to
for the planar arm's single-angle orientation.

## Section E — Integrative

**E1.** *(Motion literacy.)* For each task, say whether you'd use a **joint move** or a
**Cartesian (straight-line) move**, and why, in one line each: (a) reposition the arm from
stow to a new plant; (b) make the final approach straight onto a tomato; (c) follow a
glue bead along a straight seam.

**E2.** *(Design.)* You must route the harvester from stow, through a safe via-point above
the canopy, to a pre-grasp pose, as one smooth motion that never stops and never jolts.
Describe the joint-space trajectory you'd build (what primitive threads the via-point, what
continuity it gives), and then describe how the *final straight approach* onto the fruit
would differ in method and why.

**E3.** *(Boundary.)* A teammate says "our Module 7 trajectory generator corrects the arm
back onto the path when it drifts." Identify the error in that statement using the M7/M8
boundary, and state what the trajectory generator actually produces and what executes it.

---

*Submit your work to your coach. The coaches' answer key lives in
`coaches/answer-keys/module07/midpoint_answer_key.md`.*
