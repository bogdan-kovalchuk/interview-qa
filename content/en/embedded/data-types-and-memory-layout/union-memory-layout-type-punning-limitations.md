---
id: emb-dtypes-0109
title: "How is union represented in memory and what limitations does type punning through union have?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-draft-union
    title: "C++ working draft: Unions"
    url: https://eel.is/c++draft/class.union
---

## Short answer

In a **union**, all members start at the same offset, and storage is sized and aligned for its members according to the implementation. Writing one member makes it the active variant; reading another has different consequences under C and C++ rules, including effective type and lifetime.[^iso-c-n1570][^cpp-draft-union] <span class="warn">For portable byte interpretation, prefer `memcpy`</span> rather than assuming union type punning works identically in C and C++.

## Detailed explanation

TODO
