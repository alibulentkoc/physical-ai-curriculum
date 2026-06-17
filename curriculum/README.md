# `curriculum/` — Curriculum Architecture

This directory holds the **high-level structure** of the curriculum: the map, not the territory.

## Purpose

`curriculum/` defines *what* is taught and *in what order*. The actual teaching artifacts (lessons, notebooks, demos) live in `modules/`. Keeping the architecture separate from the content lets the sequence evolve without rewriting lessons.

## What belongs here

- The master curriculum roadmap (all 10 modules)
- Per-module **manifests** (e.g. `module01_manifest.md`) listing topics, learning objectives, prerequisites, and the build order for each topic
- Learning-objective maps and outcome tracing
- Topic-sequencing rationale and dependency graphs
- Cross-module concept threading (how the Greenhouse Harvesting Robot narrative connects modules)

## Relationship to other folders

| Folder        | Role                                              |
|---------------|---------------------------------------------------|
| `curriculum/` | The plan: roadmap, manifests, objectives          |
| `modules/`    | The execution: lessons, notebooks, exercises      |

## Next deliverable

`module01_manifest.md` — the manifest for **Module 1: Mathematical Foundations for Physical AI, Robotics, and Digital Twins**.

> **Status:** Placeholder. No manifests generated yet.
