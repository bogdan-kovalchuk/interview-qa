---
id: emb-raii-0016
title: "Що таке static RAII singleton і коли запускаються його ctor/dtor?"
description: "Function-local static: конструктор виконується один раз при першому виклику; деструктор зазвичай реєструється на program termination."
track: embedded
section: raii-and-smart-pointers
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
Driver& instance() {
  static Driver d; // ctor - при 1-му виклику
  return d;
}
```

**Function-local static: конструктор виконується один раз при першому виклику; деструктор зазвичай реєструється на program termination.**

Це lazy init, що оминає static initialization order fiasco. Але в embedded function-local static може підтягнути guard/runtime code для thread-safe initialization; за потреби перевіряй `-fno-threadsafe-statics` і політику destructors.

Правило: Meyers' singleton – heap-free, але не завжди runtime-free; перевіряй generated code на твоєму toolchain.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
