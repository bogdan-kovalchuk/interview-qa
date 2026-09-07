---
id: emb-cppfound-0053
title: "What do `sizeof(\"hello\")` and `sizeof(char*)` return on 32-bit?"
description: "How sizeof treats a string literal and a pointer."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

`sizeof("hello")` -> **6**: a string literal is an array `{'h','e','l','l','o','\0'}`, and `sizeof` returns the array size including the null terminator.

`sizeof(char*)` -> **4**: the pointer size equals the platform word size.

Key point: `sizeof("hello")` does not decay to a pointer (sizeof is one of the three array decay exceptions), so we get the array size.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
