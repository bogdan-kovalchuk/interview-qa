---
id: emb-cemb-0029
title: "Why is structure alignment needed in C, and how does it affect memory layout?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Alignment** forces structure fields to start at addresses that are multiples of their type's or ABI's requirements. The compiler may insert padding between fields and at the end of the structure, so the actual layout does not always equal the sum of field sizes.[^dou-embedded-interview] For DMA, MMIO mirror structures, and binary protocols this is critical: the layout must be fixed explicitly or serialized manually.

## Detailed explanation

TODO
