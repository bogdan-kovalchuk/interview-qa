---
id: emb-dtypes-0067
title: "What does `-fstack-usage` do in GCC, and how do you read its output?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options, -fstack-usage"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

GCC `-fstack-usage` writes per-function use to a `.su` file named from `auxname`.[^gcc-stack-usage] Each tab-separated record gives function and source location, mangled name, bytes, and qualifier: `static` is fixed, `dynamic` is variable, and `dynamic,bounded` has a known upper bound.[^gcc-stack-usage]

Without `bounded`, the byte count is not a maximum. Use the call graph because the largest frame is not the nested-call peak; include interrupts, recursion, RTOS tasks, and libraries. `-Wstack-usage=256` is a warning threshold, not proof of sufficient stack.[^gcc-stack-usage]

## Detailed explanation

TODO
