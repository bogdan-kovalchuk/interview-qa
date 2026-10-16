---
id: emb-cemb-0027
title: "How many bytes of memory does a pointer occupy?"
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

It depends on the processor architecture: **16-bit** -> 2 bytes, **32-bit** -> 4 bytes, **64-bit** -> 8 bytes. The pointer type does not matter: `char *`, `int *`, `struct Foo *` – all occupy the same number of bytes. In embedded (ARM Cortex-M) it is always 4 bytes. To check: `sizeof(void *)`.[^dou-embedded-interview]

## Detailed explanation

TODO
