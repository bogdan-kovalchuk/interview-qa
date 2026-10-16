---
id: emb-cppfound-0017
title: "What is a dangling pointer and when does it occur?"
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

**Dangling pointer** – a pointer that refers to <span class="warn">already freed or destroyed</span> memory.

Causes:

1. Returning the address of a local variable: `int* f(){ int x=5; return &x; }` – x is destroyed on return;
2. After `free(ptr)` without nulling: `free(ptr); *ptr = 1;` – undefined behavior;
3. A pointer to an object whose lifetime has ended.

The danger: the memory <span class="warn">appears valid</span> until it is reused. The bugs are extremely hard to reproduce.[^embeddedinterviewlab]

## Detailed explanation

TODO
