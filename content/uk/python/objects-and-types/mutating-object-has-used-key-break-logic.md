---
id: py-objtypes-0008
title: "Як mutation об’єкта після використання його як key може пошкодити логіку hash-based collection?"
description: "Якщо змінити об'єкт після того, як він став key у dict або елементом set, його hash зміниться і пошук за початковим hash поверне хибний результат – ключ «губиться»."
track: python
section: objects-and-types
level: senior
type: practical
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Якщо змінити об'єкт після того, як він став key у `dict` або елементом `set`, його hash зміниться і пошук за початковим hash поверне хибний результат – ключ «губиться».**[^py314-reference-datamodel] Hash-based колекції кешують hash ключа в момент вставки; після зміни значення ключа новий hash не збігається з кешованим, і колекція не може знайти запис. Щоб уникнути цього, як ключі використовують лише immutable об'єкти з стабільним `__hash__`.

## Detailed explanation

Хеш-таблиці в Python (`dict` і `set`) спираються на незмінність значення `__hash__()` та логіки `__eq__()` ключа протягом усього часу його перебування в колекції.[^py314-reference-datamodel]

Під час додавання елемента інтерпретатор обчислює його хеш і за цим значенням визначає початковий індекс у таблиці та послідовність пробінгу (probe sequence). У CPython структури `dict` кешують обчислене значення хешу в кожному записі. Коли здійснюється пошук за ключем, інтерпретатор обчислює його хеш наново, проходить відповідним ланцюжком слотів і порівнює записи за рівністю хешів, а потім – за ідентичністю (`is`) чи еквівалентністю (`==`).

Якщо об'єкт мутує після додавання, його новий хеш направляє пошук за зовсім іншою траєкторією пробінгу. Інтерпретатор потрапляє на порожні слоти або сторонні елементи і повідомляє, що ключа немає, навіть не перевіряючи слот, у якому об'єкт фізично розташований.[^py314-library-stdtypes] Виникає парадоксальний стан: ключ присутній при ітерації через `keys()` або `items()`, враховується у `len()`, але операції прямого доступу (`k in d`, `d[k]`, `s.remove(k)`) завершуються `KeyError`.

Наслідки виходять далеко за межі невдалого читання: спроба повторно додати мутований об'єкт не виявить старий запис і створить дублікат у `set` або `dict`, порушуючи фундаментальні інваріанти унікальності. Під час розширення (resize) або перехешування таблиці поведінка стає повністю недетермінованою: деякі ключі можуть випадково знову стати доступними, а інші – остаточно загубитися.

Приклад руйнування пошуку в словнику після зміни стану ключа:

```python
class MutableKey:
    def __init__(self, val: str):
        self.val = val

    def __hash__(self) -> int:
        return hash(self.val)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, MutableKey) and self.val == other.val

key = MutableKey("initial")
lookup = {key: "payload"}

# Successful initial lookup
print(lookup[key])  # 'payload'

# Mutate key state after insertion
key.val = "modified"

# Lookup fails because hash changed and targets the wrong bucket
print(key in lookup)  # False
try:
    _ = lookup[key]
except KeyError:
    print("KeyError: key cannot be found")

# The key is still physically inside the dictionary
print(len(lookup))  # 1
print([k.val for k in lookup.keys()])  # ['modified']
```

**Архітектурні вимоги та запобіжні заходи:**
- дотримуватися фундаментального інваріанта хешовності: якщо два об'єкти рівні (`a == b`), їхні хеші обов'язково рівні (`hash(a) == hash(b)`), і жодне з цих значень не має змінюватися;
- у разі перевизначення `__eq__` у користувацькому класі інтерпретатор автоматично виставляє `__hash__ = None`, захищаючи від помилок; не варто примусово повертати `__hash__` для mutable класів;
- використовувати `@dataclass(frozen=True)` або іменовані кортежі (`NamedTuple`) для складних ключів словників і елементів множин;
- якщо клас обов'язково має бути mutable, слід залишити стандартний `__hash__` на основі ідентичності об'єкта (`id`) і не прив'язувати `__eq__` до його змінних полів.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
