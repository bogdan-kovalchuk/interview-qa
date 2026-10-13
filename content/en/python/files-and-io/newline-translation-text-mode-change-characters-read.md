---
id: py-fileio-0003
title: "How can newline translation in text mode change the characters read or written on different platforms?"
description: "How can newline translation in text mode change the characters read or written on different platforms?"
track: python
section: files-and-io
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-os-os-linesep
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.linesep
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: values of os.linesep per platform and the text-mode warning."
  - source_id: py314-library-csv
    title: "Python 3.14: Library/csv"
    url: https://docs.python.org/3.14/library/csv.html#csv.writer
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the csv module asks that file objects be opened with newline=''."
---

## Short answer

**In text mode with `newline=None` (the default), reading translates every `\r\n`, `\r` and `\n` into `\n`, and writing replaces `\n` with `os.linesep`, which is `\r\n` on Windows.**[^py314-library-io][^py314-library-os-os-linesep] <span class="warn">As a result, a file's size in bytes can change after a read-and-write round trip, and hashes such as SHA-256 can differ between platforms.</span>[^py314-library-io] To avoid the translation, open the file with `newline=""` or use binary mode.[^py314-library-io]

## Detailed explanation

The `newline` parameter controls how the text layer translates line endings. The default `None` enables universal newlines mode: on reading, `\n`, `\r` and `\r\n` are translated into `\n`, and on writing, each `\n` is replaced with `os.linesep`.[^py314-library-io] The translation happens in the text layer, so the `str` in the program and the bytes on disk can differ.

Below is one file containing a CRLF line and a lone `\r` at the end. Reading with the default parameters returns `\n`, while `newline=""` keeps the line endings as they are in the file. The same text is then written with the default `newline` and with `newline="\r\n"`. The outputs in the comments were obtained on CPython 3.13 and 3.14 on Linux, where `os.linesep` is `\n`:

```python
with open("lines.txt", "wb") as f:
    f.write(b"a\r\nb\r")                    # CRLF line, then a lone CR at the end

with open("lines.txt", encoding="utf-8") as f:           # newline=None (default)
    print(f.read().splitlines(True))                      # ['a\n', 'b\n']

with open("lines.txt", encoding="utf-8", newline="") as f:
    print(f.read().splitlines(True))                      # ['a\r\n', 'b\r']

with open("lines.txt", "w", encoding="utf-8") as f:       # newline=None on write
    f.write("a\nb\n")
print(open("lines.txt", "rb").read())                     # b'a\nb\n' on Linux, b'a\r\nb\r\n' on Windows

with open("lines.txt", "w", encoding="utf-8", newline="\r\n") as f:
    f.write("a\nb\n")
print(open("lines.txt", "rb").read())                     # b'a\r\nb\r\n' on every platform
```

On Windows `os.linesep` is `\r\n`,[^py314-library-os-os-linesep] so the same text write produces different bytes. An explicit `newline="\r\n"` gives the Windows result on any platform; `newline=""` and `newline="\n"` translate nothing.[^py314-library-io] The os documentation advises not to use `os.linesep` as a line terminator when writing files opened in text mode, and to write a single `\n` on all platforms instead.[^py314-library-os-os-linesep]

The pitfall shows up wherever the bytes matter: the hash or size of a file, comparing results across operating systems, and formats with fixed line endings. The `csv` module asks that file objects be opened with `newline=""`: without it, newlines inside quoted fields may not be interpreted correctly, and on platforms that use `\r\n` an extra `\r` is added on write.[^py314-library-csv] If you need exact bytes, open the file in binary mode and encode or decode the text explicitly.

**Common mistakes:**
- comparing hashes or sizes of text files written on different operating systems;
- reading a file with the default `newline` when the line endings must be kept as they are;
- opening a CSV file without `newline=""`: an extra `\r` on write on `\r\n` platforms, and wrong parsing of fields that contain newlines.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
