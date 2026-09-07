---
id: emb-cppfound-0064
title: "Що таке pointer to function у embedded і де він застосовується?"
description: "Function pointers store code addresses and support callbacks, bootloaders, and state machines."
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

**Function pointer** – вказівник що зберігає адресу функції у .text (Flash).

Синтаксис: `void (*fp)(uint8_t) = &send_byte;`.

Застосування у embedded:
- **HAL callbacks**: `HAL_UART_RegisterCallback(huart, id, fp)`;
- **RTOS task**: `xTaskCreate(task_fn, ...)`;
- **Bootloader**: `void (*jump)(void) = (void(*)(void))app_addr; jump();`;
- **State machine**: таблиця функцій-обробників станів. Це типові embedded-випадки використання.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
