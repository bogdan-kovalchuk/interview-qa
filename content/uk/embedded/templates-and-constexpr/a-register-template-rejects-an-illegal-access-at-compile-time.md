---
id: emb-tmplcx-0023
title: "Як шаблон над регістром дає compile-time захист доступу?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Шаблон може заборонити запис у read-only або читання write-only регістра – на етапі компіляції.**

Кодуючи права доступу в тип (напр. `Register<Addr, ReadOnly>`), спроба `reg.write()` для RO (read-only) стає compile error. Сирий `#define` такого не вміє.

Правило: типізована обгортка регістра ловить помилки доступу ще до запуску, на відміну від макросів.[^embeddedinterviewlab]

## Detailed explanation

TODO
