---
id: emb-memlink-0012
title: "Як працює malloc на рівні heap allocator і чому динамічна пам'ять ризикована на MCU?"
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

`malloc` бере блок із heap, веде metadata й шукає вільний chunk достатнього розміру; `free` повертає блок allocator-у. На MCU heap малий, allocator може бути недетермінований за часом і створювати fragmentation. <span class="warn">У long-running firmware це ризик failure у runtime</span>, тому часто використовують static buffers, pools або arena allocator.[^dou-embedded-interview]

## Detailed explanation

TODO
