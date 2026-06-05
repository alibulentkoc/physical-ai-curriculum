---
module: 01
unit: 01
lesson: 1.5
title: Accuracy and Precision
estimated_time: 40
difficulty: Introductory
prerequisites: [1.4]
learning_objectives:
  - Define accuracy and precision and explain how they differ.
  - Classify measurement situations as accurate/precise in all four combinations.
  - Connect accuracy to calibration and precision to repeatability in robotics.
tags:
  - physical-ai
  - measurement
  - accuracy-precision
---

# Lesson 1.5 — Accuracy and Precision

> In everyday speech they're synonyms. In engineering they're different axes — and a robot can be excellent at one while terrible at the other.

---

## 1. Why This Matters

Two grippers, two problems. Gripper A lands all over the place — sometimes on the tomato, sometimes 2 cm left, sometimes 3 cm high. Gripper B lands in nearly the same spot every single time, but that spot is consistently 2 cm below the fruit. Both "miss," but for opposite reasons, and they need opposite fixes. Telling these situations apart is the whole point of distinguishing **accuracy** from **precision**. Treat them as the same word and you'll keep recalibrating a sensor that actually needs noise filtering, or filtering one that actually needs calibration.

## 2. Physical Intuition

The classic picture is a dartboard. **Accuracy** is how close your darts land to the bullseye (the true target). **Precision** is how close the darts land *to each other*, regardless of where the bullseye is.

That gives four combinations:
- **Accurate and precise:** tight cluster on the bullseye. The goal.
- **Precise but not accurate:** tight cluster, but off to one side. Consistent — and consistently wrong.
- **Accurate but not precise:** scattered widely, but centered on the bullseye on average.
- **Neither:** scattered and off-center.

The greenhouse gripper from §1: Gripper A is *accurate-ish but imprecise* (centered but scattered); Gripper B is *precise but inaccurate* (tight but offset).

## 3. Mathematical Foundations

Connect these to the error types from Lesson 1.4 — they map cleanly:

- **Accuracy** is about closeness to the true value: high accuracy means small **systematic** error. If you take many readings, accuracy is how close their *average* is to the truth.
- **Precision** is about repeatability: high precision means small **random** error — the readings are tightly clustered, measured by their *spread*.

If $\bar{x}$ is the average of repeated readings and $x_\text{true}$ the true value:
$$ \text{Accuracy relates to } |\bar{x} - x_\text{true}| \quad(\text{the bias}), $$
$$ \text{Precision relates to the spread of the readings around } \bar{x}. $$

The crucial insight: these are **independent axes.** You can have one without the other. A precise-but-inaccurate instrument has a tight spread around the *wrong* value — which is actually good news, because a consistent offset is correctable by calibration (subtract the bias). An imprecise instrument scatters, and no single offset fixes scatter; you need more readings or filtering.

*(Formal measures of spread — variance, standard deviation — arrive with the statistics tools later; here we reason with "tight" vs "scattered.")*

## 4. Visual Explanation

`[Visual: 2×2 dartboard grid — the four accuracy/precision combinations]`

**Rendered asset:** `assets/diagrams/m01-l5-accuracy-precision.svg` (produced; embedded on the MkDocs page).

**Diagram Specification**
- **Objective:** the viewer internalizes that accuracy (closeness to center) and precision (closeness to each other) are independent.
- **Scene:** four dartboards in a 2×2 grid; columns = low/high accuracy, rows = low/high precision; dart clusters placed to show each combination, with the greenhouse gripper's two cases highlighted.
- **Labels:** each quadrant; "bullseye = true value"; mark the "precise but inaccurate → fix by calibration" board.
- **Animation Notes:** on the precise-but-inaccurate board, animate a calibration shift sliding the tight cluster onto the bullseye.

## 5. Engineering Example

Robot arm datasheets quote a **repeatability** spec (e.g. ±0.05 mm) and sometimes a separate **accuracy** spec — and they are different numbers, usually with repeatability the tighter of the two. Repeatability (precision) says: command the same pose twice, how close do you land to yourself? Accuracy says: command a pose, how close do you land to the *commanded* point in the real world? Industrial arms are often far more precise than accurate, which is exactly why they're taught positions by demonstration (lean on their precision) rather than by absolute coordinates (which would lean on their weaker accuracy). The greenhouse robot benefits the same way: a precise arm whose offset has been calibrated out becomes accurate.

