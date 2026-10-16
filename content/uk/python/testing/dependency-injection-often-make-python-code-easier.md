---
id: py-testing-0005
title: "Чому dependency injection часто робить Python code простішим для deterministic testing?"
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
  - source_id: py314-library-unittest-mock-patch
    title: "Python 3.14: Library/unittest.mock (patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch
  - source_id: py314-tutorial-defining-functions
    title: "Python 3.14: Tutorial/Defining Functions"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock (where to patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
---

## Short answer

**Dependency injection (DI) передає залежності аргументами, тому тест підставляє fake або mock просто як аргумент.** Функція, що приймає `http_client` і `clock`, у тесті отримує `StubClient` і `FrozenClock`: жодної мережі, жодного реального часу. Коли залежність імпортовано всередині функції, її підміна вимагає `patch`, який тимчасово замінює об’єкт, на який вказує ім’я.[^py314-library-unittest-mock-patch] DI – це шаблон проєктування, а не правило Python, тож користь залежить від того, що всі входи, від яких залежить результат, передаються ззовні.

## Detailed explanation

Dependency injection (DI) – це домовленість про дизайн, а не можливість мови. Код отримує залежності (HTTP-клієнт, годинник, сховище) як параметри функції або конструктора, а не створює їх чи імпортує всередині. Python цього не вимагає, але механізм виклику працює саме так: під час виклику аргументи прив’язуються до локальних імен параметрів, тож тіло функції використовує той об’єкт, який передав виклик.[^py314-tutorial-defining-functions]

Прихована залежність – це `import` або виклик `datetime.now()` усередині функції. Щоб підмінити її, доводиться патчити атрибут модуля. `patch` працює тимчасовою заміною об’єкта, на який вказує ім’я, тож патч має стояти там, де код це ім’я шукає.[^py314-library-unittest-mock-where-to-patch] Патч у сусідньому модулі нічого не змінює, і тест може мовчки виконувати реальну залежність.

Приклад: `make_report` не читає ні мережі, ні годинника, тож тест передає fake і фіксований час аргументами, без жодного патча:

```python
import datetime as dt


def make_report(fetch_rate, now):
    rate = fetch_rate("USD")  # collaborator passed in, not imported
    return f"{now:%Y-%m-%d}: USD={rate:.2f}"


def test_make_report_is_deterministic():
    fixed_now = dt.datetime(2026, 1, 1)
    report = make_report(lambda currency: 41.5, fixed_now)  # fake, no network
    assert report == "2026-01-01: USD=41.50"
```

Результат детермінований, бо всі входи задані в самому тесті. Та сама логіка з прихованими залежностями вимагала б двох патчів у модулі, де лежить `make_report`.

DI не робить код детермінованим сам по собі. Якщо всередині функції лишилися `random.random()`, `datetime.now()` або глобальний кеш, цей вхід усе ще прихований. Fake має відповідати контракту реального об’єкта: тест із неправильним методом проходить, але нічого не доводить. Для однієї функції з одним викликом DI може бути зайвим ускладненням.

**Типові помилки:**
- вважати, що DI робить код детермінованим, коли всередині лишилися `datetime.now()` або `random`;
- передавати fake з методами чи сигнатурою, яких немає в реального об’єкта, і тест проходить із неправильним інтерфейсом;
- переводити на DI кожну функцію, навіть коли один `patch` простіший.
