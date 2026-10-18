---
id: emb-cppfound-0021
title: "What is a double pointer (`int **pp`) and why is it needed?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Double pointer** – a pointer that stores the address of another pointer.

Why:
1. **Modify the caller's pointer**: `void alloc(int **pp){ *pp = malloc(n); }` – without `**` the caller would not see the new address;
2. **2D arrays via arrays of pointers**;
3. Advancing a parse cursor: `void parse(char **p){ (*p)++; }`.

Reading the type: `int **pp` – "pointer to pointer to int"; `*pp` -> a pointer, `**pp` -> an int value.[^embeddedinterviewlab]

## Detailed explanation

TODO
