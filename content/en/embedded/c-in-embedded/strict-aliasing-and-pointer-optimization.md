---
id: emb-cppfound-0054
title: "What is pointer aliasing, and how does it affect optimization?"
description: "How strict aliasing affects pointer-based optimization."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

**Pointer aliasing** – a situation where two pointers of different types point to the same memory area.

Strict aliasing rule (C99 §6.5): the compiler may assume that pointers of different types do not alias (except for `char*`/`unsigned char*`). This allows more aggressive optimization.

Violation: `int x; float *fp = (float*)&x; *fp = 1.0f;` -> undefined behavior.

Protection: `memcpy` for type punning, `char*` for byte access, `restrict` for an explicit no-aliasing guarantee.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
