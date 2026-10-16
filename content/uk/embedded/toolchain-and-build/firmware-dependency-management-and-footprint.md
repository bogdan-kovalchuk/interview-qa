---
id: emb-build-0020
title: "Як керувати залежностями у C/C++ firmware без випадкового підтягування непортативного або heap-heavy коду?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Фіксуй версії залежностей, перевіряй licenses, supported toolchains, heap/RTTI/exceptions usage і footprint у map file. Краще явно додавати маленькі libraries з known configuration, ніж тягнути generic package з прихованими POSIX, filesystem або allocation assumptions. **Dependency review** для MCU має включати RAM/flash cost і behavior у ISR/RTOS context.[^dou-embedded-interview]

## Detailed explanation

TODO
