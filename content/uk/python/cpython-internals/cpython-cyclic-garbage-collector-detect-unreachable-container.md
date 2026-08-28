---
id: py-cpyint-0010
title: "Як cyclic garbage collector CPython виявляє unreachable container cycles поверх reference counting?"
description: "GC відстежує container-об'єкти (list, dict, user-defined instances), обходить граф їхніх посилань і звільняє групи об'єктів, на які немає зовнішніх (не від GC) посилань."
track: python
section: cpython-internals
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**GC відстежує container-об'єкти (list, dict, user-defined instances), обходить граф їхніх посилань і звільняє групи об'єктів, на які немає зовнішніх (не від GC) посилань.**[^py314-library-dis] Об'єкти розподілені за трьома поколіннями (0, 1, 2); нові контейнери потрапляють у покоління 0. Коли кількість allocation мінус deallocation перевищує поріг, запускається збір. GC перевіряє, чи можна досягти об'єктів з коренів; якщо ні – вони collectable. Старші покоління збираються рідше, що знижує overhead.

## Detailed explanation

Cyclic garbage collector CPython – це додатковий механізм, який доповнює reference counting і вміє
знаходити та звільняти групи container-об'єктів (list, dict, set, екземпляри класів), що
посилаються одне на одне по колу, навіть коли зовнішній refcount кожного з них ніколи не впаде до
нуля.[^py314-library-gc]

Лише container-об'єкти реєструються у GC, бо тільки вони можуть брати участь у циклі: числа, рядки
чи tuple без посилань на контейнери не потребують перевірки. Нові container-об'єкти потрапляють у
покоління 0; кожен об'єкт, що пережив збір, переходить у наступне покоління (0 -> 1 -> 2). Збір
покоління 0 запускається, коли різниця між кількістю allocations і deallocations перевищує поріг
`gc.get_threshold()`; старші покоління збираються рідше, бо довгоживучі об'єкти рідше стають сміттям.

Сам алгоритм – це не пошук `refcount == 0`, а «trial deletion»: GC тимчасово віднімає від refcount
кожного container-об'єкта кількість посилань, які надходять від інших об'єктів у тому самому
поколінні. Те, що лишається після цього віднімання, – це refcount «ззовні» покоління. Об'єкти з
позитивним зовнішнім refcount вважаються досяжними коренями, і GC обходить граф від них; усе
недосяжне з цих коренів – collectable, навіть якщо об'єкти циклічно тримають одне одного.

```python
import gc

gc.collect()  # force a full collection across all generations
print(gc.get_threshold())  # (700, 10, 10) by default
```

**Типові помилки з cyclic GC:**
- вважати, що цикл без `__del__` є проблемою – з Python 3.4 GC звільняє такі цикли без обмежень;
- вимикати `gc.disable()` для швидкодії, не враховуючи, що це залишає всі цикли непрацездатними;
- забувати, що об'єкти з `__del__` і участю в циклі раніше (до 3.4) взагалі не збиралися.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
