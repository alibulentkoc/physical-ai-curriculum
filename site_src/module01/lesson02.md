!!! abstract "You are here"
    **Module 1 — Mathematical Foundations**  ·  **Unit 1 — Physical Quantities & Measurement**  ·  **Lesson 1.2 — Units and Dimensions**

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

<figure markdown>
  ![Units and Dimensions](../assets/m01-l2-units-and-dimensions.svg){ width="680" }
</figure>

## 5. Engineering Example

The greenhouse robot's depth camera reports a tomato "1200 units" away. Useless until you know the unit — here, millimeters. The planner works in meters, so the value must become 1.2 m before it enters any reach calculation. A skipped conversion here is a classic failure: the arm computes a reach for 1200 m and faults out, or worse, treats 1200 mm as 1200 m of error. Every interface between subsystems (camera → planner → controller) is a place where units must be declared and converted deliberately.

## 6. Worked Example

A motor spec says the joint may rotate up to 90°. The controller wants radians.

1. Conversion ratio: $180° = \pi\ \text{rad}$, so $\frac{\pi\ \text{rad}}{180°} = 1$.
2. Convert: $90° \times \dfrac{\pi\ \text{rad}}{180°} = \dfrac{\pi}{2}\ \text{rad} \approx 1.571\ \text{rad}.$

Quick dimensional sanity check on a reach estimate $d = r\,\theta$ (arc length) with $r = 0.4$ m and $\theta = 1.571$ rad: radians are dimensionless, so $d$ has dimension of length — consistent. Numerically $d \approx 0.63$ m.

## 7. Interactive Demonstration

A unit-converter panel: type a value and pick "from" and "to" units (cm↔m, deg↔rad, mm↔m). The panel shows the conversion ratio it applied and flags an error if you try an impossible conversion (e.g. meters → seconds), reinforcing that only same-dimension conversions are valid.

## 8. Coding Exercise

!!! tip "Run the hands-on notebook"
    `modules/module01/notebooks/M01_U01_L1_2_Units_And_Dimensions.ipynb` — open in JupyterLab and run **Kernel → Restart & Run All**.

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

Formative — unlimited attempts, immediate feedback; does not affect your grade.

<iframe src="../../quizzes/module01/lesson02_quiz.html" title="Units and Dimensions knowledge check" style="width:100%;height:720px;border:1px solid #e2e8f0;border-radius:12px"></iframe>

[Open this quiz in a new tab ↗](../quizzes/module01/lesson02_quiz.html)

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

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain Lesson 1.2 (Units and Dimensions) without the Mars Orbiter example. Make clear why a number needs a unit, what a dimension is, and how a dimensional-consistency check catches a wrong equation.
```

**Practice prompt** — generate more exercises

```
Give me 6 quick problems: unit conversions (cm to m, degrees to radians) and dimensional-consistency checks on simple physics equations. Show the answers.
```

**Explore prompt** — connect it to the real world

```
Show me 3 real engineering or robotics failures caused by unit or dimension mistakes, and how a dimensional check would have caught each one.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source; these give an AI-generated explanation in your preferred language.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**

```
I just completed Lesson 1.2 — Units and Dimensions.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**

```
I just completed Lesson 1.2 — Units and Dimensions.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**

```
I just completed Lesson 1.2 — Units and Dimensions.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 1.3 — Scalars and Physical Quantities (and the first hint that some quantities need a direction).*
