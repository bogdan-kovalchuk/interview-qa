---
id: emb-macros-0028
title: "Trap: how can repeated macro argument evaluation distort an ADC filter?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-invocation
    title: "GCC: Invocation (The C Preprocessor)"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
---

## Question code

```c
#define FILT(s) ((s) + ((adc_read() - (s)) >> 3))
```

## Short answer

The macro substitutes parameter `s` twice in its replacement list, so passing `adc_read()` as the argument evaluates it twice; the body also contains a separate `adc_read()` call.[^iso-c-n1570]

If each call starts a new conversion, the formula mixes different samples; the exact behavior depends on the implementation of `adc_read()`. Read once into a local variable or pass a stable value to a `static inline` function.[^iso-c-n1570]

## Detailed explanation

TODO
