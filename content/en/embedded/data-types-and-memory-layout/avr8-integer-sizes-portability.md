---
id: emb-dtypes-0102
title: "What are integer type sizes on AVR8, and why should assumptions from 32-bit MCUs not be carried over?"
description: "On typical AVR8, int is 16 bits, while on a 32-bit MCU it is usually 32 bits, so portable firmware should use fixed-width types."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: avr-libc-faq-types
    title: "AVR-LibC User Manual: Frequently Asked Questions"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual-2.1.0/FAQ.html
    accessed: 2026-10-04
    kind: official
    version: "2.1.0"
    applicability: "Typical type sizes specifically for avr-gcc/AVR-LibC; pointer size depends on address space and target."
---

## Short answer

With ordinary avr-gcc for AVR8, `char` is 8 bits, `int` is 16 bits, and `long` is 32 bits; this describes that toolchain/target, not every 8-bit MCU.[^avr-libc-faq-types] On typical 32-bit MCUs, `int` is often 32 bits, but its exact size is set by the ABI, so arithmetic ranges and structure layouts can differ. <span class="warn">For fields that require an exact width, use `uint8_t`, `uint16_t`, or `uint32_t` from `stdint.h`; match `printf` formats to the type.</span>[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
