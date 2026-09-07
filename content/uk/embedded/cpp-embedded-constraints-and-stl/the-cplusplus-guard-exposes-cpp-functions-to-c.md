---
id: emb-cppstl-0016
title: "Як виставити C++-функції для виклику з C?"
description: "Guard #ifdef __cplusplus вмикає extern \"C\" лише для C++-компілятора."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
#ifdef __cplusplus
extern "C" {
#endif
  void app_init(void);
#ifdef __cplusplus
}
#endif
```

## Short answer

**Guard `#ifdef __cplusplus` вмикає `extern "C"` лише для C++-компілятора.**

C-компілятор не знає синтаксису `extern "C"` (це C++-ключове слово); guard дозволяє одному header працювати в обох мовах.

Правило: спільні header'и завжди мають `#ifdef __cplusplus`-guard навколо `extern "C"`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
