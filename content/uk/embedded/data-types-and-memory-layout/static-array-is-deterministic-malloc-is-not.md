---
id: emb-dtypes-0092
title: "Яка різниця між `malloc` і статичним масивом для буфера у embedded?"
description: "Статичний масив детермінований і без фрагментації, а malloc недетермінований і небезпечний у ISR."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

**Статичний масив** (`static uint8_t buf[256]`): відомий при компіляції, у `.bss`/`.data`, детермінований доступ, no fragmentation.

**malloc(256)**: runtime виділення, недетермінований час, heap fragmentation, може повернути NULL (треба перевіряти), небезпечний у ISR.

У safety-critical embedded (MISRA, IEC 61508): <span class="warn">static allocation обов'язковий</span>. `malloc` тільки при ініціалізації - і тільки до real-time частини виконання.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
