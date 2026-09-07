---
id: emb-volconst-0047
title: "What does `const volatile` mean for a memory-mapped device ID register?"
description: "Firmware must not write the register but must read it as a volatile hardware value."
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

**Firmware must not write the register, but must read it as a volatile hardware value.**

A device ID can be read-only from the CPU's perspective, but physically on the bus it is a hardware register, not an ordinary constant in Flash. Even if the value practically never changes, the type `const volatile` describes the correct ownership: hardware owns, firmware observes.

Rule: a read-only hardware register should not be described as just `const`, because the compiler may treat it as ordinary read-only data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
