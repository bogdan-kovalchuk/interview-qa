---
id: emb-fund-0023
title: "Як підходити до написання простого Linux kernel driver для character device або platform device?"
description: "Для character device визначають file operations, а для platform driver реалізують probe/remove, працюють з devicetree, MMIO та IRQ."
track: embedded
section: fundamentals
level: senior
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

Для character device визначають file operations: <code>open</code>, <code>read</code>, <code>write</code>, <code>ioctl</code>, плюс registration і lifetime cleanup.<br>Для platform driver реалізують <code>probe</code>/<code>remove</code>, беруть resources з devicetree, маплять MMIO, реєструють IRQ і exposed interface.<br><span class="warn">У kernel driver не можна мислити як у user space: інші allocation rules, locking, sleep context і error handling.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
