---
id: emb-cemb-0043
title: "Як параметри передаються у функцію за EABI на ARM Cortex-M?"
description: "За ARM EABI прості integer і pointer аргументи зазвичай ідуть у r0–r3, а додаткові або великі aggregate objects – через stack."
track: embedded
section: c-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

За ARM EABI/AAPCS перші прості integer/pointer аргументи зазвичай передаються в `r0-r3`, результат – у `r0` або `r0:r1`. Додаткові аргументи та частина великих aggregate objects ідуть через stack з потрібним alignment. Registers `r4-r11` є callee-saved, а `r0-r3,r12,lr` caller-saved у звичайному calling convention.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
