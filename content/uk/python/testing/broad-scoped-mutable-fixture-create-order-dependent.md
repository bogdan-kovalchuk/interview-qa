---
id: py-testing-0009
title: "Як broad-scoped mutable fixture може створити order-dependent tests і state leakage?"
description: "Fixture зі scope module або session віддає один спільний mutable об’єкт; зміни одного тесту бачить наступний, тож результат залежить від порядку запуску."
track: python
section: testing
level: senior
type: pitfall
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
  - source_id: pytest-how-to-fixtures-scopes
    title: "pytest documentation: How-to guides, Fixtures, Fixture scopes"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація pytest: значення scope у fixture і момент її знищення."
  - source_id: pytest-how-to-fixtures-yield
    title: "pytest documentation: How-to guides, Fixtures, yield fixtures"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація pytest: код після yield у fixture виконується як teardown."
---

## Short answer

**Fixture зі `scope="module"` або `scope="session"` створює один екземпляр на весь module чи session, тож mutable значення (dict, list, з’єднання з БД), змінене одним тестом, бачать наступні тести тієї самої області.**[^pytest-how-to-fixtures-scopes]

```python
import pytest

@pytest.fixture(scope="module")
def shared_cache():
    return {}  # one dict shared by every test in the module

def test_a(shared_cache):
    shared_cache["key"] = "value"

def test_b(shared_cache):
    assert "key" not in shared_cache  # AssertionError if test_a ran first
```

Такі тести стають order-dependent: окремо або в іншому порядку вони проходять інакше. Для mutable стану безпечніше використовувати `function` scope або скидати стан після кожного тесту.

## Detailed explanation

Fixture – це функція, результат якої pytest кешує на заданий scope. За замовчуванням scope це `function`: fixture створюється заново для кожного тесту. Значення `module` і `session` означають один екземпляр на весь модуль або всю сесію: pytest створює його, коли його вперше запитує тест, і знищує під час teardown після останнього тесту цієї області.[^pytest-how-to-fixtures-scopes] Саме спільність і є ефектом ширшого scope: усі тести в межах області отримують той самий об’єкт, а не копію.

Спільний об’єкт шкодить лише тоді, коли його можна змінити. Безпечно ділити число, рядок, `frozenset` і `tuple` з immutable елементами, а `dict`, `list`, `tuple` зі списком усередині чи з’єднання з БД – ні: тест, що додав ключ або рядок, передає наступним тестам уже змінений стан. Приклад: `test_b` проходить, якщо запустити його окремо, але падає, якщо перед ним виконався `test_a`.

```python
import pytest

@pytest.fixture(scope="module")
def shared_cache():
    return {}  # one dict shared by every test in the module

def test_a(shared_cache):
    shared_cache["key"] = "value"

def test_b(shared_cache):
    assert "key" not in shared_cache  # AssertionError if test_a ran first
```

Це і є order-dependent test: його результат визначається не його власним кодом, а тим, що раніше зробили з тим самим об’єктом інші тести. Такий баг з’являється лише тоді, коли тести запускають разом і в певному порядку, тому одиночний запуск `test_b` виглядає зеленим.

Виправлення залежить від того, що зберігається. Якщо fixture дешева, зробіть її `function`-scoped, щоб кожен тест отримував власний dict. Якщо створення дороге (БД, мережеве з’єднання), лишіть широкий scope для ресурсу, а стан відкочуйте після кожного тесту: наприклад, function-scoped fixture відкриває транзакцію і скасовує її в кінці тесту. Код після `yield` виконується в teardown, коли fixture знищується.[^pytest-how-to-fixtures-yield] Для `scope="module"` це один раз після останнього тесту модуля, тож між тестами модуля стан він не скидає; для `function`-scoped fixture знищення відбувається після кожного тесту.[^pytest-how-to-fixtures-scopes]

**Типові помилки:**
- вважати, що `scope="module"` ізолює тести: він ізолює модулі один від одного, але не тести всередині модуля;
- називати падіння «flaky» і перезапускати тест замість пошуку спільного mutable стану;
- розширювати `scope` «для швидкості», не перевіривши, чи тести пишуть у значення fixture.

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
