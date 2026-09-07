---
id: emb-align-0005
title: "How do you reorder the fields to remove the extra padding?"
description: "Sort fields from largest alignment to smallest to eliminate internal padding"
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
struct { uint8_t a; uint32_t b; uint8_t c; };
```

## Short answer

Sort from largest alignment to smallest:

```c
struct {
  uint32_t b; // @0
  uint8_t  a; // @4
  uint8_t  c; // @5, +2 tail
};
```

Now `sizeof = 8` instead of 12: small fields are grouped together, no internal padding.

Rule: "largest alignment first" is a simple and safe way to save RAM/Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
