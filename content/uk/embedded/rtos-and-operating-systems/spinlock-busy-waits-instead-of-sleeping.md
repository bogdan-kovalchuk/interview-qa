---
id: emb-rtos-0006
title: "Що таке spinlock?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**Spinlock** – примітив синхронізації, при якому потік, що не може отримати lock, **крутиться (spin) у циклі**, постійно перевіряючи доступність, замість того щоб засипати.[^dou-embedded-interview]

Перевага: низька латентність, якщо очікування дуже коротке. У kernel-space spinlock використовують там, де sleep заборонений; залежно від типу lock і контексту він може вимикати preemption або IRQ. У user-space spinlock – це просто busy waiting primitive.

Правило: <span class="warn">не можна спати, тримаючи spinlock</span>; Якщо критична секція довга або код може блокуватися – краще mutex.

## Detailed explanation

TODO
