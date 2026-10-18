---
id: emb-cppfound-0064
title: "What is a function pointer in embedded systems, and where is it used?"
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

**Function pointer** – a pointer that stores a function address in .text (Flash). Syntax: `void (*fp)(uint8_t) = &send_byte;`. Usage in embedded:
- **HAL callbacks**: `HAL_UART_RegisterCallback(huart, id, fp)`;
- **RTOS task**: `xTaskCreate(task_fn, ...)`;
- **Bootloader**: `void (*jump)(void) = (void(*)(void))app_addr; jump();`;
- **State machine**: a table of state handler functions. These are typical embedded use cases.[^embeddedinterviewlab]

## Detailed explanation

TODO
