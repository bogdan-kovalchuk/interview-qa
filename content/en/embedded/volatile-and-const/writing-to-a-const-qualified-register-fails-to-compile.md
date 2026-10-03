---
id: emb-volconst-0015
title: "Trap: can you write to a register declared like this?"
description: "No; writing must be a compile error because STATUS has a const-qualified type, and volatile does not cancel const."
track: embedded
section: volatile-and-const
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
---

## Question code

```c
volatile const uint32_t * const STATUS =
    (volatile const uint32_t *)0x40020008;

*STATUS = 0;
```

## Short answer

<span class="warn">No. This violates a C language constraint, so the implementation must issue a diagnostic</span>, because `*STATUS` has a const-qualified type.[^iso-c-n1570]

`volatile` does not cancel `const`: it qualifies access to the object, while `const` prohibits modifying it through this lvalue.[^iso-c-n1570]

Fix: declare read-only registers as `volatile const` when that matches the MCU documentation. The standard requires a diagnostic, but the compiler may continue translation after issuing it.[^iso-c-n1570]

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
