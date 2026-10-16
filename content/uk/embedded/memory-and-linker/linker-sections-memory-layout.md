---
id: emb-memlink-0015
title: "Що робить linker і як він розміщує секції .text, .rodata, .data, .bss, stack і heap?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**Linker** вирішує symbols/relocations, підтягує потрібні objects з libraries і розміщує sections у memory regions. Зазвичай `.text`/`.rodata` ідуть у Flash, `.data` має load image у Flash і runtime address у RAM, `.bss` zero-init у RAM. Stack/heap межі задаються linker script або startup code, і помилка тут дає hard fault або corruption.[^dou-embedded-interview]

## Detailed explanation

TODO
