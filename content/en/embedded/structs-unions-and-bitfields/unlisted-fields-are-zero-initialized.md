---
id: emb-structs-0030
title: "What happens to the fields that are not listed?"
description: "The parity and stopbits fields will be zero-initialized."
track: embedded
section: structs-unions-and-bitfields
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
struct Cfg {
    uint32_t baud;
    uint8_t parity;
    uint8_t stop_bits;
};

struct Cfg c = { .baud = 115200 };
```

## Short answer

**`parity` and `stop_bits` will be zero-initialized.**

Aggregate initialization in C zero-fills fields that were not explicitly initialized. This is convenient for config structs where `0` is a valid default.

Rule: designated initializers reduce the risk of mixing up positional fields, but the default zero must be semantically correct. If `0` is dangerous, a factory/default function is needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
