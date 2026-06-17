---
module: 06
unit: 04
lesson: 4.1
title: "What the Tool Can and Cannot Do: Rank, Range, and Null Space"
core_idea: "At any pose the Jacobian sorts tool motions into three kinds — directions the tool can move (the range), directions it cannot (the orthogonal complement when rank drops), and joint motions that move the tool not at all (the null space, i.e. internal self-motion)."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L2.1 — ξ = J(q) q̇ as a sum of per-joint pushes"
  - "M6 L3.4 — Kinematic singularity = rank-deficient J"
  - "Linear algebra: rank, range (column space), null space"
learning_objectives:
  - "Read the range of J as the tool-velocity directions the robot can produce right now."
  - "Identify impossible directions as the orthogonal complement of the range when J loses rank."
  - "Interpret the null space of J as internal (self-)motions that don't move the tool."
  - "Connect all three to the robot's instantaneous capability before any metric."
tags:
  - rank
  - range
  - null-space
  - capability
---

# Lesson 4.1 — What the Tool Can and Cannot Do: Rank, Range, and Null Space

## 1. Why This Matters
Before measuring *how well* a robot moves, we should know *what it can move at all*. At
every pose the Jacobian answers three capability questions: which tool-velocity
directions are available, which are unavailable, and which joint motions are "wasted"
in the sense that they don't move the tool. Those are the range, the impossible
directions, and the null space. Getting this picture first — capability before any
number — is what makes the manipulability ellipsoid (next lesson) and its measure (the
one after) meaningful rather than abstract.

## 2. Physical Intuition
Jog the arm and feel the tool respond. In most poses you can push it in any direction
in the workspace — those are the **easy/available** directions, the ones the columns of
$J$ can combine to produce. Now fold or extend the arm to a singular pose and try to
move the tool in one particular direction: it simply won't go, no matter how you drive
the joints — an **impossible** direction. Finally, on a redundant arm, there are ways to
swing the elbow while the tool stays perfectly still — **internal motion** that the tool
never feels. Available, impossible, internal: three capability buckets, all read off
$J$.

## 3. Visual Explanation
`[Visual: three panels — (1) a non-singular arm with tool-velocity arrows fanning out in all directions (range = full); (2) a singular arm with arrows confined to a line and one direction crossed out (impossible direction); (3) a redundant arm with the elbow swinging while the tool stays fixed (null-space self-motion)]`
**Diagram Specification (multi-panel)**

- **Panel 1 — available directions:** non-singular arm; the columns of $J$ span the
  plane; tool-velocity arrows in many directions. Caption "range = reachable directions."
- **Panel 2 — impossible direction:** straight/singular arm; arrows collapse to a line;
  the perpendicular direction marked with an ✗. Caption "rank drops ⇒ a direction is
  lost."
- **Panel 3 — internal motion:** redundant (3-link) arm; elbow swung to a second pose
  with the **same** tool position; a looping arrow on the elbow, tool marked "still."
  Caption "null space = self-motion the tool doesn't feel."
- Overall caption: "Available · impossible · internal — the three things J tells you
  about capability."

## 4. Mathematical Foundations
*In words first:* the columns of $J$ are the per-joint pushes; what they can add up to is
the range, what they can't reach is impossible, and any joint-rate combination that
cancels to zero tool motion is the null space.

At configuration $\mathbf{q}$, with $\boldsymbol{\xi}=J(\mathbf{q})\dot{\mathbf{q}}$:

- **Range (column space)** $\mathcal{R}(J)$: all achievable tool twists. Its dimension is
  $\operatorname{rank}J$. These are the **available** directions.
- **Impossible directions:** the orthogonal complement $\mathcal{R}(J)^\perp$ in task
  space. It is empty when $J$ has full row rank; it becomes nonempty exactly at a
  **kinematic singularity** (Lesson 3.4), where some task direction drops out.
- **Null space** $\mathcal{N}(J)=\{\dot{\mathbf{q}}: J\dot{\mathbf{q}}=\mathbf{0}\}$:
  joint velocities that produce **no** tool motion — internal/self-motion. Its dimension
  is $n-\operatorname{rank}J$; a redundant arm ($n>$ task dimension) has a nonempty null
  space even away from singularities.

*Back to motion:* range = what the tool can do, its complement = what it can't, null
space = how the arm can rearrange itself for free. The SVD (Unit 6) will make all three
precise and quantitative; here we only need the capability picture.

