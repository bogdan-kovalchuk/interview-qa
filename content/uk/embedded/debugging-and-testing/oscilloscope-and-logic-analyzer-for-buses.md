---
id: emb-debug-0003
title: "Як використовувати осцилограф або logic analyzer для перевірки UART/SPI/I2C і timing issues?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

Осцилографом перевірити рівні напруги, edges, ringing, rise/fall time, clock і reset/power timing. Logic analyzer декодує UART/SPI/I2C frames, показує baud/clock, ACK/NACK, CS timing і gaps між bytes. Найкраще міряти trigger-ом на problem event і одночасно дивитися firmware GPIO marker, щоб зв'язати code path із сигналом.[^dou-embedded-interview]

## Detailed explanation

TODO
