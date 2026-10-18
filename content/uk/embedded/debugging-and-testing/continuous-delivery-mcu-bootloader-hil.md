---
id: emb-build-0025
title: "Як забезпечити Continuous Delivery для MCU, якщо пристрій має фізичний target, bootloader і hardware-in-the-loop тести?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

CD pipeline має збирати signed artifacts, прошивати device через bootloader/debug probe, запускати smoke/HIL tests і збирати logs/trace. Потрібні керовані test rigs: power cycling, serial logs, reset control, version readback і failure recovery. **Release gate** має перевіряти не лише build, а й update path, rollback і базову роботу hardware.[^dou-embedded-interview]

## Detailed explanation

TODO
