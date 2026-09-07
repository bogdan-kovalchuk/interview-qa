---
id: emb-volconst-0013
title: "What does `volatile const uint32_t * const STATUS` mean?"
description: "STATUS is a const pointer to volatile const uint32t; the address is fixed, data is read-only yet must be reloaded each time."
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

**`STATUS` is a const pointer to volatile const `uint32_t`**.

The pointer address does not change. The data at the address cannot be written through this type, but it must be reloaded every time because hardware can change the status bits. This is the classic type for a read-only status register.

Rule: `const` guards against firmware writes, `volatile` guards against caching the hardware value.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
