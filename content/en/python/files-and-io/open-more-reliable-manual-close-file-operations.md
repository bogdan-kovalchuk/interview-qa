---
id: py-fileio-0006
title: "Why is `with open(...)` more reliable than a manual `close()` after file operations?"
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
  - source_id: py314-library-io-iobase
    title: "Python 3.14: Library/io (IOBase)"
    url: https://docs.python.org/3.14/library/io.html#io.IOBase
  - source_id: py314-reference-compound-stmts-with
    title: "Python 3.14: Reference/compound Stmts (with)"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-with-statement
---

## Short answer

**`with` guarantees that the file is closed even when an exception is raised inside the block.**[^py314-library-io-iobase] The `with` statement calls `__exit__` whenever `__enter__` has returned without error.[^py314-reference-compound-stmts-with] With a manual `f = open(...)` … `f.close()`, an exception between those calls skips `close()`, and the file stays open until its object is freed (in CPython, when the last reference disappears, including one held by a traceback).

## Detailed explanation

`with` is a context manager: the statement calls `__enter__` at the start of the block and `__exit__` when it leaves the block, whatever the reason for leaving – normal completion, `return`, `break`, or an exception. For a file object, `__exit__` closes the file. So closing does not depend on reaching a `close()` line.[^py314-reference-compound-stmts-with][^py314-library-io-iobase]

The manual version has a weak spot: `close()` comes after code that may fail. If an exception is raised between `open()` and `close()`, control jumps to the handler and `close()` is never called. The function `manual()` raises before `close()`, so `close()` is never called; `with_block()` also raises, but `__exit__` closes the file. The code then shows whether each file is closed (`#` comments show the result):

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'data.txt')
with open(path, 'w') as f:
    f.write('hello\n')

def manual(p):
    f = open(p)
    raise ValueError('boom')   # the close() below is never reached
    f.close()

def with_block(p):
    with open(p) as f:
        raise ValueError('boom')

for func in (manual, with_block):
    try:
        func(path)
    except ValueError as e:
        f = e.__traceback__.tb_next.tb_frame.f_locals['f']  # local f of func
        print(func.__name__, 'file closed:', f.closed)
# manual file closed: False
# with_block file closed: True
```

The result comes from reference counting in CPython. While the traceback holds the frame of `manual()`, its local `f` stays alive, and the file stays open. When the traceback is released, `f` is freed and the file is closed. So the descriptor remains open for as long as the exception object lives, not merely until the function returns. On implementations without reference counting, the moment of closing can be later. `with`, by contrast, closes the file when the block is left, however it was left.

`with` does not make a write atomic and does not undo what was already written. If an exception occurs in the middle of a write, part of the data is already in the file; for a safe file replacement, see qid:py-fileio-0007. A file object that is used after its block has ended is already closed, and any operation on it raises `ValueError`.

**Common mistakes:**
- assuming `with` is only needed for writing: it closes the file after reading too;
- keeping `f` outside the block and using it later, when the file is already closed;
- assuming `with` makes a write atomic: an exception in the middle of a write leaves partly written data.
