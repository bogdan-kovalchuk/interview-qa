---
id: emb-rtos-0006
title: "Що таке spinlock?"
description: "Spinlock – примітив синхронізації, у якому потік активно крутиться в циклі, чекаючи lock, замість того щоб засинати; не можна спати, тримаючи його."
track: embedded
section: rtos
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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
---

## Short answer

**Spinlock** – примітив синхронізації, при якому потік, що не може отримати lock, **крутиться (spin) у циклі**, постійно перевіряючи доступність, замість того щоб засипати.[^dou-embedded-interview]

Перевага: низька латентність, якщо очікування дуже коротке. У kernel-space spinlock використовують там, де sleep заборонений; залежно від типу lock і контексту він може вимикати preemption або IRQ. У user-space spinlock – це просто busy waiting primitive.

Правило: <span class="warn">не можна спати, тримаючи spinlock</span>. Якщо критична секція довга або код може блокуватися – краще mutex.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
