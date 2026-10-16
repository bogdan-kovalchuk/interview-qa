---
id: emb-dtypes-0102
title: "What are integer type sizes on AVR8, and why should assumptions from 32-bit MCUs not be carried over?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: avr-libc-faq-types
    title: "AVR-LibC User Manual: Frequently Asked Questions"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual-2.1.0/FAQ.html
---

## Short answer

With ordinary avr-gcc for AVR8, `char` is 8 bits, `int` is 16 bits, and `long` is 32 bits; this describes that toolchain/target, not every 8-bit MCU.[^avr-libc-faq-types] On typical 32-bit MCUs, `int` is often 32 bits, but its exact size is set by the ABI, so arithmetic ranges and structure layouts can differ. <span class="warn">For fields that require an exact width, use `uint8_t`, `uint16_t`, or `uint32_t` from `stdint.h`; match `printf` formats to the type.</span>[^iso-c-n1570]

## Detailed explanation

TODO
