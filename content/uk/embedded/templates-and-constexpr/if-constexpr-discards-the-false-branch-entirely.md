---
id: emb-tmplcx-0018
title: "Як працює `if constexpr` і чим він кращий за `#ifdef`?"
description: "Умова обчислюється на етапі компіляції; хибна гілка повністю відкидається – код для неї не генерується."
track: embedded
section: templates-and-constexpr
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

```cpp
if constexpr (std::is_same_v<P, STM32F4>) {
  USART1->BRR = compute_brr(115200);
} else {
  static_assert(always_false<P>, "unsupported");
}
```

## Short answer

**Умова обчислюється на етапі компіляції; хибна гілка повністю відкидається – код для неї не генерується.**

На відміну від препроцесора, компілятор усе одно парсить обидві гілки на синтаксис (якщо вони не залежать від template-параметра), ловлячи помилки навіть у незібраних шляхах. У прикладі `BRR` – baud rate register.

Правило: `if constexpr` – типобезпечна заміна `#ifdef` для платформо-залежного коду.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
