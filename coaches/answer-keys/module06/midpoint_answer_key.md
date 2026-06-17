---
module: 6
type: midpoint_assessment_answer_key
title: "Module 6 Midpoint Assessment — Coaches' Answer Key"
audience: coaches
---

# Midpoint Assessment — Coaches' Key (Units 1–4)

Grading philosophy: reward the **motion/capability** explanation first; the algebra
supports it. Partial credit for correct intuition with minor formula slips.

## Section A
**A1.** $R\approx I+S(\delta\boldsymbol{\theta})$. Differential rotations commute because
the cross term $S_aS_b$ is second-order and drops; finite rotations keep that term.
**A2.** $\dot R=S(\boldsymbol{\omega}_s)R$ (spatial, left) or $\dot R=R\,S(\boldsymbol{\omega}_b)$
(body, right); $\boldsymbol{\omega}_s=R\,\boldsymbol{\omega}_b$ — one spin, two frames.
**A3.** $\mathbf{v}_P=(1,0,0)+(0,0,2)\times(0,y,0)=(1-2y,0,0)=0\Rightarrow y=0.5$. Re-reporting
about that point changes only the **linear** block (here to zero); $\boldsymbol{\omega}$ is
unchanged. *(Ties Units 1.3/1.4.)*

## Section B
**B1.** $\boldsymbol{\xi}=J(\mathbf{q})\dot{\mathbf{q}}=\sum_i\dot q_i J_i$: each column is one
joint's unit-rate tool twist; the tool twist is their rate-weighted sum.
**B2.** Revolute $[\mathbf{z}\times(\mathbf{o}_n-\mathbf{o}_{i-1});\mathbf{z}]$; prismatic
$[\mathbf{z};\mathbf{0}]$. Sliding translates the outboard arm without rotating it ⇒ zero
angular block.
**B3.** Perturb each joint $\pm\varepsilon$, central-difference the position for $J_v$; for the
angular part form $R(+)R(-)^\top$ and apply vee. Central differences are **second-order**
($\varepsilon^2$).

## Section C
**C1.** Geometric: true twist $[\mathbf{v};\boldsymbol{\omega}]$. Analytic: rates of a pose
representation $[\dot{\mathbf{p}};\dot{\boldsymbol{\phi}}]$. Position rows identical
($J_p=J_v$); orientation rows differ ($\dot{\boldsymbol{\phi}}$ vs $\boldsymbol{\omega}$).
**C2.** $\boldsymbol{\omega}=B(\boldsymbol{\phi})\dot{\boldsymbol{\phi}}$, $J_\omega=BJ_\phi$.
A column of $B$ is the angular velocity produced by moving one angle-dial at unit rate (the
axis that dial currently turns the body about).
**C3.** Inspect $\det B(\boldsymbol{\phi})$ → if it collapses (e.g. pitch ≈ 90°) it is a
**representation** singularity (switch representation; the robot is fine). Inspect the
rank/smallest singular value of $J(\mathbf{q})$ → if it collapses it is a **kinematic**
singularity (real; needs damping/path change).

## Section D
**D1.** Available = range $\mathcal{R}(J)$; impossible = $\mathcal{R}(J)^\perp$ (at rank
drop); internal = null space $\mathcal{N}(J)$.
**D2.** Long axis = easy direction, short axis = hard, collapsed axis = impossible. $w=\sqrt{\det(JJ^\top)}=\prod_i\sigma_i$ (ellipsoid volume). It cannot capture **shape/isotropy**
(condition number does).
**D3.** $\boldsymbol{\tau}=J^\top\mathbf{F}$; force ellipsoid shares axes with reciprocal
lengths $1/\sigma_i$. Easy-to-move = the long velocity axis = **weak-to-push**.
**D4 (intuition).** (a) Ellipse **long forward/back** (easy), **short left/right** (hard).
(b) Joint speeds **spike** — lots of joint motion for little sideways tool motion — and the
posture is **approaching a singularity** for the left/right direction (the short axis is
shrinking toward zero). (c) **Left/right** (the hard-to-move direction): by force/velocity
duality the force ellipsoid has reciprocal axes, so the short velocity axis is the long
force axis — easy-to-move is weak-to-push, hence the strongest push is along the
*opposite* (sideways) direction. *Grading: full credit for the easy/hard axis call, the
singularity recognition, and the duality reasoning — all in words, no formulas required.*

## Section E (integrative)
**E1.** As $\theta_2\to 0$ (straight) the ellipse flattens toward a line; the **radial**
direction (straight out along the arm) becomes impossible (rank 1).
**E2.** $w(\theta_2)=|L_1L_2\sin\theta_2|=|\sin\theta_2|$; vanishes at $\theta_2=0,\pi$
(straight/folded).
**E3.** By duality the collapsing velocity axis ($\sigma\to0$) becomes a diverging force
axis ($1/\sigma\to\infty$): the arm cannot move radially but can resist (brace against)
arbitrarily large radial force.
**E4.** Inside the M5 solver the same matrix was the **local linear step generator**
($\Delta\mathbf{p}\approx J\Delta\boldsymbol{\theta}$); Module 6 has reframed it as the
velocity map and the object of study — its rank, ellipsoid, and singular structure.

### Scoring guidance
- A/B/C/D short items: 2 pts each (1 intuition, 1 formula).
- Section E: 3 pts each part; full credit requires the capability/motion explanation, not
  just the number.
- Flag any student who treats gimbal lock as a robot singularity (C3) or reads $w$ as the
  whole capability story (D2) for targeted review.
