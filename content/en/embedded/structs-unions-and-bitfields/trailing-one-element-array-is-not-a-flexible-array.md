---
id: emb-structs-0034
title: "Trap: what is wrong with the old `uint8_t data[1]` pattern at the end of a struct?"
description: "It is a real 1-byte array, not a flexible array member, so sizeof includes that byte and padding."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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

<span class="warn">This is not a flexible array member but a real 1-byte array.</span>

`sizeof(struct)` includes that byte and any padding after it. Code that allocates `sizeof(struct) + len` may get an off-by-one layout or depend on a non-standard extension. Modern C has the standard `data[]` syntax.

Defence: for C99+ use a flexible array member `uint8_t data[];` and carefully compute the allocation size with overflow checks.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
