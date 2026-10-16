---
id: emb-cppstl-0006
title: "Які стратегії виділення пам'яті використовують замість heap?"
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

**Static allocation, placement new, fixed-size memory pools, stack allocation.**

Усі об'єкти мають static/automatic storage; немає `new`/`delete`. Pool дає O(1) без фрагментації; стек – для локальних, але невеликих (стеки 1–4 КБ).

Правило: у безпеко-критичному embedded heap або заборонений, або лише на етапі ініціалізації.[^embeddedinterviewlab]

## Detailed explanation

TODO
