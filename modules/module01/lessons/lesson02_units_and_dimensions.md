---
module: 01
unit: 01
lesson: 1.2
title: Units and Dimensions
estimated_time: 45
difficulty: Introductory
prerequisites: [1.1]
learning_objectives:
  - Explain why every physical quantity needs a unit and what a dimension is.
  - Use SI base units and perform unit conversions correctly.
  - Check an equation for dimensional consistency.
tags:
  - physical-ai
  - measurement
  - units
---

# Lesson 1.2 — Units and Dimensions

> A robot acts in meters, radians, and seconds. A number without a unit is an instruction the robot cannot follow — this lesson makes every quantity say what it *is*.

---

## 1. Why This Matters

Tell the greenhouse robot to "move the gripper 5." Five what? Five millimeters and it barely twitches; five meters and it slams through the plant. The number alone is meaningless — it only becomes an instruction when paired with a **unit**.

This is not a pedantic point. In 1999 NASA lost the Mars Climate Orbiter because one team worked in pound-force-seconds and another in newton-seconds; the spacecraft burned up because two numbers that looked compatible weren't. In robotics the same trap is everywhere: a camera reports distances in pixels, a motor controller expects radians, a path planner thinks in meters. Getting these to agree — and never silently mixing them — is the first discipline of acting in the physical world.

## 2. Physical Intuition

A physical quantity has two parts: **how much** (a number) and **of what** (a unit). "30" is a number; "30 °C," "30 cm," "30 seconds" are quantities. The unit tells you what kind of thing you're counting and on what scale.

Behind units sits a deeper idea: **dimension** — the *type* of quantity, independent of the unit you measure it in. A length is a length whether you express it in centimeters, meters, or inches; its dimension is "length." Units are the specific rulers; dimensions are the categories. You can convert centimeters to meters (same dimension), but adding a length to a time is nonsense in any units — the dimensions don't match.

## 3. Mathematical Foundations

The SI system builds everything from a small set of **base units**. The ones that matter most for Module 1:

| Quantity | Dimension | SI base unit |
|---|---|---|
| Length | L | meter (m) |
| Mass | M | kilogram (kg) |
| Time | T | second (s) |
| Angle (plane) | — (dimensionless) | radian (rad) |

Other quantities are **derived**: velocity has dimension $L\,T^{-1}$ (m/s), acceleration $L\,T^{-2}$ (m/s²), force $M\,L\,T^{-2}$ (the newton).

Two rules carry most of the weight:

**Unit conversion** multiplies by a ratio equal to 1. Since $100\ \text{cm} = 1\ \text{m}$, the ratio $\frac{1\ \text{m}}{100\ \text{cm}} = 1$, and multiplying by it changes units without changing the quantity:
$$30\ \text{cm} \times \frac{1\ \text{m}}{100\ \text{cm}} = 0.30\ \text{m}.$$

**Dimensional homogeneity:** every term in a valid equation must share the same dimension. If you derive $v = d \cdot t$ and check dimensions — $L\,T^{-1}$ on the left, $L\cdot T = L\,T$ on the right — they disagree, so the equation is wrong before you plug in a single number.

## 4. Visual Explanation

`[Visual: Unit conversion as a chain of ×1 ratios, plus a dimension-matching check]`

**Gemini Storyboard Brief**
- **Objective:** show that conversion is repeated multiplication by ratios equal to 1, and that dimensions must match across an equation.
- **Scene:** left panel — a value (30 cm) flowing through conversion-factor "gates" to become 0.30 m; right panel — a balance scale comparing the dimensions of two sides of an equation, balanced when they match.
- **Labels:** each conversion ratio; the dimension symbols (L, T) on each side of the scale.
- **Animation Notes:** the value slides through each gate; the balance tips when dimensions mismatch and levels when they agree.

## 5. Engineering Example

The greenhouse robot's depth camera reports a tomato "1200 units" away. Useless until you know the unit — here, millimeters. The planner works in meters, so the value must become 1.2 m before it enters any reach calculation. A skipped conversion here is a classic failure: the arm computes a reach for 1200 m and faults out, or worse, treats 1200 mm as 1200 m of error. Every interface between subsystems (camera → planner → controller) is a place where units must be declared and converted deliberately.

## 6. Worked Example

A motor spec says the joint may rotate up to 90°. The controller wants radians.

1. Conversion ratio: $180° = \pi\ \text{rad}$, so $\frac{\pi\ \text{rad}}{180°} = 1$.
2. Convert: $90° \times \dfrac{\pi\ \text{rad}}{180°} = \dfrac{\pi}{2}\ \text{rad} \approx 1.571\ \text{rad}.$

Quick dimensional sanity check on a reach estimate $d = r\,\theta$ (arc length) with $r = 0.4$ m and $\theta = 1.571$ rad: radians are dimensionless, so $d$ has dimension of length — consistent. Numerically $d \approx 0.63$ m.

## 7. Interactive Demonstration

*(Conceptual; runnable version in the notebook track.)* A unit-converter panel: type a value and pick "from" and "to" units (cm↔m, deg↔rad, mm↔m). The panel shows the conversion ratio it applied and flags an error if you try an impossible conversion (e.g. meters → seconds), reinforcing that only same-dimension conversions are valid.

## 8. Coding Exercise

*(Snippet — full implementation in the notebook track.)*

```python
def cm_to_m(value_cm):
    return value_cm / 100.0

def deg_to_rad(value_deg):
    return value_deg * 3.141592653589793 / 180.0

print(cm_to_m(30))      # expect 0.3
print(deg_to_rad(90))   # expect ~1.5708
```

**Your task:** add a `mm_to_m` function and a one-line comment stating the *dimension* each function operates on (it should be "length" for two of them and "angle" for one). You are practicing the habit of naming dimensions, not building a library yet.

## 9. Knowledge Check

1. What two parts make up a physical quantity?
2. Give the SI base unit for length, time, and plane angle.
3. Convert 250 cm to meters.
4. Multiple choice — which is dimensionally valid? (a) length + time, (b) length ÷ time, (c) length + mass.
5. Why is "move 5" not a valid command for a robot?

## 10. Challenge Problem

You find an undocumented formula in legacy robot code: `output = a * b / c`, where `a` is a distance (m), `b` is a time (s), and `c` is a velocity (m/s). Without knowing what `output` is supposed to represent, determine its **dimension** by dimensional analysis, and state one physical quantity it could plausibly be. Explain your reasoning.

## 11. Common Mistakes

- **Dropping units mid-calculation**, then misreading the final number's scale. Carry units through every step.
- **Mixing degrees and radians.** Trig functions and motor controllers often disagree on which they expect; this is one of robotics' most common bugs.
- **Metric-prefix slips** (mm vs cm vs m). A factor of 10 or 1000 here moves the gripper to the wrong place entirely.
- **Assuming an equation is right because the numbers came out.** Dimensional consistency is a check you can run *before* trusting any result.

## 12. Key Takeaways

- A physical quantity is a **number plus a unit**; the number alone is not an instruction.
- A **dimension** is the type of quantity; **units** are the specific scales for that type.
- **Convert** by multiplying by ratios equal to 1; you can only convert within the same dimension.
- **Dimensional homogeneity** lets you catch wrong equations before computing anything.
- Every interface between robot subsystems is a place to declare and convert units deliberately.

---

*Next lesson: 1.3 — Scalars and Physical Quantities (and the first hint that some quantities need a direction).*
