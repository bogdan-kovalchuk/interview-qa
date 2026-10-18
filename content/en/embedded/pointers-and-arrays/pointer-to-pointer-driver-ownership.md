---
id: emb-cemb-0038
title: "Why are pointer-to-pointers used in drivers, resource APIs, and linked structures?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`T **` is needed when a function must change the caller's pointer: to issue a handle, add a node at the list head, or return a buffer from a pool. In drivers this often looks like `driver_open(dev_t **out)` or a queue API that updates head/tail. It is important to document ownership: who frees or returns the resource afterward.[^dou-embedded-interview]

## Detailed explanation

TODO
