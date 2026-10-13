---
id: py-testing-0001
title: "Яку boundary має unit test і чому він не повинен непомітно перетворюватися на integration test?"
description: "Unit test перевіряє один модуль (функцію, метод, клас): solitary-варіант замінює його колабораторів test doubles, а з реальними зовнішніми сервісами тест стає integration test."
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
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Есей Мартіна Фаулера (не офіційна документація): визначення integration test, вузькі й широкі варіанти, solitary і sociable unit tests, contract tests."
  - source_id: martinfowler-test-pyramid
    title: "Martin Fowler: Test Pyramid"
    url: https://martinfowler.com/bliki/TestPyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Есей Мартіна Фаулера (не офіційна документація): піраміда тестів, широкі тести як повільні, дорогі й крихкі, обмеження цього припущення."
---

## Short answer

**Solitary unit test замінює колабораторів test doubles і перевіряє лише одиницю під тестом.**[^martinfowler-integration-test] Sociable unit test з реальними колабораторами в тому самому процесі за Фаулером також є unit-тестом.[^martinfowler-integration-test] <span class="warn">Коли тест використовує реальні зовнішні сервіси, наприклад БД чи мережу, він стає integration test; непомітна заміна doubles на такі сервіси змінює сенс тесту.</span>[^martinfowler-integration-test]

## Detailed explanation

Межа unit test – це одиниця коду, яку він перевіряє: функція, метод або клас. Фаулер називає solitary unit test тест, у якому всі інші елементи програми замінено test doubles, і sociable unit test, у якому реальні колаборатори працюють разом. Обидва він називає unit-тестами й розрізняє їх за прикметником: solitary або sociable.[^martinfowler-integration-test] Для заміни колабораторів використовують `unittest.mock`: він замінює частини системи під тестом об’єктами-заглушками й дає перевірити, як їх викликали.[^py314-library-unittest-mock]

Тест стає integration test, коли в ньому беруть участь реальні зовнішні сервіси: база даних, мережа або файли іншої системи. Фаулер розрізняє вузькі integration tests, які використовують test doubles таких сервісів, і широкі, які потребують їх живих версій і відповідного середовища.[^martinfowler-integration-test] Термін при цьому розмився: деякі автори називають integration test і sociable unit test, тож за назвою тест не визначити. Перехід непомітний, коли реальний сервіс підставляють замість doubles: тест лишається зеленим, поки сервіс працює, і червоніє з причин, які не стосуються логіки одиниці.

Нижче функція читає годинник напряму. Без заміни тест перевіряє не функцію, а поточний час, тому очікуване значення неможливо задати. Коли `time.time` замінено test double-ом, тест перевіряє лише функцію і завжди дає той самий результат.

```python
import time
import unittest
from unittest import mock


def seconds_left(deadline: float) -> float:
    # Depends on the real clock, so the result changes on every run.
    return deadline - time.time()


class SecondsLeftUnitTest(unittest.TestCase):
    def test_returns_remaining_time(self):
        # The clock is a test double, so the unit under test is the only real code.
        with mock.patch("time.time", return_value=100.0):
            self.assertEqual(seconds_left(160.0), 60.0)


if __name__ == "__main__":
    unittest.main()
```

Практичний висновок: межу варто записувати явно – solitary чи sociable, і які саме колаборатори замінено. Заміна doubles має стояти там, де тест виходить у зовнішній світ (мережа, БД, файли), а взаємодію з реальним сервісом перевіряє окремий integration-тест з явною назвою. Так unit-тест зазвичай лишається швидшим за широкий тест.[^martinfowler-test-pyramid]

**Типові помилки:**
- назвати тест unit-тестом, хоча він піднімає реальну БД або HTTP-сервер, лише тому, що він лежить у теці unit;
- замінити частину залежностей, але не мережу чи файли, і тест тихо стає integration-тестом;
- перевіряти лише виклики mock-ів, а не поведінку модуля: тест проходить, хоча модуль із реальною залежністю зламаний.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
