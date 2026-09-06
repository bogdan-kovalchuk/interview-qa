---
id: emb-cppoop-0029
title: "Чим static member function відрізняється від звичайної?"
description: "Static member function не має this – не прив'язана до екземпляра."
track: embedded
section: cpp-classes-and-oop
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

**Static member function не має `this`** – не прив'язана до екземпляра.

Тому її можна викликати як `Class::func()` і вона не може звертатися до нестатичних членів. На практиці її часто використовують як callback-thunk для C API (application programming interface), бо її тип схожий на звичайний function pointer; для строгого C linkage інколи потрібна окрема `extern "C"` wrapper-функція.

Правило: static member function – зручний міст між C++ класом і C API, але перевіряй сигнатуру та linkage вимоги конкретного callback API.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
