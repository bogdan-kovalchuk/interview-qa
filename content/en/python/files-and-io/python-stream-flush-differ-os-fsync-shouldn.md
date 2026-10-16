---
id: py-fileio-0004
title: "How does a Python stream's `flush()` differ from `os.fsync()`, and why shouldn't either be described as a universal hardware-durability guarantee?"
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
  - source_id: linux-man-fsync
    title: "Linux man-pages: fsync(2)"
    url: https://man7.org/linux/man-pages/man2/fsync.2.html
---

## Short answer

**`flush()` passes buffered bytes into the raw stream, which means to the OS, while `os.fsync(fd)` asks the OS to force the file's data to disk.**[^py314-library-io][^py314-library-os-os-fsync] Neither is a universal hardware-durability guarantee: what happens below the OS, for example in a device cache, is outside Python's control, and the Python documentation does not promise it.[^py314-library-os-os-fsync] The documented sequence for a file object is `f.flush()` followed by `os.fsync(f.fileno())`.[^py314-library-os-os-fsync]

## Detailed explanation

In CPython, a text file has several buffering layers. `TextIOWrapper` may hold encoded bytes in its own queue and pass them to the `BufferedWriter` later. `BufferedWriter.flush()` forces the bytes out of the buffer into the raw stream,[^py314-library-io] which means they are handed to the OS. So `flush()` is needed, but it only gets the data to the OS; writing it to disk is a separate call.

`os.fsync()` is documented as forcing the file's data to be written to disk: on Unix it calls the native `fsync()`, and on Windows the `_commit()` function. For a file object, the documentation shows the sequence `f.flush()` followed by `os.fsync(f.fileno())`, to ensure that all internal buffers of the file are written to disk.[^py314-library-os-os-fsync] Example:

```python
import os

with open("journal.log", "a", encoding="utf-8") as f:
    f.write("record 1\n")
    f.flush()              # Python buffer -> OS
    os.fsync(f.fileno())   # request that the OS writes the file's data to disk
```

The limit of the guarantee is that `os.fsync()` is described as a request to the OS. The Python documentation does not describe the behaviour of a device's cache, a controller or a file system, and those layers are not controlled by Python. So after a successful call, you can say that Python asked the OS to write the data to disk; saying that the data is "guaranteed to be saved", without qualifying the hardware and file system, is wrong.

To replace a file, people often combine writing a temporary file, `flush()`, `os.fsync()` and `os.replace()`. The documentation says that `os.replace()` is atomic on POSIX if it succeeds; it may fail when the source and destination are on different file systems.[^py314-library-os-os-replace] Atomic replacement means a reader sees either the old or the new contents of the file, but by itself it does not make the write durable. On Linux, an `fsync()` on the file does not guarantee that the directory entry containing it has reached disk, so a durable replacement also needs an `fsync()` on a descriptor for the directory.[^linux-man-fsync]

**Common mistakes:**
- assuming that `flush()` writes the data to disk;
- calling `os.fsync(f.fileno())` without a preceding `f.flush()`: fsync does not guarantee to write the data still held in Python's buffer;
- describing `os.fsync()` as a guarantee that data survives a power failure, without qualifying the platform and hardware.
