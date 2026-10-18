---
id: emb-cemb-0001
title: "Describe the use of the `static` modifier in C and C++."
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

**In C:**
- Local variable: `static int cnt = 0;` – preserves state between calls.
- Global variable/function: `static void helper()` – visible only in the current `.c` file.[^dou-embedded-interview]

**Additionally in C++:**
- Static class member: `static int count;` – one copy for all objects, initialized outside the class.
- Static method: `static void reset();` – called as `MyClass::reset()`, has no access to `this`.

## Detailed explanation

TODO
