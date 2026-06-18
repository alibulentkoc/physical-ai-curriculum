---
module: 07
unit: 01
lesson: 1.3
title: "What Makes a Trajectory \"Good\": Smoothness, Continuity, Feasibility, Safety"
core_idea: "A good trajectory satisfies four qualities at once — smoothness (continuity of motion up to acceleration/jerk), feasibility (within velocity/acceleration limits), safety (collision-free and away from singularities), and efficiency (no waste). These are the acceptance criteria the rest of Module 7 learns to guarantee."
estimated_time: "35 min"
difficulty: "Introductory"
prerequisites:
  - "M7 L1.2 — Path vs trajectory"
  - "M6 — Singularities reduce control authority (D-060)"
learning_objectives:
  - "List the four quality criteria of a good trajectory and what each protects."
  - "Describe continuity classes C0/C1/C2 qualitatively and connect C2 to no force jumps."
  - "Explain feasibility as staying within joint velocity and acceleration limits."
  - "Explain safety as collision-free motion that avoids singular configurations."
tags:
  - physical-ai
  - robotics
  - smoothness
  - continuity
  - feasibility
  - safety
---

# Lesson 1.3 — What Makes a Trajectory "Good"

> We can now say *path* and *trajectory* precisely. This lesson names the four boxes a trajectory must tick to be acceptable for the greenhouse harvester — the checklist the whole module exists to satisfy.

---

## 1. Why This Matters
"Reach the tomato smoothly" is a goal, not a specification. Before we can *generate* good motion (Units 2–6) or *validate* it (Unit 7), we need to pin down what "good" means in checkable terms. Otherwise we cannot tell a planner "produce this" or tell a reviewer "accept this."

This lesson turns Lesson 1.1's three loose goals into **four concrete acceptance criteria** — smoothness, feasibility, safety, and efficiency — and gives each a definition precise enough to test later. Every generation technique in Module 7 is, in the end, a way to hit these criteria; every validation step in Unit 7 is a way to check them. Think of this as writing the rubric before doing the work.

## 2. Physical Intuition
Imagine four inspectors watching the harvester reach a tomato, each caring about one thing:

- The **comfort inspector** watches for jolts. Does the arm flow, or does it twitch and snap? (smoothness)
- The **motor inspector** watches the actuators. Is the arm asking a joint to spin faster or harder than it physically can? (feasibility)
- The **safety inspector** watches the surroundings. Does anything clip a stem, and does the arm wander into a pose where it suddenly can't move the way it needs to? (safety)
- The **manager** watches the clock and the wear. Is this the job done cleanly, or is there obvious waste — dawdling, detours, thrashing? (efficiency)

A trajectory is "good" only when **all four sign off.** A motion can be perfectly smooth yet demand impossible motor speeds (fails feasibility); or feasible and smooth yet drive the gripper through a leaf (fails safety). The criteria are independent, and you need all of them.

## 3. Mathematical Foundations
We keep this qualitative — the machinery comes in Unit 2 — but name each criterion precisely.

**Smoothness = continuity of the motion and its derivatives.** We grade how "connected" a motion is by **continuity class**:

- $C^0$ — **position is continuous** (no teleporting). The bare minimum; a $C^0$-but-not-$C^1$ motion can still have instantaneous velocity changes (corners).
- $C^1$ — **velocity is also continuous** (no sudden speed jumps). Better, but acceleration can still jump.
- $C^2$ — **acceleration is also continuous** (no sudden force changes). This is the usual target: because force is proportional to acceleration, a $C^2$ motion has no force discontinuities, so nothing gets shock-loaded.

Beyond $C^2$, we care about **jerk** $\dddot q$ (rate of change of acceleration) staying bounded — that is what kills the residual "twitch" and protects geartrains. So smoothness, ranked: $C^0 < C^1 < C^2 <$ bounded jerk.

**Feasibility = within the machine's limits.** Every joint has a maximum speed and a maximum acceleration:

$$|\dot q_i(t)| \le \dot q_i^{\max}, \qquad |\ddot q_i(t)| \le \ddot q_i^{\max}\quad\text{for all } t,\ \text{all joints } i.$$

