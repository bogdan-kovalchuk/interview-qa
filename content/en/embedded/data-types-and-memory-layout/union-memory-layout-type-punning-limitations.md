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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

In a **union**, all members start at the same offset, and the size and alignment are determined by the largest member. Writing to one member overwrites the same bytes that can be read through another member, but the access rules depend on the C/C++ standard, effective type, and compiler behavior. <span class="warn">For portable byte interpretation in firmware, prefer `memcpy`</span> over relying on union type punning.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
