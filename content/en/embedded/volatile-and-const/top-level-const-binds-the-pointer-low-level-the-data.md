---
id: emb-volconst-0040
title: "What are top-level and low-level `const` in a pointer type?"
description: "Top-level const qualifies the pointer object itself; low-level const qualifies the pointed-to data."
track: embedded
section: volatile-and-const
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

**Top-level `const` qualifies the pointer object itself; low-level `const` qualifies the pointed-to data.**

In `int * const p`, the top-level const means `p` cannot be reassigned. In `const int *p`, the low-level const means `*p` cannot be modified through `p`. For an API, low-level const matters more because it describes what the function does with the caller's data.

Rule: `const` after `*` protects the pointer; `const` before the base type protects the data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
