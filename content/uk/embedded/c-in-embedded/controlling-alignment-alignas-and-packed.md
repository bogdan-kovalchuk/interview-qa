---
id: emb-cemb-0017
title: "Для чого використовують вирівнювання, чи можна його контролювати?"
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

Вирівнювання потрібне для швидкого й коректного доступу CPU до даних.[^dou-embedded-interview] Багато архітектур читають 2/4/8-байтові значення ефективніше, коли адреса кратна розміру типу; деякі MCU на misaligned access можуть згенерувати fault.

Контролювати можна через порядок полів у struct, стандартні засоби `alignas` у C++ або `_Alignas`/`alignas` у сучасному C, а також compiler-specific атрибути типу `__attribute__((aligned))`, `__attribute__((packed))`, `#pragma pack`. `packed` треба використовувати обережно: він економить байти, але може сповільнити доступ або зламати вимоги hardware.

## Detailed explanation

TODO
