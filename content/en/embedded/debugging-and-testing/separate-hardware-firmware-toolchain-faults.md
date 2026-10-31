---
id: emb-debug-0002
title: "How do you distinguish a hardware fault, firmware bug, and toolchain or configuration issue while debugging a board?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
  - source_id: gcc-optimize-options
    title: "GCC manual: Options That Control Optimization"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
  - source_id: ld-options
    title: "GNU ld manual: Command-line Options"
    url: https://sourceware.org/binutils/docs/ld/Options.html
---

## Short answer

First check power, clocks, reset, boot pins, and signal levels with an oscilloscope or logic analyzer. Then minimize the firmware to a known-good test: blink, UART, single peripheral, no RTOS/DMA. If the symptom depends on optimization, linker script, startup, or wrong flags, it looks like toolchain/config; if it repeats with minimal code and is visible on signals, it is a hardware/power issue.[^dou-embedded-interview]

## Detailed explanation

TODO
