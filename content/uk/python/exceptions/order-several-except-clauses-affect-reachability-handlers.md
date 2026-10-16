---
id: py-excpt-0002
title: "Як порядок кількох `except` clauses впливає на досяжність handlers для subclass exceptions?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
---

## Short answer

**Python перевіряє `except` clauses зверху вниз і спрацьовує перший збіг; якщо parent class стоїть перед child, handler для child стає недосяжним.**[^py314-reference-compound-stmts-the-try-statement] Clause `except` ловить і підкласи свого класу, тому `except Exception` перед `except ValueError` перехоплює `ValueError` першим, і другий clause не виконується.[^py314-library-exceptions] У CPython 3.13 і 3.14 такий порядок не дає ні warning-у, ні error-у. Правильний порядок: від найвужчих (subclass) до найширших (parent).

## Detailed explanation

Коли в `try` виникає виняток, interpreter перевіряє `except` clauses у тому порядку, в якому вони записані, і виконує перший clause, що підходить. Перевірка на цьому зупиняється, тож в одному `try` виконується не більше одного handler-а.[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors]

Clause з класом `C` підходить до винятку, якщо клас винятку є `C` або його підкласом; навпаки це не працює. Тож `except ValueError` ловить і `UnicodeDecodeError` (він наслідує `UnicodeError`, а той – `ValueError`), але `except UnicodeDecodeError` не ловить звичайний `ValueError`.[^py314-library-exceptions] Саме тому порядок має значення: широкий clause, поставлений раніше, поглинає винятки, які мали б піти до вужчого clause нижче.

Пастка виглядає так:

```python
def parse(text):
    try:
        return int(text)
    except Exception:          # matches every Exception, including ValueError
        return "generic failure"
    except ValueError:         # never reached for int("x")
        return "bad number"

print(parse("x"))  # generic failure, not 'bad number'
```

Якщо поміняти clauses місцями, `int("x")` дасть `bad number`, а виняток, що не є `ValueError` (наприклад, `TypeError` від `int(None)`), піде в загальний `generic failure`. Interpreter такого порядку не перевіряє: у CPython 3.13 і 3.14 код компілюється без жодного попередження, тому помилку видно лише в тесті, який подає вхід, що викликає саме цей handler.

Порядок важливий тоді, коли один виняток може підійти до обох clauses. Це буває у двох випадках: класи пов’язані відношенням підкласу або виняток належить класу, який наслідує обидва. Наприклад, `class E(ValueError, KeyError)` підходить і до `except ValueError`, і до `except KeyError`, тож спрацьовує той clause, що стоїть першим. Пари вбудованих винятків на кшталт `OSError` і `ValueError` не перекриваються: жоден вбудований клас не наслідує обидва, тому їх перестановка нічого не змінює. Правило просте: спочатку найвужчі класи, далі батьківські, а `except Exception` – останнім.

**Типові помилки:**
- ставити `except Exception` перед конкретними винятками, які мають оброблятися окремо;
- очікувати, що interpreter попередить про недосяжний handler (у CPython 3.13 і 3.14 він цього не робить);
- вважати, що порядок ніколи не важливий для непов’язаних класів: він важливий, якщо один клас винятку наслідує обидва.
