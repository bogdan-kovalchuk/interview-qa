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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

On typical AVR-GCC for AVR8: `char` is 8 bits, `int` is 16 bits, `long` is 32 bits, pointer is often 16 bits for the data address space. On a 32-bit MCU, `int` is usually 32 bits, so overflow, printf format, and struct layout can change. <span class="warn">In portable firmware, prefer `stdint.h`: `uint8_t`, `uint16_t`, `uint32_t`</span>.[^dou-embedded-interview]

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
