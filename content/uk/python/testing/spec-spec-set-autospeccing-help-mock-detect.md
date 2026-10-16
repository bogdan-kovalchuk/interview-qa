---
id: py-testing-0012
title: "Як `spec`, `spec_set` та autospeccing допомагають mock виявляти drift від real interface?"
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
  - source_id: py314-library-unittest-mock-mock-class
    title: "Python 3.14: Library/unittest.mock, Mock class"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock
  - source_id: py314-library-unittest-mock-autospeccing
    title: "Python 3.14: Library/unittest.mock, Autospeccing"
    url: https://docs.python.org/3.14/library/unittest.mock.html#autospeccing
---

## Short answer

**`spec` дає доступ лише до атрибутів реального об’єкта, `spec_set` забороняє також записувати неіснуючі атрибути.**[^py314-library-unittest-mock-mock-class] Autospeccing рекурсивно копіює інтерфейс і сигнатури.[^py314-library-unittest-mock-autospeccing] Читання неіснуючого атрибута в mock зі `spec` або `spec_set` підніме `AttributeError`. `TypeError` на неправильні аргументи дає лише autospeccing (`create_autospec` або `patch(..., autospec=True)`), тож дрейф інтерфейсу видно в тесті.[^py314-library-unittest-mock-autospeccing]

## Detailed explanation

Звичайний `Mock()` приймає будь-який атрибут і будь-які аргументи: він створює атрибут при першому зверненні. Тому тест, який звертається до старого імені методу на mock, пройде, навіть коли реальний клас уже перейменовано. Документація описує саме цю проблему: тести з mock-об’єктами можуть проходити, поки код уже зламаний.[^py314-library-unittest-mock-autospeccing]

Параметр `spec` задає, які імена існують. Mock береться зі списку `dir()` об’єкта (класу, екземпляра або функції), і читання атрибута поза цим списком дає `AttributeError`. Запис при цьому не обмежений: `spec` дозволяє присвоїти будь-який атрибут, а `spec_set` забороняє й запис.[^py314-library-unittest-mock-mock-class]

Приклад: читання й запис на mock зі `spec`, `spec_set` і autospec.

```python
from unittest import mock

class Repo:
    def save(self, item):
        return item

spec_mock = mock.Mock(spec=Repo)
spec_mock.delete = 1            # allowed: spec restricts reads, not writes
try:
    spec_mock.remove            # Repo has no 'remove'
except AttributeError as e:
    print(e)                    # Mock object has no attribute 'remove'

spec_set_mock = mock.Mock(spec_set=Repo)
try:
    spec_set_mock.delete = 1    # spec_set also blocks writes
except AttributeError as e:
    print(e)                    # Mock object has no attribute 'delete'

autospec_mock = mock.create_autospec(Repo, instance=True)
try:
    autospec_mock.save()        # the copied signature requires 'item'
except TypeError as e:
    print(e)                    # missing a required argument: 'item'
```

`create_autospec` (і `patch(..., autospec=True)`) копіює інтерфейс рекурсивно: методи отримують сигнатуру оригіналу, тому неправильна кількість аргументів дає `TypeError`.[^py314-library-unittest-mock-autospeccing] Звичайний `spec` цього не робить: він не відхиляє виклик з неправильними аргументами, а сигнатуру використовує, щоб зіставляти виклики.[^py314-library-unittest-mock-mock-class] Перевірка сигнатури – окремий механізм, і його треба вмикати свідомо.

**Типові помилки:**
- `Mock()` без spec у тестах, де важлива відповідність реальному API: такий тест не помітить перейменування;
- `spec=Repo` для атрибута, який створюється в `__init__` (`self.conn = ...`): клас його не містить, тож читання дає `AttributeError`, хоча на екземплярі атрибут є (перевірено на 3.13 і 3.14); тоді беріть `spec` від екземпляра, якщо його створення безпечне;
- вважати, що звичайний `spec` перевіряє сигнатури викликів: `TypeError` дає лише autospeccing.
