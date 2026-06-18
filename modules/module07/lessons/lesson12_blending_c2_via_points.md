---
module: 07
unit: 03
lesson: 3.4
title: "Blending for C² Continuity at Via-Points"
core_idea: "A cubic spline through via-points chooses the interior velocities and accelerations so the whole multi-segment trajectory is C² — it flows through every via-point without stopping and without an acceleration jump. The natural spline does this by solving one linear system for the knot second-derivatives."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L3.3 — Via-points and multi-segment trajectories"
  - "M7 L2.2 — Continuity classes and jerk"
learning_objectives:
  - "Explain how blending makes a multi-segment trajectory C² at the via-points."
  - "Describe a cubic spline as the C² interpolant that picks interior derivatives automatically."
  - "Use the engine's spline to build a flow-through trajectory and verify continuity at the via-points."
---

# Lesson 3.4 — Blending for C² Continuity at Via-Points

> Lesson 3.3 left a question: to flow through a via-point we need a *passing velocity* — but which one? Pick them wrong and the seams between segments jerk. The **cubic spline** answers it: it chooses every interior velocity and acceleration so the entire trajectory is $C^2$. This lesson builds that flow-through motion and closes Unit 3.

---

## 1. Why This Matters
Stop-at-each (3.3) was simple but stuttering. Flow-through needs a passing velocity and acceleration at each via-point, and those can't be guessed independently: the value that makes the *incoming* segment smooth must also make the *outgoing* segment smooth, or the seam jerks. Coordinating all of them at once is exactly what a **spline** does.

A cubic spline through the via-points produces a single $C^2$ trajectory: it passes through every via-point, never stops, and has **no acceleration jump** at any seam — the harvester glides through its safe via-points carrying fruit without a single jolt. This is the culmination of Unit 3: from one smooth joint move (3.1), to coordinated multi-joint moves (3.2), through routed via-points (3.3), to a smooth flow-through trajectory that threads them all (3.4).

## 2. Physical Intuition
Think of a flexible drafting spline — the thin wooden strip draftsmen bent through pins to draw smooth curves. Pin it at your via-points and let it relax: it passes through every pin, but between pins it takes the *smoothest* shape it can, with no kinks and no sudden changes in curvature. It automatically "decides" how fast and how curved to be at each pin so the whole strip is smooth — you don't set the slopes by hand; the strip's stiffness sets them for you by sharing the bending across pins.

A cubic spline is the mathematical version of that strip. Give it the via-points (the pins); it solves for the interior slopes and curvatures that make the whole curve $C^2$. The "no kinks" is $C^1$ (continuous velocity); the "no sudden curvature change" is $C^2$ (continuous acceleration). That is precisely the flow-through, jolt-free motion we wanted.

## 3. Mathematical Foundations
Interpolate one joint through knots $(t_0,y_0),\dots,(t_M,y_M)$ (the via-times and via-angles) with a **cubic spline**: a piecewise cubic $S(t)$ that is cubic on each $[t_k,t_{k+1}]$ and satisfies

$$S(t_k)=y_k\ \text{(passes through)},\quad S\in C^2\ \text{(continuous } S,\dot S,\ddot S \text{ at every interior knot).}$$

On each interval the cubic has 4 coefficients ($4M$ unknowns for $M$ intervals). The constraints: interpolation at both ends of each interval ($2M$), continuity of $\dot S$ at interior knots ($M-1$), and continuity of $\ddot S$ at interior knots ($M-1$) — that's $4M-2$. The remaining **2** come from boundary conditions; the **natural** spline sets $\ddot S(t_0)=\ddot S(t_M)=0$ (relaxed ends), while a **clamped** spline sets the end velocities.

Writing the unknowns as the knot second-derivatives $m_k=\ddot S(t_k)$, the $C^2$ conditions reduce to a **tridiagonal linear system**

