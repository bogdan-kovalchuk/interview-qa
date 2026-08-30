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

За ARM EABI/AAPCS перші прості integer/pointer аргументи зазвичай передаються в <code>r0-r3</code>, результат – у <code>r0</code> або <code>r0:r1</code>. Додаткові аргументи та частина великих aggregate objects ідуть через stack з потрібним alignment. Registers <code>r4-r11</code> є callee-saved, а <code>r0-r3,r12,lr</code> caller-saved у звичайному calling convention.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
