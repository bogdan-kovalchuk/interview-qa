---
id: emb-cemb-0036
title: "What is a bit-field in C, and why is it risky for MMIO registers or protocols?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

A **bit-field** is a struct field with a specified number of bits, for example `unsigned mode:3`. Its bit order, allocation unit, padding, and even the signedness of some forms depend on the implementation. <span class="warn">This is dangerous for MMIO and wire protocols</span>: it is better to use masks/shifts over `uint32_t`.[^dou-embedded-interview]

## Detailed explanation

TODO
