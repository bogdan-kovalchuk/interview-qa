---
id: emb-dtypes-0002
title: "В яку секцію пам'яті потрапить? `const uint32_t FIRMWARE_VERSION = 0x0102;`"
description: "const глобальна змінна з ненульовим значенням потрапляє у .rodata і не займає RAM."
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

У секцію **.rodata** (read-only data) у Flash. Ця змінна **не займає RAM** - CPU читає значення безпосередньо з Flash.

Правило: `const` глобальна/static з ненульовим значенням -> `.rodata`. Це критично у embedded: оголошуй константи як `const`, щоб не витрачати RAM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
