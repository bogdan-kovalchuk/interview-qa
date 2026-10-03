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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

If a function is intended only to read data, `const T *` expresses that restriction in its interface; by itself, this type does not make the object immutable through other available access paths.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
