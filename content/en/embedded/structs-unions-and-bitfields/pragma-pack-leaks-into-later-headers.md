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

<span class="warn">It can change packing for subsequent structs in other code.</span>

If a header enables packing and does not restore the previous state, it breaks the layout of unrelated structs, the ABI, and alignment. This is especially nasty in embedded, where one header can affect driver structs or RTOS control blocks.

Mitigation: use push/pop pragmas or local attributes, minimize the scope of packing, and verify layout with static assertions.[^embeddedinterviewlab]

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
