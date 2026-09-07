---
id: emb-volconst-0035
title: "Is reading a volatile object a side effect?"
description: "Yes, a volatile access is considered an observable side effect for the C abstract machine."
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

**Yes, a volatile access is considered an observable side effect for the C abstract machine.**

Therefore, the compiler cannot simply discard a hardware register read as an "unused result" if the read itself can clear a flag, acknowledge an interrupt, or trigger a bus transaction. This is one reason why register definitions must be volatile.

Embedded rule: if a read-to-clear or read-has-side-effect register is described without `volatile`, the optimizer can break the peripheral protocol.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
