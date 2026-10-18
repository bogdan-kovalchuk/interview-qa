---
id: emb-irq-0002
title: "Що таке watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

**Watchdog Timer (WDT)** – апаратний таймер, що автоматично скидає (reset) мікроконтролер, якщо програма не «погодувала» його вчасно.[^dou-embedded-interview]

Принцип: програма повинна регулярно записувати спеціальне значення в регістр WDT («kick» або «feed»). Якщо цього не відбулося – таймер спрацьовує і виконується system reset.

Захищає від: зависання програми, нескінченного циклу, stack overflow. Типи: **IWDG** (independent, від окремого генератора, не зупиняється при зупинці основного тактування) і **WWDG** (window watchdog – скидати треба лише у певному часовому вікні, захист від «годування занадто часто»).

## Detailed explanation

TODO
