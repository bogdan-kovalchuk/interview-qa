---
id: emb-macros-0032
title: "What does `__attribute__((always_inline))` do and when is it needed?"
description: "Forces the compiler to inline a function even when its heuristics would choose a regular call."
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
  - source_id: gcc-always-inline
    title: "GCC: Common Function Attributes – always_inline"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "GNU C always_inline function attribute behavior; not a C standard guarantee or a guarantee for other compilers."
---

## Short answer

**For a direct call GCC requires inlining**, diagnosing a failure if it cannot do so; an indirect call has no equivalent guarantee. This is a GNU extension, not a C standard requirement.[^gcc-always-inline]

In embedded code it is sometimes used for a measured critical path, but size and speed must be checked on the target; the opposite GCC extension is `__attribute__((noinline))`. The C keyword `inline` alone also does not require body substitution.[^iso-c-n1570] [^gcc-always-inline]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
