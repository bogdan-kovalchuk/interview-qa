---
id: emb-macros-0045
title: "Why are compiler errors inside a macro hard to read?"
description: "The compiler reports errors at the expanded call site rather than at the #define line, and nested macros make it worse."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

**The error points to the expanded code, not to the `#define` line.**

The compiler sees the already-substituted text at the call site, so diagnostics refer there; nested macros multiply the effect. This is a classic reason why complex logic should not be hidden in a macro.

Fix: use `gcc -E` to see the actual expansion; for logic that will need debugging, choose `static inline`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
