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

## Question code

```c
volatile const uint32_t * const STATUS =
    (volatile const uint32_t *)0x40020008;

*STATUS = 0;
```

## Short answer

<span class="warn">No. This must be a compile error</span>, because `*STATUS` has a const-qualified type.

`volatile` does not cancel `const`: it only says that reads must not be cached or removed, while `const` says that through this lvalue the firmware must not write data.

Fix: declare read-only registers as `volatile const`; if a vendor header allows a write into a read-only register, that is a weak type contract.[^embeddedinterviewlab]

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
