---
id: emb-macros-0007
title: "What is an `inline` function and why is it better than a function-like macro?"
description: "An inline function is a real function the compiler can expand at the call site while preserving type checking and scope."
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

**`inline`** is a real function that the compiler can expand at the call site, removing the call overhead.

Unlike a macro, it preserves type checking and scope, evaluates its arguments exactly once and is visible to the debugger (breakpoints, step-into). The compiler itself decides whether to inline or emit a regular call.

Rule: anything that looks like a function, make it `inline`/`static inline`, not a function-like macro.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
