---
id: py-testing-0014
title: "Коли використати `AsyncMock` і що в такому тесті треба перевіряти окрім call arguments?"
description: "AsyncMock потрібен для підміни async-функцій, бо повертає awaitable і коректно працює з await; окрім аргументів треба перевіряти, що mock було саме await-нуто."
track: python
section: testing
level: middle
type: practical
tags: [asyncmock]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
---

## Short answer

**`AsyncMock` потрібен для підміни async-функцій, бо його виклик повертає awaitable, який коректно працює з `await`; окрім аргументів треба перевіряти, що mock було саме await-нуто.**[^py314-library-unittest-mock] `AsyncMock` надає `assert_awaited()`, `assert_awaited_with()`, `await_count` та `await_args_list`.[^py314-library-unittest-mock] Звичайний `assert_called_with` не гарантує, що результат було awaited: виклик записується одразу, а coroutine могло бути створено, але не виконано.

## Detailed explanation

`AsyncMock` – це підміна для async-функції: його виклик повертає awaitable (coroutine), а не результат одразу. Тому в тестах async-коду його ставлять замість залежності з `async def`, наприклад HTTP-клієнта, черги чи репозиторію. Тест задає, що «повертає» залежність, і перевіряє, як код із нею взаємодіє.[^py314-library-unittest-mock]

У такому тесті є два окремі записи, і їх легко сплутати. Виклик mock-а фіксується в момент виклику, тому `assert_called_with(...)` проходить навіть тоді, коли coroutine ніхто не await-ив. Факт await-у фіксується лише під час виконання coroutine; його перевіряють `assert_awaited*`, `await_count` і `await_args_list`. Документація прямо відокремлює ці події: виклик об’єкта і його await – різні речі, і для await потрібне ключове слово `await`.[^py314-library-unittest-mock]

Нижче код із пропущеним `await`. Тест із `assert_called_with` проходить, хоча `send` ніколи не виконався:

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

У CPython такий код видає `RuntimeWarning` про coroutine, яку не було await-нуто, але тест його не валить. Виправлена версія перевіряє саме await: `assert_awaited_once_with` вимагає, щоб mock було await-нуто рівно один раз і з цими аргументами.[^py314-library-unittest-mock]

Окрім аргументів, зазвичай перевіряють три речі: що await відбувся, скільки разів він відбувся (`await_count` або `assert_awaited_once_with`) і що результат awaitable далі використано. Останню річ mock сам не покаже: якщо код відкидає результат `await`, тест має перевіряти поведінку, яка від нього залежить.

**Типові помилки:**
- перевіряти лише `assert_called_with`, бо він проходить і без `await`;
- підставити `MagicMock` замість `AsyncMock`: `await` на результаті `MagicMock` кидає `TypeError` (текст повідомлення залежить від версії Python);
- обмежитися `assert_awaited()` без аргументів і кількості викликів, коли потрібні точні значення.

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
