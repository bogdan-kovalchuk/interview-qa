---
id: emb-volconst-0026
title: "Which section does a mutable lookup table land in?"
description: "A mutable table lands in .data as initialized mutable global or static data, copied from Flash to RAM before main."
track: embedded
section: volatile-and-const
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
uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

Into `.data`: initialized mutable global/static data.

The initial values sit in Flash as a load image, but before `main()` the startup code copies them into RAM because the array can be modified. This costs both Flash and RAM, and boot copy time.

Fix: if the table does not change at runtime, make it `const` so it becomes a candidate for `.rodata` in Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
