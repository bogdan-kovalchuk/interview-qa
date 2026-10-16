---
id: emb-memlink-0016
title: "Що таке linker script і які помилки в ньому можуть зламати firmware startup?"
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

**Linker script** описує Flash/RAM regions, entry point, sections, vector table і symbols для startup. Типові помилки: неправильна адреса vector table, overlap `.data/.bss/heap/stack`, неекспортовані `_sidata/_sdata/_edata/_sbss/_ebss`, невірний RAM origin/length. <span class="warn">Такі помилки часто виглядають як reset loop або HardFault до main</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
