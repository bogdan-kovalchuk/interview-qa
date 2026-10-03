---
id: emb-volconst-0037
title: "Why can a read-modify-write on a volatile register be unsafe?"
description: "The read-modify-write operation is not atomic: it reads the register, modifies in the CPU, then writes back."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: stm32-bsrr
    title: "STMicroelectronics STM32L1 reference manual, GPIO bitwise handling"
    url: https://www.st.com/resource/en/reference_manual/cd00240193.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0038"
    applicability: "Describes BSRR atomic set/reset for GPIO ODR on STM32L1 specifically; other MCUs and registers may behave differently."
---

## Question code

```c
GPIOA_ODR |= (1u << pin);
```

## Short answer

The operation is <span class="warn">not atomic</span>: it reads, modifies in the CPU, then writes back.

If hardware or an ISR changes bits between the read and write, the final write can overwrite them. For example, STM32 GPIO has BSRR, which changes selected ODR bits with one write; this is a property of that specific peripheral, not every register.[^stm32-bsrr]

Protection: use documented set/clear registers where available; otherwise protect the RMW from concurrent access, for example with a critical section for an ISR. `volatile` does not make the sequence atomic.[^stm32-bsrr]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
