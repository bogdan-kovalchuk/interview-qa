---
id: emb-tmplcx-0023
title: "Як шаблон над регістром дає compile-time захист доступу?"
description: "Шаблон може заборонити запис у read-only або читання write-only регістра – на етапі компіляції."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

**Шаблон може заборонити запис у read-only або читання write-only регістра – на етапі компіляції.**

Кодуючи права доступу в тип (напр. `Register<Addr, ReadOnly>`), спроба `reg.write()` для RO (read-only) стає compile error. Сирий `#define` такого не вміє.

Правило: типізована обгортка регістра ловить помилки доступу ще до запуску, на відміну від макросів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
