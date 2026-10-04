---
id: emb-macros-0019
title: "What does MISRA C Directive 4.9 recommend about function-like macros?"
description: "MISRA C Directive 4.9 recommends using a function instead of an interchangeable function-like macro."
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
  - source_id: misra-c2012-amd3-dir49
    title: "MISRA C:2012 Amendment 3"
    url: https://misra.org.uk/app/uploads/2022/12/MISRA-C-2012-AMD3.pdf
    accessed: 2026-10-04
    kind: spec
    version: "2012 Amendment 3"
    applicability: "Page 11 clarifies an exception to Directive 4.9 for function-like macros using _Generic; the full directive text is in the main MISRA C:2012 document."
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains the preprocessor's purpose and macro substitution before compilation; it is not MISRA guidance."
---

## Short answer

**MISRA C Directive 4.9 recommends a function over a function-like macro** where the two are interchangeable.

It is a directive with Required category, but it does not unconditionally prohibit macros; Amendment 3 clarifies an exception for macros using `_Generic`.[^misra-c2012-amd3-dir49]

In practice, check whether a function can provide the same behaviour; `static inline` may be an option, but the directive does not mandate that specific mechanism.[^misra-c2012-amd3-dir49]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
