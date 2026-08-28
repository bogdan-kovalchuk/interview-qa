---
id: py-cpyint-0012
title: "Яка різниця між Python object lifetime і повернення пам’яті process allocator операційній системі?"
description: "Object lifetime – це момент, коли Python-об'єкт стає недосяжним і його пам'ять звільняється на рівні Python; повернення пам'яті ОС – це окремий етап, коли allocator процесу (pymalloc arena або mimalloc) вирішує віддати..."
track: python
section: cpython-internals
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L270-L333
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Object lifetime – це момент, коли Python-об'єкт стає недосяжним і його пам'ять звільняється на рівні Python; повернення пам'яті ОС – це окремий етап, коли allocator процесу (pymalloc arena або mimalloc) вирішує віддати сторінку назад.**[^py314-library-dis] У CPython об'єкт звільняється, коли його refcount досягає нуля (або cyclic GC його збирає), але його блок пам'яті повертається у pool allocator'а, а не одразу в ОС. Arena (256 KiB/1 MiB) повертається ОС лише коли стає повністю порожньою. Тому об'єкт може бути «мертвим» з погляду Python, але його пам'ять залишається в RSS процесу.

## Detailed explanation

Python object lifetime і повернення пам'яті операційній системі – це дві різні стадії одного
процесу, розділені шаром allocator, і плутати їх означає неправильно тлумачити, чому RSS процесу не
падає одразу після того, як об'єкти стали «мертвими».[^py314-c-api-memory]

Lifetime об'єкта закінчується на рівні Python: коли `refcount` падає до нуля (або коли cyclic GC
звільняє цикл), CPython викликає деструктор і звільняє блок пам'яті об'єкта. Це видно з погляду
Python – наступний виклик `id()` для того самого адреса дасть інший об'єкт, а `sys.getrefcount()`
для видаленого імені вже не має сенсу.

Звільнений блок, однак, не повертається одразу в ОС. Для малих об'єктів (до 512 байт) CPython
використовує `pymalloc`: блок повертається у pool певного розміру всередині arena (типово 1 MiB),
щоб наступний allocation того самого розміру не звертався до ОС. Arena повертається операційній
системі лише тоді, коли всі pool у ній стають повністю порожніми – якщо хоч один блок в arena ще
живий, уся arena лишається зарезервованою за процесом.

```python
big = [object() for _ in range(1_000_000)]
del big  # objects are freed at the Python level immediately
# process RSS typically does not shrink here: arenas stay reserved
```

Тому довгоживучий процес, який один раз виділив і звільнив велику структуру, може тримати значний
RSS без жодного memory leak на рівні Python: фрагментація arena, а не витік, пояснює графік
пам'яті.[^py314-c-api-memory]

**Практичні наслідки цієї різниці:**
- падіння RSS після `del` чи `gc.collect()` не гарантоване і не є ознакою leak, якщо його немає;
- для перевірки саме leak варто відстежувати кількість живих об'єктів (`tracemalloc`,
  `gc.get_objects()`), а не RSS;
- періодичний restart worker-процесів – типовий обхідний шлях для фрагментації arena, а не баг у
  коді.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
