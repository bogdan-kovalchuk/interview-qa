---
id: emb-cemb-0003
title: "What pointer operations are there?"
description: "Pointer operations include address-of, dereference, field access, comparison, assignment, casting, and passing to functions; pointer arithmetic advances by sizeof the pointed-to type."
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

Main operations: take the address `&x`, dereference `*p`, access a field via `p->field`, compare with `NULL` or another pointer, assign an address, cast the type, pass to a function.[^dou-embedded-interview]

There is pointer arithmetic: `p + 1` advances not by 1 byte but by `sizeof(*p)` bytes. So for `int *p`, `p++` shifts by the size of `int`. Correct arithmetic is defined within a single array or one past its end; going out of bounds and dereferencing an invalid address is undefined behavior.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
