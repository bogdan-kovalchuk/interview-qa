---
id: emb-patterns-0024
title: "Why must peripheral registers be `volatile`?"
description: "The status register is changed by hardware asynchronously not by code"
track: embedded
section: common-code-patterns
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
  - source_id: linux-volatile-mmio
    title: "The Linux kernel documentation: Why the volatile type class should not be used"
    url: https://docs.kernel.org/next/process/volatile-considered-harmful.html
    accessed: 2026-10-04
    kind: official
    version: "next documentation"
    applicability: "Explains volatile's limits and Linux kernel use of I/O accessors; it is not a specification for an individual MCU."
---

## Short answer

**The status register is changed by hardware asynchronously, not by code.**

`volatile` tells the compiler that accesses to the object are observable and must be preserved under the C abstract machine, but it does not guarantee physical RAM access, atomicity, or MCU transaction ordering.[^iso-c-n1570] Without it, repeated reads of an ordinary object may be optimized even when a device changes the corresponding location.

For ordinary memory-mapped registers, volatile access is a typical part of the compiler contract, but accessors and any extra barriers are platform-specific.[^linux-volatile-mmio]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
