---
id: emb-patterns-0017
title: "How do you write a multi-bit field without disturbing the other bits?"
description: "First clear the field bits then insert the new shifted and masked value"
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
reg = (reg & ~PRESC_MASK)
    | ((value << PRESC_SHIFT) & PRESC_MASK);
```

## Short answer

**First clear the field bits (`& ~MASK`), then insert the new value (shifted and masked).**

Masking `value` with `& MASK` guards against overflow into adjacent bits if `value` is too large.

Rule: writing a register field is always clear + set, otherwise you corrupt neighboring settings.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
