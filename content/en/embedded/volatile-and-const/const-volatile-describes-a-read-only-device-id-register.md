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

**`const volatile` forbids writes through this lvalue while retaining volatile access semantics.**

A device ID can be read-only from firmware's perspective, while its value is supplied by hardware. `const` and `volatile` describe different access properties; they do not guarantee physical immutability or specific device behaviour.[^iso-c-n1570]

Use `const volatile` for a memory-mapped register only when the MCU documentation defines it as read-only.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
