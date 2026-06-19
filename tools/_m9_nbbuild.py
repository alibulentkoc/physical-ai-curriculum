"""Build + execute-verify Module 9 notebooks. Not shipped; a production tool."""
import sys, os, nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from nbconvert.preprocessors import ExecutePreprocessor

REPO = "/home/claude/repo"


def build(path, cells):
    nb = new_notebook()
    nb.cells = [
        new_markdown_cell(c[1]) if c[0] == "md" else new_code_cell(c[1])
        for c in cells
    ]
    nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python",
                                  "name": "python3"},
                   "language_info": {"name": "python"}}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        nbformat.write(nb, f)


def verify(path):
    nb = nbformat.read(path, as_version=4)
    ep = ExecutePreprocessor(timeout=180, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": REPO}})
    txt = "\n".join(
        out.get("text", "")
        for cell in nb.cells if cell.cell_type == "code"
        for out in cell.get("outputs", [])
        if out.get("output_type") == "stream"
    )
    ok = "All checks passed." in txt
    # persist executed outputs
    with open(path, "w") as f:
        nbformat.write(nb, f)
    return ok, txt
