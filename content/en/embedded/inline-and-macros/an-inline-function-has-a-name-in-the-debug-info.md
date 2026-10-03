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
  - source_id: gdb-inline-functions
    title: "GDB: Inline Functions"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Inline-Functions.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GDB behavior for inline frames when suitable debug info is present; support depends on compiler, format and optimization."
---

## Short answer

**A debugger can show an inline function as a logical frame** when the compiler emits compatible debug info. This can expose arguments and allow stepping even when no separate machine call exists. A macro is expanded before compilation and has no distinct call frame; breakpoints for inline code depend on optimization and the actual debug configuration.[^gdb-inline-functions]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
