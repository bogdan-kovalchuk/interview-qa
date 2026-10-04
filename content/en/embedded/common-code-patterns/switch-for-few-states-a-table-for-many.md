---
id: emb-patterns-0029
title: "When do you choose enum plus switch and when a function-pointer table for an FSM?"
description: "enum+switch for few states with debug simplicity and warnings on missing cases"
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 4
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
  - source_id: gcc-warning-options
    title: "GCC 16.1.0: Warning Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
    accessed: 2026-10-04
    kind: official
    version: "16.1.0"
    applicability: "Documents -Wswitch and -Wswitch-enum for omitted enum cases; makes no performance guarantee for switches or tables."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**enum+switch** is convenient when transitions are clearer explicitly; a compiler can warn about omitted `enum` cases when the relevant warning option is enabled.[^gcc-warning-options]

Function-pointer table can reduce repetitive dispatch code, but does not by itself guarantee `O(1)` or better speed; validate the index.

Choose based on readability and measurements on the target platform, not a fixed state count.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
