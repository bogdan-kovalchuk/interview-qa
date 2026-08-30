---
id: emb-dtypes-0090
title: "Що виведе на little-endian? `uint32_t x = 0xDEADBEEF; uint8_t *p = (uint8_t*)&x; printf(\"%02X\", p[0]);`"
description: "На little-endian молодший байт лежить за найменшою адресою, тож p[0] дає EF."
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

`EF`.

На little-endian (Cortex-M) LSB зберігається за найменшою адресою. `0xDEADBEEF` у пам'яті: `[EF][BE][AD][DE]`.

`p[0]` = перший байт за адресою `&x` = `0xEF` (LSB).
`p[1] = 0xBE`, `p[2] = 0xAD`, `p[3] = 0xDE` (MSB).

Доступ через byte pointer дозволений для character types (`unsigned char*`). На практиці `uint8_t` зазвичай є typedef до `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