$$h_{k-1}m_{k-1} + 2(h_{k-1}+h_k)m_k + h_k m_{k+1} = 6\!\left(\frac{y_{k+1}-y_k}{h_k}-\frac{y_k-y_{k-1}}{h_{k-1}}\right),\quad h_k=t_{k+1}-t_k,$$

for $k=1,\dots,M-1$, with $m_0=m_M=0$ (natural). Solve once; the interior velocities and accelerations fall out, and they are exactly the passing values that make the whole trajectory flow through the via-points $C^2$. For a multi-joint arm, run one spline **per joint** over the shared via-times — the joints stay coordinated.

The engine provides `cubic_spline_natural(ts, ys)` and `eval_spline(sp, t)` returning $(S,\dot S,\ddot S)$. The spline guarantees $C^2$ at interior knots by construction — the notebook checks that the acceleration matches across each seam.

**Why this is the blend.** "Blending" a via-point means smoothing the corner there. The spline blends *every* via-point simultaneously and optimally (smoothest $C^2$ interpolant), instead of hand-tuning each. Stop-at-each was the degenerate case where every passing velocity is forced to zero; the spline frees them.

## 4. Visual Explanation
`[Visual: a cubic spline through three via-points — position passes through every knot, velocity is continuous (no kinks), acceleration is continuous across every seam (C²)]`

**Diagram Specification**

- **Objective:** show the spline interpolating the via-points while keeping velocity and acceleration continuous at the seams.
- **Scene:** three stacked panels over time. Position: a smooth curve through start, two via dots, goal. Velocity: continuous, nonzero at the vias (marked "passes through, no stop"). Acceleration: continuous across each interior knot (mark the seams green, "C² — no jump"); contrast a faint dashed stop-at-each acceleration with red jumps at the seams.
- **Labels:** "spline (C²)" vs "stop-at-each (C¹ with halts)"; via-points as dots on all three panels.
- **Form:** SVG, 3 panels. Spline emerald `#10b981`; stop-at-each baseline error `#b91c1c` dashed; via dots violet.

## 5. Engineering Example
This is what a controller's "blend through waypoints with continuous acceleration" mode does under the hood, and what motion libraries (e.g., spline-based path interpolators in robot SDKs) compute for a list of waypoints. Feeding the harvester's safe-corridor via-points to a per-joint cubic spline yields a single smooth sweep from stow, through the canopy-clearing via, to the pre-grasp pose — no stops, no jolts, fruit undisturbed. The natural-spline "relaxed ends" suit a rest-to-rest overall move (zero end accelerations); a clamped spline is used when the trajectory must start or end matching a specific velocity (e.g., handing off to a Cartesian approach in Unit 4).

## 6. Worked Example
One joint through knots $(t,y)=(0,0^\circ),(1,60^\circ),(2,40^\circ)$ — the same route that stop-at-each handled with a halt in 3.3.

