---
id: emb-volconst-0017
title: "What does `uint8_t * const buf` mean in a parameter or a local variable?"
description: "buf is a const pointer to mutable uint8t; the address cannot change but the bytes it points to can be modified."
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

**`buf` is a const pointer to mutable `uint8_t`**.

You cannot assign `buf = other`, but you can modify `buf[0]`. In a function parameter, top-level `const` on the pointer itself is rarely part of the API, because the parameter is already a copy of the pointer value.

Embedded use case: a local alias for a fixed address or register pointer that must not be accidentally reassigned.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
