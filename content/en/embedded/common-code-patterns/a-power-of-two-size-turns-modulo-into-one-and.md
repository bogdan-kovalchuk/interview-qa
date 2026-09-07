---
id: emb-patterns-0012
title: "Why is a ring buffer sized to a power of two?"
description: "A power-of-two size replaces modulo with a single AND instruction, avoiding expensive division."
track: embedded
section: common-code-patterns
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

## Question code

```c
#define RB_SIZE 64
#define RB_MASK (RB_SIZE - 1)
```

## Short answer

**`(index + 1) & MASK` is a single AND instruction, whereas `(index + 1) % SIZE` requires division.**

Cortex-M0 has no hardware divider, so modulo is <span class="warn">10–20 times slower</span>. A power of two allows replacing `%` with a bit mask.

Rule: ring buffer size is a power of 2, wrap via `& (SIZE-1)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
