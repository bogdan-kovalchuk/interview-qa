---
id: py-itergen-0007
title: "Чому generator pipeline може зменшити peak memory, але не обов’язково total execution time?"
description: "Stages передають елементи по одному, тож pipeline не будує проміжних списків і знижує пік пам’яті, але не гарантує меншого загального часу."
track: python
section: iterators-and-generators
level: middle
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Кожен stage віддає один елемент на запит `next()`.**[^py314-library-stdtypes-iterator-types] Тому generator pipeline не будує проміжних списків і знижує peak memory: у вимірюванні з пояснення пік упав із близько 81 МБ до близько 0,001 МБ. Кількість роботи при цьому та сама: кожен елемент проходить усі stages, тому total execution time не зменшується автоматично і його треба виміряти. Пік пам’яті все одно включає все, що тримає джерело, або результат, якщо його збирають у list.

## Detailed explanation

Pipeline з generators – це ланцюжок ітераторів. Споживач викликає `next()` на останньому stage, той викликає `next()` на попередньому, і так до джерела.[^py314-library-stdtypes-iterator-types] Тому через ланцюжок у кожен момент проходить один елемент, і проміжний список не потрібен. Пік пам’яті визначають те, що одночасно тримають stages, а також джерело та результат, якщо вони є повними списками.

Нижче два варіанти одного обчислення: з проміжними списками та з ланцюжком generator expressions.

```python
import tracemalloc

N = 1_000_000

def peak_mb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return round(peak / 1e6, 3)

def eager():
    a = [x * 2 for x in range(N)]      # intermediate list
    b = [x + 1 for x in a]             # second intermediate list
    return sum(b)

def lazy():
    a = (x * 2 for x in range(N))      # generator, no list
    b = (x + 1 for x in a)
    return sum(b)

print(peak_mb(eager))                  # 80.889
print(peak_mb(lazy))                   # 0.001
```

У цьому запуску на CPython 3.14 eager-варіант тримав близько 81 МБ, а ланцюжок над `range` – близько 0,001 МБ. Якщо джерело вже є готовим списком з мільйона елементів, сам список займає близько 40 МБ (побудова `list(range(1_000_000))` під tracemalloc дає пік 39,992 МБ), а pipeline над ним додає близько 0,001 МБ. Економія стосується проміжних послідовностей, а не всього, що лежить у пам’яті.

Час – окреме питання. Pipeline не зменшує кількість роботи: кожен елемент проходить кожен stage. У CPython до цієї роботи додаються накладні витрати на перемикання між generator frames, але відпадають великі проміжні списки. Тому total execution time залежить від балансу цих факторів, і гарантії, що він зменшиться, немає. Заміри виконано для функцій `eager` і `lazy` з прикладу, найкращий час із 5 запусків через `time.perf_counter`, `N = 1_000_000`. На CPython 3.14 eager займав близько 0,09–0,10 с, lazy близько 0,05 с; на CPython 3.13 eager близько 0,10 с, lazy від 0,06 до 0,09 с. У цих запусках lazy був швидшим, але точні числа залежать від машини, тож вимірюйте на своїх даних.

**Типові помилки:**
- вважати, що generator pipeline завжди швидший, бо не створює списків;
- не враховувати, що джерело, яке вже є списком, тримає всі свої елементи в пам’яті;
- збирати результат через `list(...)` і очікувати низького піку пам’яті.

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
