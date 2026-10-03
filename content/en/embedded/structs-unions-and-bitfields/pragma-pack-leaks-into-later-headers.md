---
id: emb-structs-0047
title: "Trap: what is wrong with `#pragma pack` in a public header used carelessly?"
description: "A packing pragma can change packing for subsequent structs in other code."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
  - source_id: gcc-structure-layout-pragmas
    title: "GCC documentation: Structure-Layout Pragmas"
    url: https://gcc.gnu.org/onlinedocs/gcc/Structure-Layout-Pragmas.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GCC's effect on alignment of subsequent struct/union declarations and pack(push)/pack(pop); other compilers may differ."
---

## Short answer

<span class="warn">It can change packing for subsequent structs in other code.</span>

In GCC, `#pragma pack(n)` affects the alignment of subsequent `struct` and `union` declarations; if the prior state is not restored, it can change types declared later in the same translation unit.[^gcc-structure-layout-pragmas]

Surround the required type with `#pragma pack(push, 1)` and `#pragma pack(pop)`, check support in the target compiler, and assert expected `sizeof` and field offsets.[^gcc-structure-layout-pragmas]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
