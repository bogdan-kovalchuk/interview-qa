---
id: py-excpt-0010
title: "Які властивості роблять custom exception hierarchy стабільною частиною library API?"
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

**Стабільна ієрархія зазвичай починається з одного базового класу бібліотеки, що походить від `Exception` (це конвенція, а не вимога мови).**[^py314-tutorial-errors] Проміжні класи для категорій, як `LookupError` для `KeyError` і `IndexError`, дають змогу перехоплювати цілу категорію.[^py314-library-exceptions] Конкретні підкласи зазвичай називають із суфіксом `Error`, як більшість стандартних винятків.[^py314-tutorial-errors]

## Detailed explanation

Мова не задає правил стабільності API бібліотеки, тож нижче йдеться про конвенції, які випливають з того, як працює `except`. Клауза `except X` спрацьовує, коли exception є екземпляром `X` або його підкласом.[^py314-reference-compound-stmts-the-try-statement] Отже, назва класу і його місце в ієрархії є частиною контракту: споживачі пишуть `except` на конкретний клас, і зміна його предків змінює, що саме вони перехоплюють.

Корінь від `Exception` задуманий саме для таких споживачів. Документація `Exception` рекомендує, щоб усі user-defined exceptions походили від нього.[^py314-library-exceptions] Тоді один `except LibraryError` ловить усе, що кидає бібліотека, і не треба перелічувати класи.

Проміжні класи дають різні рівні деталізації. У стандартній бібліотеці це видно на `LookupError`: він є базою для `IndexError` і `KeyError`, тож `except LookupError` ловить обидва.[^py314-library-exceptions] Новий підклас під наявною категорією не ламає код, який перехоплює категорію. Переставлення існуючого класу в іншу гілку, навпаки, тихо змінює, які `except`-блоки його ловлять. Тому стабільною частиною API є не лише імена, а й місце кожного класу в ієрархії.

Дані про помилку варто передавати атрибутами, а не лише текстом повідомлення. Споживач тоді читає `err.key`, а не розбирає рядок, який може змінитися в наступній версії. Приклад: `except QueryError` ловить конкретний `NotFoundError`, а ключ береться з атрибута:

```python
class LibraryError(Exception):
    """Base class: callers can catch everything the library raises."""

class QueryError(LibraryError):
    """Category: the request itself is wrong."""

class NotFoundError(QueryError):
    """Specific condition with its own name."""
    def __init__(self, key):
        super().__init__(f"no record for key {key!r}")
        self.key = key  # data lives in an attribute, not in parsed message text

try:
    raise NotFoundError("user-42")
except QueryError as err:
    print(type(err).__name__, err.key)  # NotFoundError user-42
```

**Типові помилки:**
- не мати власного базового класу: споживачам доводиться перелічувати всі класи, щоб перехопити помилки бібліотеки;
- переставити існуючий клас в іншу гілку ієрархії: змінюються `except`-блоки споживачів, хоча код бібліотеки формально правильний;
- розбирати `str(err)`, щоб визначити причину: текст повідомлення зазвичай не вважають частиною API.
