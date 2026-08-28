---
id: py-fund-0011
title: "Why can automatically loading plugin classes through reflection be worse than an explicit registry, even though it removes manual registration?"
description: "Why can automatically loading plugin classes through reflection be worse than an explicit registry, even though it removes manual registration?"
track: python
section: fundamentals
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L394-L407
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Automatic loading through reflection makes the set of active plugin classes implicit, fragile under renaming, and without an allowlist.**[^py314-reference-executionmodel] Reflection scanning (dynamically importing a package's modules, finding subclasses via `__subclasses__()` or `getattr`) depends on naming conventions and import order, and can pick up classes nobody intended - test doubles, deprecated aliases or third-party types. An explicit registry (a dict or a list) gives a controlled allowlist, reduces import-time side effects and is easy to test, because the active set of classes is visible in the code instead of hiding behind a runtime scan.

## Detailed explanation

Reflection-based loading of plugin classes means finding the implementations at run time:
dynamically importing every module of a package, walking a base class's `__subclasses__()`, or
`getattr` by an assembled name, instead of listing the classes in code.

The problem is not the technique itself but that the set of active plugins stops being written down
anywhere. It becomes a function of which modules happened to be imported by the time of the scan,
and that depends on import order, on whether someone accidentally imported a test module, and on the
file naming convention.[^py314-reference-executionmodel]

Walking `__subclasses__()` shows this most clearly: the method returns **every** subclass that
exists in the process at that moment, including ones created in tests, deprecated aliases and
abstract intermediate bases.[^py314-reference-datamodel] The list has no filter other than the fact
of inheritance itself.

An example of what ends up in such an "automatic" set:

```python
class Plugin:
    ...

class RealPlugin(Plugin):
    ...

class DeprecatedAlias(Plugin):
    ...

# in tests/test_plugins.py, imported by the test runner:
class FakePlugin(Plugin):
    ...

Plugin.__subclasses__()  # [RealPlugin, DeprecatedAlias, FakePlugin] - the fake is in production
```

An explicit registry solves this by making the set data rather than a consequence. A dict
`PLUGINS = {'csv': CsvPlugin, 'json': JsonPlugin}` can be read, diffed in code review, covered by a
test and changed, with no fear that something will get picked up on its own.

The second cost of reflection is import-time side effects. To find the classes you first have to
import every module of the package, and a module body in Python executes during import, so any file
or connection opened at module level runs purely because of the
scan.[^py314-reference-executionmodel]

**What specifically breaks with reflection-based loading:**
- renaming a class or a file silently disables the plugin, and no test fails, because it is simply
  absent from the set;
- classes that had no business being there end up in it: test doubles, stale aliases, foreign types
  from imported libraries;
- the set depends on import order, so it can differ between running the application and running the
  tests;
- static analysers and code search see no connection, because the code never mentions the concrete
  class.

Reflection stays appropriate where the set really is open and outside the author's control - entry
points registered by third-party packages, for instance. There the allowlist is the responsibility
of the package installation mechanism, not of scanning a namespace.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
