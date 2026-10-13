---
id: py-testing-0010
title: "Для repository, який має поводитися як real in-memory storage, коли обрати Fake, а коли Stub чи interaction-verifying Mock?"
description: "Fake – спрощена, але робоча реалізація контракту (in-memory dict замість БД); Stub – пасивний об’єкт із фіксованими відповідями; Mock – записує виклики для interaction verification."
track: python
section: testing
level: middle
type: comparison
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
  - source_id: py314-library-unittest-mock-quick-guide
    title: "Python 3.14: Library/unittest.mock, Quick Guide"
    url: https://docs.python.org/3.14/library/unittest.mock.html#quick-guide
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: Mock і MagicMock зберігають відомості про те, як їх використали."
  - source_id: py314-library-unittest-mock-assert-called-with
    title: "Python 3.14: Library/unittest.mock, Mock.assert_called_with"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: assert_called_with перевіряє, що останній виклик mock відбувся з вказаними аргументами."
---

## Short answer

**Fake – робоча, але спрощена реалізація контракту (in-memory dict замість БД); Stub – пасивний об’єкт із фіксованими відповідями.** Mock записує виклики для interaction verification.[^py314-library-unittest-mock-quick-guide] Для repository, що має поводитися як real storage, потрібен Fake: він реалізує повний контракт, а Stub повертає одну фіксовану відповідь на будь-який запит. Interaction-verifying Mock (`mock.assert_called_with(...)`) доречний, коли важливий протокол викликів, а не стан.[^py314-library-unittest-mock-assert-called-with] <span class="warn">Fake має проходити ті самі interface-тести, що й реальна імплементація, інакше розбіжність лишиться непоміченою.</span>

## Detailed explanation

Test double мають різну мету, і вибір залежить від того, що тест перевіряє. Fake має робочу, але спрощену реалізацію контракту: для repository це in-memory dict, у якому `save` справді зберігає, `get` повертає збережене, а `delete` прибирає. Тест з Fake перевіряє стан після операцій, тож спрощення має бути правильним для всього контракту, а не для одного сценарію.

Stub не має стану: він повертає заготовлені відповіді незалежно від аргументів. Mock налаштовується так само (через `return_value`), але ще й записує, як його використали: `unittest.mock.Mock` зберігає відомості про виклики.[^py314-library-unittest-mock-quick-guide] Тест може перевірити їх через `assert_called_with`.[^py314-library-unittest-mock-assert-called-with] Тому Stub і Mock у коді можуть виглядати однаково; різниця в тому, що тест перевіряє.

Для repository, що має поводитися як real storage, вибір – Fake: тест перевіряє результат (наприклад, `find` після `save`) і не ламається, коли внутрішню реалізацію змінили. Stub тут небезпечний, бо мовчки повертає одну й ту саму відповідь на будь-який запит. Interaction-verifying Mock доречний, коли важливий протокол, наприклад, що повідомлення надіслано рівно один раз, а не стан сховища.

Приклад: Fake зберігає й повертає реальні дані, а Stub віддає одну відповідь на будь-який запит.

```python
from unittest import mock

class InMemoryUserRepo:  # Fake: a working, simplified implementation
    def __init__(self):
        self._users = {}

    def save(self, user):
        self._users[user["id"]] = user

    def get(self, user_id):
        return self._users.get(user_id)

    def delete(self, user_id):
        self._users.pop(user_id, None)

    def find(self, name):
        return [u for u in self._users.values() if u["name"] == name]

user = {"id": 1, "name": "alice"}

fake = InMemoryUserRepo()
fake.save(user)
print(fake.find("alice"))  # [{'id': 1, 'name': 'alice'}]
print(fake.find("bob"))    # []

stub = mock.Mock()         # Stub: one fixed answer, whatever the query
stub.find.return_value = [user]
print(stub.find("bob"))    # [{'id': 1, 'name': 'alice'}]: the query is ignored
```

Щоб Fake не розходився з реальним сховищем, одні й ті самі тести контракту запускають і на Fake, і на реальній реалізації, наприклад на SQLite. Тоді розбіжність поведінки видно в тестах, а не в продакшені.

**Типові помилки:**
- Fake, що реалізує лише частину контракту (наприклад, `find` без фільтра), і тести проходять на хибній поведінці;
- Stub там, де тест читає збережене: він нічого не запам’ятовує, тож розбіжність лишається непоміченою;
- перевірка `save` через `assert_called_with` там, де важливий результат збереження: такий тест ламається від рефакторингу без зміни поведінки.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
