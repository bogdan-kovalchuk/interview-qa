---
id: emb-fnptr-0056
title: "Why do function pointers affect optimisation?"
description: "An indirect call is harder to optimise than a direct call."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: gcc-indirect-calls
    title: "GCC manual: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GCC optimisations for indirect calls and their conditions; it does not guarantee identical capabilities in other compilers."
---

## Short answer

**An indirect call is harder to optimise than a direct call.**

The compiler may not know the exact callee, so it usually cannot inline the call or perform optimisations that depend on the specific body. Analysis of visible values and LTO can sometimes identify a target and transform the call, but this depends on the program and toolchain.[^gcc-indirect-calls]

Embedded conclusion: function pointers give flexibility, but an indirect call can have extra cost; in hot paths inspect generated assembly and measurements.[^gcc-indirect-calls]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
