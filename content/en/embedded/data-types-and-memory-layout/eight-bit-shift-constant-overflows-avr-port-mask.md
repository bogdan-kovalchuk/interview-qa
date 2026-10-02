---
id: emb-dtypes-0081
title: "What's wrong on an 8-bit AVR MCU? `if(!(PORTA & (1<<8)))`"
description: "18 = 256 does not fit the 8-bit PORTA, so the mask always evaluates to 0 and the condition is always true."
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
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
    title: "AVR-LibC 2.1.0 FAQ: Data types"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual-2.1.0/FAQ.html
    accessed: 2026-10-04
    kind: official
    version: "2.1.0"
    applicability: "Confirms type sizes in a typical avr-gcc configuration; -mint8 changes them and is unsupported by avr-libc."
---

## Short answer

In ordinary avr-gcc, `int` is 16 bits, so `1 << 8` is valid and evaluates to `0x0100`; the result itself does not overflow. That mask does not correspond to any bit in an 8-bit `PORTA` register.

After integer promotions, the byte value of `PORTA` is converted to `int`; its upper byte is zero, so `PORTA & 0x0100` is zero.

The condition is <span class="warn">always true</span> regardless of the PORTA state.

To test the port's most significant bit, use `if (!(PORTA & (1u << 7)))`; the actual register and available bits depend on the MCU model.[^avr-libc-faq-types] [^iso-c-n1570]

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
