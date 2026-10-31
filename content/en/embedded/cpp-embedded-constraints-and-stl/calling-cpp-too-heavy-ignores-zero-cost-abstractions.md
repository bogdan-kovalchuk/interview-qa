---
id: emb-cppstl-0026
title: "Trap: why is saying \"C++ is too heavy for embedded\" a poor answer?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: stroustrup-dnr
    title: "The Design and Evolution of C++ (Bjarne Stroustrup)"
    url: https://www.stroustrup.com/
---

## Short answer

<span class="warn">It demonstrates ignorance of zero-cost abstractions and the real levers of runtime control.</span>

Non-virtual classes, templates, `constexpr`, RAII (resource acquisition is initialization) can compile with zero additional runtime overhead if heavy features are disabled/avoided and the map file is checked. The real cost depends on ABI, standard library, and optimisation.

Protection: be specific – what you disable (`-fno-exceptions`/`-fno-rtti`) and what subset of STL you use.[^embeddedinterviewlab]

## Detailed explanation

TODO
