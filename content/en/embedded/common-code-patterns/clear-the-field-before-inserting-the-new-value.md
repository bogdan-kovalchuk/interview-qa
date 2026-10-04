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
reg = (reg & ~PRESC_MASK)
    | ((value << PRESC_SHIFT) & PRESC_MASK);
```

## Short answer

**First clear the field bits (`& ~MASK`), then insert the new value (shifted and masked).**

Masking the shifted value limits the result to the field bits only when the shift itself is valid; check `value` before shifting.[^iso-c-n1570]

Clear the old field bits before inserting the new value so neighboring settings are preserved.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
