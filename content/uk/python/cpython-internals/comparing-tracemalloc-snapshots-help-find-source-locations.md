---
id: py-cpyint-0019
title: "Як порівняння `tracemalloc` snapshots допомагає знайти source locations зростання allocations?"
description: "Snapshot.compare_to(old_snapshot, key_type) обчислює різницю (size_diff, count_diff) між двома знімками, згруповану за filename, lineno або traceback, і сортує за абсолютним size_diff."
track: python
section: cpython-internals
level: middle
type: practical
tags: [tracemalloc]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L334-L381
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Snapshot.compare_to(old_snapshot, key_type)` обчислює різницю (`size_diff`, `count_diff`) між двома знімками, згруповану за filename, lineno або traceback, і сортує за абсолютним `size_diff`.**[^py314-library-dis] Типовий workflow: `tracemalloc.start()` -> зробити перший snapshot у контрольній точці -> виконати підозрілий код -> зробити другий snapshot -> `current.compare_to(prev, 'lineno')` повертає `StatisticDiff` список, де перші рядки – source locations з найбільшим зростанням. `key_type='traceback'` дає повні call stacks для точнішої діагностики, але вимагає `nframe > 1` у `tracemalloc.start()`.

## Detailed explanation

`tracemalloc` – це вбудований модуль, який записує, звідки (source location) було виконано кожен
allocation пам'яті для Python-об'єктів, і дозволяє порівнювати ці записи між двома моментами
часу.[^py314-library-tracemalloc]

Метод `Snapshot.compare_to(old_snapshot, key_type)` порівнює поточний snapshot з попереднім і
повертає список `StatisticDiff`, де кожен елемент має поля `size`, `size_diff`, `count` і
`count_diff` – абсолютне значення та зміну відносно старого snapshot. Параметр `key_type` визначає
рівень групування: `'filename'` групує за файлом, `'lineno'` – за конкретним рядком, а
`'traceback'` – за повним call stack allocation. Список завжди відсортований за спаданням
абсолютного `size_diff`, тому перші елементи – це місця з найбільшим зростанням.

Типовий workflow – зробити snapshot до підозрілого коду, виконати цей код, зробити другий snapshot і
порівняти їх; так видно лише зміну, а не весь baseline allocations процесу.

Приклад порівняння двох snapshots за рядком коду:

```python
tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
run_suspect_code()
snapshot2 = tracemalloc.take_snapshot()

diff = snapshot2.compare_to(snapshot1, 'lineno')
for stat in diff[:3]:
    print(stat)  # top growth: <file>:<line>: size=..., count=...
```

Щоб отримати `key_type='traceback'` з повним call stack, а не лише останнім рядком, треба викликати
`tracemalloc.start(nframe)` з `nframe > 1` ще до першого snapshot – кількість збережених кадрів
фіксується на старті і не може бути змінена заднім числом.

**Типові помилки при роботі з tracemalloc:**
- порівнювати snapshots з різних процесів або перезапусків interpreter – адреси й lineno можуть не
  відповідати одна одній;
- забувати викликати `tracemalloc.start(nframe)` з потрібним `nframe` до першого snapshot, коли
  потрібен `key_type='traceback'`;
- інтерпретувати `count_diff` без `size_diff` – багато дрібних allocations можуть важити менше, ніж
  кілька великих.

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
