---
id: py-modimp-0011
title: "What tasks are appropriate to perform in a package's `__init__.py`, and which ones create unwanted import-time side effects?"
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
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
  - source_id: py314-tutorial-modules-importing-from-a-package
    title: "Python 3.14: Tutorial/modules, Importing * From a Package"
    url: https://docs.python.org/3.14/tutorial/modules.html#importing-from-a-package
---

## Short answer

**`__init__.py` runs when a package is imported, so lightweight setup belongs there: convenience re-exports (`from .sub import Class`) and configuration that needs no I/O.**[^py314-reference-import-regular-packages] The `__all__` variable names what `from package import *` binds, so the public API can be declared there too.[^py314-tutorial-modules-importing-from-a-package] Unwanted import-time side effects are heavy computation, network calls, file writes or global state changes; they usually run once, at the first successful `import`.[^py314-reference-import-module-cache] They slow down startup and create hidden dependencies on initialization order.

## Detailed explanation

`__init__.py` is code that Python runs automatically when a regular package is imported: the objects it defines become attributes of the package.[^py314-reference-import-regular-packages] This also applies to submodules. The statement `import shop.models` first runs `shop/__init__.py`, and then `shop/models.py`.[^py314-reference-import-regular-packages] So everything in `__init__.py` runs for anyone who imports any submodule, even if they need only one class.

Appropriate tasks are cheap, deterministic actions that do not depend on the environment: exporting the public API (`from .models import Order` makes `Order` available as `shop.Order`), `__all__`, and constants. Without `__all__`, `from shop import *` only imports the package and binds the names defined in `__init__.py`.[^py314-tutorial-modules-importing-from-a-package]

Unwanted side effects are actions outside the module: reading and writing files, network requests, opening database connections, starting threads, changing `sys.path` or global logging. The user called nothing explicitly, yet the `import` already ran this code. The `sys.modules` cache usually prevents the code from running again: a successfully imported package is taken from the cache for as long as its entry stays there.[^py314-reference-import-module-cache] If an import fails, its entry is removed, and the next import runs `__init__.py` again.[^py314-reference-import-loading] The code itself can run at an unexpected moment, for example during tests. Python adds a module to `sys.modules` before its code runs, so a circular import can see the package only partly populated.[^py314-reference-import-loading]

Example: a `shop/__init__.py` with a side effect. The file `shop/models.py` contains only `class Order: pass`.

```python
# shop/__init__.py
from .models import Order          # lightweight re-export: no I/O
__all__ = ["Order"]                # names bound by "from shop import *"

print("shop/__init__.py runs")     # import-time side effect: runs once per interpreter
```

A script that imports submodules of this package:

```python
# main.py  (output: "shop/__init__.py runs" once, then the class line)
import shop.models      # runs shop/__init__.py first, then shop/models.py
import shop             # already in sys.modules: __init__.py does not run again
from shop import *      # __all__ limits the names to Order
print(Order)            # <class 'shop.models.Order'>
```

**Common mistakes:**
- assuming that `__init__.py` runs only when the package itself is imported, and not when one of its submodules is imported;
- opening files or network connections in `__init__.py`, then wondering why tests or tools start slowly;
- assuming that `__all__` restricts everything that can be imported: it affects only `from package import *`.
