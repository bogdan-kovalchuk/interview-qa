---
id: emb-cppstl-0023
title: "What do MISRA C++ rules typically restrict in embedded C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: misra-cpp-2008
    title: "MISRA C++:2008 Guidelines for the use of the C++03 language in critical systems"
    url: https://www.misra.org.uk/
  - source_id: misra-cpp-2023
    title: "MISRA C++:2023 Guidelines for the use of the C++17 language in critical systems"
    url: https://www.misra.org.uk/
---

## Short answer

**MISRA (Motor Industry Software Reliability Association) C++ restricts exception-based control flow, dynamic allocation, RTTI (run-time type information), unsafe casts, `goto`, complex inheritance hierarchies, and raw unions.**

The goal is determinism, analysability, and controlled data/control flow. Specific rules depend on the standard edition and project profile, so in an interview it is better to say "restricts/regulates" rather than "forbids everything".

Rule: MISRA C++ is about predictability; write for it with return codes, static allocation, and minimal runtime magic.[^embeddedinterviewlab]

## Detailed explanation

TODO
