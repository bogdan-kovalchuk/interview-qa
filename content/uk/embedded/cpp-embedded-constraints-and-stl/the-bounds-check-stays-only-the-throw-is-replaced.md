---
id: emb-cppstl-0034
title: "Чи прибирає `-fno-exceptions` сам перевірочний код у `at()`?"
description: "Ні – bounds check лишається; у libstdc++-подібних реалізаціях шлях помилки без exceptions часто веде до abort()/fatal handler."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Ні – bounds check лишається; у libstdc++-подібних реалізаціях шлях помилки без exceptions часто веде до `abort()`/fatal handler.</span>

Тобто bounds check у `vector::at()`/`array::at()` усе ще виконується; змінюється лише реакція на провал – аварійна зупинка без діагностики замість винятку.

Захист: для гарячого шляху, де перевірка зайва, використовуй `operator[]` з власною валідацією; для безпеки – логуй перед зупинкою.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
