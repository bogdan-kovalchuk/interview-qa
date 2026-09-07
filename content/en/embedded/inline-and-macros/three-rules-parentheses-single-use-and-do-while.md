---
id: emb-macros-0006
title: "What are the three rules of a safe function-like macro?"
description: "Parentheses around parameters and the whole expression plus do-while-zero wrapping eliminate most classic macro bugs."
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

1. **Parentheses around every use of a parameter**: `(x)`;
2. **Parentheses around the whole expression**: `((x) + (y))`;
3. **Wrap a statement macro in `do { ... } while(0)`** so it behaves correctly with `if/else` and requires a `;`.

Rule: these three points eliminate most classic macro bugs – precedence, truncated expressions and broken control flow.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
