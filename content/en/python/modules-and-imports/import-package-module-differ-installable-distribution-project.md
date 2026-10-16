---
id: py-modimp-0014
title: "How does an import package/module differ from an installable distribution project with build metadata?"
track: python
section: modules-and-imports
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import, Regular packages"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
  - source_id: py314-reference-import-namespace-packages
    title: "Python 3.14: Reference/import, Namespace packages"
    url: https://docs.python.org/3.14/reference/import.html#namespace-packages
  - source_id: packaging-distribution-package-vs-import-package
    title: "Python Packaging User Guide: Distribution package vs. import package"
    url: https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/#distribution-package-vs-import-package
---

## Short answer

**An import package or module is a runtime concept: a module that the import system finds and loads, usually a directory with `__init__.py` or a single `.py` file.**[^py314-reference-import-regular-packages] A distribution project is a packaging concept: a source tree, usually with a `pyproject.toml` that describes the metadata (name, version, dependencies), from which a build backend creates an installable archive such as a wheel.[^py-packaging-guide] One distribution can provide several import packages, and `pip install` installs a distribution, not an import package.[^packaging-distribution-package-vs-import-package]

## Detailed explanation

Import packages and modules belong to the import system, that is, to how Python finds code when `import` runs. An import package is a special kind of module that can contain submodules.[^packaging-distribution-package-vs-import-package] Usually a package is a directory with `__init__.py`, but namespace packages without `__init__.py` also exist.[^py314-reference-import-namespace-packages] The name written after `import` is the import name. It is what gets searched for at run time, regardless of which distribution the package was installed from.

A distribution is what `pip` installs. The packaging documentation describes a distribution package as an installable piece of software; in practice the word "project" usually means the same thing.[^packaging-distribution-package-vs-import-package] The source project describes its metadata (`name`, `version`, `dependencies`) in `pyproject.toml`. A build backend reads the project configuration and builds a distribution package, such as a wheel, from the source files.[^py-packaging-guide]

The relationship between the names is a convention, not a rule. An index such as PyPI requires distribution names to be unique, but it does not tie them to import names. So three situations are possible: the distribution `Pillow` provides the import package `PIL`; the distribution `attrs` provides two import packages, `attrs` and `attr`; and several distributions can provide the same import name, for example through forks.[^packaging-distribution-package-vs-import-package] This is why a name on PyPI does not guarantee that `import` with that name will bring in the expected package.

An example after `pip install pillow`: the distribution is called `pillow`, and the import name is `PIL`.

```python
import PIL                     # import name: the package directory PIL/
from PIL import Image          # a module inside the import package

try:
    import pillow              # the distribution name is not an import name
except ModuleNotFoundError as error:
    print(error)               # No module named 'pillow'
```

**Common mistakes:**
- assuming that `pip install X` gives an import package named `X` (for Pillow it is `PIL`);
- looking up a module by the distribution name instead of the import name;
- assuming that the `name` in `pyproject.toml` creates an import package: the names are not required to match.[^packaging-distribution-package-vs-import-package]
