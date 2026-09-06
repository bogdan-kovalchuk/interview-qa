---
id: emb-cppoop-0034
title: "Чому в abstract base слід надавати `= default` для virtual destructor?"
description: "Забезпечує коректне поліморфне знищення без ручного порожнього тіла."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
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

```c
virtual ~Sensor() = default;
```

**Забезпечує коректне поліморфне знищення без ручного порожнього тіла.**

`= default` просить компілятор згенерувати destructor; через `virtual` він не є trivial у строгому сенсі, але код може бути порожнім і оптимізованим. `virtual` гарантує, що при `delete base_ptr` викличеться dtor нащадка.

Правило: інтерфейсний base – `virtual ~T() = default;` якщо можливе polymorphic delete; для глобальних об'єктів пам'ятай про можливу `atexit` реєстрацію non-trivial dtor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
