---
id: emb-cppfound-0044
title: "Why is `volatile` needed when accessing hardware registers through a pointer?"
description: "How volatile affects compiler access to hardware registers."
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

Without `volatile`, the compiler may:
1. <span class="warn">Cache</span> the register value in a CPU register and not re-read it (missing a hardware change);
2. <span class="warn">Remove "unnecessary" writes</span> (dead store elimination) – if the value is not read later;
3. <span class="warn">Reorder</span> operations for optimization.

With `volatile`: every read/write is actually performed in the order written.

Pattern: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