A trajectory the motors cannot physically execute is infeasible no matter how pretty it looks on paper. (Unit 5 makes trajectories feasible by *time-scaling*.)

**Safety = collision-free and well-conditioned.** The motion must keep the arm clear of obstacles (canopy, stems, structure) along its *entire* length — not just at the endpoints — and should avoid the **singular** configurations of Module 6, where the arm loses the ability to move in some direction and joint rates can blow up.

**Efficiency = no waste.** Among trajectories that pass the first three, prefer shorter time, shorter path length, lower jerk, more obstacle clearance. (We make these into numbers — quality *metrics* — in Unit 7.)

## 4. Visual Explanation
`[Visual: a 2x2 "quality scorecard" — four panels (Smooth / Feasible / Safe / Efficient), each showing a pass example and a fail example in miniature]`

**Diagram Specification**

- **Objective:** present the four criteria as a single scannable rubric, each with a tiny good/bad illustration.
- **Scene / panels:**
  - *Smooth:* two acceleration-vs-time curves — one continuous (✓, emerald `#10b981`), one with a vertical jump (✗, error `#b91c1c`).
  - *Feasible:* a velocity curve under a dashed `q̇_max` line (✓) vs one poking above it (✗).
  - *Safe:* an arm path skirting a leaf/obstacle (✓) vs one cutting through it (✗); plus a small "✕ singular pose" marker.
  - *Efficient:* a short direct route (✓) vs a long looping one (✗).
- **Labels:** each panel titled; ✓/✗ paired with green/red and words (never colour alone).
- **Form:** SVG, 2×2 grid. Obstacle in muted slate; fruit rose `#e11d48`; limit lines dashed.

## 5. Engineering Example
Consider certifying the harvester for a customer. The acceptance test is literally these four checks run on every commanded reach:

