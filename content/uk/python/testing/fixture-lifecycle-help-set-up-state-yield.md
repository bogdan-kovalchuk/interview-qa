---
id: py-testing-0007
title: "Як fixture lifecycle допомагає задати setup, yield resource і teardown після тесту?"
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
  - source_id: pytest-how-to-fixtures-yield
    title: "pytest documentation: How to use fixtures (yield fixtures)"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended
  - source_id: pytest-how-to-fixtures-errors
    title: "pytest documentation: Handling errors for yield fixture"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#handling-errors-for-yield-fixture
  - source_id: pytest-how-to-fixtures-scopes
    title: "pytest documentation: Fixture scopes"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes
---

## Short answer

**Фікстура виконує код до `yield` як setup, передає ресурс тесту через значення `yield`, а код після `yield` – teardown після завершення тесту.**[^pytest-how-to-fixtures-yield]

```python
@pytest.fixture
def db_conn():
    conn = create_connection()  # setup, runs before the test
    yield conn  # the test receives conn here
    conn.close()  # teardown, runs after the test
```

Scope визначає, як довго живе ресурс: `function` (за замовчуванням) створює його на кожен тест, а `module` або `session` ділять один ресурс, що зменшує overhead, але вимагає уваги до mutable state.[^pytest-how-to-fixtures-scopes]

## Detailed explanation

Фікстура – це функція, позначена `@pytest.fixture`. Тест запитує її, назвавши параметр її іменем, і pytest викликає її до тесту. Якщо фікстура використовує `yield`, код до `yield` є setup, а значення, яке віддає `yield`, отримує тест. Код після `yield` – це teardown: pytest виконує його, коли тест завершено, у зворотному порядку до setup.[^pytest-how-to-fixtures-yield]

Teardown належить тій самій фікстурі, тому він не виконується, якщо setup упав до `yield`. Фікстури, які вже успішно піднялися для цього тесту, pytest усе одно знищує.[^pytest-how-to-fixtures-errors] Тому `yield` варто ставити одразу після відкриття ресурсу: ризиковані кроки перед ним можуть залишити ресурс відкритим.

Приклад: фікстура веде журнал подій, а тест перевіряє, що setup відбувся до тесту:

```python
import pytest

LOG = []


@pytest.fixture
def db_conn():
    LOG.append("setup")  # runs before the test
    yield "connection"  # the test receives this value
    LOG.append("teardown")  # runs after the test


def test_query_uses_connection(db_conn):
    assert db_conn == "connection"
    assert LOG == ["setup"]
```

Тест проходить, бо setup уже записано. Коли тест падає, teardown усе одно виконується: перевірено на pytest 9.1.1 із фікстурою, яка друкує повідомлення в setup і teardown, і тестом з `assert False`; запуск із `pytest -s` показав `setup`, потім `F`, потім `teardown`.

Scope визначає, коли pytest знищує фікстуру: `function` – наприкінці кожного тесту (за замовчуванням), `module` – після останнього тесту в модулі, `session` – наприкінці сесії.[^pytest-how-to-fixtures-scopes] Ширший scope означає, що ресурс створюється рідше, але тести ділять його стан, і зміна, яку залишив один тест, дійде до наступних.

Teardown не є абсолютною гарантією: якщо процес жорстко зупинено, код після `yield` не виконається. Cleanup, записаний після `assert` у тілі тесту, теж не запуститься, коли `assert` падає, тому його переносять у фікстуру.

**Типові помилки:**
- писати cleanup в кінці тіла тесту замість teardown фікстури: при падінні тесту цей код не виконається;
- ставити `scope="session"` для ресурсу з mutable state, який тести змінюють;
- вважати, що teardown виконається, якщо setup упав до `yield`.
