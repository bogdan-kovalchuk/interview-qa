---
id: emb-irq-0003
title: "Що таке переривання?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

**Переривання (Interrupt)** – апаратний або програмний сигнал, що змушує CPU призупинити виконання поточного коду і виконати спеціальну функцію – **ISR (Interrupt Service Routine)**.[^dou-embedded-interview]

Послідовність: подія, потім контролер переривань (NVIC), потім CPU зберігає контекст (PC, регістри), потім виконує ISR, потім відновлює контекст і повертається до основного коду.

Правила ISR: коротка та швидка; не використовувати блокуючих функцій; спільні змінні – `volatile`; можливо потрібні критичні секції (disable/enable IRQ для атомарного доступу).

## Detailed explanation

TODO
