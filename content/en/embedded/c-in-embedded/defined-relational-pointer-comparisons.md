---
id: emb-cppfound-0059
title: "Can pointers be compared with `<` and `>`, and when is this defined behavior?"
description: "When relational pointer comparisons are defined."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

Comparisons `==` and `!=` are always **defined** between any two pointers of the same type.

Comparisons `<`, `>`, `<=`, `>=` are **defined only** if both pointers point to the **same array** (or struct). Comparing pointers to different objects -> <span class="warn">undefined behavior per the standard</span>.

In practice: most platforms give a correct answer even for different objects, but do not rely on this in portable code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
