---
id: emb-cemb-0035
title: "How can you determine system endianness without violating strict aliasing?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

It is safe to store an integer and copy its bytes via `memcpy` into an `unsigned char` buffer, because character types can represent object representation. For example, `uint32_t x=1`, `memcpy(b,&x,4)`, then check `b[0]`. For portable protocol code it is better not to depend on host endianness but to explicitly assemble and disassemble bytes.[^dou-embedded-interview]

## Detailed explanation

TODO
