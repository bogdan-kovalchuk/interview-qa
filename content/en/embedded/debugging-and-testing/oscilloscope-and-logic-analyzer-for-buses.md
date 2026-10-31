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
  - source_id: ti-slva704-i2c
    title: "TI SLVA704: Understanding the I2C Bus"
    url: https://www.ti.com/lit/an/slva704/slva704.pdf
  - source_id: ti-slva689-i2c-pullup
    title: "TI SLVA689: I2C Bus Pullup Resistor Calculation"
    url: https://www.ti.com/lit/an/slva689/slva689.pdf
  - source_id: linux-spi-summary
    title: "Linux kernel documentation: Overview of Linux kernel SPI support"
    url: https://docs.kernel.org/spi/spi-summary.html
  - source_id: ti-sprugp1-uart
    title: "TI SPRUGP1: KeyStone Architecture Universal Asynchronous Receiver/Transmitter (UART) User Guide"
    url: https://www.ti.com/lit/ug/sprugp1/sprugp1.pdf
---

## Short answer

Use an oscilloscope to check voltage levels, edges, ringing, rise/fall time, clock, and reset/power timing. A logic analyzer decodes UART/SPI/I2C frames, showing baud/clock, ACK/NACK, CS timing, and gaps between bytes. Best practice is to trigger on the problem event and simultaneously watch a firmware GPIO marker to link the code path with the signal.[^dou-embedded-interview]

## Detailed explanation

TODO
