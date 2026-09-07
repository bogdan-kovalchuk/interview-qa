---
id: emb-raii-0007
title: "Як використати `unique_ptr` з custom deleter для HAL-ресурсу?"
description: "unique_ptr з stateless лямбдою-deleter автоматично викликає HAL teardown при виході зі scope."
track: embedded
section: raii-and-smart-pointers
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
auto del = [](UART_HandleTypeDef* h) {
  HAL_UART_DeInit(h);
};
std::unique_ptr<UART_HandleTypeDef, decltype(del)>
  uart(&huart1, del);
```

## Short answer

**unique_ptr з stateless лямбдою-deleter автоматично викликає HAL teardown при виході зі scope.**

HAL означає hardware abstraction layer. Тут `unique_ptr` не алокує `huart1`; він лише керує teardown-викликом для вже існуючого handle. Немає control block і reference counting.

Правило: для pointer-sized `unique_ptr` використовуй stateless deleter type (лямбда без capture або empty functor); function pointer deleter теж можливий, але зазвичай збільшує розмір `unique_ptr`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
