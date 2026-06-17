# Answer Key — Lesson 2.1: One Joint: Solve by Inspection

**Coaches only.** Formative.

1. **One-joint IK** — θ = atan2(y, x).
2. **Valid only when √(x²+y²)=L** — True.
3. **Why atan2 not arctan** — atan2 returns the correct quadrant (arctan(y/x) loses sign/quadrant).
4. **L=0.5, target (−0.354, 0.354) (short).** θ = atan2(0.354, −0.354) = 135°.

**Challenge rubric.** Full credit: a telescoping (prismatic) link makes any (x,y) within range reachable, and IK now solves for **two** variables — θ = atan2(y,x) and L = √(x²+y²). Partial: notes reachability improves without identifying the second solved variable.
