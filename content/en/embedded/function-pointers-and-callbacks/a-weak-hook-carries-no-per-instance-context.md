---
id: emb-fnptr-0053
title: "Trap: why are weak hooks worse than an explicit callback for several driver instances?"
description: "A weak function has one global name and carries no per-instance context."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "GCC current documentation"
    applicability: "Describes GNU weak attribute and override support on supported ELF/a.out toolchains; this is a compiler extension, not an ISO C guarantee."
---

## Short answer

<span class="warn">A weak hook does not carry per-instance context by itself.</span>[^gcc-weak-attribute]

If there are two UARTs or two timers, a function with one global name does not identify which instance owns the event. A weak override is also selected at link time rather than registered separately for each device.[^gcc-weak-attribute]

For reusable drivers, pass the callback and context separately; reserve weak hooks for global startup defaults or board-level extension points.

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
