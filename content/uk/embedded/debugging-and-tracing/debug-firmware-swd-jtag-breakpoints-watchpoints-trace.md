---
id: emb-debug-0001
title: "Як налагоджувати firmware на реальному MCU через SWD/JTAG, breakpoints, watchpoints і trace?"
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

Підключити probe через SWD/JTAG, завантажити ELF із symbols і перевірити reset/halt sequence. Breakpoints ставлять зупинки в code, watchpoints ловлять read/write конкретної адреси, а trace/SWO/ETM показує події без грубого printf. Для ISR/DMA bugs краще комбінувати debugger з logic analyzer і не зупиняти timing-sensitive code без потреби.[^dou-embedded-interview]

## Detailed explanation

TODO
