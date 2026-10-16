---
id: emb-cppstl-0026
title: "Trap: чому казати «C++ занадто важкий для embedded» – погана відповідь?"
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

<span class="warn">Це демонструє незнання zero-cost abstractions і реальних важелів контролю runtime.</span>

Non-virtual класи, templates, `constexpr`, RAII (resource acquisition is initialization) можуть компілюватися без додаткового runtime-оверхеду, якщо вимкнути/уникати важких фіч і перевіряти map-файл. Реальна ціна залежить від ABI, стандартної бібліотеки й оптимізацій.

Захист: говори конкретно – що саме вимикаєш (`-fno-exceptions`/`-fno-rtti`) і яку підмножину STL береш.[^embeddedinterviewlab]

## Detailed explanation

TODO
