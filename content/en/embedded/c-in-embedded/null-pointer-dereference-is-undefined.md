---
id: emb-cppfound-0019
title: "What is a NULL pointer and what happens when it is dereferenced?"
description: "A guaranteed invalid address (0 or nullptr); dereferencing it is undefined behavior and on Cortex-M can corrupt the Vector Table."
track: embedded
section: c-in-embedded
level: junior
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

**NULL pointer** – a guaranteed invalid address (null pointer constant): `0` or `(void*)0` in C, `nullptr` in C++.

Dereferencing NULL -> <span class="warn">undefined behavior</span>. On Cortex-M: address `0x00000000` is the start of Flash (Vector Table). Writing there -> HardFault or Vector Table corruption.

Protection: always check before dereferencing: `if(p != NULL) *p = val;`; initialize: `int *p = NULL;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
