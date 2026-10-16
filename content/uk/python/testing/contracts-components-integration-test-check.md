---
id: py-testing-0002
title: "Які контракти між компонентами перевіряє integration test?"
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
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
---

## Short answer

**Integration test перевіряє стик між компонентами: чи код, що викликає інший компонент, правильно з ним працює за його контрактом.**[^martinfowler-integration-test] Наприклад, SQL-запит має відповідати реальній схемі БД, а HTTP-відповідь має коректно перетворюватися на очікуваний тип даних. Заглушку для такого тесту треба окремо перевіряти на відповідність реальному компоненту: для цього існують contract tests.[^martinfowler-integration-test]

## Detailed explanation

Integration test відповідає на інше питання, ніж unit-тест: чи правильно окремо розроблені одиниці працюють, коли їх з’єднано.[^martinfowler-integration-test] Об’єкт перевірки – місце, де код перетинає межу між компонентами: виклик іншого модуля, запит до БД, HTTP-клієнт або черга повідомлень. Контракт на цій межі – це домовленість про те, що через неї проходить: схема таблиць, поля й типи відповіді, формат повідомлення, коди помилок, порядок викликів.

Фаулер розрізняє вузькі і широкі integration tests. Вузький перевіряє лише той код свого сервісу, що говорить із зовнішнім компонентом, і використовує test doubles цього компонента; широкий використовує живі версії всіх сервісів і проходить через них. Фаулер радить розглянути вузький варіант, якщо є лише широкі тести: він, імовірно, суттєво покращить швидкість, зручність і стійкість тестування.[^martinfowler-integration-test]

Приклад показує, чому заглушка небезпечна без перевірки. Перший тест використовує `Mock`, який приймає будь-який виклик і створює атрибути під час доступу, тож реальна схема його не обмежує.[^py314-library-unittest-mock] Другий працює з реальним движком SQLite і схемою, і помилка в запиті стає видимою.

```python
import sqlite3
from unittest import mock


def find_email(conn, user_id):
    row = conn.execute("SELECT email FROM users WHERE id = ?", (user_id,)).fetchone()
    return row[0] if row else None


# Unit test with a double: passes, although the real schema has no 'email' column.
fake = mock.Mock()
fake.execute.return_value.fetchone.return_value = ("a@example.com",)
print(find_email(fake, 1))  # a@example.com

# Integration test with the real engine and schema: the query is wrong.
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, mail TEXT)")  # the column is 'mail'
try:
    find_email(conn, 1)
except sqlite3.OperationalError as error:
    print(error)  # no such column: email
```

Щоб заглушка не розійшлася з реальністю, її перевіряють окремо: Фаулер для цього пропонує contract tests.[^martinfowler-integration-test] Він описує поєднання вузьких integration tests із заглушками та contract tests як спосіб інтегруватися із зовнішнім сервісом, не запускаючи тести проти його живого екземпляра. Широкі тести з усіма живими сервісами тоді лишаються як тонкий фінальний smoke test з малою кількістю сценаріїв.[^martinfowler-integration-test]

**Типові помилки:**
- тестувати SQL- або HTTP-код лише з `Mock`: тест пройде з будь-якою схемою чи відповіддю;
- вважати, що integration test обов’язково піднімає всі сервіси: вузький варіант із заглушками теж integration test;
- довіряти заглушці, яку ніхто не перевіряв проти реального компонента.
