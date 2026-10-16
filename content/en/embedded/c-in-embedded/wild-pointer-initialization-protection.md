---
id: emb-cppfound-0099
title: "What is dangerous about an uninitialized pointer and how can it be protected?"
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

**Wild pointer** – a pointer with a garbage address (stack value), not NULL. A check `if(p != NULL)` does not detect it.

Dangers:
- Write to an arbitrary address -> corruption of critical data;
- On an MCU: write to peripheral registers -> unpredictable hardware behavior;
- Hard to reproduce – depends on stack state.

Protection:
- Always initialize: `int *p = NULL;` or immediately `= &x`;
- `-fsanitize=address` during development;
- Static analysis: PC-lint, Coverity.[^embeddedinterviewlab]

## Detailed explanation

TODO
