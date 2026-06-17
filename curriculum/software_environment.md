# Software Environment

> **Scope:** Approved environment for **Module 1**. Later modules extend this stack; those tools are listed here as forward context only.
> **Authority:** Architect Decision **D-009**.
> **Goal:** A reproducible, minimal environment so every student runs the same code and gets the same results.

---

## 1. Approved stack (Module 1)

| Tool | Role | Minimum version |
|---|---|---|
| Python | Language runtime | 3.12+ |
| NumPy | Vectors, matrices, linear algebra | latest stable |
| Matplotlib | 2D/3D visualization | latest stable |
| SymPy | Symbolic math / verification | latest stable |
| Jupyter | Interactive notebooks | latest stable (JupyterLab or Notebook) |

**Explicitly excluded from Module 1** (introduced later): OpenCV (Module 3), ROS 2 (Module 8), Gazebo / Isaac Sim (Modules 9–10). Do not import these in Module 1 material.

---

## 2. Reproducible install

The repository pins exact versions in `requirements.txt` (committed alongside Module 1 notebooks). Recommended setup uses a virtual environment so the curriculum never collides with a student's system Python.

### Option A — venv + pip (default, no extra tooling)

```bash
# 1. Create and activate a virtual environment
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Upgrade pip, then install pinned dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Launch
jupyter lab
```

### Option B — conda (for students already using Anaconda/Miniconda)

```bash
conda create -n physical-ai python=3.12
conda activate physical-ai
pip install -r requirements.txt
jupyter lab
```

### Reference `requirements.txt` (Module 1)

```text
numpy
matplotlib
sympy
jupyterlab
ipykernel
```

> Exact pinned versions (`numpy==x.y.z`, …) are committed with the Module 1 notebooks once the first notebook is authored, so that pins reflect a tested-together set rather than guesses.

---

## 3. Environment verification

Students run this once after install. It belongs in a `00_environment_check.ipynb` notebook (authored at notebook-generation time, not here).

```python
import sys, numpy, matplotlib, sympy
print("Python :", sys.version.split()[0])
print("NumPy  :", numpy.__version__)
print("Matplotlib:", matplotlib.__version__)
print("SymPy  :", sympy.__version__)
assert sys.version_info >= (3, 12), "Python 3.12+ required"
print("Environment OK")
```

A passing run prints versions and `Environment OK`. A failure here is resolved before any unit begins.

---

## 4. Notebook conventions

- Notebooks must **run top to bottom with no hidden state** (Restart & Run All passes).
- One concept-cluster per notebook; clear the heaviest outputs before committing to keep diffs readable.
- Set a fixed random seed wherever randomness appears, for reproducibility.
- Prefer vectorized NumPy over Python loops; comment the *why*, not the *what*.
- Figures use Matplotlib with labeled axes and units.

(These align with `CONTRIBUTING.md`.)

---

## 5. Platform notes

- **Windows / macOS / Linux** all supported via venv or conda.
- **Cloud fallback:** the stack runs unmodified on hosted Jupyter (e.g. Binder, Colab) for students without a local install; Colab users `pip install -r requirements.txt` at the top of a session.
- No GPU is required for Module 1.

---

## 6. Forward compatibility (not installed yet)

To avoid rework later, keep the Module 1 environment isolated in its own venv/conda env. Later modules add their own tooling on top:

| Tool | Enters at | Notes |
|---|---|---|
| OpenCV | Module 3 | Perception / camera geometry |
| ROS 2 | Module 8 | Communication & control; may warrant a container |
| Gazebo / Isaac Sim | Modules 9–10 | Simulation & digital twin; heavier system requirements |

A separate environment spec will accompany each of those modules so Module 1's lightweight setup stays clean.
