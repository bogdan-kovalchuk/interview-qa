---
id: emb-volconst-0004
title: "Trap: чи робить `volatile` операцію атомарною?"
description: "Ні. volatile не гарантує atomicity."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

Ні. `volatile` не гарантує atomicity.

Він лише змушує компілятор виконати доступ до пам'яті. Наприклад, `volatile uint32_t` на 8-bit MCU може читатися кількома інструкціями; ISR може спрацювати між байтами і побачити частково оновлене значення. Навіть на Cortex-M операція `counter++` є read-modify-write, а не одна неподільна дія.

Захист: для shared state використовуй atomic operations, critical section, вимкнення interrupts на короткий час або спеціальні CMSIS/RTOS primitives.[^embeddedinterviewlab]

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
