---
id: py-modimp-0002
title: "What role does `sys.modules` play when the same module name is imported again?"
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
---

## Short answer

**`sys.modules` is a cache that stores already loaded module objects; a repeated `import` of the same name returns the cached object without searching or running the code.**[^py314-reference-import-module-cache] If `sys.modules[name]` holds a module object, the import returns it immediately. If the value is `None`, a `ModuleNotFoundError` is raised.[^py314-reference-import-module-cache] Deleting the key from `sys.modules` makes the next import search for and execute the module again, creating a new module object.[^py314-reference-import-module-cache]

## Detailed explanation

`sys.modules` is the first place an import looks. Its keys are full module names and its values are module objects. If the key is present and the value is not `None`, Python returns that object without searching the finders and without running any code.[^py314-reference-import-module-cache] The import statement still binds the name in the local namespace each time, but the module is not executed again.

The example creates a throwaway module and shows three cases: a cache hit, a manual deletion of the key, and a `None` value.

```python
import sys
import tempfile
from pathlib import Path

# A throwaway module on disk, so the example can run as-is.
folder = Path(tempfile.mkdtemp())
(folder / 'counter_mod.py').write_text("print('executing counter_mod')\n")
sys.path.insert(0, str(folder))

import counter_mod   # not cached yet: the file is found and executed
import counter_mod   # sys.modules hit: nothing is printed
first = counter_mod

del sys.modules['counter_mod']   # manually drop the cache entry
import counter_mod   # cache miss: the file is searched and executed again
print(counter_mod is first)      # False: a new module object

sys.modules['blocked_mod'] = None  # None in the cache forces a failure
try:
    import blocked_mod
except ModuleNotFoundError:
    print('ModuleNotFoundError')
# Output: executing counter_mod, executing counter_mod, False, ModuleNotFoundError
```

The second `import` prints nothing because it is served from the cache. After `del sys.modules[...]`, the next `import` runs the file again and creates a new module object, so `is` gives `False`. The old object lives on while `first` refers to it.[^py314-reference-import-module-cache]

A `None` value makes Python raise `ModuleNotFoundError` at once, even if the file exists.[^py314-reference-import-module-cache] To rerun the code in the existing object, use `importlib.reload()`.[^py314-reference-import-module-cache] A module whose loading raised an exception is removed from `sys.modules`, so the next import tries again.[^py314-reference-import-loading]

**Common mistakes:**
- assuming every repeated `import` runs the module code again (it does only when there is no cache entry or the previous import failed);
- deleting a key from `sys.modules` to "reload" a module and then comparing old references with new ones;
- expecting `importlib.reload()` to produce a new module object (reload reuses the same object).
