---
id: py-fileio-0005
title: "What data can remain in a Python buffered stream after `write()`, and what does `flush()` change?"
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
---

## Short answer

**After `write()`, data can remain in Python's internal buffers, either in the `TextIOWrapper` text layer or in the `BufferedWriter`, and not yet have been passed to the OS raw stream.**[^py314-library-io] `flush()` forces the buffer into the raw stream, and other file descriptors for the same file see the data (observed on Linux). A write to disk is done with `os.fsync()`.[^py314-library-os-os-fsync] Closing the stream also flushes the buffer.[^py314-library-io]

## Detailed explanation

Writing passes through several places. `TextIOWrapper` encodes `str` into bytes and may hold them in its own queue. `BufferedWriter` accumulates bytes in a buffer and passes them to the raw stream, that is, to the OS, when the buffer has to be written out, or when `flush()` is called.[^py314-library-io] So after `write()` the data may not yet have reached the OS, and the file on disk does not contain it.

The file size shows where the data is. Both `print` calls run inside the `with` block, that is, before the file is closed:

```python
import os

with open("events.txt", "w", encoding="utf-8") as f:
    f.write("started\n")
    print(os.path.getsize("events.txt"))  # 0: the text is still in Python's buffers
    f.flush()
    print(os.path.getsize("events.txt"))  # 8: flush() passed the bytes to the OS
```

Apart from `flush()`, the buffer is also flushed on `close()`: the documentation describes it as "flush and close this stream".[^py314-library-io] In CPython, a flush is also observed on `seek()` and when the buffer fills up, but the documentation does not give a fixed threshold for filling. The buffer size depends on the version: `print(io.DEFAULT_BUFFER_SIZE)` gives 8192 on 3.12 and 3.13 and 131072 on 3.14 (observed; the documentation does not give the value), and `open()` uses the block size from `os.stat()` when possible.[^py314-library-io] Do not build logic on a particular buffer size.

After `flush()` the data is already in the OS: a second descriptor for the same file, in the same process, read the written bytes without `fsync` (observed on Linux). This is visibility within the OS, not a write to disk, for which `os.fsync()` is needed.[^py314-library-os-os-fsync] To remove Python's buffering, you can open the file in binary mode with `buffering=0`: the documentation describes this as a way to create a raw stream, and then `write()` goes to the OS without an intermediate buffer.[^py314-library-io]

**Common mistakes:**
- checking the file right after `write()` and concluding that the write failed;
- assuming that `flush()` writes the data to disk, rather than only passing it to the OS;
- relying on a particular buffer size: it differs between Python versions and depends on the file.
