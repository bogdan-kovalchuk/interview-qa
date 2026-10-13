---
id: py-modimp-0012
title: "What exactly does `if __name__ == \"__main__\"` protect, and what does it not change about import semantics?"
description: "What exactly does `if __name__ == \"__main__\"` protect, and what does it not change about import semantics?"
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [if-name-main]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Python Packaging User Guide."
  - source_id: py314-library-main
    title: "Python 3.14: Library/__main__, Top-level code environment"
    url: https://docs.python.org/3.14/library/__main__.html#name-main
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __name__ is '__main__' in the top-level program and the module's name when imported; code under if __name__ == '__main__' does not run on import."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: a module is added to sys.modules before its code runs, and a repeated import returns the already created module."
  - source_id: py314-reference-import-special-considerations-for-main
    title: "Python 3.14: Reference/import, Special considerations for __main__"
    url: https://docs.python.org/3.14/reference/import.html#special-considerations-for-main
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: a file run as a script and the same file imported under its own name are distinct modules."
---

## Short answer

**`if __name__ == "__main__"` protects only its own block: the block runs when the module is the top-level program (for example `python3 file.py`), and on `import` it is skipped because `__name__` equals the module's dotted name.**[^py314-library-main] The guard does not change import semantics: the rest of the module's code runs on `import` as usual, and the module itself is cached in `sys.modules`.[^py314-reference-import-loading] If the same file is run as a script and then imported, Python treats them as two distinct module objects.[^py314-reference-import-special-considerations-for-main]

## Detailed explanation

The guard rests on one rule. A module that Python runs as the top-level program gets `__name__ == "__main__"`, while any imported module gets its own name, for example `calc`, or `pkg.calc` if the file is inside a package.[^py314-library-main] So `if __name__ == "__main__":` protects only the block under it: command-line parsing, a demonstration, a call to `main()`. That block does not run on import, which is why functions and classes can be imported from the same file without side effects.

The file `calc.py` contains code that always runs, and code that runs only as a script:

```python
# calc.py
print("calc: top-level code runs on import too")  # not guarded

def square(x):
    return x * x

if __name__ == "__main__":
    print("calc: guarded block, only when run as a script")
    print(square(3))
```

`python3 calc.py` prints both lines and `9`. If you run `import calc` instead, only the first line is printed: the function `square` is available, but the guarded block is not.

The guard does not mean "do not execute the module on import": Python still creates a module object, registers it in `sys.modules`, and runs all the top-level code, including the lines outside the block. Only the block itself is skipped. A repeated `import` of the same name returns the cached object without running the code again.[^py314-reference-import-loading]

The trap appears when a file is run as a script and is also imported under its own name. An entry `__main__` appears in `sys.modules`, but `import dup` looks for an entry `dup`, which does not exist yet, so the file runs a second time as a separate module object. The documentation explicitly treats such modules as distinct.[^py314-reference-import-special-considerations-for-main]

The file `dup.py` demonstrates this trap: it is run as a script, and it imports itself under its own name.

```python
# dup.py, run as: python3 dup.py
import sys

print("dup executed as", __name__)
if __name__ == "__main__":
    import dup                       # the same file, loaded again under the name "dup"
    print("same module object:", dup is sys.modules["__main__"])
```

Output of the run:

```text
dup executed as __main__
dup executed as dup
same module object: False
```

Consequences: code outside the guard runs twice, and classes defined in both copies are different classes.

**Common mistakes:**
- assuming that the guard makes a module safe to import: code outside the block always runs;
- keeping functions and classes that other modules need inside `if __name__ == "__main__":`: importers will not see them;
- importing a file that was run as a script and expecting its code to run only once.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
