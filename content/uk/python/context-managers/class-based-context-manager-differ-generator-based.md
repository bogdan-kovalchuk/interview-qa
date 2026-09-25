---
id: py-ctxmgr-0004
title: "Чим class-based context manager відрізняється від generator-based manager через `@contextmanager`?"
description: "Class-based визначає __enter__ і __exit__ як окремі методи та легко зберігає стан у self; generator-based використовує одну функцію з yield, де код до yield – це enter, а після – exit."
track: python
section: context-managers
level: middle
type: comparison
tags: [contextmanager]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Class-based визначає `__enter__` і `__exit__` як окремі методи та легко зберігає стан у `self`; generator-based використовує одну функцію з `yield`, де код до yield – це enter, а після – exit.**[^py314-reference-datamodel-with-statement-context-managers] `@contextmanager` скорочує boilerplate для простих менеджерів, але створює "one-shot" об'єкт – повторне використання того самого instance викличе `RuntimeError`. Class-based підхід кращий, коли потрібна reuse, reentrancy або складна ініціалізація.

## Detailed explanation

Контекстний менеджер на основі класу безпосередньо реалізує протокол мови через методи `__enter__` і `__exit__`, тоді як генераторний підхід використовує декоратор `@contextmanager` із бібліотеки `contextlib` для перетворення генераторної функції з одним `yield` на об'єкт контексту.[^py314-reference-datamodel-with-statement-context-managers][^py314-library-contextlib]

Під капотом `@contextmanager` огортає функцію допоміжним класом `_GeneratorContextManager`. Під час входу у `with` викликається `next(gen)`, який виконує код до ключового слова `yield`, а повернуте виразом значення передається у змінну після `as`. Під час виходу з блоку інтерпретатор викликає `__exit__`, де за відсутності помилок викликається повторний `next(gen)` для виконання коду після `yield`, а при виникненні винятку – метод `gen.throw()`. Це дозволяє писати очищення через звичну конструкцію `try...finally`.

Ключова відмінність полягає в життєвому циклі та повторному використанні: генераторний менеджер завжди є одноразовим (one-shot). Оскільки генератор не можна перемотати назад після вичерпання, збереження екземпляра в змінну та повторне використання в іншому блоці `with` призведе до помилки `RuntimeError`. Менеджер на основі класу повністю контролює свій внутрішній стан у `self` і може бути спроєктований як багаторазовий (reusable) або навіть повторно-вхідний (reentrant), якщо стан коректно скидається або інкрементується в `__enter__`.

Порівняння реалізації class-based та generator-based контекстних менеджерів:

```python
from contextlib import contextmanager


# 1. Generator-based manager: concise, one-shot
@contextmanager
def managed_resource_gen(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")


# 2. Class-based manager: explicit protocol, reusable instance
class ManagedResourceClass:
    def __init__(self, name):
        self.name = name
        self.active = False

    def __enter__(self):
        print(f"Acquiring {self.name}")
        self.active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active = False
        print(f"Releasing {self.name}")
        return False  # Propagate any exception


with managed_resource_gen("connection-A") as conn:
    print(f"Using {conn}")

res = ManagedResourceClass("connection-B")
with res:
    print(f"Using {res.name}, active: {res.active}")
# Class-based instances can be reused if written to support it:
with res:
    print(f"Reused {res.name}, active: {res.active}")
```

**Критерії вибору між підходами:**
- generator-based ідеально підходить для швидких, лінійних сценаріїв (тимчасова зміна конфігурації, взяття блокування, вимірювання часу виконання);
- class-based незамінний, коли контекстний менеджер повинен мати публічні методи, властивості або складний внутрішній стан, доступний користувачеві;
- обробка винятків: у `@contextmanager` для пригнічення винятку достатньо перехопити його у блоці `except` навколо `yield`, тоді як у класі необхідно явно повертати `True` з `__exit__`;
- накладні витрати: виклики генераторів мають незначний overhead на створення фрейму генератора, тоді як виклики методів класу виконуються дещо швидше при критичних вимогах до latency.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
