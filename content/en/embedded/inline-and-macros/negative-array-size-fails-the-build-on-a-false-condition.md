---
id: emb-macros-0033
title: "How do you do a compile-time check without `static_assert` in older C?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: iso-c-array-static-assert
    title: "ISO/IEC 9899:201x Committee Draft N1570, array declarators and static assertions"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
#define STATIC_ASSERT(c, name) \
  typedef char name[(c) ? 1 : -1]
```

## Short answer

**The negative array size trick**: if a constant condition is false, the bound becomes `-1` and violates a language constraint, so the compiler must diagnose it but may continue.[^iso-c-array-static-assert]

This is an old way to check a type property at compile time, such as a structure size, when the condition is constant: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)`.[^iso-c-array-static-assert]

Since C11 and C++11, `_Static_assert` and `static_assert` respectively provide a diagnostic message.[^iso-c-array-static-assert]

## Detailed explanation

TODO