## 6. Worked Example

A distance sensor is checked against a true 2.00 m target. Five readings: 1.78, 1.80, 1.79, 1.81, 1.80 (m).

1. Average: $\bar{x} = \frac{1.78+1.80+1.79+1.81+1.80}{5} = 1.796\ \text{m}.$
2. **Accuracy:** average is 1.796 vs true 2.00 → bias $\approx -0.20\ \text{m}$. That's a large, consistent offset → **low accuracy**.
3. **Precision:** readings span only 1.78–1.81, a 3 cm spread → tightly clustered → **high precision**.
4. Diagnosis: **precise but inaccurate.** Fix by adding a +0.20 m calibration offset; no extra filtering needed.

## 7. Interactive Demonstration

*(Conceptual; notebook version later.)* A dartboard sandbox with two sliders — "bias" (moves the cluster's center off the bullseye → controls accuracy) and "scatter" (spreads the darts → controls precision). The learner sets each independently and watches the cluster, confirming the two effects don't depend on each other. A "calibrate" button slides a tight off-center cluster onto the bullseye, showing why precision-without-accuracy is the easy problem.

## 8. Coding Exercise

*(Snippet — full implementation in the notebook track.)*

```python
readings = [1.78, 1.80, 1.79, 1.81, 1.80]
true_value = 2.00

avg = sum(readings) / len(readings)
bias = avg - true_value                 # accuracy indicator
spread = max(readings) - min(readings)  # crude precision indicator

print(f"avg={avg:.3f}  bias={bias:.3f}  spread={spread:.3f}")
```

**Your task:** in a comment, classify this sensor as accurate/precise (which of the four cases?), and state the one-line fix. Then describe — in words — a set of readings that would be *accurate but not precise*. (Proper spread statistics come later; `max - min` is a stand-in.)

## 9. Knowledge Check

1. In one sentence each, define accuracy and precision.
2. A cluster of darts is tight but in the top-left corner. Accurate? Precise?
3. Which is easier to correct: precise-but-inaccurate, or imprecise-but-accurate? Why?
4. Match: accuracy ↔ (systematic/random) error; precision ↔ (systematic/random) error.
5. Why do industrial robots advertise repeatability rather than absolute accuracy?

## 10. Challenge Problem

A greenhouse robot's vision system reports fruit positions that are, on average, dead-on, but any single reading can be several centimeters off in any direction. Classify this in accuracy/precision terms, explain why simply taking *one* reading before each grasp is risky, and propose a strategy that uses the system's strength (its accuracy) to overcome its weakness (its imprecision).

## 11. Common Mistakes

- **Using "accurate" and "precise" as synonyms.** They're independent; conflating them hides which fix is needed.
- **Calibrating to fix scatter.** A bias offset does nothing for random spread.
- **Averaging to fix bias.** Averaging a consistently offset sensor returns the offset value, precisely wrong.
- **Reading one sample from an imprecise sensor and trusting it.** Precision matters precisely because single reads from a noisy sensor can be far off.

## 12. Key Takeaways

- **Accuracy** = closeness to the true value (small bias / systematic error).
- **Precision** = repeatability / tight clustering (small random error).
- They are **independent axes**; all four combinations exist.
- **Precise-but-inaccurate is the friendly case** — calibrate out the bias. Scatter needs averaging/filtering instead.
- Robots often exploit high precision (teach-by-demonstration, calibrated offsets) to compensate for weaker accuracy.


## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain Lesson 1.5 (Accuracy and Precision) using the dartboard idea. Stress that they are independent axes, and make clear which problem calibration can fix.
```

**Practice prompt** — generate more exercises

```
Give me 6 dartboard or sensor scenarios and ask me to label each as accurate and/or precise (cover all four combinations), then reveal the answers.
```

**Explore prompt** — connect it to the real world

```
Show me how robot-arm datasheets quote repeatability versus accuracy, and why industrial robots are often taught positions by demonstration.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source; these give an AI-generated explanation in your preferred language.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**

```
I just completed Lesson 1.5 — Accuracy and Precision.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**

```
I just completed Lesson 1.5 — Accuracy and Precision.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**

```
I just completed Lesson 1.5 — Accuracy and Precision.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```


---

*Next lesson: 1.6 — Engineering Estimation (the fast sanity check that catches errors before they cost anything).*
