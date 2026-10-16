---
id: py-stdlib-0010
title: "When is it fine to stay with `os` for a filesystem operation, and when should you choose `pathlib`?"
track: python
section: standard-library
sources:
  - source_id: py314-library-os-open
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.open
  - source_id: py314-library-os-scandir
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.scandir
  - source_id: py314-library-os-fspath
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fspath
---

## Short answer

**`pathlib` is more convenient for manipulating paths and building new ones, while `os` is still needed for low-level operations on file descriptors, such as `os.open()` and `os.fstat()`.**[^py314-library-os-open] `os.scandir()` accepts path-like objects, so a `Path` can be passed to it without conversion.[^py314-library-os-scandir] When an API requires a str, use `os.fspath(path)`, which returns a string.[^py314-library-os-fspath]

## Detailed explanation

Both modules work with the same files, so the choice depends on what you are doing. `pathlib` models a path as an object: a `Path` has methods for building, checking, and reading, and the code reads as a statement of intent. `os` is closer to the system calls: `os.open()` returns an integer file descriptor, and `os.fstat()` reads the metadata of that descriptor.[^py314-library-os-open] `Path` has neither `fstat()` nor `fileno()`, so `os` remains necessary for such operations.

The example combines both approaches: `os.open()` accepts a `Path`, while `os.environ` needs a string:

```python
import os
from pathlib import Path

script = Path(__file__)
fd = os.open(script, os.O_RDONLY)        # os.open accepts a Path and returns an int descriptor
print(os.fstat(fd).st_size > 0)          # True; pathlib has no fstat()
os.close(fd)
os.environ["SCRIPT"] = os.fspath(script) # env values must be str; a bare Path raises TypeError
```

Moving between the two is mostly straightforward. `os.scandir()` accepts a path-like object, so a `Path` can be passed directly.[^py314-library-os-scandir] In the other direction, an explicit step is needed where an API expects a str: `os.fspath()` returns a string for a path-like object, and returns an existing str or bytes unchanged.[^py314-library-os-fspath] Without that step, assigning a `Path` to `os.environ` raises `TypeError: str expected, not PosixPath`, because environment variable values must be str.

In practice, `pathlib` is a sensible default, since it reads better and offers `glob()`, `rglob()`, and `suffix`. `os` is appropriate when you need a file descriptor or a low-level call that `pathlib` does not provide.[^py314-library-os-open]

**Common mistakes:**
- passing a `Path` where a str is expected, such as `os.environ`, without `os.fspath()`;
- assuming `pathlib` replaces all of `os`: `Path` has no file-descriptor-level operations such as `os.open()` or `os.fstat()`;
- mixing a `Path` and a string in one expression: `Path("report") + ".txt"` raises `TypeError`; use `with_name()` to change the name.
