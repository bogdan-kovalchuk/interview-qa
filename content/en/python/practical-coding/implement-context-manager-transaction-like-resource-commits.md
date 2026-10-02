---
id: py-prac-0019
title: "Implement a context manager for a transaction-like resource that commits on success, rolls back on exception, and never hides a failure."
description: "In __exit__, commit when exc_type is None and rollback otherwise."
track: python
section: practical-coding
level: senior
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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

Implement `Transaction(resource)` as a context manager. Return the resource on entry, commit after a successful body, rollback after a body exception, and never suppress failures.

## Constraints

- The resource is already acquired and exposes commit() and rollback().
- Acquisition and closing are outside this contract.
- Commit failure propagates without automatic rollback; rollback failure propagates with the body exception as its context.

## Short answer

**In `__exit__`, commit when exc_type is None and rollback otherwise.** Return False so a body exception propagates. If commit or rollback itself fails, propagate that failure instead of claiming success.

## Detailed explanation

The with protocol supplies the body exception to __exit__. A false return does not suppress it; an exception raised by __exit__ becomes the outward failure, with automatic context chaining for a prior body exception. This wrapper specifies control flow, not database durability or atomicity. [^py313-compound] [^py313-model]

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

O(1) wrapper work and storage. Actual commit and rollback time and resource storage depend on the supplied implementation. [^py313-compound] [^py313-model]

## Edge cases

Test success, body failure, BaseException, commit failure and rollback failure with exception chaining.

## Tests

Run after the Solution block with pytest installed.

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

Assert exactly which resource method ran. Do not promise automatic recovery from an ambiguous commit failure.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

What policy would you choose if both the body and rollback fail?

## Sources

<!-- generated from frontmatter -->
