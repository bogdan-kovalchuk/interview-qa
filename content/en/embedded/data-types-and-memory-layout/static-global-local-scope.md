---
id: emb-cemb-0020
title: "How does `static` affect global and local variables?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

For a **local variable**, `static` changes its lifetime: the variable is initialized once, lives until the program terminates, and retains its value between function calls. Its scope remains local to the block.

For a **global variable** or function, `static` changes its linkage: the name is visible only in the current `.c`/`.cpp` file. This is called internal linkage and helps avoid name collisions between translation units.[^dou-embedded-interview]

## Detailed explanation

TODO
