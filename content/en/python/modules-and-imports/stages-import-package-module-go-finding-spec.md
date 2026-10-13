---
id: py-modimp-0001
title: "What stages does `import package.module` go through, from finding the spec to executing the module code?"
description: "What stages does `import package.module` go through, from finding the spec to executing the module code?"
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [import-package-module]
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
  - source_id: py314-reference-import-searching
    title: "Python 3.14: Reference/import, Searching"
    url: https://docs.python.org/3.14/reference/import.html#searching
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “Searching” of the official Python 3.14 documentation: for import foo.bar.baz, the top-level foo is imported first, then foo.bar and foo.bar.baz."
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “The module cache” of the official Python 3.14 documentation: sys.modules is checked first; if the name is there, the cached module object is returned."
  - source_id: py314-reference-import-meta-path
    title: "Python 3.14: Reference/import, The meta path"
    url: https://docs.python.org/3.14/reference/import.html#the-meta-path
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “The meta path” of the official Python 3.14 documentation: find_spec() and its path argument (for a submodule, the parent’s __path__); a returned spec or None passes the search on."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “Loading” of the official Python 3.14 documentation: the module is placed in sys.modules before its code runs; the loader creates the module object; exec_module() runs the module code."
  - source_id: py314-reference-import-submodules
    title: "Python 3.14: Reference/import, Submodules"
    url: https://docs.python.org/3.14/reference/import.html#submodules
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “Submodules” of the official Python 3.14 documentation: after loading, a submodule is an attribute of its parent package."
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import, Regular packages"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “Regular packages” of the official Python 3.14 documentation: a regular package’s __init__.py is implicitly executed when the package is imported."
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “The import statement” of the official Python 3.14 documentation: for a top-level module the module’s name is bound; for a module inside a package the top-level package’s name is bound."
---

## Short answer

**`import package.module` imports `package` first, then `module`, and for each name runs the same chain: a `sys.modules` check, a search through `sys.meta_path`, creation of the module object, and execution of its code.**[^py314-reference-import-searching] The search for `module` uses `package.__path__`, not `sys.path`.[^py314-reference-import-meta-path] The module is added to `sys.modules` before its code runs.[^py314-reference-import-loading] The import statement itself binds only the name `package` in the local namespace.[^py314-reference-simple-stmts-import]

## Detailed explanation

`import package.module` is two imports, not one. First `package` is imported.[^py314-reference-import-searching] If it is a regular package with an `__init__.py`, Python imports it the way a plain `import package` would: it finds the package and runs its `__init__.py`; a namespace package has no such file.[^py314-reference-import-regular-packages] Only then is `module` searched for, and its search path comes from `package.__path__`.[^py314-reference-import-meta-path]

For each of the two names the stages are the same:

- `sys.modules`: if the name is there, the cached object is returned and nothing else runs.[^py314-reference-import-module-cache]
- `sys.meta_path`: finders call `find_spec()`; the first one that returns a spec decides the result.[^py314-reference-import-meta-path]
- creation: the loader creates the module object (through `create_module()`, or a plain `ModuleType`), and the module is already in `sys.modules` before its code runs.[^py314-reference-import-loading]
- execution: `exec_module()` runs the module code in its namespace.[^py314-reference-import-loading]

The example replaces the files with memory and logs every `find_spec()` call:

```python
import sys
import importlib.abc
import importlib.machinery

# Fake package "demo" with submodule "demo.mod", served from memory.
SOURCES = {
    'demo': "print('demo/__init__ runs')\n",
    'demo.mod': "print('demo.mod module code runs')\nVALUE = 42\n",
}


class MemoryFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        where = 'None' if path is None else 'parent __path__'
        print(f'find_spec({fullname!r}, {where})')
        if fullname not in SOURCES:
            return None  # let the next meta path finder try
        return importlib.machinery.ModuleSpec(
            fullname, self, is_package=(fullname == 'demo'))

    def exec_module(self, module):
        code = SOURCES[module.__name__]
        exec(compile(code, module.__name__, 'exec'), module.__dict__)


sys.meta_path.insert(0, MemoryFinder())

# Output: find_spec('demo', None), demo/__init__ runs,
#         find_spec('demo.mod', parent __path__), demo.mod module code runs
import demo.mod
print(demo.mod.VALUE)  # 42
```

For `demo.mod` the finder receives the parent's `__path__`, so the submodule is searched inside the package, not in `sys.path`. After loading, the submodule is an attribute of the package.[^py314-reference-import-submodules] The name `demo` is bound by the import statement, not by the import machinery.[^py314-reference-simple-stmts-import]

**Common mistakes:**
- assuming `import package.module` binds the name `module` in the local namespace (it binds `package`);
- searching for the submodule in `sys.path` when the search uses the parent package's `__path__`;
- confusing `find_spec()`, which only finds a spec, with `exec_module()`, which runs the module code.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
