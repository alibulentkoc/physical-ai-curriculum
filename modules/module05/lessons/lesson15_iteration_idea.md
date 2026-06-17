---
module: 05
unit: 04
lesson: 4.3
title: "The Iteration Idea: Guess, Measure Error, Step"
core_idea: "Numerical inverse kinematics repeats a simple loop: guess a configuration, measure the gripper's error from the target, and step the joints to shrink it using the Jacobian. Repeat until the error is small enough."
estimated_time: 45
difficulty: Core
prerequisites: [4.2]
learning_objectives:
  - State the guess–measure–step loop of numerical inverse kinematics.
  - Use the Jacobian to convert a gripper-error vector into a joint step.
  - Explain the roles of the seed, step size, and stopping tolerance.
tags:
  - physical-ai
  - kinematics
  - inverse-kinematics
  - numerical
  - iteration
---

# Lesson 4.3 — The Iteration Idea: Guess, Measure Error, Step

> With the Jacobian in hand, the numerical method is a short loop. This lesson assembles it: guess, measure how wrong the gripper is, step the joints to reduce the error, repeat. It is the engine Unit 5 refines.

---

## 1. Why This Matters

This loop is the heart of general-purpose inverse kinematics. Every numerical IK method — the ones in Unit 5, and the industrial solvers behind real robots — is a variation on guess–measure–step. Getting the core loop clear now means the refinements later (different step rules, damping, convergence handling) are recognizable as tweaks to one familiar idea rather than separate mysteries.

## 2. Physical Intuition

Reaching for something with your eyes closed, you might miss, feel how far off you are, and adjust — miss less, adjust again — until your hand lands on it. That is the loop. The "guess" is your first reach, the "error" is how far your hand is from the target, and the "step" is the correction. The Jacobian is what tells you *which way* to correct: it converts "my hand needs to move two centimeters left" into "so bend these joints by this much." A few rounds and you are there.

## 3. Mathematical Foundations

Target $\mathbf p_{\text{target}}$, forward map $f$, Jacobian $J$. Start from a **guess** $\boldsymbol\theta_0$ (a seed). Then repeat:

1. **Measure error.** Current gripper $\mathbf p = f(\boldsymbol\theta)$; error $\mathbf e = \mathbf p_{\text{target}} - \mathbf p$.
2. **Solve for a joint step.** We want a $\Delta\boldsymbol\theta$ that produces gripper change $\mathbf e$. Using the local linear map $\mathbf e \approx J\,\Delta\boldsymbol\theta$, solve

$$\Delta\boldsymbol\theta = J^{-1}\mathbf e \quad(\text{square } J), \qquad \text{or} \qquad \Delta\boldsymbol\theta = J^{+}\mathbf e \quad(\text{non-square: pseudoinverse}).$$

3. **Step.** $\boldsymbol\theta \leftarrow \boldsymbol\theta + \alpha\,\Delta\boldsymbol\theta$, where $\alpha \in (0, 1]$ is a step-size (gain) that keeps moves small enough for the linear approximation to hold.
4. **Check.** If $\|\mathbf e\| < \texttt{tol}$, stop (converged). If too many iterations, stop (failed to converge).

Three knobs govern behavior:

- **Seed $\boldsymbol\theta_0$** — determines *which* solution you land on (the nearest one) and whether you converge at all.
- **Step size $\alpha$** — too large overshoots (the linear map is only local); too small crawls.
- **Tolerance `tol`** — how close is "close enough," e.g. $10^{-4}$ m.

Because each step relies on the *local* Jacobian, the loop re-evaluates $J$ at the new configuration every iteration. This is the bare method (a Jacobian/Newton step); Unit 5 makes it robust.

## 4. Visual Explanation

`[Visual: a gripper walking toward a target over several iterations, the error vector shrinking each step, annotated guess → measure e → step Δθ = J⁺e → repeat]`

**Diagram Specification**
- **Objective:** show the loop as a shrinking-error walk to the target.
- **Scene:** a fixed target dot; the gripper at successive positions $\mathbf p_0, \mathbf p_1, \mathbf p_2, \dots$ approaching it; an error arrow $\mathbf e$ at each step getting shorter; a side box listing "1 measure e = p_target − p, 2 Δθ = J⁺e, 3 θ ← θ + αΔθ, 4 stop if |e| < tol."
- **Labels:** "seed θ₀," "error shrinks," "converged when |e| < tol."
- **Form:** SVG.

## 5. Engineering Example

