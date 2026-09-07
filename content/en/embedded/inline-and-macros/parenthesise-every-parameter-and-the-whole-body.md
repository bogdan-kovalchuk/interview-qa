---
id: emb-macros-0003
title: "What does a correct function-like `MAX` macro look like and why is every parenthesis needed?"
description: "Parentheses around every parameter and around the whole expression protect against operator precedence problems after substitution."
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

## Short answer

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

Parentheses around every parameter and around the whole expression protect against operator precedence problems after substitution.

Without them, an expression like `MAX(x & 1, y)` or `MAX(a, b) * 2` can expand with the wrong order of operations.

Rule: always write a function-like macro using the `((param)...)` pattern – parameters in parentheses, result in parentheses.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
