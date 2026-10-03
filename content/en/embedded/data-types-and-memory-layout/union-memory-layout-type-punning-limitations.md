---
id: emb-dtypes-0109
title: "How is union represented in memory and what limitations does type punning through union have?"
description: "In a union all members share the same offset and the size is determined by the largest member; for portable byte interpretation in firmware, prefer memcpy over union type punning."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: cpp-draft-union
    title: "C++ working draft: Unions"
    url: https://eel.is/c++draft/class.union
    accessed: 2026-10-04
    kind: spec
    version: null
    applicability: "Defines active union members and lifetime constraints in C++; it does not describe C rules."
---

## Short answer

In a **union**, all members start at the same offset, and storage is sized and aligned for its members according to the implementation. Writing one member makes it the active variant; reading another has different consequences under C and C++ rules, including effective type and lifetime.[^iso-c-n1570][^cpp-draft-union] <span class="warn">For portable byte interpretation, prefer `memcpy`</span> rather than assuming union type punning works identically in C and C++.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
