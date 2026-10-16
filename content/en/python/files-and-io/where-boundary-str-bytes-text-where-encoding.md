---
id: py-fileio-0001
title: "Where is the boundary between `str` and `bytes` in text I/O, and where should encoding and decoding happen?"
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

**Text I/O works with `str`, binary I/O works with `bytes`; encoding happens when `str` is written as bytes, and decoding happens when bytes are read back as `str`.**[^py314-library-io] In CPython, the `TextIOWrapper` layer sits on top of a buffered binary stream: on `write()` it encodes text into bytes and passes them down, and on `read()` it decodes the bytes back into `str`. The binary layer (`BufferedWriter`/`BufferedReader`) does neither encoding nor newline translation.

## Detailed explanation

The boundary runs between the text and binary layers of the `io` stack. Text I/O accepts and returns `str`, while binary I/O works with bytes-like objects and returns `bytes`.[^py314-library-io] Encoding and decoding are done by the text layer: `open()` in text mode returns a `TextIOWrapper`, which turns `str` into bytes with the chosen encoding on write, and turns bytes back into `str` on read. That is why a binary stream does not accept `str`, and a text stream does not return `bytes`.

Here is the same boundary in code: a string is converted to bytes and back explicitly, and then two standard-library modules show which type each layer expects.

```python
import json
import pickle

data = "Привіт".encode("utf-8")
print(data)                          # b'\xd0\x9f\xd1\x80...' (12 bytes for 6 characters)
print(data.decode("utf-8"))          # Привіт
print(len("Привіт"), len(data))      # 6 12

with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Привіт"}, f, ensure_ascii=False)   # json writes str: text file

with open("data.pkl", "wb") as f:
    pickle.dump({"name": "Привіт"}, f)                     # pickle writes bytes: binary file
```

`json.dump()` needs a text file, because the module always produces `str`, so `fp.write()` must accept `str`.[^py314-library-json] `pickle.dump()` writes to a binary file, because a pickle is a stream of bytes.[^py314-library-pickle] `Path.write_text()` takes `encoding` and `newline` (`newline` since Python 3.10), like `open()`; `Path.read_text()` takes `encoding` and `errors`, and its `newline` parameter appeared only in 3.13, so on 3.12 and earlier use `open()` for it.[^py314-library-pathlib] The rule for `encoding` is the same in all three cases.

The mistake is quiet. Text decoded with the wrong codec raises no exception when the bytes are valid in that codec; it just becomes different text. For example, the UTF-8 bytes of `"Привіт"` decoded as `cp1251` give a string of other letters. The encoding must come from the file's contract, not from guessing the bytes.

**Common mistakes:**
- comparing the result of `read()` from a file opened in binary mode with a `str` (`b'...' != '...'`);
- expecting text-mode `open()` to return `bytes`, and decoding a `str` that was already read;
- guessing a file's encoding instead of setting it explicitly.
