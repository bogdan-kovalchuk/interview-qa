---
id: emb-cppstl-0035
title: "Що має продемонструвати кандидат про C++ constraints і STL в embedded?"
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

**Чому вимикають exceptions/RTTI, яка безпечна STL-підмножина, як працює `extern "C"`, placement new, що зазвичай обмежує MISRA C++.**

Плюс: `std::array` як дефолтний контейнер, `std::optional`/`std::string_view` замість null/`std::string`, і що C++ дає zero-cost абстракції (не «важкий для embedded»).

Правило: показуй конкретні прапорці, конкретні заміни контейнерів і конкретні стандарти.[^embeddedinterviewlab]

## Detailed explanation

TODO
