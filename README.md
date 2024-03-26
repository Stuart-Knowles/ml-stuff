# ML stuff

## Setup

The devcontainer definition should allow this to be run out the box in VSCode.
If you want to run it locally, make sure you have python 3.11 or higher installed, and [poetry](https://python-poetry.org/docs/) installed with it, then simply run `poetry install` in the root of this repo to create the virtual environment required.

## Running code
Everything here is intended to be run interactively through IPython/Jupyter. However, the Jupyter notebook format (`.ipynb`) is terrible for anything other than learning to code. We're using proper python scripts (`.py` format) with cell markers, which allows all of the benefits of interactive python whilst still being runnable as whole modules and being much easier to manage in source control.

Cells are separated with special comments beginning with `#%%`, and in VSCode are run in an interactive window opened with `>Jupyter: Create Interactive Window`, either with keyboard shortcuts or GUI.
[View the full tutorial here](https://code.visualstudio.com/docs/python/jupyter-support-py).

[Spyder](https://www.spyder-ide.org/) is an open-source IDE which is designed from the ground up to work with interactive python. It's not as polished an IDE as VSCode in general, but has much better IPython integration.

Since the scripts here are `.py`, they can also be run from the terminal with `poetry run python -m <path.to.script>`.
Note that the path is python module syntax, so dot separated with no extension at the end.
