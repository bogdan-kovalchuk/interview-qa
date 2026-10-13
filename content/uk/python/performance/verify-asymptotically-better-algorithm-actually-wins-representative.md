---
id: py-perf-0005
title: "Як перевірити, що asymptotically кращий algorithm реально виграє на representative input sizes та distributions?"
description: "Перевірити повторними вимірами timeit на розмірах і розподілах, близьких до продакшн: асимптотика не гарантує переможця на конкретних даних."
track: python
section: performance
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
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація profile (Python 3.14): профайлер показує, як часто і як довго виконувались частини програми, додає накладні витрати для коду на Python і не призначений для бенчмаркінгу, для якого є timeit."
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація timeit (Python 3.14): для точного вимірювання рекомендовано повторити його кілька разів і взяти найкращий час; за замовчуванням збирач сміття вимикається на час вимірювання."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація tracemalloc (Python 3.14): трасування блоків пам’яті, виділених Python; статистика виділень за файлом і рядком; порівняння двох знімків."
---

## Short answer

**Перевірити можна бенчмарком на розмірах `n`, близьких до продакшн, і на кількох розподілах вхідних даних, порівнюючи найкращий час із кількох повторів `timeit`.**[^py314-library-timeit] Асимптотично краща складність (наприклад, `O(n log n)` проти `O(n²)`, де перша – класична межа для сортування порівнянням) не гарантує виграшу при конкретному `n`: на малих розмірах більші константи можуть переважити. Спершу `profile` показує, де в workload іде час, а `tracemalloc` показує, скільки пам’яті виділяє кожен варіант.[^py314-library-profile][^py314-library-tracemalloc]

## Detailed explanation

Асимптотика описує, як зростає час при збільшенні `n`, але не каже, який із двох алгоритмів швидший при конкретному `n`. Час приблизно дорівнює `c*f(n)` плюс накладні витрати, а константи `c` залежать від реалізації, структур даних і версії Python. Тому алгоритм із кращою асимптотикою може програти на малих розмірах. Перевірка має відповісти, на яких `n` працює система і які розподіли вхідних даних там трапляються.

Для кожного варіанта беруть найкращий час із кількох повторів, бо окремі вимірювання зашумлені; документація `timeit` рекомендує саме це.[^py314-library-timeit] Нижче порівнюються два способи прибрати дублікати: сортування за O(n log n) (класична межа для сортування порівнянням; джерело тут не цитується) і сканування списку унікальних значень, яке коштує O(n*u), де `u` – кількість різних значень. Код друкує переможця для кожного `n`:

```python
import random
import timeit

def unique_sorted(xs):
    # O(n log n): sort first, then drop neighbouring duplicates
    out = []
    for x in sorted(xs):
        if not out or out[-1] != x:
            out.append(x)
    return out

def unique_scan(xs):
    # O(n*u), u = number of distinct values: each test scans the list so far
    out = []
    for x in xs:
        if x not in out:
            out.append(x)
    return out

random.seed(1)
for n in (8, 64, 512, 4096):
    data = [random.randrange(n) for _ in range(n)]
    number = max(1, 1000 // n)
    # best of 5 repeats, as the timeit docs recommend
    a = min(timeit.repeat(lambda: unique_sorted(data), number=number, repeat=5))
    b = min(timeit.repeat(lambda: unique_scan(data), number=number, repeat=5))
    print(n, 'scan' if b < a else 'sort')

# expected output (CPython 3.13 and 3.14):
# 8 scan
# 64 sort
# 512 sort
# 4096 sort
```

Переможець залежить і від розподілу, а не лише від `n`: сканування може виграти, коли `u` значно менше за `n`, бо тоді воно працює майже лінійно; коли значення здебільшого різні, як у прикладі вище, виграє сортування. Тому в бенчмарку потрібні випадкові, майже відсортовані й сильно дубльовані дані. Висновок справедливий лише для перевірених розмірів, розподілів, версії Python і машини.

`timeit` за замовчуванням вимикає збирач сміття на час вимірювання, тож витрати GC у реальній програмі можуть не відобразитися в цифрі.[^py314-library-timeit] `profile` призначений для пошуку місць, де йде час, а не для бенчмаркінгу: він додає накладні витрати для коду на Python, тому варіанти порівнюють через `timeit`.[^py314-library-profile]

**Типові помилки:**
- порівняти на одному `n` і перенести висновок на інші розміри;
- тестувати лише випадкові дані, тоді як у продакшні багато дублікатів або майже відсортовані дані;
- брати одне вимірювання або середнє замість найкращого часу з повторів;
- бенчмаркати функцію ізольовано, хоча її вартість у системі визначає інший код.

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
