---
id: py-testing-0012
title: "How do `spec`, `spec_set`, and autospeccing help a mock detect drift from the real interface?"
description: "How do `spec`, `spec_set`, and autospeccing help a mock detect drift from the real interface?"
track: python
section: testing
level: middle
type: mechanism
tags: [spec, spec-set]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official pytest documentation."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Hypothesis (property-based testing) documentation."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official mutmut (mutation testing) documentation."
  - source_id: py314-library-unittest-mock-mock-class
    title: "Python 3.14: Library/unittest.mock, Mock class"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the spec and spec_set parameters of the Mock class; the names come from dir() of the object, and its signature is used to match calls."
  - source_id: py314-library-unittest-mock-autospeccing
    title: "Python 3.14: Library/unittest.mock, Autospeccing"
    url: https://docs.python.org/3.14/library/unittest.mock.html#autospeccing
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: autospeccing copies the interface and signatures; a call with wrong arguments raises TypeError."
---

## Short answer

**`spec` allows access only to attributes of the real object, `spec_set` also forbids writing non-existent attributes.**[^py314-library-unittest-mock-mock-class] Autospeccing recursively copies the interface and signatures.[^py314-library-unittest-mock-autospeccing] Reading a missing attribute on a mock with `spec` or `spec_set` raises `AttributeError`. Only autospeccing (`create_autospec` or `patch(..., autospec=True)`) raises `TypeError` for wrong arguments, so interface drift shows up in the test.[^py314-library-unittest-mock-autospeccing]

## Detailed explanation

A plain `Mock()` accepts any attribute and any arguments: it creates an attribute on first access. So a test that calls the old method name on the mock still passes, even when the real class has already renamed that method. The documentation describes exactly this problem: tests with mock objects in place of real ones can keep passing while the code is already broken.[^py314-library-unittest-mock-autospeccing]

The `spec` parameter defines which names exist. The mock takes its names from `dir()` of the object (a class, an instance or a function), and reading an attribute outside that list raises `AttributeError`. Writing is not restricted in the same way: `spec` lets you assign any attribute, while `spec_set` also forbids writes.[^py314-library-unittest-mock-mock-class]

Example: reading and writing on mocks with `spec`, `spec_set` and autospec.

```python
from unittest import mock

class Repo:
    def save(self, item):
        return item

spec_mock = mock.Mock(spec=Repo)
spec_mock.delete = 1            # allowed: spec restricts reads, not writes
try:
    spec_mock.remove            # Repo has no 'remove'
except AttributeError as e:
    print(e)                    # Mock object has no attribute 'remove'

spec_set_mock = mock.Mock(spec_set=Repo)
try:
    spec_set_mock.delete = 1    # spec_set also blocks writes
except AttributeError as e:
    print(e)                    # Mock object has no attribute 'delete'

autospec_mock = mock.create_autospec(Repo, instance=True)
try:
    autospec_mock.save()        # the copied signature requires 'item'
except TypeError as e:
    print(e)                    # missing a required argument: 'item'
```

`create_autospec` (and `patch(..., autospec=True)`) copies the interface recursively: methods get the signature of the original, so a wrong number of arguments raises `TypeError`.[^py314-library-unittest-mock-autospeccing] A plain `spec` does not do this: it does not reject a call with wrong arguments, but it uses the signature to match calls.[^py314-library-unittest-mock-mock-class] Signature checking is a separate mechanism, and you must enable it on purpose.

**Common mistakes:**
- using a plain `Mock()` without a spec in tests where agreement with the real API matters: such a test does not notice a rename;
- using `spec=Repo` for an attribute created in `__init__` (`self.conn = ...`): the class does not have it, so reading it raises `AttributeError` even though an instance has it (checked on 3.13 and 3.14); in that case take the spec from an instance, if creating it is safe;
- assuming that a plain `spec` checks call signatures: only autospeccing raises `TypeError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
