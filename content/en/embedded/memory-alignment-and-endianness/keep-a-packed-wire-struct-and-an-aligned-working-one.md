---
id: emb-align-0010
title: "What is the recommended pattern for working with a packed wire format?"
description: "Keep a packed struct for the wire and a separate aligned struct for processing, copying field by field"
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

**Keep two structs: packed for the wire and a regular aligned one for processing.**

```c
typedef struct {
  uint32_t ts; uint16_t val; uint8_t id;
} __attribute__((packed)) wire_t;

typedef struct {
  uint32_t ts; uint16_t val; uint8_t id;
} reading_t; // aligned
```

Copy from packed to aligned (field by field) and work with the aligned copy.

Rule: do not access packed-struct fields directly in hot code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
