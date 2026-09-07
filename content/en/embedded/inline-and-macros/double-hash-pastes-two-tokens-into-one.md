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
#define REG(periph, r) periph##_##r
// REG(GPIOA, ODR) -> GPIOA_ODR
```

## Short answer

**`##` joins two tokens into one** at the preprocessing stage: `GPIOA` + `_` + `ODR` -> the identifier `GPIOA_ODR`.

Used to generate register names, wrapper functions, unique identifiers and X-macro patterns.

Rule: the result of pasting must be a valid token; otherwise it is a preprocessor error.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
