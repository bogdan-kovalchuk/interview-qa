---
id: emb-dtypes-0101
title: "What is EABI, and why does ABI matter when mixing object files, libraries, and compiler flags?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-aapcs32
    title: "Arm ABI: Procedure Call Standard for the Arm Architecture"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
---

## Short answer

**EABI** is an ABI for embedded environments; a specific ABI family defines object format, calls, and data passing. For Arm, for example, AAPCS32 specifies function arguments, register preservation, and floating-point argument variants.[^arm-aapcs32] Soft-float and hard-float can use incompatible calling conventions, so the linker or runtime may detect a mismatch when such modules are combined.[^arm-aapcs32] Modules need compatible external contracts, not necessarily identical local compiler options.

## Detailed explanation

TODO