The greenhouse arm seeds the solver at its *current* pose, so the loop converges to a solution close to where the arm already is — a short, smooth move to the fruit rather than a wild reconfiguration. Each iteration measures the gripper-to-fruit error, asks the Jacobian for the joint correction, and steps. In a handful of iterations the gripper is within tolerance, and the arm commits the move. Seeding from the current pose is also what makes the *redundancy* of Lesson 4.1 resolve sensibly.

## 6. Worked Example

Planar 2-link arm $L_1=0.4, L_2=0.3$, target $(0.5, 0.2)$, seed $(\theta_1,\theta_2) = (10°, 20°)$, gain $\alpha = 0.5$.

- Iter 0: $\mathbf p = f(10°,20°) \approx (0.667, 0.169)$; $\mathbf e = (0.5,0.2)-(0.667,0.169) = (-0.167, 0.031)$, $\|\mathbf e\|\approx0.170$.
- Compute $J$ at the seed, solve $\Delta\boldsymbol\theta = J^{-1}\mathbf e$, step $\boldsymbol\theta \mathrel{+}= 0.5\,\Delta\boldsymbol\theta$.
- Repeat; the error falls (roughly $0.170 \to 0.07 \to 0.02 \to \dots$) until $\|\mathbf e\| < 10^{-4}$ in a few iterations.

The arm converges to one of the two true solutions — whichever the seed was closer to. (The notebook runs the loop and prints the shrinking error.)

## 7. Interactive Demonstration

**Guided prediction.** For the worked example, predict whether seeding at $(10°, 20°)$ versus $(10°, -20°)$ lands on the elbow-down or elbow-up solution. Predict what happens with gain $\alpha = 1.5$ (overshoot) versus $\alpha = 0.1$ (slow). Then trace the first two iterations by hand-ish reasoning: error measured, step taken, error smaller.

## 8. Coding Exercise

Implement `ik_numerical(target, theta0, L1, L2, alpha=0.5, tol=1e-4, max_iter=100)` running the guess–measure–step loop with `jacobian_2link` and `np.linalg.solve` (or `pinv`). Return the solution, the iteration count, and the error history. Confirm it converges to a true solution (FK-verify), that the error history is decreasing, and that two different seeds reach the two different solutions. Use a fixed seed/tolerance so the self-check is deterministic.

## 9. Knowledge Check

Checks on the loop steps, $\Delta\boldsymbol\theta = J^{+}\mathbf e$, and the roles of seed, gain, and tolerance.

## 10. Challenge Problem

The bare step $\Delta\boldsymbol\theta = J^{-1}\mathbf e$ fails when $J$ is non-invertible (a special configuration). Without invoking the full theory (that is Module 6), explain what would go wrong in the loop at such a pose, and why Unit 5's *damped* step ($\Delta\boldsymbol\theta = J^\top(JJ^\top + \lambda^2 I)^{-1}\mathbf e$) is introduced to keep the iteration stable there.

## 11. Common Mistakes

- Forgetting to re-evaluate $J$ at each new configuration (it is local).
- Using a gain $\alpha$ so large the linear approximation breaks and the loop diverges.
- No iteration cap, so a non-converging case loops forever.
- Expecting the loop to find *all* solutions — it finds the one near the seed.

## 12. Key Takeaways

- Numerical IK is the loop: measure error $\mathbf e$, solve $\Delta\boldsymbol\theta = J^{+}\mathbf e$, step $\boldsymbol\theta \mathrel{+}= \alpha\Delta\boldsymbol\theta$, stop when $\|\mathbf e\| < $ tol.
- The Jacobian converts the gripper-error vector into a joint correction.
- Seed, step size, and tolerance govern which solution, stability, and accuracy.
- This bare loop is the engine; Unit 5 makes it robust (transpose, damped least squares, convergence handling).

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Re-explain Lesson 4.3 (Module 5) — the guess–measure–step loop of numerical inverse kinematics — using the eyes-closed reaching analogy. Show e = p_target − p, Δθ = J⁺e, θ ← θ + αΔθ, stop when |e| < tol.
```

**Practice prompt** — generate more exercises
```
Give me 5 exercises tracing the first iterations of a numerical IK loop for a planar 2-link arm: measure error, compute the joint step from J, and show the error shrinking. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how real robot solvers seed the iteration from the current pose, choose a step size, and decide when they have converged.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 4.3 (Module 5) — The Iteration Idea: Guess, Measure Error, Step.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 4.3 (Module 5) — The Iteration Idea: Guess, Measure Error, Step.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 4.3 (Module 5) — The Iteration Idea: Guess, Measure Error, Step.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 4.4 — From Geometry to Numerical IK (Unit 4 Recap · Midpoint).*
