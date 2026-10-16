---
id: emb-macros-0019
title: "What does MISRA C Directive 4.9 recommend about function-like macros?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: misra-c2012-amd3-dir49
    title: "MISRA C:2012 Amendment 3"
    url: https://misra.org.uk/app/uploads/2022/12/MISRA-C-2012-AMD3.pdf
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
---

## Short answer

**MISRA C Directive 4.9 recommends a function over a function-like macro** where the two are interchangeable.

It is a directive with Required category, but it does not unconditionally prohibit macros; Amendment 3 clarifies an exception for macros using `_Generic`.[^misra-c2012-amd3-dir49]

In practice, check whether a function can provide the same behaviour; `static inline` may be an option, but the directive does not mandate that specific mechanism.[^misra-c2012-amd3-dir49]

## Detailed explanation

TODO
