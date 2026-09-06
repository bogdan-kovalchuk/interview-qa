---
id: emb-cppstl-0017
title: "Що таке name mangling і чому через нього потрібен `extern \"C\"`?"
description: "C++ кодує сигнатуру у символ (для overload resolution): sensor_read(uint8_t) -> _Z10sensor_readh; C не мангли́ть."
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

**C++ кодує сигнатуру у символ (для overload resolution): `sensor_read(uint8_t)` -> `_Z10sensor_readh`; C не мангли́ть.**

Без `extern "C"` лінкер шукатиме mangled-ім'я й не знайде немангленого C-символу -> помилка лінкування.

Правило: mangling – причина, чому міжмовний інтерфейс вимагає C linkage.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
