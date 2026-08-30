---
id: emb-dtypes-0035
title: "Де буде рядковий літерал `\"Hello, World!\"` у пам'яті embedded програми?"
description: "Рядкові літерали компілятор кладе у .rodata у Flash, тож вони не займають RAM."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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

У секції **.rodata** у Flash. Компілятор поміщає рядкові літерали у read-only секцію - вони не займають RAM.

Однаковий рядок використовується лише один раз (deduplication залежить від компілятора).

<span class="warn">Виняток</span>: `char arr[] = "hello";` - компілятор ініціалізує масив значеннями рядка, а масив (локальний/static) розміщується у stack / `.data` відповідно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
