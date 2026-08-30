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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

<span class="key">Function pointer</span> – вказівник що зберігає адресу функції у .text (Flash).<br><br>Синтаксис: <code>void (*fp)(uint8_t) = &amp;send_byte;</code>.<br><br>Застосування у embedded:<br>• <span class="key">HAL callbacks</span>: <code>HAL_UART_RegisterCallback(huart, id, fp)</code>;<br>• <span class="key">RTOS task</span>: <code>xTaskCreate(task_fn, ...)</code>;<br>• <span class="key">Bootloader</span>: <code>void (*jump)(void) = (void(*)(void))app_addr; jump();</code>;<br>• <span class="key">State machine</span>: таблиця функцій-обробників станів. Це типові embedded-випадки використання.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
