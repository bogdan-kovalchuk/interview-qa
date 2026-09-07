---
id: emb-align-0009
title: "Що робить `__attribute__((packed))` і чим це небезпечно?"
description: "Прибирає padding – поля кладуться впритул, а розмір наближається до суми полів."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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

**Прибирає padding** – поля кладуться впритул, а розмір наближається до суми полів.

<span class="warn">Ризик</span>: багатобайтове поле може опинитися за невирівняною адресою. На Cortex-M0 прямий доступ до такого поля може дати HardFault; на M3/M4 компілятор часто генерує <span class="warn">побайтові load/store</span>, які повільніші.

Правило: `packed` – для wire-форматів і заголовків протоколів. Для MMIO (memory-mapped I/O) register maps зазвичай краще природно вирівняна `volatile`-структура з явними reserved fields, щоб не отримати неправильну ширину доступу до регістрів.[^embeddedinterviewlab]

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
