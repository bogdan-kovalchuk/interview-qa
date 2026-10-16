---
id: py-fileio-0007
title: "How do you update a file within the same filesystem via a temporary file and `os.replace()`, so a reader never sees partial content?"
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
  - source_id: py314-library-tempfile-mkstemp
    title: "Python 3.14: Library/tempfile (mkstemp)"
    url: https://docs.python.org/3.14/library/tempfile.html#tempfile.mkstemp
  - source_id: py314-library-functions-open
    title: "Python 3.14: Built-in Functions (open)"
    url: https://docs.python.org/3.14/library/functions.html#open
---

## Short answer

**Write the new data to a temporary file in the same directory, that is, on the same filesystem, then call `os.replace(tmp_path, target_path)`.**[^py314-library-os-os-replace] On POSIX a successful replace is an atomic operation, so a reader that opens `target_path` at any moment sees the old or the new version, never an intermediate state. <span class="warn">If the temporary file is on another filesystem, `os.replace()` may fail; in CPython on Linux this is an `OSError` with `errno.EXDEV`.</span> Before the replace, call `flush()` and `os.fsync()` on the temporary file.[^py314-library-os-os-fsync]

## Detailed explanation

The problem is that `open(path, 'w')` first truncates the file to zero length.[^py314-library-functions-open] A reader that opens the file at that moment, or during the write, sees partial content, for example incomplete JSON. So replacing a file in place is unsafe: the new data is written to a separate temporary file, which is then renamed over the old one.

`os.replace(src, dst)` replaces `dst` with `src`. The documentation says that a successful replace is atomic and that this is a POSIX requirement.[^py314-library-os-os-replace] A reader that opened `dst` after the replacement sees the new content. A reader that opened the old file earlier keeps reading the old data through its already open descriptor. So atomicity applies to the rename itself, not to the whole update.

The temporary file must be on the same filesystem as the target. A rename across filesystems may fail; in CPython on Linux this is an `OSError` with `errno.EXDEV`.[^py314-library-os-os-replace] So the temporary file is created in the same directory as the target, as in the function below:

```python
import os
import tempfile
from pathlib import Path

def write_atomic(target: Path, data: str) -> None:
    # The temp file must be in the same directory, so the rename stays on one filesystem.
    fd, tmp_name = tempfile.mkstemp(dir=target.parent, prefix=target.name, suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        # mkstemp() creates the file with mode 0600; set the mode the target needs before this line.
        os.replace(tmp_name, target)   # atomic on POSIX: readers see the old or the new content
    except BaseException:
        os.unlink(tmp_name)            # the replace did not happen: remove the temp file
        raise
```

`flush()` moves Python's buffer into the OS buffer, and `os.fsync()` asks the OS to write the data to disk.[^py314-library-os-os-fsync] Without `fsync`, after a system crash on some filesystems the rename can reach the disk before the data does. `mkstemp()` creates a file readable and writable only by its creator,[^py314-library-tempfile-mkstemp] so in practice the mode is 0600, and after the replacement the file keeps those permissions. The function does not restore the original mode; if other users need to read the file, set the mode explicitly.

**Common mistakes:**
- creating the temporary file in `/tmp` or another directory: `os.replace()` may fail with `EXDEV`;
- skipping `flush()` and `os.fsync()` and assuming the data is on disk after the rename;
- not checking the file's permissions after the replacement;
- assuming atomicity is guaranteed on every platform: the documentation describes it as a POSIX requirement.
