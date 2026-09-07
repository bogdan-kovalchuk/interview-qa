---
id: emb-volconst-0061
title: "How does `const` help the compiler catch mistakes?"
description: "const turns an accidental write into a compile-time error when the access goes through a const-qualified type."
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

**`const` turns an accidental write into a compile-time error** when the access goes through a const-qualified type.

For example, a parser with a `const uint8_t *frame` parameter cannot accidentally modify the input packet. This is especially important when the input can be in Flash, in a shared communication buffer, or in a memory region with MPU read-only permissions.

Rule: const-correctness is cheaper than debugging accidental side effects in a driver or protocol stack.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
