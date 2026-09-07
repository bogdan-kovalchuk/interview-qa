---
id: emb-tmplcx-0006
title: "Як згенерувати CRC-32 (cyclic redundancy check) таблицю на етапі компіляції?"
description: "Уся таблиця на 1 КБ обчислюється компілятором і зазвичай кладеться у Flash .rodata."
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
constexpr auto make_crc_table() {
  std::array<uint32_t, 256> t{};
  for (uint32_t i = 0; i < 256; ++i)
    t[i] = crc32_for_byte(i);
  return t;
}
constexpr auto crc_table = make_crc_table();
```

## Short answer

**Уся таблиця на 1 КБ обчислюється компілятором і зазвичай кладеться у Flash `.rodata`.**

Це замінює ручні (помилкові) таблиці й startup-цикли, що марнують boot time. У runtime таблиця вже готова.

Правило: великі незмінні таблиці (CRC, gamma/lookup tables) генеруй через `constexpr`, а не рахуй при старті.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
