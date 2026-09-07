---
id: emb-volconst-0060
title: "Чому `volatile` не треба ставити на всі змінні \"про всяк випадок\"?"
description: "Надмірний volatile погіршує оптимізацію і може маскувати неправильну модель синхронізації."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Надмірний `volatile` погіршує оптимізацію і може маскувати неправильну модель синхронізації.</span>

Компілятор змушений частіше ходити в пам'ять, не тримати значення в регістрах і обмежувати reorder. Це збільшує код, час виконання і енергоспоживання. При цьому race conditions, atomicity і ordering для non-volatile data воно не лікує.

Правило: використовуй `volatile` як точний контракт для hardware/ISR/DMA observable state, а не як загальне "антиоптимізаційне" заклинання.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
