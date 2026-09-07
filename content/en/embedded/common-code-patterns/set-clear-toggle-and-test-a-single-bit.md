---
id: emb-patterns-0014
title: "What do the four basic bit operations look like?"
description: "Set uses OR, clear uses AND with inverted mask, toggle uses XOR, test uses AND."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
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
#define BIT32(n) (UINT32_C(1) << (n))
```

## Short answer

**Set / Clear / Toggle / Test:**

```c
reg |=  BIT32(n);   // set
reg &= ~BIT32(n);   // clear
reg ^=  BIT32(n);   // toggle
if (reg & BIT32(n)) { ... } // test
```

Set is OR, clear is AND with the inverted mask, toggle is XOR, test is AND.

Rule: these four idioms are the foundation of register and flag configuration; for 32-bit registers use a 32-bit unsigned literal.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
