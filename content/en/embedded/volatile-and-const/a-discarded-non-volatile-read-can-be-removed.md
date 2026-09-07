---
id: emb-volconst-0036
title: "Trap: what is wrong with reading a register and discarding the result?"
description: "If the macro is not volatile, the compiler can remove that read."
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
#define ADC_DR (*( uint32_t *)0x4001204C)

ADC_DR;
```

## Short answer

<span class="warn">If the macro is not volatile, the compiler can remove that read.</span>

For a data register, a read may clear a hardware flag or pull a sample from a FIFO. But for a plain `uint32_t`, an expression statement that discards the result has no observable effect, so the optimizer is free to remove it.

Protection: a register macro must be `(*(volatile uint32_t *)address)`. If the read is intentionally discarded, an explicit `(void)ADC_DR` cast is sometimes added for readability.[^embeddedinterviewlab]

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
