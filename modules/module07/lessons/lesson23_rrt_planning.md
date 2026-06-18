---
module: 07
unit: 06
lesson: 6.3
title: "Finding a Safe Path: Sampling-Based Planning (RRT)"
core_idea: "A Rapidly-exploring Random Tree (RRT) finds a collision-free path by growing a tree from the start: repeatedly sample a random configuration, extend the nearest tree branch a small step toward it (keeping only collision-free extensions), and connect to the goal when close. It explores free space without ever building the whole C-obstacle."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L6.1 — Configuration space and free space"
  - "M7 L6.2 — Collision checking (the primitive RRT calls)"
learning_objectives:
  - "Explain the RRT loop: sample, find nearest, steer a step, collision-check, connect to goal."
  - "Describe why sampling-based planning scales where grid search and full C-obstacle construction do not."
  - "Use the engine's RRT to find a collision-free path around an obstacle and read off its structure."
---

# Lesson 6.3 — Finding a Safe Path: Sampling-Based Planning (RRT)

> Lesson 6.2 gave us a way to test a configuration. Now we **search**: find a collision-free path from start to goal through free space. We won't build the whole forbidden region (too expensive) — instead we grow a tree that *explores* free space with random samples. The **RRT** is the practical, intuitive workhorse; we lead with how the tree spreads, then the loop.

---

## 1. Why This Matters
We can test any configuration (6.2), but the start and goal can be separated by a forbidden region, and the straight path between them blocked (6.1). We need an actual **search** for a route through free space. Two naive ideas don't scale: building the entire C-obstacle (the grid we drew in 6.1 was only feasible because the arm had two joints — it explodes with more joints), and gridding C-space and running a shortest-path search (same explosion). Real arms have six or seven joints; their C-space is six- or seven-dimensional, far too big to enumerate.

**Sampling-based planning** sidesteps this. Instead of mapping all of free space, it **probes** free space with random configurations and connects the safe ones into a tree reaching from start toward goal — calling the cheap collision check (6.2) only where it looks. The **RRT** (Rapidly-exploring Random Tree) is the canonical, intuitive version: it spreads quickly into unexplored regions and, given enough samples, finds a path if one exists. It's how a planner routes the harvester's whole arm around canopy obstacles without ever enumerating the forbidden region. We keep it practical — the loop and the intuition — not the theory.

## 2. Physical Intuition
Imagine exploring a dark, cluttered room from the doorway, trying to reach a far corner, by repeatedly doing this: pick a random spot in the room, walk from your **nearest already-explored point** a short step toward that spot, and if the step doesn't hit furniture, mark it as explored. Repeat. Your explored region grows like a tree of safe little hops, reaching outward and naturally **bending around** furniture (you can't step through it, so the tree flows around). Every so often you aim at the far corner; once you're close enough and the way is clear, you connect — and trace your hops back to the door to get a route.

That's an RRT. The "random spot" pulls the tree into unexplored areas (so it spreads fast); the "nearest point + small step" keeps it connected and local; the "if not blocked" is the collision check; "aim at the goal sometimes" biases it toward finishing. The tree never needs a map of the furniture — it discovers free space by hopping through it. The result is a collision-free path, found by exploration rather than by enumerating everything.

## 3. Mathematical Foundations
The **RRT** grows a tree $\mathcal T$ rooted at $\mathbf q_{\text{start}}$ in configuration space. Each iteration:

1. **Sample.** Draw a random configuration $\mathbf q_{\text{rand}}$ uniformly from $\mathcal C$ — but with small probability (**goal bias**) sample $\mathbf q_{\text{goal}}$ directly, to pull the tree toward the goal.
2. **Nearest.** Find the tree node $\mathbf q_{\text{near}}$ closest to $\mathbf q_{\text{rand}}$ (Euclidean distance in C-space).
3. **Steer.** Take a small **step** of size $\eta$ from $\mathbf q_{\text{near}}$ toward $\mathbf q_{\text{rand}}$: $\mathbf q_{\text{new}}=\mathbf q_{\text{near}}+\eta\,\frac{\mathbf q_{\text{rand}}-\mathbf q_{\text{near}}}{\lVert\cdot\rVert}$.
4. **Collision-check.** If the **edge** $\mathbf q_{\text{near}}\to\mathbf q_{\text{new}}$ is collision-free (Lesson 6.2), add $\mathbf q_{\text{new}}$ to $\mathcal T$ with parent $\mathbf q_{\text{near}}$; otherwise discard it.
5. **Try to connect.** If $\mathbf q_{\text{new}}$ is within a tolerance of $\mathbf q_{\text{goal}}$ and the edge to the goal is free, add the goal and **stop**: trace parents back from goal to start to recover the path.

