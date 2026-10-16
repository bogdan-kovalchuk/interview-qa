---
id: py-modimp-0008
title: "What does a partially initialized module mean during a circular import, and why aren't all of its names already available?"
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
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import (Loading)"
    url: https://docs.python.org/3.14/reference/import.html#loading
---

## Short answer

**A partially initialized module is a module object that is already in `sys.modules` while its code is still running, so only the names defined before the circular import point are available.**[^py314-reference-import-loading] The import machinery adds the module to `sys.modules` before running its code, so that a cycle cannot cause unbounded recursion.[^py314-reference-import-loading] If module A imports B and B imports A again, the second import of A returns an unfinished object. Accessing a name that is not yet defined raises `AttributeError` (`a.name`) or `ImportError` (`from a import name`).

## Detailed explanation

First the import system creates the module and registers it in `sys.modules`; only then does the loader run the module's code. The documentation requires the module to be in `sys.modules` before its code runs; otherwise code that imports itself, directly or indirectly, would recurse without end.[^py314-reference-import-loading] So a repeated `import left` does not run the module again; it returns an object whose execution has not finished yet.

Which names are available from such an object depends on execution order: a name appears once the statement that binds it has run. Below, `left.py` defines `LIMIT` before the `import right` line and `compute` after it. Run with `python main.py` (illustrative example; output checked on 3.12, 3.13 and 3.14):

```python
# left.py
LIMIT = 10              # bound before the cycle point
import right            # right.py runs now, while left is only partly initialized

def compute():          # not bound yet during the cycle
    return LIMIT * 2


# right.py
import left

print(left.LIMIT)                # 10: bound before the import line in left.py
print(hasattr(left, "compute"))  # False: def compute has not run yet
# from left import compute       # ImportError at this point: compute is not bound yet

def use():
    return left.compute()        # looked up when use() runs, after both modules load


# main.py
import left
import right

print(right.use())               # prints 10 and False from right.py, then 20
```

`main.py` imports `left` first, so `right` sees an unfinished `left`: `LIMIT` is already there, `compute` is not. Calling `left.compute()` inside `use()` works because the attribute is looked up at call time, after both modules have loaded. Entry order matters: if you start with `right`, `left` finishes before `hasattr` runs, and `hasattr(left, "compute")` gives `True`.

The line `from left import compute` at that stage raises `ImportError`, because `compute` is not bound yet. The exception type is the same in 3.12, 3.13 and 3.14, but the text differs. In 3.12: `cannot import name 'compute' from partially initialized module 'left' (most likely due to a circular import)`. In 3.13 and 3.14, when `left.py` is in the script's directory: `cannot import name 'compute' from 'left' (consider renaming ... if it has the same name as a library you intended to import)`; from 3.13 the message no longer names the circular import. If `left` is found through `PYTHONPATH`, all three versions say "partially initialized module" and "most likely due to a circular import".

**Common mistakes:**
- assuming that `import left` in `right.py` gives the complete module; it gives an unfinished object, and names defined below the cycle point are missing;
- writing `from left import compute` at the top level of a module that is part of the cycle: that is an `ImportError` at load time, not an `AttributeError` later;
- "fixing" the cycle by reordering import lines without checking which names are needed during import itself.
