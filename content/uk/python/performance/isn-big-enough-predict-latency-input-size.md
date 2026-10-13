---
id: py-perf-0007
title: "Чому Big O недостатньо для прогнозу latency без розміру input, constants та memory-access behavior?"
description: "Big O відкидає константи й поведінку пам’яті, тому на практичних розмірах клас складності може не визначати, який код швидший."
track: python
section: performance
level: senior
type: pitfall
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
  - source_id: py314-library-array
    title: "Python 3.14: Library/array"
    url: https://docs.python.org/3.14/library/array.html#module-array
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація модуля array (Python 3.14): тип, що компактно представляє масив базових значень одного типу."
  - source_id: cpython-listobject-h
    title: "CPython 3.14: Include/cpython/listobject.h"
    url: https://github.com/python/cpython/blob/v3.14.6/Include/cpython/listobject.h
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Заголовок CPython 3.14 (тег v3.14.6): список зберігає масив покажчиків на елементи (ob_item). Опис реалізації CPython, а не гарантія мови."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація tracemalloc (Python 3.14): трасування блоків пам’яті, виділених Python; статистика виділень за файлом і рядком; порівняння двох знімків."
---

## Short answer

**Big O описує лише зростання при великих `n` і відкидає константи, тому на практичних розмірах вона не визначає, який код швидший.** Два алгоритми однієї складності можуть відрізнятися в кілька разів через накладні витрати інтерпретатора, а розташування даних у пам’яті змінює латентність. Для вимірювання використовують `timeit`, а не профайлер, бо профайлер сам додає накладні витрати.[^py314-library-profile]

## Detailed explanation

Big O – це верхня межа зростання, коли `n` прямує до нескінченності, і множники навмисно відкидаються. Для конкретного `n` час складається з множника на кожен крок плюс накладні витрати, тому два алгоритми однієї складності можуть відрізнятися в кілька разів. Приклад: обидва варіанти шукають останнє значення у списку зі 100 000 елементів і обидва мають O(n), але цикл на Python виконує кожну ітерацію через інтерпретатор, а `list.index` – у C:

```python
def python_find(seq, value):
    for index, item in enumerate(seq):   # every step runs through the interpreter
        if item == value:
            return index
    return -1

data = list(range(100_000))
print(python_find(data, 99_999))   # 99999
print(data.index(99_999))          # 99999: same O(n) scan, but the loop runs in C
```

Константи можуть переставити порядок навіть між різними класами. Припустімо, що один алгоритм займає приблизно `50*n*log2(n)` умовних одиниць, а другий `2*n**2`. При `n = 100` швидший квадратичний (близько 20 000 проти 33 200), а при `n = 1000` – варіант `n log n` (близько 498 000 проти 2 000 000). Це арифметика умовної моделі, а не виміряні значення; у вашому коді їх треба виміряти.

Другий фактор – пам’ять. `list` у CPython зберігає масив покажчиків на елементи, тож обхід списку звертається і до самих об’єктів, розташованих у пам’яті окремо.[^cpython-listobject-h] Модуль `array` компактно представляє масив базових значень.[^py314-library-array] Це зазвичай краще лягає в кеш процесора, але ефект залежить від розміру, платформи й патерну доступу, тому його треба вимірювати, а не вважати гарантованим. Для обсягу виділень використовують `tracemalloc`, який показує статистику за рядками коду.[^py314-library-tracemalloc]

На практиці спершу `profile` показує, де в повному workload іде час,[^py314-library-profile] потім кандидати порівнюють `timeit`-ом на реальному `n` і даних. Big O лишається корисною при зростанні `n`: при достатньо великому `n` асимптотика переважить будь-яку константу. Для рішень на конкретних розмірах вона не замінює вимірювання.

**Типові помилки:**
- вважати, що однакова Big O означає однакову латентність;
- вибирати алгоритм, не оцінивши реальний розмір `n`;
- пояснювати різницю ефектом кешу там, де домінують накладні витрати інтерпретатора.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
