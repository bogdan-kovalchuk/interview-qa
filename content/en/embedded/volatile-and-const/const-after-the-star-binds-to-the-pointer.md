---
id: emb-volconst-0020
title: "How do you read the declaration `int * const p`?"
description: "p is a const pointer to int; the address cannot change but the pointed-to value can be modified if not const."
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

## Short answer

**`p` is a const pointer to `int`**.

`p = &other` is forbidden, but `*p = 5` is allowed if the object is not const. This is often confused with `const int *p`, where const applies to the data, not the address.

Embedded example: a pointer to a fixed RAM cell or writable register address that must not change after initialization.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
