---
id: emb-fund-0010
title: "Що таке MMU і чим MCU без MMU відрізняється від Embedded Linux системи?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**MMU** транслює virtual addresses у physical addresses і забезпечує page permissions/isolation. Більшість bare-metal MCU не має MMU: код працює в одному address space, без process isolation і demand paging. Embedded Linux зазвичай потребує MMU для processes, virtual memory, mmap і захисту kernel/user space.[^dou-embedded-interview]

## Detailed explanation

TODO
