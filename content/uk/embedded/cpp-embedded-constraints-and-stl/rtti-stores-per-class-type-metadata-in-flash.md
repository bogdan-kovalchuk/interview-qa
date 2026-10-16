---
id: emb-cppstl-0003
title: "Чому вимикають RTTI (`-fno-rtti`) і що це забирає?"
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

**RTTI (run-time type information) зберігає метадані типу на клас у Flash; вимкнення економить ROM.**

Наслідки: недоступний `dynamic_cast` (використовуй `static_cast`, коли тип відомий) і `typeid` (заміни на template specialization / tag dispatch). Virtual-функції працюють – vtable ≠ RTTI.

Правило: без RTTI покладайся на compile-time знання типів, а не runtime-перевірки.[^embeddedinterviewlab]

## Detailed explanation

TODO
