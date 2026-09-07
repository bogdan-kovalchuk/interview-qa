---
id: emb-align-0018
title: "How do you write `swap32` for a 32-bit byte swap?"
description: "Each byte is moved to its mirror position using shifts and masks and the compiler folds it into one REV instruction"
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

## Short answer

```c
static inline uint32_t swap32(uint32_t v) {
  return ((v >> 24) & 0xFF)
       | ((v >>  8) & 0xFF00)
       | ((v <<  8) & 0xFF0000)
       | ((v << 24) & 0xFF000000);
}
```

Each byte moves to its mirror position; masks cut off the extras.

Rule: GCC/Clang fold this into a single `REV` instruction on ARM – fast and portable.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