Why it works in practice: the uniform sampling makes the tree **rapidly explore** (nodes are pulled toward the largest unexplored Voronoi regions), so free space fills quickly; the collision check confines growth to $\mathcal C_{\text{free}}$, so the tree bends around C-obstacles automatically. RRT is **probabilistically complete**: if a path exists, the probability of finding it approaches 1 as samples increase (stated as a fact, not proved here). The engine implements this as `rrt(q_start, q_goal, center, radius, rng, step, goal_bias, max_iter, goal_tol)`, returning a collision-free path (list of configurations) or `None`.

**What RRT is — and isn't.** It finds *a* feasible path, not the shortest or smoothest one (the raw path is jagged — Lesson 6.4 smooths it). We use **basic RRT** deliberately. We do **not** cover: optimal variants (RRT*) and other **optimization-based planning**, **kinodynamic** planning (planning velocities/accelerations together), or anything involving dynamics or feedback — all out of Module 7's scope. Here, the planner finds a geometric collision-free **path**; timing it into a feasible **trajectory** is the next lesson (the deliberate, non-kinodynamic decoupling: plan the path, then time-scale it).

## 4. Visual Explanation
`[Visual: an RRT growing from the start in C-space — random samples, nearest-node extensions bending around the C-obstacle, goal-biased connection, and the recovered start→goal path]`

**Diagram Specification**

- **Objective:** show the tree exploring free space and bending around the C-obstacle to reach the goal.
- **Scene:** the $(q_1,q_2)$ C-space with the shaded C-obstacle. A tree of edges rooted at the start spreads outward, visibly **avoiding** the obstacle (no edges enter it). A few faint random-sample dots with arrows to the nearest node show the extend step. The goal node is connected, and the recovered start→goal path is highlighted threading around the obstacle.
- **Labels:** "start", "goal", "$\mathcal C_{\text{obs}}$", "random sample → nearest → step", "recovered path (jagged)".
- **Form:** SVG, C-space panel. Tree edges muted/teal; obstacle error-tint; recovered path emerald `#10b981`; samples violet dots.

## 5. Engineering Example
Sampling-based planners (RRT and its relatives, and roadmap methods like PRM) are the standard in robotics motion-planning libraries — used for arm manipulation, mobile-robot navigation, and even protein folding — precisely because they scale to high-dimensional C-spaces where enumeration is hopeless. A 7-DOF arm reaching into a cluttered bin is planned this way: sample configurations, collision-check, grow a tree (or roadmap) until start connects to goal. For the harvester, the planner RRTs through the arm's joint space to route the *whole arm* from its current pose to a pre-grasp pose around the canopy's obstacles, then hands the jagged path to a smoother and a timer. The planner's only world-knowledge is the collision check from 6.2 — it never builds the forbidden region.

## 6. Worked Example
Plan around the disk obstacle $\mathbf c=(0.5,0.05)$, $r=0.06$ from start (tool $(0.45,0.25)$, elbow-up) to goal (tool $(0.45,-0.25)$, elbow-up) — both free, direct edge blocked (Lessons 6.1–6.2).

- Run `rrt` with step $\eta=0.2$, goal bias $0.15$, and a fixed seed. The tree grows from the start, repeatedly sampling and extending; edges that would cross the C-obstacle are rejected, so the tree flows around the band.
- Within a few thousand iterations (often far fewer) the tree reaches within tolerance of the goal with a clear connecting edge; the path is recovered by tracing parents.
- The returned path is a short list of configurations (e.g. ~8–18 nodes) that is **collision-free** (verified by `path_collision_free`) but **jagged** — it zig-zags because it's built from random steps. Re-running with a different seed gives a different (also valid) path: RRT is randomized.
- The notebook runs this, asserts the path is collision-free and connects start to goal, and shows two seeds giving two valid routes — motivating the smoothing of Lesson 6.4.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Grow a tree to the goal.** In the notebook you:

1. Run the RRT on the canonical obstacle scenario and plot the tree in C-space, the C-obstacle, and the recovered path.
2. Confirm the path is collision-free and connects start to goal; note how the tree avoided the obstacle without ever enumerating it.
3. Re-run with different seeds to see different valid paths — and observe that the raw paths are jagged (the cue for smoothing).

