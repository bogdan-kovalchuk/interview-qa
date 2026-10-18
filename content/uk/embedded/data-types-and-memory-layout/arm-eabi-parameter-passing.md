---
id: emb-cemb-0043
title: "Як параметри передаються у функцію за EABI на ARM Cortex-M?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

За ARM EABI/AAPCS перші прості integer/pointer аргументи зазвичай передаються в `r0-r3`, результат – у `r0` або `r0:r1`. Додаткові аргументи та частина великих aggregate objects ідуть через stack з потрібним alignment. Registers `r4-r11` є callee-saved, а `r0-r3,r12,lr` caller-saved у звичайному calling convention.[^dou-embedded-interview]

## Detailed explanation

TODO
