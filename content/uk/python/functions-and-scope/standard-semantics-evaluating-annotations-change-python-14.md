---
id: py-funcs-0024
title: "Як у Python 3.14 змінилася стандартна семантика обчислення annotations і чому для їх безпечної інспекції варто використовувати `annotationlib`, а не покладатися лише на пряме читання `__annotations__`?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-howto-annotations
    title: "Python 3.14: Howto/annotations"
    url: https://docs.python.org/3.14/howto/annotations.html
  - source_id: py314-library-annotationlib
    title: "Python 3.14: Library/annotationlib"
    url: https://docs.python.org/3.14/library/annotationlib.html
  - source_id: pep-649
    title: "PEP 649"
    url: https://peps.python.org/pep-0649/
  - source_id: py314-reference-compound-stmts-annotations
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#annotations
---

## Short answer

**У Python 3.14 annotations обчислюються ліниво за замовчуванням (PEP 649): компілятор генерує `__annotate__`-callable, який виконується лише при доступі до анотацій, а не під час визначення.**[^pep-649] Для безпечної інспекції використовуйте `annotationlib.get_annotations()`, а не читайте `__annotations__` напряму.[^py314-howto-annotations] Формат `Format.FORWARDREF` повертає `ForwardRef` для невизначених імен замість `NameError`, який може викликати формат за замовчуванням `Format.VALUE`.[^py314-library-annotationlib] PEP 563 (`from __future__ import annotations`) зберігає анотації рядками, і його заплановано позначити застарілим та вилучити.[^py314-reference-compound-stmts-annotations]

## Detailed explanation

До Python 3.14 анотації обчислювалися під час виконання `def` або `class`, тож звернення до ще не визначеного імені одразу давало `NameError`.[^py314-library-annotationlib] У 3.14 за замовчуванням інтерпретатор зберігає лише те, що потрібно для обчислення анотації пізніше, і обчислює її тоді, коли до анотацій звертаються.[^py314-reference-compound-stmts-annotations] Для цього компілятор створює окрему `__annotate__`-функцію, яка повертає словник анотацій.[^pep-649]

Наслідок: помилка в анотації переходить із моменту визначення в момент доступу. Приклад:

```python
# Python 3.14+
from annotationlib import Format, get_annotations

class Node:
    def link(self, other: Later) -> None:  # Later is not defined yet
        ...

try:
    get_annotations(Node.link)
except NameError as e:
    print("VALUE:", e)                     # VALUE: name 'Later' is not defined
print(get_annotations(Node.link, format=Format.FORWARDREF)["other"].__forward_arg__)  # Later
print(get_annotations(Node.link, format=Format.STRING))  # {'other': 'Later', 'return': 'None'}

class Later: ...
print(get_annotations(Node.link)["other"].__name__)  # Later

def outer():
    Item = int
    def inner(x: Item) -> Item:
        return x
    return inner

print(outer().__annotations__)  # {'x': <class 'int'>, 'return': <class 'int'>}
```

Формат за замовчуванням `Format.VALUE` падає з `NameError`, поки `Later` не існує, а `Format.FORWARDREF` і `Format.STRING` такого винятку не дають. `get_annotations()` повертає новий словник за кожним викликом.[^py314-library-annotationlib]

Локальні змінні теж працюють інакше. Якщо анотація посилається на вільну змінну функції, `__annotate__` є замиканням, тож `x: Item` у `inner` бачить локальну `Item` і дає `int`.[^pep-649] За PEP 563 той самий `__annotations__` повернув би рядок `'Item'`.

Без обробки `NameError` читати `__annotations__` напряму ризиковано: звернення до атрибута запускає обчислення, і `NameError` виходить саме там.[^py314-library-annotationlib]

**Типові помилки:**
- вважати, що помилка в анотації з’явиться під час `def`: у 3.14 вона з’являється під час доступу до анотацій;
- читати `__annotations__` напряму в інструментах без обробки `NameError`; замість цього використовувати `get_annotations()` з потрібним форматом;
- додавати `from __future__ import annotations` у новий код як засіб для forward references: цей режим зберігає рядки, його заплановано вилучити, а `get_annotations()` і `typing.get_type_hints()` гірше розв’язують такі анотації.[^py314-reference-compound-stmts-annotations]