## 8. Coding Exercise
*(Snippet / notebook task — uses `rrt`, `path_collision_free`, a seeded rng.)*

In the companion notebook:

1. Run `rrt` on the obstacle scenario with a seeded generator; assert it returns a path that is **collision-free** and starts/ends at the start/goal configurations.
2. Assert the direct start→goal edge is blocked while the RRT path is free — the planner genuinely routed around the obstacle.
3. Run two or three seeds and confirm each yields a valid (collision-free, connecting) path, illustrating RRT's randomness — and measure each path's length to set up smoothing (6.4).

## 9. Knowledge Check
1. State the five steps of one RRT iteration.
2. What does the goal bias do, and what does the random sampling do?
3. Why does sampling-based planning scale where grid search or full C-obstacle construction does not?
4. Is the RRT path the shortest/smoothest? What is done about that?

## 10. Challenge Problem
RRT is *probabilistically complete* — it finds a path if one exists, eventually. But consider a planning problem where the only route passes through a very **narrow corridor** of free space. Explain why basic RRT can take a long time here (think about the chance a random sample + step lands in the corridor), and propose one practical adjustment (e.g. step size, goal/region biasing, or more samples) to help — *without* invoking optimal/optimization-based planners. Then explain why, if no path exists, RRT simply never returns one (it can't prove infeasibility). *(This is the practical character of sampling-based planning.)*

## 11. Common Mistakes
- **Expecting a clean, short path.** RRT returns a jagged, feasible path; smoothing comes next (6.4).
- **Forgetting the goal bias.** Pure random sampling explores but connects to the goal slowly; a small goal bias speeds finishing.
- **Skipping the edge collision check.** Checking only the new node (not the edge to it) can let an edge clip the obstacle — check the whole extension.
- **Assuming failure means no path.** Basic RRT can't prove infeasibility; "not found in N iterations" isn't "impossible."

## 12. Key Takeaways
- An **RRT** finds a collision-free path by **growing a tree** from the start: sample → nearest → small step → collision-check → connect to goal.
- It **explores free space** with random samples and the cheap collision check, **never building the whole C-obstacle** — so it scales to high-DOF arms.
- It returns *a* feasible, **jagged** path (not shortest/smoothest), and is **probabilistically complete** (finds a path if one exists, given enough samples).
- We use **basic RRT** only — no optimal/optimization-based, kinodynamic, dynamics, or feedback planning (out of Module 7's scope). Timing the path into a trajectory is Lesson 6.4.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain the RRT using the 'explore a dark cluttered room with small hops from your nearest explored point' analogy. Walk through sample → nearest → step → collision-check → connect. Then ask me what the goal bias does."
- **Practice (generate exercises):** "Quiz me on the RRT loop: give me partial descriptions of an iteration and ask me to fill in the missing step, and ask why it scales better than gridding C-space. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain where sampling-based planners (RRT, PRM) are used in robotics and why they dominate high-dimensional motion planning, keeping it intuitive (no optimization theory)."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain the RRT (Rapidly-exploring Random Tree) for robot motion planning: the sample/nearest/step/collision-check/connect loop, why it scales to high dimensions, and that it returns a jagged feasible path, at a robotics-course level (basic RRT only, no optimization)."
- **Español:** "Explica el RRT (árbol aleatorio de exploración rápida) para la planificación de movimiento de robots: el bucle muestrear/más cercano/paso/comprobar colisión/conectar, por qué escala a altas dimensiones, y que devuelve una trayectoria factible pero irregular, a nivel de curso de robótica (solo RRT básico, sin optimización)."
- **中文（简体）：** "用机器人课程的水平，解释用于机器人运动规划的 RRT（快速扩展随机树）：采样/最近点/步进/碰撞检测/连接的循环，为何能扩展到高维，以及它返回的是一条可行但锯齿状的路径（仅基础 RRT，不涉及优化）。"
- **Türkçe:** "Robot hareket planlaması için RRT'yi (Hızla-keşfeden Rastgele Ağaç) açıkla: örnekle/en yakın/adım/çarpışma-kontrol/bağlan döngüsü, neden yüksek boyutlara ölçeklendiği ve düzgün olmayan ama uygulanabilir bir yol döndürdüğü — robotik dersi düzeyinde (yalnızca temel RRT, optimizasyon yok)."

---

*Next lesson: 6.4 — From Safe Path to Feasible Trajectory: Smoothing and Time Scaling (turning a jagged path into a smooth, executable trajectory), and the Unit 6 recap.*
