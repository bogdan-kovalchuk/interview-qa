---
id: emb-volconst-0014
title: "What is `volatile const` and what is it for?"
description: "volatile const describes an object the program must not modify but whose value can change without the program's involvement."
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

**`volatile const`** describes an object the program must not modify, but whose value can change without the program's involvement.

Typical example: a read-only status register. Firmware only reads; hardware updates the status bits. Without `volatile`, the compiler may reuse an old value; without `const`, the programmer may accidentally write to the read-only register.

Embedded rule: for hardware read-only registers, use a pointer to `volatile const` data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
