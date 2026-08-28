---
id: py-compfn-0007
title: "How do you build a lazy pipeline with `itertools` so intermediate collections are never materialized?"
description: "How do you build a lazy pipeline with `itertools` so intermediate collections are never materialized?"
track: python
section: comprehensions-and-functional
level: middle
type: practical
tags: [itertools]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L19-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Compose `itertools` functions into a chain where each takes an iterator and returns an iterator, passing the data through element by element with no intermediate lists.**[^py314-howto-functional] For example, `itertools.islice(itertools.chain(iter1, iter2), n)`, or a composition of `filter` -> `map` -> `itertools.takewhile`. <span class="warn">Final consumption (a `for` loop, or `list()`) is what starts the computation; until that moment not a single element is computed.</span>

## Detailed explanation

A "lazy pipeline" is a chain of computations where every link takes an iterator and returns a new
iterator rather than a list: no element is computed until something starts iterating the final
result.[^py314-howto-functional]

Such a chain is built from generator expressions (`(x for x in ...)`) and from functions that
themselves return an iterator: `map`, `filter`, `itertools.chain`, `itertools.islice`,
`itertools.takewhile`, `itertools.dropwhile`.[^py314-library-itertools] Each of those merely
remembers the source and the transformation rule, without invoking it right away.

The main trap is the list comprehension (`[x for x in ...]`), which materialises the whole result in
memory at once. The links of a lazy pipeline therefore have to be generator expressions or functions
returning an iterator, not a comprehension in square brackets.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

A pipeline that reads a file, filters its lines and takes the first ten, without loading the file
into memory in full:

```python
lines = (line.strip() for line in open('access.log'))
errors = (line for line in lines if 'ERROR' in line)
first_ten = itertools.islice(errors, 10)

for msg in first_ten:  # nothing is read from disk until this loop runs
    print(msg)
```

The computation starts only at the final consumer - the `for` loop, a `list()` call or `next()`.
Until that moment `lines`, `errors` and `first_ten` are just iterator objects that have computed
nothing.

**The usual building blocks of a lazy pipeline:**
- `filter(predicate, it)` and `map(func, it)` - the basic single-pass transformations;
- `itertools.chain(*its)` - concatenating several iterables without copying;
- `itertools.islice(it, n)` - limiting the number of elements without exhausting the whole iterator;
- `itertools.takewhile(predicate, it)` and `itertools.dropwhile(predicate, it)` - cutting on a
  condition.

The advantage of the approach is constant memory: the pipeline handles one element at a time, so the
size of the input is not bounded by the amount of RAM, unlike a chain of list comprehensions where
every link builds its own complete list.[^py314-howto-functional]

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
