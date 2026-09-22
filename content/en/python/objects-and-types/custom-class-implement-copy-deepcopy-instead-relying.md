---
id: py-objtypes-0011
title: "When should a custom class implement `__copy__` or `__deepcopy__` instead of relying on the default behaviour?"
description: "When should a custom class implement `__copy__` or `__deepcopy__` instead of relying on the default behaviour?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [copy, deepcopy]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Custom `__copy__` and `__deepcopy__` methods are needed when default copying breaks class invariants: when a class manages external resources or contains shared state that must not be cloned (cycles are handled safely by `deepcopy` via `memo`).**[^py314-reference-datamodel] By default, `copy.copy` creates a new object and copies attribute references, while `copy.deepcopy` recursively duplicates everything using a `memo` dictionary. <span class="warn">If a class contains, for example, a shared cache or logging handler, those attributes often must remain shared across copies – which is precisely controlled via `__deepcopy__`.</span>

## Detailed explanation

Implementing custom `__copy__` and `__deepcopy__` methods is necessary when the standard `copy` module cannot faithfully duplicate an object's state or when it violates class invariants.[^py314-library-copy] By default, `copy.copy()` constructs a new instance of the same type and duplicates attribute references, whereas `copy.deepcopy()` recursively duplicates all nested objects. If an object owns system handles (open files, sockets, thread locks) or interfaces with shared infrastructure such as a connection pool or logger, naive copying produces runtime defects (such as duplicating OS file descriptors or failing with unpicklable object errors).[^py314-reference-datamodel]

The `__copy__(self)` method is invoked by `copy.copy()` without extra arguments and should return a new instance with shallowly copied attributes. The `__deepcopy__(self, memo)` method receives a `memo` dictionary designed to prevent infinite recursion in cyclic data structures. Within `__deepcopy__`, developers must record the newly created instance in `memo[id(self)]` before recursively copying nested attributes, ensuring that cycles back to `self` resolve without raising `RecursionError`.

Custom methods also enable selective deep copying: cloning domain data while preserving shared references to caches, configuration singletons, or global registries.

An example demonstrating selective copying and cyclic safety using `memo`:

```python
import copy


class SessionData:
    def __init__(self, user_id: int, tags: list[str], shared_cache: dict):
        self.user_id = user_id
        self.tags = tags
        self.shared_cache = shared_cache  # should remain shared across copies

    def __copy__(self):
        # Shallow copy: duplicate list, keep shared cache reference
        return type(self)(self.user_id, list(self.tags), self.shared_cache)

    def __deepcopy__(self, memo):
        # Prevent infinite recursion on cyclic references
        if id(self) in memo:
            return memo[id(self)]
        new_instance = type(self)(self.user_id, [], self.shared_cache)
        memo[id(self)] = new_instance
        new_instance.tags = copy.deepcopy(self.tags, memo)
        return new_instance


cache = {"hits": 0}
s1 = SessionData(1, ["admin", "dev"], cache)
s2 = copy.deepcopy(s1)

s2.tags.append("tester")
s2.shared_cache["hits"] += 1

print(s1.tags)          # ['admin', 'dev'] (isolated copy)
print(s2.tags)          # ['admin', 'dev', 'tester']
print(s1.shared_cache)  # {'hits': 1} (shared reference preserved)
```

**Common use cases for custom copy implementations:**
- isolating OS descriptors: duplicating file descriptors with system calls (such as `os.dup`) rather than sharing raw handles;
- preserving shared state: preventing duplication of singletons, shared caches, connection pools, or loggers;
- performance optimizations: skipping ephemeral or easily recomputed cached values;
- avoiding `TypeError`: gracefully handling attributes containing types that the default `copy` machinery cannot duplicate.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
