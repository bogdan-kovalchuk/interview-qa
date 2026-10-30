---
id: emb-memlink-0002
title: "What problems can arise if memory is not freed?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: misra-c-2023-addendum-2
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
---

## Short answer

**Memory leak** – allocated memory is not returned to the system, although it is no longer used.[^dou-embedded-interview] Consequences:

- heap is gradually exhausted, so `malloc` returns `NULL`
- system slows down or hangs
- in Embedded (MCU without MMU and OS) this is especially critical: a small heap can run out after hours or days of operation, and the device will go into reset/fault or an inconsistent state

Related problems: <span class="warn">dangling pointer</span> (accessing freed memory), <span class="warn">double free</span> (UB).

## Detailed explanation

TODO
