---
id: py-modimp-0006
title: "When is an absolute import preferable to an explicit relative import inside a package?"
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
  - source_id: pep-8-imports
    title: "PEP 8: Style Guide for Python Code (Imports)"
    url: https://peps.python.org/pep-0008/#imports
  - source_id: py314-reference-import-package-relative-imports
    title: "Python 3.14: Reference/import (Package Relative Imports)"
    url: https://docs.python.org/3.14/reference/import.html#package-relative-imports
---

## Short answer

**Absolute imports (`from package.module import name`) are the form PEP 8 recommends, because they are more readable and give better error messages when the import system is misconfigured.**[^pep-8-imports] PEP 8 accepts explicit relative imports (`from .module import name`) for complex layouts where absolute names would be unnecessarily long.[^pep-8-imports] An absolute import needs the directory containing the top-level package on `sys.path`, as after `python -m` from the project root; after a file moves to another package depth, its relative dots must be recounted.

## Detailed explanation

An absolute import spells out the full path from the top-level package: `from pkg.models import User`. An explicit relative import names the same module through dots counted from the current package: one dot means the current package, and each extra dot goes up one level.[^py314-reference-import-package-relative-imports] Both forms find the same module, so the choice is about readability, resistance to moves, and behaviour when the setup is wrong, not about whether the code runs at all.

PEP 8 recommends absolute imports because they are more readable and, when the import system is misconfigured, usually give better error messages.[^pep-8-imports] The same guide accepts explicit relative imports as an alternative for complex package layouts where absolute names would be unnecessarily verbose.[^pep-8-imports]

The difference shows up at run time. An absolute import searches `sys.path` for `pkg`. After `python -m pkg.service` from the project root, that root is on `sys.path`, so the line works. With `python pkg/service.py`, the first entry of `sys.path` is the `pkg/` directory itself, so the same line fails with `ModuleNotFoundError: No module named 'pkg'`. A relative import fails in that run with `ImportError`, because the file does not know its package.

Illustrative file (run checked on CPython 3.12, 3.13 and 3.14):

```python
# pkg/service.py, run from the project root as: python -m pkg.service
from pkg.models import User   # absolute: the full path from the top-level package
# from .models import User    # explicit relative: same module, but the dots change if the file moves
```

Moving a file is the main argument for absolute imports. If `service.py` moves to `pkg/api/`, the line `from pkg.models import User` stays correct, while the relative form must become `from ..models import User`. Relative imports are shorter and often more convenient inside a large internal package whose files move together, which is why PEP 8 does not forbid them.

**Common mistakes:**
- assuming an absolute import works however the file is run; it needs the directory that contains the top-level package on `sys.path`;
- mixing both forms in one package without a reason, so a file move means checking both kinds of lines;
- rewriting every relative import to an absolute one just for style, without checking how the package is run and tested.
