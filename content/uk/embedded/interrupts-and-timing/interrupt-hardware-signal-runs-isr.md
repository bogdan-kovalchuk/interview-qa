---
id: emb-irq-0003
title: "Що таке переривання?"
description: "Переривання – апаратний чи програмний сигнал, що змушує CPU призупинити код і виконати ISR, зберігши й потім відновивши контекст."
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

**Переривання (Interrupt)** – апаратний або програмний сигнал, що змушує CPU призупинити виконання поточного коду і виконати спеціальну функцію – **ISR (Interrupt Service Routine)**.[^dou-embedded-interview]

Послідовність: подія, потім контролер переривань (NVIC), потім CPU зберігає контекст (PC, регістри), потім виконує ISR, потім відновлює контекст і повертається до основного коду.

Правила ISR: коротка та швидка; не використовувати блокуючих функцій; спільні змінні – `volatile`; можливо потрібні критичні секції (disable/enable IRQ для атомарного доступу).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
