---
id: emb-align-0017
title: "How do you write `swap16` to reverse the byte order?"
description: "Shift the high byte down and the low byte up then combine them with bitwise OR"
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
static inline uint16_t swap16(uint16_t v) {
  return (v << 8) | (v >> 8);
}
```

## Short answer

**The high byte is shifted down, the low byte – up, and they are combined with `|`.**

For `0xAABB` -> `0xBBAA`. GCC/Clang recognize this pattern and generate a single `REV16` instruction on ARM.

Rule: write byte-swap in readable C – inline asm is usually not needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
