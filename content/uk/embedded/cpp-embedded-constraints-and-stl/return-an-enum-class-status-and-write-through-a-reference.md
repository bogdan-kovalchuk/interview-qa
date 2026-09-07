---
id: emb-cppstl-0004
title: "Як передавати помилки без exceptions через error codes?"
description: "enum class зі статусами + дані через reference/output-параметр."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
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

## Question code

```cpp
enum class Status { Ok, Timeout, CrcError, Busy };
Status sensor_read(uint8_t a, uint16_t& out) {
  if (!bus_ready()) return Status::Busy;
  out = raw;
  return Status::Ok;
}
```

## Short answer

**`enum class` зі статусами + дані через reference/output-параметр.**

`enum class` дає типобезпеку (на відміну від голого `enum`), а викликач зобов'язаний перевірити результат. Це embedded-аналог винятків.

Правило: return codes – дефолтний error handling без exceptions.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
