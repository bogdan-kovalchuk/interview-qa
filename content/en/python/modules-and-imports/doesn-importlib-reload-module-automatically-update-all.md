---
id: py-modimp-0013
title: "Why doesn't `importlib.reload(module)` automatically update all previously created instances and names imported via `from ... import ...`?"
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
  - source_id: py314-library-importlib-reload
    title: "Python 3.14: Library/importlib, importlib.reload()"
    url: https://docs.python.org/3.14/library/importlib.html#importlib.reload
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
---

## Short answer

**`importlib.reload()` usually re-runs the module's code in the same module object, but it does not update names copied with `from ... import ...` into other modules, and it does not change the classes of existing instances.**[^py314-library-importlib-reload] The reason is that `from ... import ...` stores a reference in the importing module's namespace, so reload does not change other namespaces.[^py314-reference-simple-stmts-import] A redefined class becomes a new class object, while existing instances keep the old one.[^py314-library-importlib-reload] Names the new version does not define keep their old values.

## Detailed explanation

`importlib.reload(module)` usually does not create a new module object: it recompiles the file and executes the module-level code in the already imported module, and the new objects are bound to names in the same dictionary. Names that the new version does not define keep their old values.[^py314-library-importlib-reload]

The most common surprise comes from `from ... import ...`. This statement takes the value at import time and stores a reference to it in the importer's namespace, rather than creating a link to the module.[^py314-reference-simple-stmts-import] So after a reload, `MODE` in `main.py` stays `"v1"`, while `config.MODE` becomes `"v2"`.

The module `config.py` initially contains `MODE = "v1"` and a class `Service`:

```python
# config.py (first version)
MODE = "v1"

class Service:
    def run(self):
        return "v1 run"
```

The script `main.py` imports the module in two ways, changes the file on disk and calls reload. The comments show the result:

```python
# main.py
import importlib
import config
from config import MODE, Service

svc = Service()                      # instance of the original class

# Edit config.py on disk here: MODE = "v2", and run() returns "version 2 run".
with open("config.py", "w") as f:
    f.write('MODE = "v2"\n\nclass Service:\n    def run(self):\n        return "version 2 run"\n')

importlib.reload(config)
print(MODE)                          # v1: the name copied by from-import is not rebound
print(config.MODE)                   # v2: attribute lookup sees the new value
print(svc.run())                     # v1 run: the instance keeps the old class
print(Service is config.Service)     # False: reload created a new class object
print(isinstance(svc, config.Service))  # False: the old instance is not an instance of the new class
```

`reload` executes the `class` statement again, so `config.Service` is a new class object, and the old `svc` remains an instance of the old class. The documentation says that instances created earlier continue to use the old class definition.[^py314-library-importlib-reload]

To avoid the trap, access the module's attributes (`config.MODE`, `config.Service`) or re-execute the `from` statement: the documentation names both ways.[^py314-library-importlib-reload] Reload itself is not thread-safe, so calls from several threads need synchronization.[^py314-library-importlib-reload]

**Common mistakes:**
- expecting reload to update every reference: names imported with `from` into other modules, and instances that already exist;
- reloading a module that defines a class, then checking `isinstance` against old instances;
- reloading `sys`, `__main__` or `builtins`: the documentation does not recommend this, and extension modules may fail.[^py314-library-importlib-reload]
