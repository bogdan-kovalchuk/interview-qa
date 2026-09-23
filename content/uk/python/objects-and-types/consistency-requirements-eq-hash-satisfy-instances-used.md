---
id: py-objtypes-0004
title: "Які узгоджені вимоги мають виконувати `__eq__` і `__hash__`, якщо instances використовуються як keys словника?"
description: "Об'єкти, що рівні за __eq__, обов'язково мають повертати однакове значення __hash__."
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [eq, hash]
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

**Об'єкти, що рівні за `__eq__`, обов'язково мають повертати однакове значення `__hash__`.**[^py314-reference-datamodel] Якщо клас визначає `__eq__` без `__hash__`, його `__hash__` неявно встановлюється в `None` і екземпляри стають непридатними для hash-based колекцій. Mutable об'єкти не повинні реалізовувати `__hash__`, бо їхня рівність може змінитися після зміни значення.

## Detailed explanation

Для коректної роботи об'єктів як ключів у словниках або елементів у множинах модель даних Python вимагає дотримання фундаментального інваріанту: якщо два об'єкти рівні за `__eq__`, вони обов'язково повинні повертати однаковий `__hash__`.[^py314-reference-datamodel]

Словники (`dict`) та множини (`set`) у Python побудовані на основі геш-таблиць. Під час пошуку або збереження ключа інтерпретатор спочатку обчислює `hash(key)`, щоб визначити індекс кошика (bucket). Якщо кошик зайнятий, Python перевіряє рівність за формулою `k is target or k == target`. Якщо два рівні об'єкти повертають різні геш-значення, інтерпретатор шукає їх у різних кошиках і не може знайти наявний ключ, що призводить до дублювання записів у `set` або неможливості отримати значення з `dict`.[^py314-library-stdtypes]

За замовчуванням користувацькі класи успадковують `__eq__` і `__hash__` від `object`: рівність перевіряється за ідентичністю (`is`), а геш генерується на основі адреси в пам'яті. Проте, якщо клас перевизначає `__eq__`, Python автоматично встановлює `__hash__ = None`. Це запобігає випадковому використанню екземплярів із кастомною рівністю у геш-таблицях без узгодженого хешування, генеруючи `TypeError: unhashable type`.

Щоб зробити екземпляри з кастомним `__eq__` придатними для гешування, необхідно явно реалізувати `__hash__`, обчислюючи його виключно на основі незмінних атрибутів, які беруть участь у `__eq__`. Якщо хоча б одне з цих полів зміниться після додавання об'єкта до словника, його геш зміниться, але сам об'єкт залишиться у старому кошику геш-таблиці, через що знайти його знову буде неможливо.

Приклад правильної узгодженої реалізації `__eq__` та `__hash__`:

```python
class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self._x, self._y) == (other._x, other._y)

    def __hash__(self):
        # Consistent hash based on the exact same fields as __eq__
        return hash((self._x, self._y))

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)              # True: equal coordinates
print(hash(p1) == hash(p2))  # True: satisfies the hash consistency invariant

point_map = {p1: "origin_offset"}
print(point_map[p2])         # "origin_offset": successfully resolved via hash and equality
```

**Вимоги до реалізації та типові помилки:**
- порушення інваріанту узгодженості: об'єкти з однаковими полями повертають різні геші, через що словник не знаходить наявний ключ;
- обчислення `__hash__` за змінними полями: після модифікації атрибутів ключ стає недосяжним у колекції, порушуючи внутрішній стан геш-таблиці;
- включення в `__hash__` атрибутів, що відсутні в `__eq__`: це призводить до розбіжності гешів для об'єктів, які метод `__eq__` вважає рівними;
- пропущена реалізація `__hash__` при зміні `__eq__`: клас автоматично отримує `__hash__ = None`, що робить його об'єкти unhashable.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
