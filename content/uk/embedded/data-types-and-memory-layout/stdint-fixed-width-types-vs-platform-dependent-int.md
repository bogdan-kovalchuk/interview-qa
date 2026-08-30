---
id: emb-dtypes-0009
title: "Навіщо використовують `stdint.h` типи замість стандартних `int`, `short`, `long`?"
description: "stdint.h типи гарантують точний розмір незалежно від платформи, на відміну від int/short/long."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Розміри `int`, `short`, `long` залежать від платформи та ABI: `int` - 2 байти на MSP430, 4 байти на Cortex-M.

`<stdint.h>` гарантує точний розмір: `uint8_t` - завжди 8 біт, `uint32_t` - завжди 32 біти.

У embedded: register maps, протоколи, struct layout - **завжди fixed-width типи**. "For anything stored in a struct, sent over a protocol, or written to a register - use fixed-width types."[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
