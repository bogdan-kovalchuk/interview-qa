---
id: emb-dtypes-0044
title: "Що таке stack canary і як він захищає від stack overflow?"
description: "Stack canary - магічне значення перед адресою повернення, чия зміна при виході з функції виявляє переповнення стека."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Stack canary - **магічне значення** (часто рандомне або `0xDEADBEEF`), що записується між stack frame і критичними даними (адресою повернення) при вході у функцію.

При виході: якщо canary змінився -> відбувся stack overflow -> виклик `__stack_chk_fail()`.

GCC: `-fstack-protector-strong`. У bare-metal: заповнюй стек патерном у startup, перевіряй у watchdog/idle task через `arm_cmse_nonsecure_caller()` або вручну.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
