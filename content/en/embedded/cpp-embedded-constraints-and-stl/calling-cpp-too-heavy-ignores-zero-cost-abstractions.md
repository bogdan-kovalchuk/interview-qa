---
id: emb-cppstl-0026
title: "Trap: why is \"C++ is too heavy for embedded\" a poor answer?"
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

<span class="warn">It demonstrates ignorance of zero-cost abstractions and the real levers for controlling runtime.</span>

Non-virtual classes, templates, `constexpr`, RAII (resource acquisition is initialization) can compile with no extra runtime overhead if you disable/avoid heavy features and check the map file. The real cost depends on the ABI, the standard library and optimizations.

Protection: speak specifically – what exactly you disable (`-fno-exceptions`/`-fno-rtti`) and which subset of the STL you take.[^embeddedinterviewlab]

## Detailed explanation

TODO
