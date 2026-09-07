---
id: emb-macros-0026
title: "Trap: is it true that a macro is always faster than a function?"
description: "No, the claim that a macro is always faster than a function is an outdated myth."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

<span class="warn">No – this is an outdated myth.</span>

Modern compilers inline small `static inline` functions the same way a macro expands, and additionally apply constant folding, dead-code elimination, and other optimizations unavailable to already-substituted preprocessor text.

Protection: at an interview do not say 'a macro is faster'; say '`static inline` gives the same speed plus type safety and single evaluation of arguments'.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
