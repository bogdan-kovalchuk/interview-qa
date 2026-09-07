---
id: emb-irq-0002
title: "Що таке watchdog?"
description: "Watchdog Timer скидає мікроконтролер, якщо програма регулярно не «годує» його, захищаючи від зависання і нескінченних циклів."
track: embedded
section: interrupts-and-timing
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Авторитетне джерело рівня секції для понять розділу interrupts-and-timing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Watchdog Timer (WDT)** – апаратний таймер, що автоматично скидає (reset) мікроконтролер, якщо програма не «погодувала» його вчасно.[^dou-embedded-interview]

Принцип: програма повинна регулярно записувати спеціальне значення в регістр WDT («kick» або «feed»). Якщо цього не відбулося – таймер спрацьовує і виконується system reset.

Захищає від: зависання програми, нескінченного циклу, stack overflow. Типи: **IWDG** (independent, від окремого генератора, не зупиняється при зупинці основного тактування) і **WWDG** (window watchdog – скидати треба лише у певному часовому вікні, захист від «годування занадто часто»).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
