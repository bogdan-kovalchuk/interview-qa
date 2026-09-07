---
id: emb-cemb-0028
title: "What bitwise operations exist?"
description: "Bitwise AND, OR, XOR, NOT, and shifts are used to test, set, clear, and toggle bits in registers."
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

`&` AND – clear a bit: `reg &= ~(1<<n)` `|` OR – set a bit: `reg |= (1<<n)` `^` XOR – toggle: `reg ^= (1<<n)` `~` NOT – bitwise inversion `<<` left shift: `x << 3` = x × 8 `>>` right shift: `x >> 1` = x / 2.

Typical patterns in Embedded: Test a bit: `if (reg & (1<<n))` Set: `reg |= (1<<n)` Clear: `reg &= ~(1<<n)` Toggle: `reg ^= (1<<n)`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
