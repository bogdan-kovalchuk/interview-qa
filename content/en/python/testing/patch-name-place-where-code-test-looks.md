---
id: py-testing-0011
title: "Why must you patch the name at the place where the code under test looks it up during `patch()`?"
description: "Why must you patch the name at the place where the code under test looks it up during `patch()`?"
track: python
section: testing
level: middle
type: pitfall
tags: [patch]
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
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock, Where to patch"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Where to patch: the patch applies where the code under test looks up the name."
---

## Short answer

**`patch()` changes the object that a name points to in one specific namespace, so you must patch the name where the code under test looks it up.**[^py314-library-unittest-mock-where-to-patch] If module `b` does `from a import SomeClass`, then `b` already holds its own reference to the class, and `patch('a.SomeClass')` has no effect on the code in `b`. The correct patch is `patch('b.SomeClass')`.

## Detailed explanation

`patch()` temporarily replaces the object that a name points to, but only in the namespace named in its target argument. So what matters is not where the class is defined but where the code under test looks the name up at run time. The `unittest.mock` documentation states the rule this way: patch where the object is looked up, which is not necessarily where it is defined.[^py314-library-unittest-mock-where-to-patch]

Suppose `a.py` defines `SomeClass` whose `run()` method returns `"real"`, and `b.py` contains `from a import SomeClass` and a function `some_function()` that returns `SomeClass().run()`. When `b` is imported, it gets its own reference to the class. Patching `a.SomeClass` replaces the attribute of module `a`, but `b` already holds the old reference. Example: the patch in the wrong place misses `b`, and the patch in `b` reaches it.

```python
from unittest import mock
import b  # b.py: from a import SomeClass; some_function() calls SomeClass().run()

# Wrong: replaces a.SomeClass, but b already holds the real class
with mock.patch("a.SomeClass") as fake:
    fake.return_value.run.return_value = "fake"
    print(b.some_function())  # real

# Right: replaces the name in b, where some_function looks it up
with mock.patch("b.SomeClass") as fake:
    fake.return_value.run.return_value = "fake"
    print(b.some_function())  # fake
```

The rule does not change when the code reaches the class through a module. If `c.py` does `import a` and calls `a.SomeClass()` when the function runs, then `patch('a.SomeClass')` works, because `c` looks the name up in `a` every time. So there is no universal "patch in a": find where the code under test reads the name, and patch it there.

**Common mistakes:**
- patching `a.SomeClass` when the module did `from a import SomeClass`, and then trusting a test that in fact uses the real class;
- patching the defining module without checking how the tested module imports the name;
- "fixing" a patch by changing the imports in the production code instead of patching the place where the name is used.

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
