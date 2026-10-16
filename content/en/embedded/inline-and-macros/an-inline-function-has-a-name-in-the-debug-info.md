---
id: emb-macros-0009
title: "Why is a `static inline` function easier to debug than a macro?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gdb-inline-functions
    title: "GDB: Inline Functions"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Inline-Functions.html
---

## Short answer

**A debugger can show an inline function as a logical frame** when the compiler emits compatible debug info. This can expose arguments and allow stepping even when no separate machine call exists. A macro is expanded before compilation and has no distinct call frame; breakpoints for inline code depend on optimization and the actual debug configuration.[^gdb-inline-functions]

## Detailed explanation

TODO
