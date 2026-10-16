---
id: emb-volconst-0012
title: "What does `volatile uint32_t * const reg` mean?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`reg` is a const pointer to volatile `uint32_t`**.

The pointer address cannot be changed: `reg = other` violates a language constraint and requires a diagnostic. The data at that address has type `volatile uint32_t`, so accesses to it follow the volatile rules of the implementation. This is a typical type for a fixed address of a writable hardware register.[^iso-c-n1570]

Embedded use case: the address of a GPIO output register is constant, while the register contents can change by hardware or by firmware writes.[^embeddedinterviewlab]

## Detailed explanation

TODO
