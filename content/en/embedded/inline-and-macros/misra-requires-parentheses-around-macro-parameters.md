---
id: emb-macros-0020
title: "What does MISRA C Rule 20.7 require and why?"
description: "MISRA C Rule 20.7 requires parenthesizing macro parameters in expressions to prevent operator precedence bugs after expansion."
track: embedded
section: inline-and-macros
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

## Short answer

**MISRA C (Motor Industry Software Reliability Association C) Rule 20.7 requires parenthesizing macro parameters that participate in expressions** to avoid operator precedence errors after expansion.

That is, `#define ADD(a,b) a+b` is dangerous; the correct form is `#define ADD(a,b) ((a) + (b))`. This eliminates bugs like `ADD(1,2) * 3`, where without parentheses you get `1 + 2 * 3`.

Rule 20.7 does not make macros desirable; together with Rule 4.9 it pushes toward replacing function-like macros with `static inline` where possible.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
