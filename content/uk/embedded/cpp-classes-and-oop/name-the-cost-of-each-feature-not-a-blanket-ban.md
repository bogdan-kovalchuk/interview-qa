---
id: emb-cppoop-0037
title: "Що має сказати кандидат про C++ OOP в embedded?"
description: "OOP (object-oriented programming) у embedded: non-virtual класи можуть бути zero-overhead у release; vtable живе в ROM, vptr коштує RAM на екземпляр; CRTP дає compile-time polymorphism; композиція – default."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**OOP (object-oriented programming) у embedded: non-virtual класи можуть бути zero-overhead у release; vtable живе в ROM, vptr коштує RAM на екземпляр; CRTP дає compile-time polymorphism; композиція – default.**

Плюс startup-вимоги: bare-metal мусить ітерувати `.init_array`; global destructors можуть тягнути `atexit`; `-fno-exceptions`/`-fno-rtti` для контролю runtime support.

Правило: показуй, що знаєш ціну кожної фічі в байтах і тактах, а не лише синтаксис.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
