---
id: emb-cppstl-0015
title: "Як викликати C-код із C++ через `extern \"C\"`?"
description: "extern \"C\" вмикає C linkage – без name mangling, тож лінкер знаходить C-символи."
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
extern "C" {
  #include "vendor_hal.h"
  #include "freertos/task.h"
}
```

## Short answer

**`extern "C"` вмикає C linkage – без name mangling, тож лінкер знаходить C-символи.**

Без нього C++ шукав би mangled-ім'я (`_Z...`), якого в C-об'єктнику немає -> undefined reference. Багато vendor headers уже мають власний `__cplusplus`-guard; тоді додаткова обгортка не потрібна.

Правило: C API (application programming interface) має бути оголошений із C linkage, але не загортай header, якщо він уже робить це сам.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
