---
id: py-modimp-0003
title: "Why don't two `import module` statements usually run the module's top-level code twice, yet they can create different local bindings?"
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
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
---

## Short answer

**Top-level code runs during the first import, while the module stays in `sys.modules`; later `import` statements for the same name return the same module object.**[^py314-reference-import-module-cache] Each import statement binds its own names in the importer's namespace: `import math` binds `math` to the module object, while `from math import pi` binds `pi` to the value it had at import time.[^py314-reference-simple-stmts-import] So a later change to the module's attribute does not change a name bound with `from`.

## Detailed explanation

The first `import` finds the module, creates the module object and runs its top-level code. While the entry stays in `sys.modules`, later imports of the same name find it in the cache and run nothing.[^py314-reference-import-module-cache] So an implicit import runs the code only once, under two conditions: the cache entry has not been removed, and the earlier import did not fail with an exception. After a failure the module is removed from `sys.modules`, and the next import runs the file again.[^py314-reference-import-loading] Calling `importlib.reload()` explicitly runs the module code again while keeping the same module object; it is not an import statement.[^py314-reference-import-module-cache]

The second part of the question is about binding. Each import statement binds a name in the local namespace of the importer, and the form decides which name:[^py314-reference-simple-stmts-import]

- `import m` binds `m` to the module object;
- `import m as x` binds `x` to the same module object;
- `from m import name` binds `name` to the value of the attribute `m.name` at import time.

The example shows that two names refer to one object, but a `from` binding does not follow the module attribute:

```python
import sys
import tempfile
from pathlib import Path

# A throwaway module on disk, so the example can run as-is.
folder = Path(tempfile.mkdtemp())
(folder / 'settings_demo.py').write_text("print('executing settings_demo')\nvalue = 1\n")
sys.path.insert(0, str(folder))

import settings_demo as a        # prints: executing settings_demo
import settings_demo as b        # cache hit: nothing printed
from settings_demo import value  # binds the local name to the int 1

print(a is b)                    # True: one module object, two local names
print(a.value, value)            # 1 1
a.value = 2                      # rebind the attribute on the module object
print(a.value, value)            # 2 1: the from-import kept the old value
```

`a is b` gives `True`: there is one module and two names. Changing `a.value` changes the attribute of the module object, but `value` stays `1`, because the `from` statement kept a reference to the value, not to the attribute.

Different names do not mean different objects. If `value` were a list, `a.value.append(2)` would also be visible through `value`, because it is the same list.

**Common mistakes:**
- expecting a repeated `import` to run the module's top-level code again;
- assuming `from m import name` follows later changes to `m.name`;
- assuming `import m as a` and `import m as b` create two copies of the module.
