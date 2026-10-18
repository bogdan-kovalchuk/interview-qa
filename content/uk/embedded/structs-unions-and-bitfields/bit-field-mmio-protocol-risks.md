---
id: emb-cemb-0036
title: "Що таке bit-field у C і чому його небезпечно використовувати для MMIO-регістрів або протоколів?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Bit-field** – поле struct із заданою кількістю бітів, наприклад `unsigned mode:3`. Його порядок бітів, allocation unit, padding і навіть signedness деяких форм залежать від implementation. <span class="warn">Для MMIO і wire protocols це небезпечно</span>: краще використовувати masks/shifts над `uint32_t`.[^dou-embedded-interview]

## Detailed explanation

TODO
