# `assets/` — Visual & Media Assets

Shared **visual and media assets** used across the curriculum: diagrams, animations, storyboards, figures, and other static files.

## Purpose

Centralizing assets keeps binary and media files out of the lesson folders, makes them reusable across modules, and gives the visual workflow (Gemini → storyboards → final figures) a single home.

## Suggested layout

```
assets/
├── diagrams/        # technical diagrams (SVG preferred, PNG fallback)
├── animations/      # rendered animations / GIFs / video
├── storyboards/     # animation storyboards & shot plans
├── figures/         # static figures used in lessons
└── branding/        # logos, color palette, typography
```

## Conventions

- **Prefer vector formats** (`.svg`) for diagrams so they scale and stay editable.
- **Name descriptively and namespace by module**, e.g. `m04-dh-frames.svg`, `m03-pinhole-camera.svg`.
- **Keep large binaries lean.** For very large media, consider Git LFS or an external host and link from lessons.
- **Caption and attribute** every asset that needs it; record sources in a sidecar `.md` or in the diagram metadata.

## Workflow note

Per the project AI workflow, **Gemini** produces diagrams, animation storyboards, and visual assets. Final reviewed assets land here and are referenced from lessons in `modules/`.

> **Status:** Placeholder. No assets added yet.
