---
id: py-fileio-0009
title: "How does `pathlib.Path` make building and traversing paths easier compared to manual string concatenation?"
track: python
section: files-and-io
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
  - source_id: py314-library-pathlib-path
    title: "Python 3.14: Library/pathlib (Path)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path
  - source_id: py314-library-pathlib-pure-paths
    title: "Python 3.14: Library/pathlib (Pure paths)"
    url: https://docs.python.org/3.14/library/pathlib.html#pure-paths
  - source_id: py314-library-pathlib-purepath-joinpath
    title: "Python 3.14: Library/pathlib (PurePath.joinpath)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.joinpath
  - source_id: py314-library-pathlib-path-rglob
    title: "Python 3.14: Library/pathlib (Path.rglob)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob
---

## Short answer

**`pathlib.Path` provides an object-oriented API: the `/` operator to join path parts, the methods `iterdir()`, `glob()`, `rglob()`, and the properties `.suffix`, `.stem`, `.parent`.**[^py314-library-pathlib-path] Unlike manual string concatenation, `Path` inserts one separator by itself, and its paths are immutable and hashable (they can be used as dict keys); `PurePosixPath` and `PureWindowsPath` let you handle paths in another syntax without OS calls.[^py314-library-pathlib-pure-paths]

## Detailed explanation

A string path is just text. With manual concatenation you must insert the separator yourself, its form depends on the OS, and it is easy to omit it or write two. `Path` builds a path from objects: the `/` operator adds exactly one separator, and the running OS determines the syntax.[^py314-library-pathlib-path] Comparison on POSIX (`#` comments show the result):

```python
from pathlib import Path

base = '/srv/app'
name = 'logs/app.log'
print(base + name)                  # /srv/applogs/app.log: the separator is lost
print(base + '/' + name)            # /srv/app/logs/app.log: correct only if written by hand every time
print(Path(base) / name)            # /srv/app/logs/app.log: one separator, inserted by pathlib
print(Path(base) / '/etc/passwd')   # /etc/passwd: an absolute right side replaces the left one
```

The rule for an absolute operand is worth knowing in advance. `Path(base) / '/etc/passwd'` gives `/etc/passwd`: if a segment is an absolute path, the previous segments are discarded.[^py314-library-pathlib-purepath-joinpath] `os.path.join(base, '/etc/passwd')` behaves the same way (checked on 3.13 and 3.14). On Windows there is a condition: a right operand that has only a root and no drive is not absolute, so the left operand's drive is kept. `PureWindowsPath('c:/a') / '/b'` gives `c:\b` (checked on 3.13 and 3.14). So a path that arrives from outside must not simply be joined onto a directory; see qid:py-fileio-0010.

Tree traversal is also handled by `Path`: `iterdir()` returns the direct contents of a directory, `glob()` matches a pattern within one directory, and `rglob()` searches recursively.[^py314-library-pathlib-path-rglob] The results are again `Path` objects, so `.suffix`, `.stem` and `.parent` are available without manual `split()` and `rfind()`. Example (`#` comments show the result):

```python
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp())
(root / 'logs').mkdir()
(root / 'logs' / 'app.log').write_text('x')
(root / 'app.txt').write_text('y')

for p in sorted(root.rglob('*.*')):   # recursive search, yields Path objects
    print(p.relative_to(root), p.suffix, p.stem)
# app.txt .txt app
# logs/app.log .log app
```

`Path` is immutable and hashable, so it can be used as a dict key or as a set member. Comparison normalizes the spelling: `Path('a/b') == Path('a//b/')` gives `True`.[^py314-library-pathlib-pure-paths] `Path` does not check that a path exists when it is created; it touches the filesystem only in methods such as `exists()`. The pure classes (`PurePath`, `PurePosixPath`, `PureWindowsPath`) never call the OS, which makes them convenient for paths of another OS.

**Common mistakes:**
- building a path with `+`: `Path('a') + 'b'` raises `TypeError`, because `Path` does not support concatenation with a string;
- assuming that creating `Path(...)` checks whether a file or directory exists;
- assuming that an absolute right operand is simply appended to the left one.
