---
id: py-testing-0006
title: "Як відтворити timeout та retry behavior без flaky dependence від реального external service?"
description: "Mock HTTP-клієнта з side_effect імітує послідовність помилок і успіх, а тест перевіряє кількість викликів і результат без реальної мережі та sleep."
track: python
section: testing
level: senior
type: practical
tags: []
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
  - source_id: py314-library-unittest-mock-side-effect
    title: "Python 3.14: Library/unittest.mock (Mock.side_effect)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ Mock.side_effect: iterable має віддавати значення на кожен виклик; елемент-виняток кидається замість повернення значення."
---

## Short answer

**Mock HTTP-клієнта з `side_effect` відтворює послідовність помилок і успіх, а тест перевіряє кількість викликів і результат без реальної мережі.**[^py314-library-unittest-mock-side-effect]

```python
call = Mock(side_effect=[TimeoutError(), TimeoutError(), "ok"])
assert fetch_with_retry(call, sleep=lambda seconds: None) == "ok"
assert call.call_count == 3
```

DI підставляє mock замість реального клієнта, а injectable `sleep` прибирає реальне очікування. <span class="warn">Реальні sleep у retry-логіці варто підмінювати на injectable delay-функцію, інакше тест стане повільним.</span>

## Detailed explanation

Реальний timeout важко відтворити на справжньому сервісі: він залежить від навантаження й мережі, тож тест стає повільним або flaky. Натомість відтворюють саму послідовність результатів. `Mock` з `side_effect` як iterable на кожен виклик повертає наступний елемент, а елемент-виняток кидає замість повернення.[^py314-library-unittest-mock-side-effect]

Retry-логіка отримує клієнт параметром (той самий прийом, що й у DI), тому mock підставляється без патчів. Затримку також передають параметром: з `time.sleep` тест чекав би 1 + 2 секунди, а з `delays.append` записує затримки й перевіряє backoff миттєво. Повний приклад, який проходить без мережі й без очікування:

```python
import time
from unittest.mock import Mock


def fetch_with_retry(call, max_attempts=3, sleep=time.sleep):
    for attempt in range(1, max_attempts + 1):
        try:
            return call()
        except TimeoutError:
            if attempt == max_attempts:
                raise
            sleep(2 ** (attempt - 1))  # backoff: 1 s, then 2 s


def test_retries_twice_then_succeeds():
    call = Mock(side_effect=[TimeoutError(), TimeoutError(), "ok"])
    delays = []  # the injected sleep records the delays instead of waiting

    assert fetch_with_retry(call, sleep=delays.append) == "ok"
    assert call.call_count == 3
    assert delays == [1, 2]
```

Тест перевіряє три речі: кількість викликів, результат і затримки між спробами. Шлях після вичерпання спроб окремий: якщо клієнт завжди кидає `TimeoutError`, `fetch_with_retry` після останньої спроби повторно кидає той самий виняток. Це варто перевірити окремим тестом з `Mock(side_effect=TimeoutError())`.

Iterable у `side_effect` має віддавати значення на кожен виклик.[^py314-library-unittest-mock-side-effect] Після останнього елемента mock кидає `StopIteration` (перевірено на CPython 3.13 і 3.14). Mock відтворює лише ті винятки, які ви йому задали, тож типи винятків беріть із документації реального клієнта, а не з уяви.

**Типові помилки:**
- тестувати retry з реальним `time.sleep`, через що тест чекає секунди;
- перевіряти лише кількість викликів, без результату й без поведінки після вичерпання спроб;
- задавати список `side_effect` коротшим за кількість викликів, через що тест падає на `StopIteration`.

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
