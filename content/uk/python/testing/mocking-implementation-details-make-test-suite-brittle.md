---
id: py-testing-0013
title: "Як over-mocking implementation details робить test suite крихкою під час behavior-preserving refactoring?"
description: "Якщо тест перевіряє кількість і порядок викликів внутрішніх mock-об’єктів замість результату, рефакторинг, що змінює ці виклики, ламає тест."
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
  - source_id: py314-library-unittest-mock-assert-has-calls
    title: "Python 3.14: Library/unittest.mock, Mock.assert_has_calls"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: assert_has_calls перевіряє список mock_calls; порядок важливий, якщо any_order не увімкнено."
---

## Short answer

**Якщо тест перевіряє кількість і порядок викликів внутрішніх mock-об’єктів замість спостережуваного результату, такий тест ламається від behavior-preserving рефакторингу, що змінює ці виклики.**[^py314-library-unittest-mock-assert-has-calls] Наприклад, заміна циклу викликів `save` на один batch-виклик `save_many` зберігає результат, але `assert_has_calls` на mock `save` перестає проходити. Вихід – тестувати вхід і вихід публічного контракту, а mock використовувати для зовнішніх залежностей, де сам виклик є результатом, наприклад надісланого листа.

## Detailed explanation

Mock фіксує деталі реалізації, коли тест перевіряє не результат, а протокол: скільки разів і в якому порядку викликано залежність. `assert_has_calls` перевіряє список `mock_calls`: якщо `any_order` не увімкнено, потрібні виклики мають іти підряд, а зайві виклики до або після них допускаються.[^py314-library-unittest-mock-assert-has-calls] Тож зміна кількості чи порядку викликів ламає тест, навіть коли для користувача сервісу нічого не змінилося.

Сервіс раніше викликав `save` для кожного рядка; після рефакторингу він викликає `save_many`. Результат у сховищі той самий. Тест `BehaviourTest` перевіряє стан Fake і проходить для обох варіантів сервісу. `BrittleTest` перевіряє виклики `save` і після рефакторингу падає.

```python
import unittest
from unittest import mock

class UserServiceBatched:
    def __init__(self, repo):
        self.repo = repo

    def import_users(self, rows):
        self.repo.save_many(rows)  # refactored: one batch call, same stored rows
        return len(rows)

class InMemoryRepo:  # Fake
    def __init__(self):
        self.rows = []

    def save(self, row):
        self.rows.append(row)

    def save_many(self, rows):
        self.rows.extend(rows)

class BrittleTest(unittest.TestCase):
    def test_import_calls_save_per_row(self):
        repo = mock.Mock()
        UserServiceBatched(repo).import_users(["alice", "bob"])
        # Fails: the code now calls save_many, so save has no calls
        repo.save.assert_has_calls([mock.call("alice"), mock.call("bob")])

class BehaviourTest(unittest.TestCase):
    def test_import_stores_rows(self):
        repo = InMemoryRepo()
        UserServiceBatched(repo).import_users(["alice", "bob"])
        self.assertEqual(repo.rows, ["alice", "bob"])  # passes for both service versions

if __name__ == "__main__":
    unittest.main(verbosity=1)
```

Mock доречний, коли сам виклик є результатом: лист надіслано рівно один раз, платіж списано один раз. Для внутрішніх залежностей, які самі мають поведінку (сховище, кеш), краще взяти Fake і перевіряти стан: тоді рефакторинг, що зберігає поведінку, тест не ламає.

**Типові помилки:**
- перевіряти кожен внутрішній виклик, хоча тест мав би перевіряти результат;
- вважати, що більше mock робить тест ізольованішим: ізоляція потрібна від зовнішнього світу, а не від власного коду, який тест і так виконує;
- підганяти очікування тесту під нову послідовність викликів, після чого тест більше нічого не перевіряє.

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
