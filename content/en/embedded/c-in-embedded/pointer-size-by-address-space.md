---
id: emb-cemb-0027
title: "How many bytes of memory does a pointer occupy?"
description: "A pointer's size is determined by the architecture's address space: typically 2 bytes for 16-bit, 4 for 32-bit, and 8 for 64-bit systems."
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
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

It depends on the processor architecture: **16-bit** -> 2 bytes, **32-bit** -> 4 bytes, **64-bit** -> 8 bytes. The pointer type does not matter: `char *`, `int *`, `struct Foo *` – all occupy the same number of bytes. In embedded (ARM Cortex-M) it is always 4 bytes. To check: `sizeof(void *)`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
