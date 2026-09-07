---
id: emb-tmplcx-0003
title: "Як виглядає class template для буфера фіксованого розміру?"
description: "Тип і розмір – template-параметри, тож буфер живе на стеку без heap."
track: embedded
section: templates-and-constexpr
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
template<typename T, size_t N>
class CircularBuffer {
  T buf_[N];
  size_t head_ = 0, tail_ = 0;
};
CircularBuffer<uint8_t, 64> uart_rx;
```

## Short answer

**Тип і розмір – template-параметри, тож буфер живе на стеку без heap.**

Розмір `N` відомий на етапі компіляції, масив `buf_[N]` вбудований в об'єкт. Жодного `malloc`, оптимальний розмір, без runtime-гнучкості.

Правило: параметризуй контейнери типом і розміром – отримаєш heap-free структуру з типобезпекою.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
