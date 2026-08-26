---
id: py-prac-0019
title: "Реалізуйте context manager для transaction-like resource, який commit при success, rollback при exception та не приховує failure."
description: "__exit__ перевіряє exc_type is None для commit, інакше rollback; return False (або неявний None) не приховує exception – він propagate далі."
track: python
section: practical-coding
level: senior
type: coding
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: false
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Task

TODO

## Constraints

TODO

## Short answer

**`__exit__` перевіряє `exc_type is None` для commit, інакше rollback; `return False` (або неявний `None`) не приховує exception – він propagate далі.** Водночас <span class="warn">`return True` з `__exit__` приховує exception – це небезпечно для transaction semantics, бо caller не дізнається про failure.</span>

```python
class Transaction:
    def __init__(self, name):
        self.name = name
        self.committed = False
        self.rolled_back = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.committed = True
        else:
            self.rolled_back = True
        return False  # do not suppress exception

t = Transaction("tx1")
with t:
    pass
t.committed  # True
```

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
