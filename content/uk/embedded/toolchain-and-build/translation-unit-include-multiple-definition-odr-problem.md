---
id: emb-build-0015
title: "Що таке translation unit і чому include-файли можуть викликати multiple definition або ODR-проблеми?"
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

**Translation unit** – результат preprocessing одного `.c/.cpp` файлу разом з усіма included headers. Якщо header містить non-static object/function definition, вона потрапить у кожну translation unit і linker побачить multiple definitions. У C++ це також може порушити ODR; у headers лишають declarations, `inline`/`constexpr` або templates за правилами мови.[^dou-embedded-interview]

## Detailed explanation

TODO
