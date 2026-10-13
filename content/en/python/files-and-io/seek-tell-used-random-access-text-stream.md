---
id: py-fileio-0008
title: "How are `seek()` and `tell()` used for random access, and why can't text-stream offsets always be treated as character positions?"
description: "How are `seek()` and `tell()` used for random access, and why can't text-stream offsets always be treated as character positions?"
track: python
section: files-and-io
level: middle
type: mechanism
tags: [seek, tell]
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
  - source_id: py314-library-io-iobase-seek
    title: "Python 3.14: Library/io (IOBase.seek)"
    url: https://docs.python.org/3.14/library/io.html#io.IOBase.seek
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: seek() sets the stream position to a byte offset relative to whence."
  - source_id: py314-library-io-textiobase-seek
    title: "Python 3.14: Library/io (TextIOBase.seek)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOBase.seek
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: in text mode the offset must be a value returned by tell() or zero; other values produce undefined behavior; four call forms are supported."
  - source_id: py314-library-io-textiobase-tell
    title: "Python 3.14: Library/io (TextIOBase.tell)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOBase.tell
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: tell() returns an opaque number that usually does not represent a number of bytes in the underlying storage."
  - source_id: ietf-rfc3629
    title: "RFC 3629: UTF-8, a transformation format of ISO 10646"
    url: https://www.rfc-editor.org/rfc/rfc3629#section-3
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "RFC 3629, section 3: UTF-8 encodes Unicode characters in sequences of 1 to 4 octets; it does not describe Python behavior."
---

## Short answer

**In binary mode `seek()` and `tell()` work with byte offsets; in text mode `tell()` returns an opaque number that usually is not a byte count, and `seek()` accepts only values obtained from `tell()` or zero offsets.**[^py314-library-io-iobase-seek][^py314-library-io-textiobase-tell][^py314-library-io-textiobase-seek] With UTF-8 text, one character takes from 1 to 4 bytes, so a byte position is not the same as a character position.[^ietf-rfc3629] An arbitrary number passed to `seek()` is undefined behavior; in CPython, an offset inside a multibyte character raises `UnicodeDecodeError`.

## Detailed explanation

Random access means moving to a required place without reading all the content before it. For a binary file the position is a byte offset. `seek(offset)` moves the cursor, and `tell()` returns the current position.[^py314-library-io-iobase-seek] For fixed-size records, record number `i` starts at byte `i * record_size`. Example (`#` comments show the result):

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'records.bin')
with open(path, 'wb') as f:
    for i in range(5):
        f.write(i.to_bytes(4, 'little'))  # fixed-size records of 4 bytes

with open(path, 'rb') as f:
    f.seek(3 * 4)                               # jump to record 3 without reading 0..2
    print(int.from_bytes(f.read(4), 'little'))  # 3
    print(f.tell())                             # 16: a byte offset
```

In text mode, positions cannot be read as character numbers. A text stream decodes bytes into characters, and one character in UTF-8 takes from 1 to 4 bytes.[^ietf-rfc3629] `tell()` returns an "opaque number": according to the documentation, it usually is not a byte count, but a value that can be passed to `seek()` to restore the position.[^py314-library-io-textiobase-tell] In the example below, after reading three characters `tell()` returns 6, not 3. The same code also shows restoring a position and using an offset that did not come from `tell()`:

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'text.txt')
with open(path, 'w', encoding='utf-8') as f:
    f.write('aж€😀bc\n')       # 7 characters, 13 bytes in UTF-8

with open(path, encoding='utf-8') as f:
    print(repr(f.read(3)))     # 'aж€'
    print(f.tell())            # 6, not 3: this is not a character index
    f.seek(0)
    f.read(2)                  # 'a', 'ж'
    pos = f.tell()             # 3
    print(f.read(1))           # €
    f.seek(pos)                # restores a value returned by tell()
    print(f.read(1))           # €
    try:
        f.seek(pos + 1)        # not a value from tell(): undefined behavior
        f.read(1)
    except UnicodeDecodeError:
        print('UnicodeDecodeError')  # byte 4 is inside '€' (bytes 3 to 5)
```

The limits of `seek()` in text mode are narrow. `seek(0)`, `seek(0, SEEK_END)` and `seek(0, SEEK_CUR)` are allowed, and `seek(cookie)` accepts only a value from `tell()`.[^py314-library-io-textiobase-seek] CPython rejects nonzero relative seeks with `io.UnsupportedOperation` (for example `seek(1, SEEK_CUR)`, checked on 3.13 and 3.14). So a character number is not turned into a position for `seek()`: you read characters, or work with bytes.

**Common mistakes:**
- computing an offset as a character number, for example `seek(n)` for the n-th character of UTF-8 text;
- assuming that `tell()` in text mode is a byte count or a character count, and comparing it with the length of a string;
- passing an arbitrary number to `seek()`, such as an index found by a regular expression, instead of a value from `tell()`: this is undefined behavior.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
