---
module: 07
unit: 06
lesson: 6.2
title: "Collision Checking: Is This Configuration Safe?"
core_idea: "Collision checking is the primitive test that decides whether a single configuration is in free space: compute the arm's geometry at that configuration and test it against the obstacle. A path is checked by testing densely-sampled configurations along it — fine enough not to tunnel through a thin obstacle."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L6.1 — Configuration space and C-obstacles"
  - "M2 — Forward kinematics (configuration → link geometry)"
learning_objectives:
  - "Implement a configuration collision test from the arm's link geometry and the obstacle."
  - "Check a path for collisions by sampling configurations along it densely enough."
  - "Explain why coarse sampling can tunnel through a thin obstacle and how to avoid it."
---

# Lesson 6.2 — Collision Checking: Is This Configuration Safe?

> Lesson 6.1 said the free space is where the arm doesn't collide — but how do we *test* a configuration? This lesson builds the **collision-checking primitive**: given joint angles and an obstacle, is the arm clear? It's the single most-called operation in any planner, and the gate that turns C-space from a picture into something computable. We lead with the geometric test, then checking whole paths.

---

## 1. Why This Matters
Everything in motion planning rests on one fast question, asked millions of times: *is this configuration safe?* The planner doesn't precompute the whole C-obstacle (too expensive in high dimensions); instead it **collision-checks individual configurations on demand** as it searches. So the quality and correctness of planning hinge on this primitive being both **correct** (it must catch real collisions) and **cheap** (it runs constantly).

Equally important is checking a *path*, not just a point. A motion is safe only if **every** configuration along it is safe — and since we can only test finitely many, we sample. Sample too coarsely and the check can **tunnel**: the arm is clear at each sampled instant but sweeps through a thin obstacle in between, like stepping over a tripwire because you only checked your foot position every two meters. Getting the configuration test right and sampling a path finely enough is what makes "collision-free" actually mean collision-free. For the harvester, this is the difference between a planned approach that's truly clear and one that clips a stem between samples.

## 2. Physical Intuition
To check if your arm hits a pole in a given pose, you don't think about "configuration space" — you just look at where your **upper arm and forearm** are and ask whether either touches the pole. That's the whole test: take the pose, work out where the limbs are in space, and check each limb against the obstacle. For a robot, "work out where the limbs are" is forward kinematics (Module 2/4): the configuration gives the elbow and tool positions, so each link is a known line segment in the workspace. The obstacle is a known shape. "Does the arm hit it?" becomes "does either segment come within the obstacle?"

Checking a *path* is like checking whether you can walk through a doorway carrying a ladder: it's not enough that the ladder fits at the start and end poses — it must clear the frame at **every** pose in between. You mentally sweep through the motion, checking continuously. A computer can't check continuously, so it checks at closely-spaced steps — close enough that the ladder can't swing through the frame between checks. The art is spacing the steps finely relative to how thin the obstacle is.

## 3. Mathematical Foundations
**Configuration collision test.** At configuration $\mathbf q$, forward kinematics gives the arm's geometry: for the planar 2R arm, the base $\mathbf b=(0,0)$, elbow $\mathbf e = \mathbf b + L_1(\cos q_1,\sin q_1)$, and tool $\mathbf t = \mathbf e + L_2(\cos(q_1{+}q_2),\sin(q_1{+}q_2))$. The two links are the segments $\overline{\mathbf b\mathbf e}$ and $\overline{\mathbf e\mathbf t}$. For a disk obstacle (center $\mathbf c$, radius $r$), the arm is **in collision** iff either segment comes within $r$ of $\mathbf c$:

$$\text{collision}(\mathbf q) \iff \min\big(d(\overline{\mathbf b\mathbf e},\mathbf c),\, d(\overline{\mathbf e\mathbf t},\mathbf c)\big) \le r,$$

