---
id: emb-macros-0043
title: "Why is `static inline` safer than a macro for a bit operation?"
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

## Question code

```c
static inline uint32_t set_bit(uint32_t v, unsigned n) {
  return v | (1u << n);
}
```

## Short answer

**Typed parameters and single evaluation of arguments.**

The macro `#define SET_BIT(v,n) ((v) | (1u << (n)))` may work in this simple case, but the preprocessor does not check parameter types and can substitute an argument in multiple places. A `static inline` function takes typed parameters, and each argument expression is evaluated once; the compiler may inline it, but is not required to.

For the shown shift, `n` must be less than the width of the left operand's type; enforce that bound separately.[^iso-c-n1570]

## Detailed explanation

TODO
