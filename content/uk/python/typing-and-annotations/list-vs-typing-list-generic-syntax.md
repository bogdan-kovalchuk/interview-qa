---
id: py-typing-0001
title: "У чому різниця між List[str] з typing і list[str] вбудованим у Python 3.9+?"
track: python
section: typing-and-annotations
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
  - source_id: pep585
    title: "PEP 585: Type Hinting Generics In Standard Collections"
    url: https://peps.python.org/pep-0585/
  - source_id: pep-563
    title: "PEP 563: Postponed Evaluation of Annotations"
    url: https://peps.python.org/pep-0563/
---

## Short answer

**`typing.List[str]` є legacy typing alias, а `list[str]` є вбудованим generic-синтаксисом, запровадженим у Python 3.9 і рекомендованим для коду з цільовою версією 3.9 або новішою.**[^py314-library-typing][^pep585] Static type checkers зазвичай трактують обидва варіанти як список рядків. Проте це не ідентичні runtime objects, і жодна з цих анотацій не перевіряє елементи списку під час виконання. Python 3.8 не може обчислити `list[str]`; там використовуйте `typing.List[str]` або postpone annotation evaluation, якщо це підтримує решта tooling.

## Detailed explanation

`List[str]` з `typing` і `list[str]` для type checker означають один і той самий тип: список рядків. Відрізняються вони як runtime-об’єкти. `typing.List` є deprecated alias до built-in `list`, який модуль `typing` зберігає для сумісності.[^py314-library-typing] Built-in `list` тепер сам параметризується через `__class_getitem__()`, тому `list[str]` створює окремий generic-alias об’єкт.[^pep585] У CPython `List[str]` є `typing._GenericAlias`, а `list[str]` – `types.GenericAlias`. Обидва мають `__origin__` (`list`) і `__args__` (`(str,)`), але `List[str] == list[str]` дає `False`.

Раніше `typing.List` був єдиним способом параметризувати колекцію під час виконання, бо built-in `list` не приймав `[]`. PEP 585 додав цю можливість у Python 3.9, і з того часу документація позначає старі aliases як deprecated. Інтерпретатор на них не видає попереджень, а їх видалення з `typing` може відбутися в майбутньому.[^pep585]

Анотації не перевіряють значення під час виконання. Функція з `items: list[str]` приймає `[42]` і повертає `42`; помилку може знайти лише type checker. Для runtime-перевірки типу контейнера `list[str]` не підходить: `isinstance(x, list[str])` кидає `TypeError` (у CPython 3.12–3.14), тому пишіть `isinstance(x, list)`. Приклад:

```python
from typing import List

print(List[str] == list[str])                              # False: two different runtime objects
print(type(List[str]).__name__, type(list[str]).__name__)  # _GenericAlias GenericAlias

def first(items: list[str]) -> str:
    return items[0]

print(first([42]))                                         # 42: the annotation is not checked at runtime
```

Вираз `list[str]` у runtime-контексті вимагає Python 3.9 або новішого: PEP 585 прив’язує вбудований generic-синтаксис до 3.9 і зазначає, що type alias та cast потребують типу поза анотацією.[^pep585] Якщо код має працювати на 3.8, у runtime-виразах використовуйте `typing.List[str]`. Для анотацій можна ввімкнути `from __future__ import annotations` (доступно з 3.7), щоб `list[str]` не обчислювався,[^pep-563] але це працює лише там, де tooling розуміє такий запис.[^pep585]

**Типові помилки:**
- вважати, що `list[str]` перевіряє елементи списку під час виконання (див. приклад вище);
- порівнювати `List[str]` і `list[str]` через `==` або `isinstance` і очікувати однакову поведінку;
- писати `list[str]` у runtime-коді (alias, cast, виклики `isinstance`), що має працювати на 3.8, і отримати `TypeError` лише на старій версії.
