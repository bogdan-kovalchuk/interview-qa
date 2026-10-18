---
id: emb-cemb-0019
title: "What is the purpose of the `static` keyword?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Depending on context, `static` does three different things:[^dou-embedded-interview]

1. **Local variable** – retains its value between function calls, lives for the entire program lifetime, and is not placed on the stack.
2. **Global variable or function** – restricts visibility to the current file (internal linkage) and prevents name conflicts between `.c` files.
3. **C++ class member** – has a single copy for the entire class, not a separate copy for each object.

## Detailed explanation

TODO
