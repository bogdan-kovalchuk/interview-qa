---
id: emb-cemb-0013
title: "What does the inline keyword mean?"
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

`inline` is a hint plus a linkage/ODR rule for a function that may be defined in a header.[^dou-embedded-interview] The optimizer may substitute the body at the call site to remove call overhead, but is **not required** to.

C and C++ differ slightly, yet the practical idea is the same: small helpers or getters can be `static inline` in headers, and on large functions `inline` usually does not help. The compiler makes the real inlining decision; the keyword separately governs multiple definitions across translation units.

## Detailed explanation

TODO
