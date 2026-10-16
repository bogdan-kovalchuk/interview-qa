---
id: emb-macros-0023
title: "What are macros still irreplaceable for, even in a MISRA project?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Where `static inline` cannot replace the preprocessor:

• Register addresses with `volatile` cast; • utilities that cannot be functions: `ARRAY_SIZE`, `UNUSED`, `STATIC_ASSERT`; • Conditional compilation (`#ifdef`, `#if defined`); • X-macros and code generation; • stringification (`#`) and token pasting (`##`).

Rule: a macro is for textual/compile-time tricks; `static inline` is for everything that behaves like a function.[^iso-c-n1570]

## Detailed explanation

TODO
