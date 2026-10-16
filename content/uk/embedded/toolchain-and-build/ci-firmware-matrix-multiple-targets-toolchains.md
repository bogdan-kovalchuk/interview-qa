---
id: emb-build-0022
title: "Як налаштувати CI для збірки firmware під кілька target-платформ і toolchains?"
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

CI має матрицю **target x toolchain x config**: наприклад GCC/Clang, debug/release, board variants. Кожна job ставить pinned toolchain, запускає configure/build, static analysis, unit tests і збирає artifacts: ELF, HEX/BIN, map, logs. Для target-only перевірок окремо підключають HIL runners або nightly hardware jobs.[^dou-embedded-interview]

## Detailed explanation

TODO
