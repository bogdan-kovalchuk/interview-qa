---
id: emb-structs-0042
title: "What does `alignas`/`_Alignas` or a compiler-specific alignment attribute do?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-draft-dcl-align
    title: "C++ working draft: Alignment specifier [dcl.align]"
    url: https://eel.is/c++draft/dcl.align
---

## Short answer

**Sets or strengthens the alignment requirement of a declared object**; applying it to a type itself depends on the language or a compiler-specific extension.

In embedded, this is needed for DMA buffers, cache line alignment, vector tables, or peripheral requirements. For example, a DMA descriptor may require 16-byte alignment; cache maintenance on Cortex-M7 often operates on cache lines.

Rule: alignment is part of the hardware contract. Check the address at runtime or compile time and describe the requirement in the declaration, attribute, or linker script.[^iso-c-n1570] [^cpp-draft-dcl-align]

## Detailed explanation

TODO
