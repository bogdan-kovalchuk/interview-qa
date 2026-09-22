---
id: py-objtypes-0013
title: "Чим hashability відрізняється від immutability і чому ці властивості не є повними синонімами?"
description: "Hashability означає, що об'єкт має незмінний протягом lifetime hash і підтримує __eq__; immutability означає, що значення об'єкта не можна змінити після створення."
track: python
section: objects-and-types
level: middle
type: comparison
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L3-L16
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Hashability означає, що об'єкт має незмінний протягом lifetime hash і підтримує `__eq__`; immutability означає, що значення об'єкта не можна змінити після створення.**[^py314-reference-datamodel] Це не синоніми: `tuple` immutable, але `(1, [2, 3])` unhashable, бо містить mutable елемент. І навпаки, custom клас може бути фактично immutable, але якщо він визначає `__eq__` без `__hash__`, Python автоматично робить його unhashable (`__hash__ = None`).

## Detailed explanation

У моделі даних Python властивості hashability (гешованість) та immutability (незмінність) вирішують різні задачі й не є взаємозамінними.[^py314-reference-datamodel] Об'єкт вважається hashable, якщо він має метод `__hash__`, що повертає ціле число, яке залишається незмінним протягом усього його життєвого циклу, реалізує порівняння через `__eq__` і задовольняє умову: якщо `a == b`, то `hash(a) == hash(b)`. Immutability ж стосується лише стану: об'єкт є незмінним, якщо його значення та посилання на вкладені елементи не можна змінити після ініціалізації (`int`, `str`, `tuple`, `frozenset`).

Ці властивості не збігаються з трьох основних причин. По-перше, незмінний контейнер може містити мутабельні елементи. Наприклад, `tuple` є структурно незмінним, але кортеж `(1, [2, 3])` є unhashable: функція `hash()` рекурсивно обчислює геші вмісту, і при спробі гешувати вкладений список виникає помилка `TypeError: unhashable type: 'list'`. Для гешованості кортежу обов'язковою є гешованість кожного його елемента.

По-друге, мутабельний об'єкт може бути hashable. Екземпляри звичайних користувацьких класів, які не перевизначають `__eq__`, успадковують гешування та перевірку рівності за ідентичністю (`id()`) від `object`. Стан такого екземпляра можна вільно модифікувати, але його геш базується на адресі об'єкта і ніколи не змінюється. По-третє, клас із незмінними полями автоматично стає unhashable (`__hash__ = None`), щойно в ньому визначається метод `__eq__` без явного `__hash__`.

Приклади, що демонструють різницю між hashability та immutability:

```python
# 1. An immutable container holding a mutable object is unhashable
t = (1, 2, [3, 4])
try:
    hash(t)
except TypeError as error:
    print(error)  # unhashable type: 'list'

# 2. A mutable object can be hashable via object identity
class MutableNode:
    def __init__(self, value: int):
        self.value = value

node = MutableNode(10)
print(isinstance(hash(node), int))  # True
node.value = 99                     # Mutated state, but identity hash is unchanged
print(isinstance(hash(node), int))  # True

# 3. Defining __eq__ without __hash__ disables hashing
class Point:
    def __init__(self, x: int):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x

print(Point.__hash__ is None)  # True (Python sets __hash__ = None)
```

**Ключові відмінності та практичні висновки:**
- незмінність контейнера не гарантує гешованості: `tuple` або `frozenset` є hashable лише тоді, коли всі їхні елементи є hashable;
- мутабельність не виключає гешованості за замовчуванням: класи без `__eq__` гешуються за ідентичністю незалежно від змін їхнього стану;
- явний контракт при value-based рівності: для використання власних класів як ключів словника слід або використовувати незмінні поля й реалізувати узгоджений `__hash__`, або використовувати `dataclass(frozen=True)`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
