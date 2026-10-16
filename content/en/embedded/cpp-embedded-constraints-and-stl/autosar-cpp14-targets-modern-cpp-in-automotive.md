---
id: emb-cppstl-0024
title: "How does AUTOSAR C++14 differ from MISRA C++?"
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

**AUTOSAR (AUTomotive Open System ARchitecture) C++14 is an automotive rule set for modern C++14; it governs templates, `constexpr`, `auto`, range-based for and other features.**

It is not "C++ banned" but a set of rules for safe use of the language in safety-critical code. MISRA C++ and AUTOSAR are close in purpose but have different editions, scope and specific rules.

Rule: AUTOSAR C++14 is modern C++ within a safety discipline, not a license to write any abstraction without control.[^embeddedinterviewlab]

## Detailed explanation

TODO
