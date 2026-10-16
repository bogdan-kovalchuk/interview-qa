---
id: py-modimp-0007
title: "Why can a relative import fail when a package module is run as an ordinary script file?"
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
  - source_id: py314-reference-import-special-main
    title: "Python 3.14: Reference/import (Special considerations for __main__)"
    url: https://docs.python.org/3.14/reference/import.html#special-considerations-for-main
  - source_id: py314-reference-datamodel-module-package
    title: "Python 3.14: Reference/datamodel (module.__package__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#module.__package__
  - source_id: py314-reference-import-package-relative-imports
    title: "Python 3.14: Reference/import (Package Relative Imports)"
    url: https://docs.python.org/3.14/reference/import.html#package-relative-imports
  - source_id: py315-whatsnew-other-language-changes
    title: "Python 3.15: What's New (Other language changes)"
    url: https://docs.python.org/3.15/whatsnew/3.15.html#other-language-changes
---

## Short answer

**When `python package/module.py` runs, the module gets `__name__ = '__main__'` and `__spec__ = None`, so its relative import does not know its package and raises ImportError.**[^py314-reference-import-special-main] The import system finds the package through `__spec__.parent`; `__package__` is only a fallback.[^py314-reference-datamodel-module-package] It has been deprecated since 3.13, and the What's New for 3.15 still lists it as deprecated and scheduled for removal.[^py315-whatsnew-other-language-changes] The simplest correct way to run it is `python -m package.module` from the project root, which sets `__spec__` automatically.[^py314-reference-import-special-main]

## Detailed explanation

A relative import starts with a dot and is resolved from the current package: one dot means the current package, and each extra dot goes up one level.[^py314-reference-import-package-relative-imports] To find that package, the import system uses `__spec__.parent`, the package name stored in the module's spec. `__package__` used to play the same role; since Python 3.13 it is deprecated.[^py314-reference-datamodel-module-package] The What's New for 3.15 repeats that it is scheduled for removal.[^py315-whatsnew-other-language-changes]

When Python runs a file directly, it executes it as `__main__` without importing it as a module: `__spec__` is `None`, so there is no package, and the relative import has nothing to resolve against.[^py314-reference-import-special-main] When Python runs `python -m package.module`, the module is located through the import system, and `__spec__` holds a spec named `package.module`.[^py314-reference-import-special-main] In both cases `__name__` is `'__main__'`, so that name alone does not show whether a package exists.

Illustrative file that fails when run directly (output checked on 3.12, 3.13 and 3.14):

```python
# pkg/module.py (illustrative)
print(__name__, __package__, __spec__)
# python pkg/module.py    -> __main__ None None, then ImportError
# python -m pkg.module    -> __main__ pkg ModuleSpec(name='pkg.module', ...)
from . import sibling
```

There are two common fixes. The first is to run from the project root with `-m`. The second is to keep the module part of the package and run a separate script in the root that imports it as `pkg.module`; then the relative imports work, because the module is loaded normally.

**Common mistakes:**
- assuming that `__name__ == '__main__'` means there is no package: with `python -m` the name is also `__main__`, but `__spec__` and the package are present;
- writing new code with `__package__` even though the import system prefers `__spec__.parent`, and `__package__` is deprecated and scheduled for removal;
- adding a `sys.path` hack to get around the error instead of running with `-m` from the project root.
