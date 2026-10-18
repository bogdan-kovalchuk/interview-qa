---
id: emb-cemb-0006
title: "What is the size of a union?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The size of a `union` equals the size of its largest field plus possible padding to satisfy the strictest alignment requirement among the fields.[^dou-embedded-interview] That is, a union must be large enough and properly aligned for any of its members.

For example, `union U { char c[5]; float f; };` may have size 8: the largest field takes 5 bytes, but `float` requires alignment of 4, so padding is added. The exact value is always checked with `sizeof(union U)`.

## Detailed explanation

TODO
