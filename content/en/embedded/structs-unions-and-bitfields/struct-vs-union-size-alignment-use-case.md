---
id: emb-dtypes-0110
title: "How do struct and union differ in size, alignment, and use-case?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`struct` contains all fields as separate members with implementation-defined padding; `union` gives its members shared storage. Thus `sizeof(struct)` need not equal a simple sum of field sizes, and `sizeof(union)` need not equal exactly its largest field because of padding. Both types have implementation-defined alignment.[^iso-c-n1570]

## Detailed explanation

TODO
