---
id: emb-align-0004
title: "What `sizeof` will this have on a 32-bit MCU?"
description: "12 bytes due to internal and trailing padding for natural alignment of each field"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
typedef struct {
  uint8_t  flags;
  uint32_t timestamp;
  uint8_t  sensor_id;
} bad_t;
```

## Short answer

**12 bytes.**

Layout: `flags`@0 (1B) -> <span class="warn">3B padding</span> -> `timestamp`@4 (4B) -> `sensor_id`@8 (1B) -> <span class="warn">3B trailing padding</span> (so the size is a multiple of 4).

Fix: reorder fields from largest alignment to smallest – then it becomes 8 bytes.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
