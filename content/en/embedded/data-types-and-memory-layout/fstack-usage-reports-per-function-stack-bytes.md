---
id: emb-dtypes-0058
title: "How do you check a function's stack frame size in GCC?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
---

## Short answer

The `-fstack-usage` option makes GCC emit a `.su` report estimating stack usage per function.[^gcc-stack-usage]

Each `.su` entry has four tab-separated fields: source location and function name, mangled name, byte count, and qualifiers such as `static`, `dynamic`, or `bounded`.[^gcc-stack-usage]

The report describes an individual function, not the total maximum for a call path or task stack.[^gcc-stack-usage]

GCC also provides `-Wstack-usage=N` threshold warnings, but that threshold does not prove the full call path fits the available stack.[^gcc-stack-usage]

## Detailed explanation

TODO
