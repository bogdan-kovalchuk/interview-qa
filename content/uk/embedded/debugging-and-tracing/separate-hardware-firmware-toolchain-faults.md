---
id: emb-debug-0002
title: "Як відрізнити hardware fault, firmware bug і toolchain/configuration issue під час debug на платі?"
track: embedded
section: debugging-and-tracing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

Спершу перевірити power, clocks, reset, boot pins і signal levels осцилографом або logic analyzer. Потім мінімізувати firmware до known-good test: blink, UART, single peripheral, без RTOS/DMA. Якщо симптом залежить від optimization, linker script, startup або wrong flags, це схоже на toolchain/config; якщо повторюється при мінімальному коді й видно на сигналах – hardware/power issue.[^dou-embedded-interview]

## Detailed explanation

TODO
