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
  - source_id: autosar-cpp14-guidelines
    title: "AUTOSAR Guidelines for the use of the C++14 language in critical and safety-related systems"
    url: https://www.autosar.org/fileadmin/standards/adaptive/18-10/AUTOSAR_RS_CPP14Guidelines.pdf
  - source_id: misra-cpp-2008
    title: "MISRA C++:2008 Guidelines for the use of the C++03 language in critical systems"
    url: https://www.misra.org.uk/
  - source_id: misra-cpp-2023
    title: "MISRA C++:2023 Guidelines for the use of the C++17 language in critical systems"
    url: https://www.misra.org.uk/
---

## Short answer

**AUTOSAR (AUTomotive Open System ARchitecture) C++14 is an automotive rule set for modern C++14; it regulates templates, `constexpr`, `auto`, range-based for, and other features.**

It does not mean "C++ is forbidden"; it is a set of rules for applying the language safely in safety-critical code. MISRA C++ and AUTOSAR share similar goals, but have different editions, scope, and specific rules.

Rule: AUTOSAR C++14 = modern C++ within safety discipline, not permission to write arbitrary abstractions without control.[^embeddedinterviewlab]

## Detailed explanation

TODO
