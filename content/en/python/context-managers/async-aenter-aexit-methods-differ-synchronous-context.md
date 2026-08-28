---
id: py-ctxmgr-0008
title: "How do `async with` and the `__aenter__`/`__aexit__` methods differ from the synchronous context-manager protocol?"
description: "How do `async with` and the `__aenter__`/`__aexit__` methods differ from the synchronous context-manager protocol?"
track: python
section: context-managers
level: middle
type: comparison
tags: [async-with, aenter, aexit]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L3-L98
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`__aenter__` and `__aexit__` are coroutine methods: they return an awaitable the event loop has to await, whereas the synchronous `__enter__`/`__exit__` are called as ordinary functions.**[^py314-reference-datamodel-with-statement-context-managers] `async with` can only be used inside an `async def`. The suppression semantics are the same: a truthy return from `__aexit__` suppresses the exception. The async variant is needed when enter and exit perform I/O (network connections, database pools, async locks).

## Detailed explanation

`__aenter__` and `__aexit__` are the asynchronous counterparts of `__enter__` and `__exit__`: they
are declared `async def`, so calling one returns a coroutine that `async with` awaits, instead of
handing back a value directly.[^py314-reference-datamodel-with-statement-context-managers]

Because of that, `async with` can only be written inside an `async def` - outside a coroutine
function it does not exist syntactically. The statement itself works exactly like `with`:
`async with expr as x:` calls `__aenter__()`, awaits the result and binds it to `x`, and on the way
out awaits `__aexit__(exc_type, exc_val, exc_tb)`.

The exception suppression semantics are the same as in the synchronous protocol: a truthy return
from `__aexit__` suppresses the exception, and a falsy one (`None` included) lets it
propagate.[^py314-reference-datamodel-with-statement-context-managers] The only difference is that
the `__aexit__` call itself, and any await inside it, may suspend the coroutine while the event loop
handles other tasks.

An asynchronous context manager that opens a connection in `__aenter__` and closes it in
`__aexit__`:

```python
class AsyncConn:
    async def __aenter__(self):
        self.conn = await connect()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        return False

async def main():
    async with AsyncConn() as conn:
        ...
```

A class that has only `__aenter__`/`__aexit__` does not work with a plain `with` - Python looks for
`__enter__`/`__exit__` specifically and does not substitute the asynchronous variants. The
asynchronous counterpart of the generator-based synchronous `@contextmanager` is
`contextlib.asynccontextmanager`, which likewise turns an `async def` generator with a single
`yield` into an async context manager.[^py314-library-contextlib]

**When the async variant is the one you need:**
- enter and exit perform network I/O (HTTP, queues, databases) and must not block the event loop;
- async-safe synchronization is required (`asyncio.Lock` as a context manager, for instance);
- the resource itself offers only an async API for opening and closing the connection.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
