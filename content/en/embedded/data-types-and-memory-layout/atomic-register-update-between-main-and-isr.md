---
id: emb-dtypes-0104
title: "How do you ensure an atomic register update when both main code and an ISR modify one register?"
description: "Use a peripheral set/clear register when provided; otherwise protect the full critical section from the relevant ISR."
track: embedded
section: data-types-and-memory-layout
level: senior
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
  - source_id: stm32g0-gpio-bsrr
    title: "STMicroelectronics STM32G0x0 Reference Manual, GPIO bit set/reset register"
    url: https://www.st.com/resource/en/reference_manual/dm00463896-stm32g0x0-advanced-armbased-32bit-mcus-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0454 Rev 5"
    applicability: "Describes atomic bit manipulation through BSRR on STM32G0x0 specifically; other peripherals and MCUs can have different rules."
---

## Short answer

Prefer a peripheral set/clear register when its documentation guarantees that a write changes only the selected bits: for example, STM32G0 `GPIOx_BSRR` atomically changes the corresponding `GPIOx_ODR` bits.[^stm32g0-gpio-bsrr] Otherwise, on a single-core system, protect the read-modify-write with a critical section that temporarily masks the interrupt competing for that register. <span class="warn">`volatile` and an ordinary atomic primitive do not make an arbitrary peripheral read-modify-write safe.</span>[^iso-c-n1570]

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
