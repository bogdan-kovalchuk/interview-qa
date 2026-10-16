---
id: emb-cemb-0016
title: "Tell me about bitfields."
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

**Bitfields** are struct fields with an explicit bit width: `struct Flags { unsigned ready:1; unsigned mode:3; };`.[^dou-embedded-interview] They compactly store flags or describe parts of a register or status word.

Limitations: a bitfield has no address, and packing order, signedness and padding are often implementation-defined, so the layout differs between compilers and ABIs. For hardware registers and protocols, masks and shifts on `uint32_t` are usually more reliable; use bitfields only where the layout is controlled and verified.

## Detailed explanation

TODO
