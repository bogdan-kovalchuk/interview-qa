---
id: emb-cppfound-0069
title: "Why is a cast used with `void*`, and what are the limitations?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

In **C**: assigning `void*` to `T*` (and vice versa) does not require an explicit cast – conversion is implicit. `int *p = malloc(n);` – valid in C. In **C++**: <span class="warn">an explicit cast is required</span>: `int *p = (int*)malloc(n);`. void* limitations:
- Cannot be dereferenced without a cast;
- No pointer arithmetic (C standard);
- Does not preserve type-safety;
Before dereferencing: `*(int*)vp = 42;`. This rule preserves the correct access type.[^embeddedinterviewlab]

## Detailed explanation

TODO
