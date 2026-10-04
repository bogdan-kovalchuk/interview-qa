---
id: emb-macros-0021
title: "What is an X-macro and which problem does it solve?"
description: "An X-macro is a single list expanded in multiple contexts to keep related definitions in sync."
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
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains macro substitution underlying the X-macro technique; the technique example is illustrative."
---

## Short answer

**An X-macro is a list defined once that is expanded in different contexts**.

The classic task is keeping an `enum` and a string or handler table in sync. The elements are listed as `X(...)` calls, then `X` is defined differently at each expansion site to generate an enum, a name array, a switch, and so on.

Adding an element to the single list updates each generated location, provided each location uses that list.[^gcc-cpp-overview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
