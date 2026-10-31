---
id: emb-cemb-0010
title: "What is alignment in structs?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Alignment** places struct fields at addresses that are multiples of their alignment requirement.[^dou-embedded-interview] `uint32_t`, for example, often needs an address that is a multiple of 4, so the compiler inserts padding bytes to keep access fast and correct for the CPU.

This matters in embedded: misaligned access on some MCUs is slow or faults, and register or protocol layouts may require exact offsets. Reordering fields from largest to smallest shrinks the size, but for a binary protocol or hardware registers, serialize explicitly or verify the layout with `static_assert` and `offsetof`.

## Detailed explanation

TODO
