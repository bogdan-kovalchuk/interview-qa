---
id: py-prac-0019
title: "Реалізуйте context manager для transaction-like resource, який commit при success, rollback при exception та не приховує failure."
description: "У __exit__ виконуйте commit, коли exc_type є None, і rollback інакше."
track: python
section: practical-coding
level: senior
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-compound
  title: 'Python 3.13: Compound statements: with and finally'
  url: https://docs.python.org/3.13/reference/compound_stmts.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-model
  title: 'Python 3.13: Data model: hashing and context managers'
  url: https://docs.python.org/3.13/reference/datamodel.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Реалізуйте `Transaction(resource)` як context manager. Повертайте resource при вході, виконуйте commit після successful body, rollback після body exception й ніколи не приховуйте failures.

## Constraints

- Resource уже отриманий і має commit() та rollback().
- Acquisition і closing поза цим контрактом.
- Commit failure поширюється без automatic rollback; rollback failure поширюється з body exception як context.

## Short answer

**У `__exit__` виконуйте commit, коли exc_type є None, і rollback інакше.** Повертайте False, щоб body exception поширювався. Якщо commit або rollback сам завершується failure, поширюйте її замість повідомлення success.

## Detailed explanation

With protocol передає body exception у __exit__. False return не приховує його; exception із __exit__ стає зовнішньою failure з automatic context chaining для попереднього body exception. Wrapper задає control flow, а не database durability чи atomicity. [^py313-compound] [^py313-model]

## Examples

```python
# A minimal resource supplied by the caller.
class Resource:
    def commit(self):
        self.committed = True
    def rollback(self):
        self.rolled_back = True
r = Resource()
with Transaction(r) as value:
    assert value is r
assert r.committed
```

## Solution

```python
class Transaction:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.resource.commit()
        else:
            self.resource.rollback()
        return False
```

## Complexity

O(1) роботи й пам’яті wrapper. Реальний час commit та rollback і пам’ять resource залежать від наданої implementation. [^py313-compound] [^py313-model]

## Edge cases

Перевірте success, body failure, BaseException, commit failure та rollback failure з exception chaining.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

class Resource:
    def __init__(self, failing=None):
        self.events = []
        self.failing = failing
    def commit(self):
        self.events.append("commit")
        if self.failing == "commit":
            raise RuntimeError("commit failed")
    def rollback(self):
        self.events.append("rollback")
        if self.failing == "rollback":
            raise RuntimeError("rollback failed")
r = Resource()
with Transaction(r) as value:
    assert value is r
assert r.events == ["commit"]
for failure in (ValueError("body"), KeyboardInterrupt()):
    r = Resource()
    with pytest.raises(type(failure)) as caught:
        with Transaction(r):
            raise failure
    assert caught.value is failure and r.events == ["rollback"]
r = Resource("commit")
with pytest.raises(RuntimeError):
    with Transaction(r):
        pass
assert r.events == ["commit"]
r = Resource("rollback")
failure = ValueError("body")
with pytest.raises(RuntimeError) as caught:
    with Transaction(r):
        raise failure
assert caught.value.__context__ is failure and r.events == ["rollback"]
```

## Evaluation guide

### Expected signals

Перевіряйте, який саме resource method виконався. Не обіцяйте automatic recovery після ambiguous commit failure.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Яку policy ви оберете, якщо і body, і rollback завершуються failure?

## Sources

<!-- generated from frontmatter -->
