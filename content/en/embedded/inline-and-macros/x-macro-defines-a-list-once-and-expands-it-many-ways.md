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

**An X-macro is a list defined once that is expanded in different contexts**.

The classic task: keeping `enum` and a string/handler table in sync. The list of elements is described through a macro `X(...)`, and then `X` is defined differently each time to generate an enum, a name array, a switch, and so on.

Adding a new element to a single list automatically updates all generated entities – <span class="warn">impossible to forget</span> to update a pair.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
