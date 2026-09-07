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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
GPIOA_ODR |= (1u << pin);
```

## Short answer

The operation is <span class="warn">not atomic</span>: it reads the register, modifies in the CPU, then writes back.

If hardware or an ISR changes other bits between the read and the write, the final write can overwrite those changes. On Cortex-M, GPIO ports often have set/reset registers such as BSRR in STM32, which allow atomically setting or clearing bits without RMW.

Protection: for hardware registers, use atomic set/clear registers, bit-banding where available, or a critical section if RMW is unavoidable.[^embeddedinterviewlab]

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
