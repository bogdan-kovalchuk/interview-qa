---
id: emb-cemb-0020
title: "How does `static` affect global and local variables?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

For a **local variable**, `static` changes the lifetime: the variable is created once, lives until the program ends, and retains its value between function calls. The scope remains local to the block.

For a **global variable** or function, `static` changes the linkage: the name is visible only in the current `.c`/`.cpp` file. This is called internal linkage and helps avoid name conflicts between translation units.[^dou-embedded-interview]

## Detailed explanation

TODO