- Build the natural cubic spline: solve the tridiagonal system for $m_1$ (with $m_0=m_2=0$). With $h_0=h_1=1$: $4m_1 = 6[(40-60)-(60-0)]\cdot(\pi/180)$... numerically the spline yields a single smooth curve.
- At the via $t=1$: the spline passes through $60^\circ$ with a **nonzero** velocity (it's still rising slightly / turning over), and its acceleration is **continuous** across $t=1$ — no jump. Contrast 3.3, where the joint halted at $60^\circ$.
- The motion flows $0^\circ \to$ through $60^\circ \to 40^\circ$ as one $C^2$ glide. The notebook confirms interpolation at all knots, $\dot S$ and $\ddot S$ continuity at $t=1$, and a shorter/gentler profile than stop-at-each.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**Watch the seams stay smooth.** In the notebook you:

1. Build a natural cubic spline through three via-points with `cubic_spline_natural`.
2. Evaluate position, velocity, and acceleration densely and plot them.
3. Zoom in on an interior knot and confirm the acceleration matches from the left and the right ($C^2$) — then overlay the stop-at-each acceleration to see its jumps.

## 8. Coding Exercise
*(Snippet / notebook task — uses `cubic_spline_natural`, `eval_spline`.)*

In the companion notebook:

1. Fit a natural cubic spline through given via-points (one joint, then per-joint for the arm).
2. Assert the spline **interpolates** every knot exactly and that $\ddot S$ is continuous across each interior knot (left-limit ≈ right-limit) — a runnable proof of $C^2$.
3. Assert the via-point passing velocity is **nonzero** (it flows through, not stops), and compare total time/peak speed against the 3.3 stop-at-each baseline.

## 9. Knowledge Check
1. What does "blending" a via-point mean, and what continuity does a cubic spline deliver?
2. What unknowns does the natural cubic spline solve for, and via what kind of linear system?
3. How do natural and clamped boundary conditions differ?
4. How does stop-at-each relate to the spline as a special case?

## 10. Challenge Problem
You have via-points but must also **start and end at rest** (zero end velocity) *and* keep $C^2$ throughout. Which spline boundary condition do you use, natural or clamped, and what exactly do you clamp? Then argue why a *natural* spline (zero end acceleration) and a *clamped* spline (specified end velocity) can give different interior velocities for the same via-points — i.e., the boundary conditions propagate inward. *(This previews why a Cartesian hand-off in Unit 4 needs clamped, not natural, ends.)*

## 11. Common Mistakes
- **Hand-picking via velocities independently.** They're coupled; let the spline solve them together for $C^2$.
- **Forgetting per-joint splines must share via-times.** Different knot times per joint break coordination.
- **Assuming natural ends are always right.** If the move must start/finish at a nonzero velocity, use a clamped spline.
- **Reading the spline as collision-free.** A $C^2$ spline through via-points is *smooth*, not automatically *safe* — collision checking is Unit 6.

## 12. Key Takeaways
- A **cubic spline** through via-points is the $C^2$ interpolant: it passes through every via-point with **no velocity kink and no acceleration jump** at the seams.
- It **solves for the interior velocities/accelerations automatically** via a single tridiagonal system (the knot second-derivatives).
- **Natural** ends relax the end acceleration to zero; **clamped** ends fix the end velocity (used for hand-offs).
- **Unit 3 recap:** one smooth joint move (3.1) → synchronized multi-joint moves (3.2) → routed via-points (3.3) → a $C^2$ flow-through spline threading them (3.4). All joint-space; the **tool path stays curved** — which is exactly what Unit 4 takes on.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain cubic splines through via-points using the flexible drafting-spline analogy. Stress that the spline picks interior velocities/accelerations to be C². Then give me a three-knot spline to reason about."
- **Practice (generate exercises):** "Give me three via-point sets and ask me whether a natural or clamped cubic spline fits the stated end conditions, and what continuity the spline guarantees at the seams. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain where cubic/B-splines are used to smooth robot or CNC waypoint paths, and what 'natural' vs 'clamped' end conditions mean for a real move."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain cubic-spline blending through via-points for a robot: how it produces a C² flow-through trajectory by solving for the knot second-derivatives, and natural vs clamped ends, at a robotics-course level."
- **Español:** "Explica el suavizado por splines cúbicos a través de puntos de paso para un robot: cómo produce una trayectoria C² que fluye sin detenerse resolviendo las segundas derivadas en los nudos, y los extremos naturales vs sujetos (clamped), a nivel de curso de robótica."
- **中文（简体）：** "用机器人课程的水平，解释通过途经点的三次样条混合：如何通过求解节点二阶导数得到一条 C² 的不停顿穿越轨迹，以及自然端点与夹紧（clamped）端点的区别。"
- **Türkçe:** "Bir robot için ara noktalardan geçen kübik spline harmanlamasını açıkla: düğüm ikinci türevlerini çözerek nasıl C² akıp-geçen bir yörünge ürettiğini ve doğal (natural) ile kenetli (clamped) uçlar arasındaki farkı robotik dersi düzeyinde anlat."

---

*Next lesson: 4.1 — Why Cartesian Space? Straight-Line Tool Motion (Unit 4 begins — controlling the tool's path, not just the joints).*
