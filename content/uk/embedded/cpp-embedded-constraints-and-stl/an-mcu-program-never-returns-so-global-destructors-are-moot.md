---
id: emb-cppstl-0021
title: "Що робить `-fno-use-cxa-atexit` і чому це ок для MCU?"
description: "Не реєструє деструктори глобальних об'єктів через __cxa_atexit."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Не реєструє деструктори глобальних об'єктів через `__cxa_atexit`.**

На MCU програма зазвичай ніколи не завершується, тож dtor глобалів і не потрібні – реєстрація лише тягне runtime-інфраструктуру й ROM.

Правило: статичні об'єкти на MCU «вічні»; `-fno-use-cxa-atexit` прибирає непотрібний cleanup.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
