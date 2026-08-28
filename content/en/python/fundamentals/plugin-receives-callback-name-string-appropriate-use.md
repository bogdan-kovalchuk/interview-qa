---
id: py-fund-0008
title: "A plugin receives a callback name as a string: when is it appropriate to use `getattr(plugin, name)`, and when is an explicit registry of allowed callbacks a safer API?"
description: "A plugin receives a callback name as a string: when is it appropriate to use `getattr(plugin, name)`, and when is an explicit registry of allowed callbacks a safer API?"
track: python
section: fundamentals
level: middle
type: comparison
tags: [getattr-plugin-name]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L332-L393
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`getattr()` is appropriate when dynamic attribute lookup is part of a trusted plugin API contract and the name has already been validated.**[^py314-reference-executionmodel] If the name comes from configuration or external input, an explicit registry captures the allowlist, the aliases and a stable public API better. After `getattr()` you still have to check that the value is permitted and callable.

## Detailed explanation

`getattr(obj, name)` is ordinary attribute access in which the name is computed rather than written
in the code. It goes through the same protocol as `obj.name`: `__getattribute__`, descriptors, and
`__getattr__` when the attribute is absent.[^py314-reference-datamodel] There is nothing magical or
circumventing about it.

The question is not whether `getattr` is safe in itself, but **where the string came from**. If the
name comes from a trusted, fixed contract - a plugin declares a set of hook methods and the core
asks for exactly those - this is normal dynamic dispatch.

If instead the string comes from configuration, an HTTP request or a database, then `getattr`
without validation turns every attribute of the object into a public API. A caller can reach private
methods, `__class__` and beyond, and a typo in the config gives an `AttributeError` instead of a
comprehensible message.

```python
# trusted: the hook set is part of the plugin contract, fixed in code
for hook in ('on_start', 'on_finish'):
    handler = getattr(plugin, hook, None)
    if handler is not None:
        handler()

# untrusted input: an allowlist decides, not the object's namespace
ACTIONS = {'export': do_export, 'import': do_import}
action = ACTIONS.get(user_supplied)      # None instead of a random attribute
```

An explicit registry wins not by being "faster" but by making the permitted set data: it is visible
in the code, it diffs in review, it does not depend on what other attributes the object happens to
have, and it allows aliases and stable public names that are not tied to method names.

**What to check if `getattr` is appropriate after all:**
- the name is in an explicit allowlist, not merely "does not start with an underscore";
- the value obtained really is callable - otherwise the call raises `TypeError` somewhere random;
- there is a `default` (the third argument), so that a missing hook is not an exception when it is
  optional;
- an absent attribute is handled as a normal case, not as a user error.

The last thing that is easy to forget: `getattr` makes the connection invisible to tooling. Code
search for the method name will not find the call site, and an IDE will not show that the method is
used at all.[^py314-reference-executionmodel] For an internal API that is an argument against; for a
plugin API whose implementations other people write, it is an acceptable price for extensibility.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
