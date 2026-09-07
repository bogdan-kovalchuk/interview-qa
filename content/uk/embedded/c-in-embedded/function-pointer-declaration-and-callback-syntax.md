---
id: emb-cppfound-0023
title: "Що таке function pointer і який синтаксис його оголошення?"
description: "How to declare and call a function pointer."
track: embedded
section: c-in-embedded
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Function pointer** – вказівник на функцію: зберігає адресу коду функції для виклику через нього.

Синтаксис: `return_type (*name)(param_types);` Приклад: `void (*isr)(void) = &my_handler;`

Виклик: `(*isr)();` або просто `isr();` (обидва коректні).

Застосування у embedded: ISR dispatch tables, state machine transitions, RTOS task functions, callback API (`HAL_UART_RegisterCallback`).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
