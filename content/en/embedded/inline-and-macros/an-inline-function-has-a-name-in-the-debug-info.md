---
id: emb-macros-0009
title: "Why is a `static inline` function easier to debug than a macro?"
description: "An inline function has a symbolic name and real debug info so it can be breakpointed, stepped into and seen in a backtrace."
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

**An inline function has a symbolic name and real code in the debug info**, so you can set a breakpoint on it, step into it and see it in a backtrace.

A macro is expanded before compilation, so the debugger sees only the inlined code at the call site. Error messages also point to the <span class="warn">expanded code, not the `#define` line</span>.

Rule: do not hide complex logic that you will need to debug inside a macro.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