where $d(\text{segment},\mathbf c)$ is the point-to-segment distance. This is `arm_hits_disk(q, center, radius)` in the engine; $\mathbf q\in\mathcal C_{\text{free}}$ iff it returns False. (Real systems use richer geometry — meshes, capsules, bounding volumes — but the principle is identical: build the body's geometry, test against the obstacle.)

**Path collision check.** A path is a sequence of configurations (or edges between them). Test an **edge** $\mathbf q_a\to\mathbf q_b$ by sampling configurations along it,

$$\mathbf q(u) = \mathbf q_a + u(\mathbf q_b - \mathbf q_a),\quad u\in\{0,\Delta,2\Delta,\dots,1\},$$

and collision-checking each; the edge is free iff all samples are free. The **step size** $\Delta$ (in C-space distance) must be small relative to the obstacle's thinness: if the arm can sweep across the obstacle in less than one step, the check **tunnels** (misses it). A safe rule is to choose $\Delta$ so the fastest-moving point on the arm moves less than the obstacle's smallest dimension per step. The engine's `edge_collision_free(qa, qb, ...)` samples at a fixed C-space step; `path_collision_free(path, ...)` chains the edge checks.

**Cost.** Each configuration check is $O(\text{links})$; an edge is $O(\text{length}/\Delta)$ checks. Planners call this constantly, so it's kept cheap — which is why C-space + on-demand checking beats precomputing the full C-obstacle.

## 4. Visual Explanation
`[Visual: a configuration collision test (arm segments vs disk, point-to-segment distance) and a path check sampling configurations along an edge — with a 'tunneling' case where coarse sampling misses a thin obstacle]`

**Diagram Specification**

- **Objective:** show the per-configuration test (segment vs disk) and dense path sampling, plus the tunneling failure of coarse sampling.
- **Scene:** **Left:** the arm at one configuration with the two link segments; a disk obstacle; the shortest distance from a link to the disk center drawn, with "collision if ≤ r". **Right:** an edge in the workspace sampled by several arm poses; top = dense sampling (catches the thin obstacle, green); bottom = coarse sampling (arm poses straddle the obstacle, missing it — red "tunneled").
- **Labels:** "point-to-segment distance ≤ r → collision"; "dense: caught" vs "coarse: tunneled through".
- **Form:** SVG, 2 panels. Clear emerald `#10b981`, collision/tunnel error `#b91c1c`, obstacle rose, arm ink.

## 5. Engineering Example
Collision checking is the inner loop of every motion planner and the backbone of simulation and digital-twin safety checks. Production systems wrap robot links and obstacles in fast geometric proxies (capsules, convex hulls, bounding-volume hierarchies) so a single check is microseconds, because the planner will run millions of them. Continuous collision detection (sweeping the volume between two poses) is used where tunneling must be ruled out exactly. For the harvester, the planner checks candidate configurations of the *whole arm* against a model of the canopy; the gripper alone being clear is never sufficient — a mid-link can foul a wire. The same primitive validates a finished trajectory before execution (the reachability/limit audit of Lesson 5.4 plus collision along the path).

## 6. Worked Example
Test configurations against the disk obstacle at $\mathbf c=(0.5,0.05)$, $r=0.06$ ($L_1=0.4,L_2=0.3$).

- **A clearly-free pose:** $\mathbf q=(\,-60^\circ, 40^\circ)$ (tool up-left, away from the disk). Compute $\mathbf e,\mathbf t$; both links are far from $\mathbf c$ → distance $>r$ → **free**.
- **A colliding pose:** a configuration whose forearm passes over $(0.5,0.05)$ → the segment $\overline{\mathbf e\mathbf t}$ comes within $r$ → **collision**.
- **An edge check:** the straight C-space edge from the start $(\text{tool }(0.45,0.25))$ to the goal $(\text{tool }(0.45,-0.25))$ — sampling along it finds an interior configuration in collision (a link crosses the disk), so the edge is **not** free. This is the blocked direct move from Lesson 6.1, now confirmed by the checker.
- **Tunneling demo:** with too coarse a step, the sampled poses straddle the thin disk and the edge is wrongly reported free; refining the step catches the collision. The notebook shows both.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Test, then sweep.** In the notebook you:

1. Collision-check individual configurations (a free one and a colliding one) with `arm_hits_disk`.
2. Check the straight start→goal edge and confirm it's blocked (an interior sample collides).
3. Demonstrate tunneling: coarsen the step until the check wrongly passes, then refine it until it correctly fails — internalizing the step-size rule.

## 8. Coding Exercise
*(Snippet / notebook task — uses `arm_hits_disk`, `edge_collision_free`, `path_collision_free`.)*

In the companion notebook:

1. Assert `arm_hits_disk` returns False for a clearly-free configuration and True for one whose link crosses the obstacle.
2. Assert the direct start→goal edge is **not** collision-free (an interior configuration collides) while a known detour edge **is**.
3. Reproduce **tunneling**: show that a too-large step reports a colliding edge as free, and that shrinking the step fixes it — making the sampling-density rule concrete.

## 9. Knowledge Check
1. How do you test whether a single configuration is in collision?
2. Why must a path be checked by sampling configurations along it rather than just at the endpoints?
3. What is tunneling, and how do you prevent it?
4. Why is the collision-checking primitive kept as cheap as possible?

## 10. Challenge Problem
You must collision-check an edge where the arm moves quickly through a region near a **thin** obstacle. Derive a rule for the maximum safe C-space step size in terms of the obstacle's thickness and how far the arm's fastest point moves per unit of C-space distance. Then explain the trade-off: smaller steps are safer but cost more checks, and describe one idea (e.g. adaptive stepping or swept-volume checking) to get safety without checking everywhere finely. *(This is the practical heart of making collision checks both correct and fast.)*

## 11. Common Mistakes
- **Checking only the gripper/tool.** Every link must be tested; a mid-link can collide while the tool is clear.
- **Checking only edge endpoints.** Interior configurations can collide; sample along the edge.
- **Sampling too coarsely (tunneling).** Choose the step small relative to the obstacle's thinness and the arm's speed.
- **Forgetting the obstacle's own size.** Collision is "within $r$ of the segment," not "segment passes through the center."

## 12. Key Takeaways
- **Collision checking** is the primitive that decides if a configuration is in free space: build the arm's link geometry (FK) and test it against the obstacle.
- A **path** is checked by **densely sampling** configurations along each edge and testing every one — all must be free.
- **Coarse sampling tunnels** (misses thin obstacles); pick the step small relative to obstacle thickness and arm speed.
- This primitive is the **inner loop** of planning — kept cheap because it runs constantly — and it's what makes C-space computable on demand.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain collision checking using the 'check where your limbs are' and 'carry a ladder through a doorway' analogies. Stress the per-configuration test and dense path sampling. Then ask me what tunneling is."
- **Practice (generate exercises):** "Give me three planar-arm configurations and a disk obstacle. Ask me to decide collision vs free using the link-segment-to-disk distance idea. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how real planners make collision checks fast (capsules, bounding volumes) and how continuous/swept collision detection avoids tunneling."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain collision checking for a robot arm: the per-configuration test (link geometry vs obstacle), checking a path by dense sampling, and tunneling from coarse sampling, at a robotics-course level."
- **Español:** "Explica la detección de colisiones para un brazo robótico: la prueba por configuración (geometría de los eslabones vs obstáculo), la comprobación de una trayectoria por muestreo denso, y el 'tunneling' por muestreo grueso, a nivel de curso de robótica."
- **中文（简体）：** "用机器人课程的水平，解释机械臂的碰撞检测：逐位形的测试（连杆几何 vs 障碍）、通过密集采样检查路径，以及粗采样导致的'穿隧'问题。"
- **Türkçe:** "Bir robot kolu için çarpışma kontrolünü açıkla: konfigürasyon-başına test (uzuv geometrisi vs engel), bir yolu yoğun örnekleme ile kontrol etme ve kaba örneklemeden kaynaklanan tünelleme'yi robotik dersi düzeyinde anlat."

---

*Next lesson: 6.3 — Finding a Safe Path: Sampling-Based Planning (RRT) (growing a tree through free space to the goal).*
