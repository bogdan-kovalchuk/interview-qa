---
id: py-modimp-0005
title: "In what order does Python search for a module through the import machinery and `sys.path`?"
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
  - source_id: py314-reference-import-meta-path
    title: "Python 3.14: Reference/import, The meta path"
    url: https://docs.python.org/3.14/reference/import.html#the-meta-path
  - source_id: py314-reference-import-finders-and-loaders
    title: "Python 3.14: Reference/import, Finders and loaders"
    url: https://docs.python.org/3.14/reference/import.html#finders-and-loaders
  - source_id: py314-reference-import-path-based-finder
    title: "Python 3.14: Reference/import, The Path Based Finder"
    url: https://docs.python.org/3.14/reference/import.html#the-path-based-finder
  - source_id: py314-library-sys-path
    title: "Python 3.14: Library/sys, sys.path"
    url: https://docs.python.org/3.14/library/sys.html#sys.path
---

## Short answer

**Python first checks `sys.modules`, then goes through `sys.meta_path`, which by default holds the built-in, frozen and path-based finders.**[^py314-reference-import-finders-and-loaders] The path-based finder walks the `sys.path` entries in order for a top-level module, and the parent package's `__path__` for a submodule.[^py314-reference-import-path-based-finder] The finder for each entry comes from `sys.path_importer_cache`; if it is not there, it is created through `sys.path_hooks` and cached.[^py314-reference-import-path-based-finder]

## Detailed explanation

The search runs in a fixed order that you can reproduce by hand:

- `sys.modules`: if the name is there, the search ends.[^py314-reference-import-module-cache]
- `sys.meta_path`, in order; the default finders are the built-in, frozen and path-based ones.[^py314-reference-import-finders-and-loaders] In CPython their classes are `BuiltinImporter`, `FrozenImporter` and `PathFinder` (observed on 3.13 and 3.14).
- `PathFinder` walks the `sys.path` entries for a top-level module, or the parent package's `__path__` for a submodule.[^py314-reference-import-path-based-finder]
- for each entry, the finder comes from `sys.path_importer_cache`. If it is missing, `sys.path_hooks` creates one; if no hook accepts the entry, `None` is cached.[^py314-reference-import-path-based-finder]
- the first spec found wins. If nothing is found, `ModuleNotFoundError` is raised.[^py314-reference-import-meta-path]

The order of `sys.meta_path` has a consequence: a built-in module is found before `sys.path` is consulted, so a file `itertools.py` at the front of `sys.path` does not shadow it. This is an observation from CPython 3.13 and 3.14 (`itertools.__spec__.origin` gives `'built-in'`), not a quote from the documentation.

Among the `sys.path` entries, the first one that contains the file wins:

```python
import sys
import tempfile
from pathlib import Path

first_dir = Path(tempfile.mkdtemp())
second_dir = Path(tempfile.mkdtemp())
(first_dir / 'finder_demo.py').write_text("WHERE = 'first_dir'\n")
(second_dir / 'finder_demo.py').write_text("WHERE = 'second_dir'\n")

sys.path[:0] = [str(first_dir), str(second_dir)]  # first_dir is searched first
import finder_demo
print(finder_demo.WHERE)  # first_dir: the first match wins
print(type(sys.path_importer_cache[str(first_dir)]).__name__)  # FileFinder: cached per entry
```

The initial `sys.path` is built from `PYTHONPATH` and installation defaults. Before those entries, the script's directory is prepended, or the current directory for `-m`, or an empty string for `-c` and the REPL.[^py314-library-sys-path]

The `sys.meta_path` list does not always hold only the standard finders. On the system CPython 3.13 the first entry is a finder from `_distutils_hack` (observed), so the three standard finders are not the complete list.

**Common mistakes:**
- assuming `sys.path_importer_cache` caches the found module (it caches the finder for a `sys.path` entry);
- expecting a file at the front of `sys.path` to shadow a built-in module;
- searching for a submodule in `sys.path` instead of the parent package's `__path__`.
