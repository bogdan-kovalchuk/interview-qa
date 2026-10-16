---
id: emb-fnptr-0042
title: "Why is `std::function` not always suitable for an embedded callback API?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-function
    title: "cppreference: std::function constructor"
    url: https://en.cppreference.com/w/cpp/utility/functional/function
---

## Short answer

**`std::function` is convenient but can carry overhead and potential allocations.**

It type-erases the callable and can store lambdas and functors, but this increases code size, may pull in exceptions and RTTI depending on the toolchain, and sometimes uses the heap when the callable does not fit in the small buffer optimization.

Embedded rule: in low-level drivers, `function pointer + void *ctx` is used more often; in the application layer, `std::function` is acceptable if project policy allows it.[^cppreference-function]

## Detailed explanation

TODO
