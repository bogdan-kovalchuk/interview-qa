---
id: emb-cemb-0041
title: "What are scope, linkage, and lifetime in C, and why are they often confused?"
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

**Scope** is where a name is visible in source code. **Linkage** is whether the same name can refer to the same object/function across scopes or translation units. **Lifetime/storage duration** is when the object itself exists in memory; for example, a block-scope `static` has local visibility but lives for the entire runtime.[^dou-embedded-interview]

## Detailed explanation

TODO
