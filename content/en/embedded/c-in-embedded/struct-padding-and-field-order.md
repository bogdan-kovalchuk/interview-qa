---
id: emb-cemb-0030
title: "What is structure padding, and why can field order change its size?"
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

**Padding** is unused bytes that the compiler inserts for alignment of the next field or the entire structure. If fields are ordered from larger to smaller alignment requirements, padding often decreases. <span class="warn">Padding bytes cannot be relied on as stable data</span>: they may be uninitialized and are not suitable for direct comparison or bus transmission.[^dou-embedded-interview]

## Detailed explanation

TODO
