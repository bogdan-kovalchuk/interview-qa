---
id: emb-align-0038
title: "How do you check a struct layout at compile time?"
track: embedded
section: memory-alignment-and-endianness
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
_Static_assert(sizeof(wire_t) == 7, "layout");
_Static_assert(offsetof(wire_t, id) == 6, "offset");
```

## Short answer

**Use `_Static_assert` with `sizeof` and `offsetof`** to check expected struct size and member offsets at compile time.

This is critical for packed wire formats and register maps where the exact layout is part of the contract.

Rule: pin expected `sizeof` and `offsetof` with asserts next to the struct definition.[^iso-c-n1570]

## Detailed explanation

TODO
