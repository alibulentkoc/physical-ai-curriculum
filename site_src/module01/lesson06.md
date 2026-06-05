# Lesson 1.6 Engineering Estimation

## Why this matters

If a planner says the arm must reach 8 m, you don't need a model to know it's wrong — the arm is ~1 m. A ten-second **estimate** is the cheapest error-catcher an engineer owns, and it closes Unit 1 by tying measurement sense to judgment.

## The idea, visually

<figure markdown>
  ![1.6 Engineering Estimation](../assets/m01-l6-engineering-estimation.svg){ width="680" }
</figure>

## Key idea

Reason to the **order of magnitude**. A **Fermi estimate** chains rough factors (picks/hour ≈ 3600 s ÷ 10 s ≈ 360). **Bounding** — a value the answer must be above/below — gives a decisive sanity check.

## Notebook

!!! tip "Run the hands-on notebook"
    `modules/module01/notebooks/lesson06_*.ipynb` — run **Kernel → Restart & Run All**. NumPy + Matplotlib only.

## Knowledge check

Formative — unlimited attempts, immediate feedback; does not affect your grade.

<iframe src="../../quizzes/lesson06_quiz.html" title="1.6 Engineering Estimation knowledge check" style="width:100%;height:680px;border:1px solid #e2e8f0;border-radius:12px" loading="lazy"></iframe>

## Key takeaways

- **Estimation** reasons to the order of magnitude, fast.
- **Fermi**: split into rough factors and multiply.
- **Bounding** gives a decisive check.
- Catches factor-of-1000 errors — the dangerous ones. Unit 2 next: quantities that need direction → **vectors**.


## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain Lesson 1.6 (Engineering Estimation). Show how order-of-magnitude and Fermi estimates catch big errors, using an example that is not the greenhouse robot.
```

**Practice prompt** — generate more exercises

```
Give me 5 Fermi estimation problems relevant to robotics, each with a rough-factor breakdown and a plausible range, then check my answers.
```

**Explore prompt** — connect it to the real world

```
Show me 3 real engineering decisions that were guided by quick estimation before detailed modeling, and what the estimate ruled in or out.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source; these give an AI-generated explanation in your preferred language.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**

```
I just completed Lesson 1.6 — Engineering Estimation.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**

```
I just completed Lesson 1.6 — Engineering Estimation.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**

```
I just completed Lesson 1.6 — Engineering Estimation.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```


---

*Next: 2.1 — What Is a Vector? (Unit 2)*
