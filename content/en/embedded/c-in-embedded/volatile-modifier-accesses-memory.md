---
id: emb-cemb-0026
title: "Describe the use of the `volatile` qualifier."
description: "volatile makes the compiler perform accesses that may change outside the ordinary execution flow."
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

It prevents the compiler from caching a variable's value in a register or removing accesses as "dead" – every access performs a real read or write.[^dou-embedded-interview]

It is used when a value can change outside the ordinary execution flow:
- **Peripheral registers**: `volatile uint32_t *GPIOA = (uint32_t *)0x40020000;`
- **A variable modified by an ISR**: `volatile bool flag = false;`
- **Signal handler** or hardware status flag.

For threads, `volatile` by itself <span class="warn">is not synchronization</span>: it does not guarantee atomicity, ordering, or mutual exclusion. For that you need a `mutex`, critical section, or atomics.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
