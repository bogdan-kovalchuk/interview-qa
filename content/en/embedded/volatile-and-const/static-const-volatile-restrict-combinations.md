---
id: emb-cemb-0032
title: "Why are static, const, volatile, and restrict used in C, and which combinations make sense?"
track: embedded
section: volatile-and-const
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`static` controls linkage or storage duration, `const` disallows modification through that lvalue, `volatile` forces actual access execution, and `restrict` promises no aliasing for optimization. For MMIO a typical pointer is: `volatile uint32_t *`; for a read-only register it can be `volatile const uint32_t *`. `static const` often places tables in flash/rodata, and `restrict` is appropriate in DSP/buffer code if the contract is actually honored.[^dou-embedded-interview]

## Detailed explanation

TODO
