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
  - source_id: openocd-arch-commands
    title: "OpenOCD User's Guide: Architecture and Core Commands"
    url: https://openocd.org/doc/html/Architecture-and-Core-Commands.html
  - source_id: openocd-general-commands
    title: "OpenOCD User's Guide: General Commands"
    url: https://openocd.org/doc/html/General-Commands.html
  - source_id: openocd-reset-config
    title: "OpenOCD User's Guide: Reset Configuration"
    url: https://openocd.org/doc/html/Reset-Configuration.html
  - source_id: cmsis-itm
    title: "CMSIS-Core: ITM Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__ITM__Debug__gr.html
---

## Short answer

Connect a probe via SWD/JTAG, load the ELF with symbols, and verify the reset/halt sequence. Breakpoints stop in code, watchpoints catch read/write of a specific address, and trace/SWO/ETM shows events without brute-force printf. For ISR/DMA bugs, combine the debugger with a logic analyzer and avoid stopping timing-sensitive code unless necessary.[^dou-embedded-interview]

## Detailed explanation

TODO
