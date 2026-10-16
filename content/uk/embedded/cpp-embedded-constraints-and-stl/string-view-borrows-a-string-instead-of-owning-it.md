---
id: emb-cppstl-0013
title: "Чому `std::string_view` безпечніший для embedded, а `std::string` – ризикований?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**`string_view` – non-owning, zero-copy погляд на рядок без алокації; `std::string` зазвичай володіє буфером і може алокувати heap.**

`string_view` зберігає лише вказівник + довжину, не копіює дані й не потребує null-terminated рядка. Це зручно для парсерів і логів без купи.

Захист: `string_view` не подовжує lifetime – стеж, щоб рядок-джерело жив довше за view.[^embeddedinterviewlab]

## Detailed explanation

TODO
