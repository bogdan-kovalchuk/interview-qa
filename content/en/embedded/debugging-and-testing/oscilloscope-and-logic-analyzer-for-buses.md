---
id: emb-debug-0003
title: "How do you use an oscilloscope or logic analyzer to check UART, SPI, I2C, and timing issues?"
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

Use an oscilloscope to check voltage levels, edges, ringing, rise/fall time, clock, and reset/power timing. A logic analyzer decodes UART/SPI/I2C frames, showing baud/clock, ACK/NACK, CS timing, and gaps between bytes. Best practice is to trigger on the problem event and simultaneously watch a firmware GPIO marker to link the code path with the signal.[^dou-embedded-interview]

## Detailed explanation

TODO
