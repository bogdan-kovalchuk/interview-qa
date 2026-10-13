---
id: py-fileio-0010
title: "Why doesn't a string-prefix check determine path containment when `..` is present, and how does `Path.resolve()` change the lexical path before comparison?"
description: "Why doesn't a string-prefix check determine path containment when `..` is present, and how does `Path.resolve()` change the lexical path before comparison?"
track: python
section: files-and-io
level: middle
type: pitfall
tags: [path-resolve]
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
  - source_id: py314-library-pathlib-path-resolve
    title: "Python 3.14: Library/pathlib (Path.resolve)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.resolve
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: resolve() makes the path absolute, resolves symlinks and eliminates '..' (the only Path method that does so)."
  - source_id: py314-library-pathlib-purepath-is-relative-to
    title: "Python 3.14: Library/pathlib (PurePath.is_relative_to)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: is_relative_to() is string-based, neither accesses the filesystem nor treats '..' segments specially."
---

## Short answer

**A string `startswith()` ignores `..` and symlinks: the path `/data/public/../secret` lexically starts with `/data/public`, but actually points to `/data/secret`.**[^py314-library-pathlib-path-resolve] `Path.resolve()` makes a path absolute, resolves symlinks and eliminates `..` according to the real filesystem structure.[^py314-library-pathlib-path-resolve] After that, check containment with `is_relative_to()` on both paths, the base directory and the candidate, because `is_relative_to()` itself works on strings and does not understand `..`.[^py314-library-pathlib-purepath-is-relative-to]

## Detailed explanation

A string comparison sees only characters, while the filesystem resolves a path step by step: `..` means the parent directory according to the actual structure, and a symlink changes which directory is the parent. `Path.is_relative_to()` is also string-based and does not understand `..`, so by itself it does not replace resolving the path.[^py314-library-pathlib-purepath-is-relative-to] Example (`#` comments show the result):

```python
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp()).resolve()
(root / 'data' / 'public').mkdir(parents=True)
(root / 'data' / 'secret').mkdir()
(root / 'data' / 'secret' / 'key.txt').write_text('top secret')
(root / 'data' / 'public' / 'ok.txt').write_text('hello')
(root / 'data' / 'public' / 'link').symlink_to(root / 'data' / 'secret')

base = root / 'data' / 'public'
for user in ('ok.txt', '../secret/key.txt', 'link/key.txt'):
    candidate = base / user
    prefix_ok = str(candidate).startswith(str(base))
    resolved_ok = candidate.resolve().is_relative_to(base.resolve())
    print(user, prefix_ok, resolved_ok)
# ok.txt True True
# ../secret/key.txt True False
# link/key.txt True False
```

The first path lies inside base under both checks. The second and third pass `startswith()`, but after resolution they lie outside `public`. `Path.resolve()` makes the path absolute, resolves symlinks and eliminates `..`; the documentation says this is the only `Path` method that eliminates `..`.[^py314-library-pathlib-path-resolve]

For the check to be correct, resolve both paths: the base directory and the candidate. If the base itself contains a symlink, the unresolved base is not a prefix of the resolved candidate, and a valid path is rejected by mistake (checked on 3.13 and 3.14). `is_relative_to()` compares path parts rather than characters: `Path('/data/public2/x').is_relative_to('/data/public')` gives `False`, while `startswith()` gives `True`. The function below combines these steps and returns a path only when it lies inside base:

```python
from pathlib import Path

def safe_join(base: Path, user_part: str) -> Path:
    base_resolved = base.resolve()     # resolve the base too, not only the user part
    candidate = (base_resolved / user_part).resolve()
    if not candidate.is_relative_to(base_resolved):   # compares whole components
        raise ValueError(f'path escapes base: {user_part}')
    return candidate
```

This is not complete protection: between `resolve()` and opening the file, a symlink can be created in an already checked component (a TOCTOU race). For untrusted input, the file should be opened relative to a directory descriptor without following symlinks; that is a separate topic.

**Common mistakes:**
- checking `str(path).startswith(str(base))`: `/data/public2/x` passes for `/data/public`;
- calling `is_relative_to()` without `resolve()`: `(base / '../../x').is_relative_to(base)` gives `True`, although the path leaves base;
- resolving only the user's path and leaving base unresolved when base itself contains a symlink.

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
