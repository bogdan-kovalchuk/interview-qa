---
id: py-excpt-0004
title: "Коли виконується `else` у конструкції `try/except/else/finally` і навіщо виносити туди success-path code?"
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

**`else` виконується лише тоді, коли `try` завершився без exception і без `return`/`break`/`continue`.**[^py314-reference-compound-stmts-the-try-statement] Код, який має виконатися лише тоді, коли `try` не піднімає виняток, корисно винести в `else`.[^py314-tutorial-errors] Виняток із `else` не обробляють попередні `except` clauses, але `finally` все одно виконається для cleanup.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

Блок `try` має захищати лише ту операцію, яка може піднімати очікуваний виняток, а код успішного шляху – виконуватися після неї. `else` виконується, коли управління вийшло з `try` без винятку і без `return`, `break` чи `continue`.[^py314-reference-compound-stmts-the-try-statement] Тому `return` у `try` пропускає `else`, а `finally` виконується завжди.

```python
def to_int(text):
    try:
        number = int(text)            # the only call here that may raise ValueError
    except ValueError:
        return None
    else:
        return number * 2             # runs only when int() succeeded
    finally:
        print("checked", repr(text))

print(to_int("21"))  # checked '21', then 42
print(to_int("x"))   # checked 'x', then None
```

Якщо залишити в `try` кроки успішного шляху, `except ValueError` перехопить і їхні винятки, хоча призначений він лише для помилки розбору. Наприклад, `ValueError`, який кине функція обробки числа, виглядатиме як помилка введення. Handler-и стосуються винятків, що виникають у `try`-блоці, зокрема всередині функцій, які з нього викликаються (навіть опосередковано).[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors] Тож чим менше коду там, тим точніше визначено, що перехоплюється.

Виняток, піднятий у `else`, не обробляють попередні `except` clauses, але `finally` все одно виконається, і тимчасово збережений виняток буде піднятий знову.[^py314-reference-compound-stmts-the-try-statement] Тож `else` – для коду успішного шляху, `try` – для викликів, які очікувано можуть упасти, а `finally` – для cleanup.

**Типові помилки:**
- класти ризиковий виклик в `else`, сподіваючись, що `except` його перехопить;
- вважати, що `else` виконається після `return` у `try`;
- плутати `else` з `finally`: `else` пропускається при `return`, `break` або `continue`, а `finally` ні.
