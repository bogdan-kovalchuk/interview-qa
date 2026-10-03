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

## Short answer

**`inline`** is a real function that the compiler may expand at the call site; the keyword does not guarantee this transformation.[^iso-c-n1570]

Unlike a macro, it preserves type checking and scope and evaluates an argument once for a function call. The compiler decides whether to inline it or emit a regular call.[^iso-c-n1570]

Rule: anything that looks like a function, make it `inline`/`static inline`, not a function-like macro.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
