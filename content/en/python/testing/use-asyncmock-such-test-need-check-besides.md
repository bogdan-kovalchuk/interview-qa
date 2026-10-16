---
id: py-testing-0014
title: "When should you use `AsyncMock`, and what does such a test need to check besides the call arguments?"
track: python
section: testing
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
---

## Short answer

**`AsyncMock` is needed to replace async functions because its call returns an awaitable that works with `await`; besides the arguments, the test must check that the mock was actually awaited.**[^py314-library-unittest-mock] `AsyncMock` provides `assert_awaited()`, `assert_awaited_with()`, `await_count` and `await_args_list`.[^py314-library-unittest-mock] A plain `assert_called_with` does not guarantee that the result was awaited: the call is recorded immediately, while the coroutine may have been created but never run.

## Detailed explanation

`AsyncMock` is a stand-in for an async function: calling it returns an awaitable (a coroutine) rather than the result itself. That is why tests of async code use it in place of an `async def` dependency, such as an HTTP client, a queue or a repository. The test defines what the dependency "returns" and checks how the code interacts with it.[^py314-library-unittest-mock]

A test like this has two separate records, and they are easy to confuse. The call to the mock is recorded when it happens, so `assert_called_with(...)` passes even when nobody awaited the coroutine. The fact of awaiting is recorded only when the coroutine runs; it is checked with `assert_awaited*`, `await_count` and `await_args_list`. The documentation separates these two events explicitly: calling the object and awaiting it are different, and the `await` keyword is required.[^py314-library-unittest-mock]

The code below has a missing `await`. The test with `assert_called_with` passes although `send` never ran:

```python
import asyncio
from unittest.mock import AsyncMock


async def notify_buggy(client):
    client.send("hello")            # BUG: creates a coroutine and never awaits it


async def notify_fixed(client):
    await client.send("hello")


def test_buggy_passes_anyway() -> None:
    client = AsyncMock()
    asyncio.run(notify_buggy(client))
    client.send.assert_called_with("hello")    # passes: the call itself was recorded


def test_fixed_checks_await() -> None:
    client = AsyncMock()
    asyncio.run(notify_fixed(client))
    client.send.assert_awaited_once_with("hello")
```

On CPython this code emits a `RuntimeWarning` about a coroutine that was never awaited, but the test does not fail on it. The fixed version checks the await itself: `assert_awaited_once_with` requires that the mock was awaited exactly once and with these arguments.[^py314-library-unittest-mock]

Beyond the arguments, such a test usually checks three things: that the await happened, how many times it happened (`await_count` or `assert_awaited_once_with`), and that the awaitable's result is used further on. The mock cannot show the last one by itself: if the code discards the result of `await`, the test must check behaviour that depends on it.

**Common mistakes:**
- checking only `assert_called_with`, which passes even without `await`;
- substituting `MagicMock` for `AsyncMock`: awaiting a `MagicMock` raises a `TypeError` (the message text differs between Python versions);
- stopping at `assert_awaited()` without arguments and call counts when exact values matter.
