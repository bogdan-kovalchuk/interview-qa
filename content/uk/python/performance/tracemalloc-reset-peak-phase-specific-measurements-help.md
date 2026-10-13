---
id: py-perf-0010
title: "Як `tracemalloc.reset_peak()` та phase-specific measurements допомагають відрізнити temporary allocation spike від retained memory growth?"
description: "tracemalloc.reset_peak() встановлює поточний розмір як новий маркер peak, не очищаючи trace-и, що дозволяє виміряти peak окремо для кожної фази виконання."
track: python
section: performance
level: senior
type: practical
tags: [tracemalloc-reset-peak]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: tracemalloc трасує переважно блоки пам’яті, виділені Python, починаючи з виклику start()."
  - source_id: py314-library-tracemalloc-reset-peak
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.reset_peak
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: reset_peak() встановлює peak рівним поточному розміру, не очищає trace-и, нічого не робить, якщо трасування вимкнено, а snapshot-и до і після виклику можна порівнювати."
  - source_id: py314-library-tracemalloc-get-traced-memory
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.get_traced_memory
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: get_traced_memory() повертає кортеж (current, peak) для блоків, які відстежує tracemalloc."
  - source_id: py314-library-tracemalloc-record-current-peak
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: приклад двох фаз; peak відраховується від start(), і без reset_peak() другий пік лишається піком попередньої фази."
  - source_id: py314-library-tracemalloc-snapshot-compare-to
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.Snapshot.compare_to
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: Snapshot.compare_to() обчислює різницю між двома snapshot-ами, щоб знайти витоки пам’яті."
---

## Short answer

**`tracemalloc.reset_peak()` встановлює поточний розмір як новий маркер peak, не очищаючи trace-и, тож peak можна виміряти окремо для кожної фази.**[^py314-library-tracemalloc-reset-peak] Викликаємо `reset_peak()` на початку фази, а після неї читаємо `get_traced_memory()`, що повертає `(current, peak)`.[^py314-library-tracemalloc-get-traced-memory] Peak значно вищий за current, а current повернувся до базового рівня – це temporary spike. Current, що зростає від фази до фази, вказує на retained growth: об’єкти досі не звільнено (або чекають збирання сміття). Щоб знайти рядок, який виділяє пам’ять, порівнюємо snapshot-и через `Snapshot.compare_to`.[^py314-library-tracemalloc-snapshot-compare-to]

## Detailed explanation

`tracemalloc` відстежує переважно блоки пам’яті, які виділив Python, починаючи з виклику `tracemalloc.start()`.[^py314-library-tracemalloc] `get_traced_memory()` повертає пару `(current, peak)`: поточний розмір traced-блоків і їхній максимум.[^py314-library-tracemalloc-get-traced-memory] Без скидання peak – це максимум від `start()`: у прикладі документації другий пік лишається великим значенням із попередньої фази, доки його не скинуто.[^py314-library-tracemalloc-record-current-peak] `reset_peak()` (з 3.9) встановлює peak рівним поточному розміру і не змінює trace-и, а snapshot-и, зняті до й після виклику, можна порівнювати.[^py314-library-tracemalloc-reset-peak]

Наступний приклад вимірює дві фази окремо. Вивід однаковий на CPython 3.13 і 3.14:

```python
import tracemalloc

MiB = 1024 * 1024

tracemalloc.start()
baseline, _ = tracemalloc.get_traced_memory()

# Phase 1: temporary spike, allocated and then freed
data = [0] * 1_000_000
total = sum(data)
del data
current, peak = tracemalloc.get_traced_memory()
print(f"spike: current={(current - baseline) / MiB:.1f} MiB, peak={(peak - baseline) / MiB:.1f} MiB")
# spike: current=0.0 MiB, peak=7.6 MiB

tracemalloc.reset_peak()  # measure phase 2's peak from the current size

# Phase 2: retained growth, each step keeps a reference
retained = []
for step in range(1, 4):
    retained.append(bytearray(MiB))
    current, peak = tracemalloc.get_traced_memory()
    print(f"step {step}: current={(current - baseline) / MiB:.1f} MiB, peak={(peak - baseline) / MiB:.1f} MiB")
# step 1: current=1.0 MiB, peak=1.0 MiB
# step 2: current=2.0 MiB, peak=2.0 MiB
# step 3: current=3.0 MiB, peak=3.0 MiB

tracemalloc.stop()
```

У першій фазі peak близько 7.6 MiB, а після `del data` current повертається до 0.0 MiB: це temporary spike. У другій фазі current росте на 1 MiB на кожен крок, бо список `retained` тримає посилання на кожен буфер, а після `reset_peak()` peak дорівнює current: це retained growth. Без `reset_peak()` кожен рядок другої фази показував би peak 7.6 MiB і приховував би її поведінку.[^py314-library-tracemalloc-record-current-peak]

Один вимір не доводить retained growth, бо показує стан лише в одній точці. Картина з’являється при повторенні тієї самої фази: якщо current після кожної ітерації зростає, блоки досі не звільнено (або чекають збирання сміття в reference cycles); якщо після фази current повертається до базового рівня, пам’ять звільнено. Щоб знайти рядок, який виділяє пам’ять, беремо snapshot до і після фази та викликаємо `Snapshot.compare_to()`, що обчислює різницю між ними.[^py314-library-tracemalloc-snapshot-compare-to]

Межі методу: `tracemalloc` не показує всю пам’ять процесу. Документація говорить про трасування «most memory blocks allocated by Python»,[^py314-library-tracemalloc] тож пам’ять, виділена C-розширеннями мимо алокатора Python, може бути відсутня в цих числах, а `get_traced_memory()` не дорівнює RSS процесу. Виклик `reset_peak()` без активного трасування нічого не робить.[^py314-library-tracemalloc-reset-peak] Без `start()` `get_traced_memory()` повертає `(0, 0)`:

```python
import tracemalloc

print(tracemalloc.get_traced_memory())  # (0, 0) on CPython 3.13 and 3.14 while tracing is off
```

**Типові помилки:**
- читати peak без `reset_peak()` і приписувати його останній фазі;
- зробити один вимір і назвати це retained growth, хоча потрібне повторення фази;
- сприймати traced-пам’ять за RSS процесу;
- викликати `reset_peak()` без `tracemalloc.start()` і очікувати ефекту.

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
