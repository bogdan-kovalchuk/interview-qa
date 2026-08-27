---
id: py-coll-0020
title: "Що означає stability сортування Python і як використати її для multi-key sorting без custom comparator?"
description: "Stability означає, що елементи з однаковим key зберігають початковий відносний порядок; це дозволяє сортувати за кількома keys послідовно, від менш значущого до більш значущого."
track: python
section: collections
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Stability означає, що елементи з однаковим key зберігають початковий відносний порядок; це дозволяє сортувати за кількома keys послідовно, від менш значущого до більш значущого.**[^py314-library-stdtypes] Наприклад, щоб сортувати за спаданням `grade` і зростанням `age`: спочатку `sorted(data, key=age)`, потім `sorted(result, key=grade, reverse=True)`. Stability гарантує, що порядок за `age` збережеться для однакових `grade`. Альтернатива для одного напрямку – tuple key: `key=itemgetter(grade, age)`.

## Detailed explanation

Стабільність – це властивість конкретного алгоритму сортування, а не абстрактна гарантія самого
поняття "сортування": `sorted()` і `list.sort()` в CPython реалізовані через Timsort, гібридний
merge sort, який під час злиття двох відсортованих прогонів (runs) завжди бере елемент з лівого
прогону, якщо ключі рівні, і ніколи не переставляє місцями елементи з однаковим ключем.[^py314-howto-sorting]
Саме ця властивість алгоритму, а не документація мови, робить трюк з послідовним сортуванням
коректним.

Доказ коректності послідовного підходу спирається на індукцію: після сортування за найменш значущим
ключем елементи впорядковані за ним. Наступне сортування за важливішим ключем групує елементи за
новим ключем, але оскільки воно стабільне, всередині кожної групи з однаковим новим ключем порядок,
встановлений попереднім сортуванням, не порушується. Повторюючи це від найменш значущого ключа до
найбільш значущого, отримуємо коректний multi-key порядок без написання власного comparator.

Цей трюк особливо корисний, коли різні ключі потребують протилежних напрямків сортування (один – за
зростанням, інший – за спаданням), бо tuple-key підхід (`key=itemgetter(a, b)`) сортує обидва поля
в одному напрямку, заданому одним `reverse`. Для числових полів напрямок можна інвертувати заміною
ключа на `-value`, але для рядкових полів такого прямого трюка немає – і саме тут послідовні виклики
`sorted()` з окремим `reverse` для кожного ключа виграють у tuple-key підходу.

Обмеження підходу: він вимагає стільки проходів, скільки ключів, тобто O(k * n log n) замість
одного O(n log n) для tuple-key варіанта – прийнятно для невеликої кількості ключів, але не для
великої.[^py314-library-stdtypes]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
