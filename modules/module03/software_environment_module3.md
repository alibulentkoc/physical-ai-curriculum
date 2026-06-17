---
title: Module 3 — Software Environment Note (OpenCV)
module: 03
extends: curriculum/software_environment.md
---

# Module 3 — Software Environment Note

Module 3 introduces **OpenCV** (`cv2`), the first library beyond the Module 1 foundation (NumPy, Matplotlib, SymPy, Jupyter). This note documents it; the base setup in `curriculum/software_environment.md` still applies.

## What's added

| Library | Import | Used for | First lesson |
|---|---|---|---|
| OpenCV | `import cv2` | camera geometry: `projectPoints`, undistortion, calibration utilities | 4.3 (Unit 4) |

## Install

Into the same virtual environment used since Module 1 (PEP 668 systems such as Pop!_OS need the venv):

```bash
source .venv/bin/activate
pip install opencv-python    # pulls in the cv2 module
```

Pin the version in `requirements.txt` alongside the existing pins. The headless variant `opencv-python-headless` is sufficient for the curriculum's geometry use (no GUI windows needed) and is lighter for servers/CI.

## Graceful degradation (notebook policy)

Module 3 notebooks must execute headless (no display). Therefore:

- Where OpenCV provides a function we also derive by hand (e.g. `projectPoints`), notebooks compute the result with **NumPy** as the asserted ground truth and use OpenCV as a **confirmation**, inside a `try/except import cv2` so the notebook still runs if `cv2` is absent.
- No notebook requires a GUI (`cv2.imshow`) or a camera device.
- Image-array operations use synthetic NumPy arrays, not files, unless a sample asset is bundled.

This keeps every notebook runnable in CI and on a student machine that hasn't installed OpenCV yet, while still showing the real library in use.

## Not yet introduced

Deep-learning detectors, stereo/SfM pipelines, and full calibration optimization are **not** part of Module 3 (deferred per the manifest). Module 3 uses OpenCV only for camera-geometry math with given intrinsics/extrinsics.
