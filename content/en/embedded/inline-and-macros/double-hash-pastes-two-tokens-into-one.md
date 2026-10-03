---
id: emb-macros-0013
title: "What does the token pasting operator `##` do?"
description: "The ## operator joins two tokens into one at the preprocessing stage to generate register names and identifiers."
track: embedded
section: inline-and-macros
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
#define REG(periph, r) periph##_##r
// REG(GPIOA, ODR) -> GPIOA_ODR
```

## Short answer

**`##` pastes adjacent tokens** in a macro replacement list: here `GPIOA`, `_` and `ODR` form the identifier `GPIOA_ODR`.

Arguments next to `##` are substituted without expanding any macros they contain first; an extra level is needed for that.

The pasted result must form one valid preprocessing token; otherwise the program violates a language constraint.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
