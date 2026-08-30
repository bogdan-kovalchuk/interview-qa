---
id: emb-dtypes-0094
title: "Що таке tentative definition у C і де вона розміщується?"
description: "Оголошення глобальної без ініціалізатора і extern стає визначенням з нульовою ініціалізацією у .bss."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

**Tentative definition** - оголошення глобальної змінної без ініціалізатора і без `extern`: `int x;` у файловому scope.

За правилами C: якщо немає іншого визначення у цьому translation unit - автоматично стає визначенням з нульовою ініціалізацією -> розміщується у **.bss** або common-секції залежно від компілятора/прапорців.

Якщо у тому ж translation unit є `int x = 5;` - tentative definition об'єднується з цим визначенням. Якщо `int x;` покласти у header і включити в кілька `.c` файлів, сучасний GCC з `-fno-common` дасть multiple definition. Для зовнішньої змінної у header треба `extern int x;`.

<span class="warn">У C++ немає tentative definitions</span> - кожне оголошення або `extern` або визначення (ODR).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
