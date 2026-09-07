---
id: emb-raii-0007
title: "How do you use `unique_ptr` with a custom deleter for a HAL resource?"
description: "A uniqueptr with a stateless lambda deleter calls the HAL teardown on scope exit without a control block or reference counting, managing an already existing handle."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
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

**A `unique_ptr` with a stateless lambda deleter automatically calls the HAL teardown on scope exit.**

A HAL is a hardware abstraction layer. Here `unique_ptr` does not allocate `huart1`; it only manages the teardown call for an already existing handle. There is no control block and no reference counting.

Rule: for a pointer-sized `unique_ptr`, use a stateless deleter type (a lambda without capture or an empty functor); a function pointer deleter is also possible but usually increases the `unique_ptr` size.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
