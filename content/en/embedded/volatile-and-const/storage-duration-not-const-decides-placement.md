---
id: emb-volconst-0027
title: "Trap: does a local `const` array always live in Flash?"
description: "No; const forbids writes through the identifier, but storage placement depends on storage duration, ABI, optimization, and the linker script."
track: embedded
section: volatile-and-const
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

<span class="warn">No, not always.</span>

`const` forbids writes through that identifier, but storage placement depends on storage duration, ABI, optimization, and the linker script. A local automatic `const` object may end up on the stack or be optimized into immediate constants. File-scope or `static const` objects are far more likely to land in `.rodata`.

Fix: for large embedded LUTs, use `static const` or file-scope `const` and check the map file.[^embeddedinterviewlab]

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
