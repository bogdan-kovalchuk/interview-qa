---
id: emb-volconst-0016
title: "What does `const uint8_t *buf` mean in a function parameter?"
description: "The function receives a pointer to const uint8t: it can move the pointer but cannot change the buffer bytes through it."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

**The function receives a pointer to const `uint8_t`**: it can move the pointer, but it cannot change the buffer bytes through `buf`.

For example, `void uart_write(const uint8_t *buf, size_t len)` documents that the passed buffer will only be read. This allows passing both a mutable RAM buffer and a read-only flash table.

Rule: if the function does not modify the pointed-to data, the parameter must be `const T *`. This supports const-correctness and follows the MISRA approach.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