## 5. Engineering Example
A 7-DOF arm reaching into a cluttered shelf uses its **null space** constantly: it keeps
the gripper on target (range) while swinging the elbow through self-motion to dodge a
shelf edge — the tool pose never changes. Meanwhile, if the planner drives the arm to a
near-singular stretch, a needed approach direction becomes nearly **impossible**, and the
joint rates required to fake it spike. Both behaviors are pure rank/range/null-space
phenomena, visible before any manipulability number is computed.

## 6. Worked Example
A **redundant** planar 3-link arm ($J_v$ is $2\times 3$) generically has rank 2 and a
**1-dimensional null space**: there is a joint-velocity vector
$\dot{\mathbf{q}}_{\text{null}}$ with $J_v\dot{\mathbf{q}}_{\text{null}}=\mathbf{0}$ — move
the joints that way and the tool does not budge (the elbow circulates). Separately, a
planar **2-link** arm stretched **straight** has rank 1: the two columns line up, the
tool can move tangentially but the **radial** direction (straight out along the arm) is
impossible. The notebook exhibits both — a null-space self-motion and a lost direction.

## 7. Interactive Demonstration
*(The manipulability ellipsoid gets its flagship interactive demo at L17. Guided
prediction here.)*

**Predict, then check.**

1. **Predict** the null-space dimension of a planar 3R arm (task dimension 2).
2. **Predict** which tool direction becomes impossible for a straight 2R arm.
3. **Check** in the notebook: find $\dot{\mathbf{q}}_{\text{null}}$ with
   $J\dot{\mathbf{q}}_{\text{null}}\approx 0$, and the impossible direction at the
   straight pose.

## 8. Coding Exercise
In the companion notebook:

1. For a planar 3R arm, compute $\operatorname{rank}J_v$ and a null-space vector; confirm
   $J_v\dot{\mathbf{q}}_{\text{null}}\approx \mathbf{0}$ (internal motion).
2. For a straight planar 2R arm, show rank drops to 1 and identify the impossible
   (orthogonal-complement) direction.
3. State, for each, which capability bucket you've demonstrated.

Prints `All checks passed.`

## 9. Knowledge Check
1. What does the range of $J$ represent physically?
2. When do impossible directions appear, and what are they?
3. What is a null-space joint motion, and which robots have one away from singularities?
4. Why look at capability (range/null space) before any manipulability number?

## 10. Challenge Problem
For a redundant arm, show that adding any null-space velocity to a joint-rate solution
leaves the tool twist unchanged. Explain why this is the basis for redundancy resolution
(elbow positioning, obstacle avoidance) that Unit 7 will build on — and why it exists
only when $n > \operatorname{rank}J$.

## 11. Common Mistakes
- **Confusing "impossible direction" with "null space."** One is a missing *task* output
  (rank-deficiency); the other is a *joint* motion with no output. Different spaces.
- **Assuming every arm has a null space.** Only when $n>\operatorname{rank}J$
  (redundancy, or at a singularity).
- **Treating range as fixed.** It changes with pose; a direction available now can be
  impossible after a singular configuration.

## 12. Key Takeaways
- Range of $J$ = available tool-velocity directions (dimension $=\operatorname{rank}J$).
- Impossible directions = $\mathcal{R}(J)^\perp$, appearing at kinematic singularities.
- Null space = internal/self-motion joint velocities ($\dim = n-\operatorname{rank}J$).
- This capability picture comes *first*; the ellipsoid and its measure quantify it next.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain range, impossible directions, and null space as
  available/impossible/internal motions, with the redundant-arm elbow example. Then quiz me."
- **Practice (generate exercises):** "Give me three problems on rank, range, and null
  space of robot Jacobians, including one redundant arm. Hold solutions."
- **Explore (connect to the real world):** "How do redundant arms use null-space motion
  for obstacle avoidance, and how do impossible directions show up near singularities?"

### Global Learning Support

- **English (authoritative):** "Explain the range, impossible directions, and null space
  of a manipulator Jacobian as a capability picture, at robotics-course level."
- **Español:** "Explica el rango, las direcciones imposibles y el espacio nulo del
  jacobiano como una imagen de capacidad, a nivel de robótica."
- **中文（简体）：** "用机器人学课程的水平，把雅可比的值域、不可达方向与零空间解释为机器人
  能力的图景。"
- **Türkçe:** "Jacobian'ın görüntü uzayını, imkânsız yönleri ve sıfır uzayını bir
  yetenek tablosu olarak robotik ders düzeyinde açıkla."

---

*Next lesson: 4.2 — The Manipulability Ellipsoid: A Picture of What the Robot Can Do.*
