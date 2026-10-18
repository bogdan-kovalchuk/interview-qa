---
id: emb-cppfound-0064
title: "Що таке pointer to function у embedded і де він застосовується?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
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
