---
id: py-decor-0009
title: "How does the order of stacking decorators affect authorization, caching, and logging, if any wrapper may choose not to call the next one?"
description: "How does the order of stacking decorators affect authorization, caching, and logging, if any wrapper may choose not to call the next one?"
track: python
section: decorators
level: middle
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L3-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Order determines which wrapper runs first (outermost = topmost decorator), and if it does not
call the next one, the inner decorators are skipped.**[^py314-glossary-term-decorator] For
authorization + caching + logging: authorization should be outermost, so it rejects a request
before caching or logging run. If logging sits outside authorization, even rejected requests get
logged. If caching sits outside authorization, a cached result can bypass the permission check.
<span class="warn">Any wrapper that does not call `func(*args, **kwargs)` effectively blocks the
entire chain below it.</span>

## Detailed explanation

Stacking decorators on one function builds a chain of wrapper calls: each wrapper decides whether
to call the next one in the chain at all, and that is exactly why the order decorators are written
in directly affects system behaviour, not just code aesthetics.[^py314-glossary-term-decorator]

The outermost decorator (the one written first above `def`) gets control first on a call and can
finish handling the request without ever calling the inner wrappers. If such a wrapper does not
call `func(*args, **kwargs)`, the entire chain below it – including authorization, caching, or
logging that were supposed to run later – simply does not execute.

For authorization + caching + logging, order sets concrete guarantees. Authorization on the outside
means no request reaches caching or logging without a permission check. If caching sits outside
authorization, a cached result computed for one user can be returned to another user whose
permissions for that call were never checked – that is a data leak, not just wasted work. If
logging sits outside authorization, rejected attempts are logged too, which is usually desirable
for an audit trail; but if logging sits inside authorization, rejected requests are never logged at
all, and the trace of an attack disappears.

An example of a stack where the written order matches the intended semantics:

```python
def require_auth(func):
    def wrapper(request):
        if not request.user.is_authenticated:
            raise PermissionError('not authorized')
        return func(request)
    return wrapper

def cached(func):
    def wrapper(request):
        if request.path in _cache:
            return _cache[request.path]
        result = func(request)
        _cache[request.path] = result
        return result
    return wrapper

@require_auth
@cached
@logged
def handler(request):
    ...
```

**Practical order and why:**
- `authorization` – outermost, because nothing below it should run without it;
- `caching` – right under authorization, so the cache can never bypass the permission check;
- `logging` – closest to the function if only successful calls should be logged; outermost if
  rejected attempts need an audit trail too;
- any change to this order is a deliberate decision about which requests each layer sees, not
  cosmetics.

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
