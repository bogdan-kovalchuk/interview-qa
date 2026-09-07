---
id: emb-fund-0007
title: "Що таке алгоритми сортування та які знаєте?"
description: "Алгоритми сортування впорядковують елементи за ключем; bubble/insertion прості й O(n²), merge/quick/heap sort зазвичай O(n log n)."
track: embedded
section: fundamentals
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Алгоритм сортування впорядковує елементи за ключем: за зростанням, спаданням або власним компаратором.[^dou-embedded-interview] Важливі характеристики: складність за часом, додаткова пам'ять, стабільність і поведінка на майже відсортованих даних.

Приклади: `bubble sort` і `insertion sort` прості, але зазвичай O(n²); insertion sort хороший для малих масивів. `merge sort` стабільний і O(n log n), але потребує пам'яті. `quick sort` швидкий на практиці, середньо O(n log n), але worst case O(n²). `heap sort` має O(n log n) і працює in-place.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
