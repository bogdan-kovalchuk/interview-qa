---
id: emb-cemb-0038
title: "Для чого використовують pointer-to-pointer у драйверах, API виділення ресурсів і linked structures?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`T **` потрібен, коли функція має змінити pointer у caller-а: видати handle, додати node в list head або повернути buffer із pool. У драйверах це часто виглядає як `driver_open(dev_t **out)` або queue API, що оновлює head/tail. Важливо документувати ownership: хто після цього звільняє або повертає ресурс.[^dou-embedded-interview]

## Detailed explanation

TODO
