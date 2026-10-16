---
id: emb-cppstl-0012
title: "Чим `std::optional<T>` кращий за null-вказівник?"
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

**Зберігає значення inline (без heap), робить випадок «немає значення» явним у системі типів.**

Це зменшує ризик null-dereference: перед доступом до `*opt` треба перевірити `opt.has_value()`. Наприклад, `std::optional<FaultCode>` краще показує «fault є/немає», ніж null-сигналізація.

Правило: для «значення може бути відсутнє» – `std::optional`, а не sentinel/null-вказівник.[^embeddedinterviewlab]

## Detailed explanation

TODO
