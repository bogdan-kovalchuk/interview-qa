---
id: emb-volconst-0003
title: "Назви три обов'язкові use cases для `volatile` в embedded C."
description: "Три класичні use cases: memory-mapped hardware registers, змінні, спільні з ISR, і пам'ять, яку змінює DMA."
track: embedded
section: volatile-and-const
level: junior
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

Три класичні use cases: memory-mapped hardware registers, змінні, спільні з ISR, і пам'ять, яку змінює DMA.

У всіх трьох випадках компілятор не бачить звичайного C-запису, який змінює значення. Без `volatile` він може закешувати старе значення або прибрати доступ як redundant.

Правило: якщо джерело зміни значення не видно компілятору в поточному control flow, розглядай `volatile`; якщо проблема про взаємне виключення або atomicity, одного `volatile` недостатньо.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