1. **Smoothness:** log acceleration; reject if it shows step jumps (would indicate $C^2$ violation → shock loads).
2. **Feasibility:** log joint speeds/accelerations against datasheet limits; reject any excursion (the drive would saturate or fault).
3. **Safety:** sweep the planned arm volume against the canopy model; reject any intersection; flag any pass within the singularity band (conditioning from M6's `info`).
4. **Efficiency:** report cycle time and jerk; used to compare candidates, not to pass/fail.

This is not hypothetical — it is essentially the Unit 7 validation checklist we will build. Naming the criteria now means Unit 7 is just "implement the rubric."

## 6. Worked Example
Classify four candidate motions for the same reach. For each, decide which inspectors sign off (qualitatively):

| Candidate | Description | Smooth? | Feasible? | Safe? | Verdict |
|---|---|---|---|---|---|
| A | Snap at max speed, stop dead | ✗ (C¹ at best; accel jumps) | maybe | maybe | reject (jolts) |
| B | Gentle ease-in/out, but commands 3× the joint's top speed | ✓ (C²) | ✗ | ✓ | reject (infeasible) |
| C | Smooth and within limits, but the wrist clips a leaf at $s=0.6$ | ✓ | ✓ | ✗ | reject (collision) |
| D | Smooth, within limits, clears the canopy, stays well-conditioned | ✓ | ✓ | ✓ | **accept** |

Only **D** passes all three hard criteria; efficiency then chooses among multiple D-like options. The point: a single failing criterion sinks an otherwise excellent trajectory — which is why we generate *and* validate.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Spot the violated criterion.** The notebook plays four short motions (the table above) and, for each, plots position, velocity, acceleration, and an obstacle overlay. Your task before revealing the answer: name which inspector rejects it.

You should learn to *read* each criterion off a plot: smoothness from whether the acceleration curve has jumps; feasibility from whether velocity/acceleration cross their dashed limits; safety from whether the arm sweep touches the obstacle or enters the singularity band.

## 8. Coding Exercise
*(Snippet / notebook task.)*

In the companion notebook, write four tiny predicate functions on a sampled trajectory:

1. `is_C2_ish(q_t, dt)` — numerically estimate acceleration and flag large jumps between samples.
2. `within_limits(qd_t, qdd_t, vmax, amax)` — return True iff all samples respect the limits.
3. `min_clearance(traj, obstacle)` — return the smallest distance to the obstacle along the motion (negative ⇒ collision).
4. `worst_conditioning(traj)` — using M6's `analyze`, return the smallest $\sigma_{\min}$ encountered (small ⇒ near-singular).

Then run all four on each candidate and reproduce the verdict table. This *is* a preview of Unit 7's `validate_trajectory`; here we only build the predicates, not the planner that avoids the failures.

## 9. Knowledge Check
1. List the four quality criteria and give a one-word greenhouse failure each prevents.
2. What does $C^2$ continuity guarantee about the *forces* the arm experiences, and why?
3. A motion is perfectly smooth but commands a joint to exceed its top speed. Which criterion fails?
4. Why must the safety check cover the *whole* path and not just the start and goal poses?

## 10. Challenge Problem
You are handed a trajectory that passes smoothness and feasibility but spends a long stretch near a singular configuration (small $\sigma_{\min}$), though it never actually collides. Is it "safe"? Argue both sides: why a near-singular pass might be acceptable, and why a reviewer might still reject it (recall from M6 what happens to joint rates and conditioning near a singularity, and how that interacts with feasibility). What single change to the *path* would most cleanly resolve the concern?

## 11. Common Mistakes
- **Treating smoothness as the only criterion.** A beautiful $C^2$ curve that exceeds motor limits or hits a leaf is still rejected.
- **Checking only the endpoints.** Feasibility and safety are *along the whole motion*; the middle is where limits saturate and collisions happen.
- **Confusing $C^1$ and $C^2$.** Continuous velocity ($C^1$) still allows acceleration (force) to jump; $C^2$ is what removes shock loads.
- **Forgetting singularities count as a safety/feasibility issue.** Near a singularity the arm may need impossible joint rates to follow the path — a feasibility failure dressed up as geometry.
- **Optimizing efficiency first.** Efficiency only ranks trajectories that already pass the three hard criteria; never trade away safety for speed.

## 12. Key Takeaways
- A **good trajectory** satisfies four criteria: **smooth**, **feasible**, **safe**, and **efficient** — all four, independently checkable.
- **Smoothness** is graded by continuity class: $C^0$ (position) $< C^1$ (velocity) $< C^2$ (acceleration — no force jumps) $<$ bounded **jerk**.
- **Feasibility** is staying within joint velocity and acceleration limits *everywhere along the motion*.
- **Safety** is collision-free motion that also avoids the ill-conditioned/singular configurations of Module 6; **efficiency** ranks the survivors.
- These four are the rubric the rest of Module 7 generates toward and Unit 7 validates against.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain the four trajectory-quality criteria (smooth, feasible, safe, efficient) and the continuity ladder C0→C1→C2→bounded jerk. Emphasize why C2 means 'no force jumps.' Then ask me to classify two example motions."
- **Practice (generate exercises):** "Describe five robot motions, each violating exactly one of {smooth, feasible, safe, efficient}. Ask me which criterion fails for each. Reveal answers after I respond."
- **Explore (connect to the real world):** "Where do these same four criteria appear outside robotics — elevators, roller coasters, drone flight, vehicle ride comfort? Explain how each field enforces smoothness and feasibility."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain what makes a robot trajectory 'good': the four criteria smooth, feasible, safe, efficient, and the continuity classes C0/C1/C2 plus bounded jerk, at an introductory robotics level."
- **Español:** "Explica qué hace 'buena' a una trayectoria robótica: los cuatro criterios suave, factible, segura y eficiente, y las clases de continuidad C0/C1/C2 más jerk acotado, a nivel introductorio."
- **中文（简体）：** "用机器人入门水平，解释什么样的机器人轨迹算'好'：平滑、可行、安全、高效四项标准，以及连续性等级 C0/C1/C2 与有界加加速度（jerk）。"
- **Türkçe:** "İyi bir robot yörüngesini ne yapar: pürüzsüz, uygulanabilir, güvenli ve verimli dört ölçüt ile C0/C1/C2 süreklilik sınıfları ve sınırlı jerk kavramını giriş seviyesinde açıkla."

---

*Next lesson: 1.4 — The Motion Pipeline: plan → parameterize → velocity layer (M6) → track (M8), and where Module 7 begins and ends.*
