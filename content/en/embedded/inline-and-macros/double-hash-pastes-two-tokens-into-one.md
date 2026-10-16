---
id: emb-macros-0013
title: "What does the token pasting operator `##` do?"
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
#define REG(periph, r) periph##_##r
// REG(GPIOA, ODR) -> GPIOA_ODR
```

## Short answer

**`##` pastes adjacent tokens** in a macro replacement list: here `GPIOA`, `_` and `ODR` form the identifier `GPIOA_ODR`.

Arguments next to `##` are substituted without expanding any macros they contain first; an extra level is needed for that.

The pasted result must form one valid preprocessing token; otherwise the program violates a language constraint.[^iso-c-n1570]

## Detailed explanation

TODO
