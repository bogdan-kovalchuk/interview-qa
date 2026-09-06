---
id: emb-volconst-0001
title: "Що означає кваліфікатор `volatile` у C?"
description: "volatile означає, що значення об'єкта може змінитися поза видимим потоком виконання програми: апаратурою, ISR, DMA або іншим асинхронним механізмом."
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

**`volatile`** означає, що значення об'єкта може змінитися поза видимим потоком виконання програми: апаратурою, ISR, DMA або іншим асинхронним механізмом.

Компілятор повинен виконувати реальний доступ до такого об'єкта при кожному читанні або записі, а не тримати значення лише в регістрі CPU. Для Cortex-M це критично для memory-mapped registers: читання адреси може повертати стан периферії, а запис може запускати апаратну дію.

Правило: `volatile` ставиться не "для надійності", а тільки коли об'єкт реально може змінюватися поза контролем звичайного C-коду.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
