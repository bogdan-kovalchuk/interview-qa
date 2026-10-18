---
id: emb-debug-0001
title: "How do you debug firmware on a real MCU using SWD/JTAG, breakpoints, watchpoints, and trace?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

Connect a probe via SWD/JTAG, load the ELF with symbols, and verify the reset/halt sequence. Breakpoints stop in code, watchpoints catch read/write of a specific address, and trace/SWO/ETM shows events without brute-force printf. For ISR/DMA bugs, combine the debugger with a logic analyzer and avoid stopping timing-sensitive code unless necessary.[^dou-embedded-interview]

## Detailed explanation

TODO
