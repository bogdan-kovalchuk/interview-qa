---
id: py-fileio-0002
title: "Why is it worth setting `encoding` explicitly for a portable text file, instead of relying on the platform default?"
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
  - source_id: py314-library-locale
    title: "Python 3.14: Library/locale"
    url: https://docs.python.org/3.14/library/locale.html#locale.getencoding
  - source_id: pep-0686
    title: "PEP 686: Make UTF-8 mode default"
    url: https://peps.python.org/pep-0686/
---

## Short answer

**The default encoding is set by the locale: on Windows `locale.getencoding()` returns the ANSI code page, and on most Unix systems it is `utf-8`.**[^py314-library-locale][^py314-library-io] A file written without an explicit `encoding` may be unreadable on another machine.[^py314-library-io] An explicit `encoding="utf-8"` does not depend on the locale. From Python 3.15, UTF-8 Mode is the default,[^pep-0686] and in 3.14 and earlier the default depends on the locale unless UTF-8 Mode is enabled.[^py314-library-io]

## Detailed explanation

The text layer uses the locale for its encoding when `encoding` is not given. On Windows, `locale.getencoding()` returns the ANSI code page; on Unix it returns the locale's encoding. It ignores UTF-8 Mode: `locale.getpreferredencoding(False)` respects that mode, while `locale.getencoding()` does not.[^py314-library-locale] For example, with `LC_ALL=POSIX` and `-X utf8` (checked on 3.12, 3.13 and 3.14), `locale.getencoding()` returns `ANSI_X3.4-1968`, while `open()` uses `utf-8`, which is its default in UTF-8 Mode.[^py314-library-io] So the same code can write and read different bytes on different machines. The Python documentation names this as a common source of bugs: most Unix platforms use a UTF-8 locale, while for most Windows users the locale encoding is not UTF-8.[^py314-library-io]

Set the parameter on both writing and reading, so both sides use the same codec:

```python
import locale
from pathlib import Path

Path("notes.txt").write_text("Привіт, світе\n", encoding="utf-8")   # explicit encoding: the codec does not depend on the locale
print(Path("notes.txt").read_text(encoding="utf-8"))                 # Привіт, світе
print(locale.getencoding())   # UTF-8 in this Linux run; the ANSI code page (often cp1252) on Windows
```

`Path.read_text()` without `encoding` behaves like `open()`: it uses the same locale encoding.[^py314-library-pathlib][^py314-library-io] The output of `locale.getencoding()` depends on the machine, so do not treat it as a fixed value in tests.

The mistake is often silent. Bytes written in one encoding can be read by another without an exception and produce different text, so a test on a developer's machine may pass while the same code gives garbage elsewhere. To find places where a program relies on the default encoding, run it with `-X warn_default_encoding`: then `open()` without `encoding` emits an `EncodingWarning`.[^py314-library-io] If the locale encoding is really wanted, write `encoding="locale"` (supported since Python 3.10) so the intent is visible in the code.[^py314-library-io]

From Python 3.15, UTF-8 Mode is the default (PEP 686),[^pep-0686] but code that must also run on 3.14 or earlier still needs an explicit `encoding`.[^py314-library-io] UTF-8 Mode enabled for the whole process changes the default for every file in the program; an explicit `encoding` at the place where the file is opened is visible in the code and does not depend on how the interpreter was started.

**Common mistakes:**
- testing only on Linux with a UTF-8 locale and assuming the code is portable;
- setting `encoding` only for reading or only for writing;
- assuming that the UTF-8 default in 3.15 removes the need for `encoding` in code that must run on 3.14 or earlier.
