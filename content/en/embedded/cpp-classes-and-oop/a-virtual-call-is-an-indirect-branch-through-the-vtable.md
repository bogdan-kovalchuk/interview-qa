---
id: emb-cppoop-0018
title: "How does virtual dispatch hurt determinism on simple cores?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: absint-ait-wcet
    title: "Worst-Case Execution Time Prediction by Static Program Analysis (AbsInt)"
    url: https://www.absint.com/aiT_WCET.pdf
  - source_id: arm-cortex-m7-trm
    title: "Arm Cortex-M7 Processor Technical Reference Manual (r0p2, DDI 0489B)"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
---

## Short answer

**A virtual call is an indirect branch through the vptr/vtable, so the target is not visible from the instruction.**[^itanium-cxx-abi] On simple cores it is a few extra instructions, and the main real-time problem is analysis: the target depends on the dynamic type,[^cpp-draft-expr-call] and a worst-case execution time tool must know the possible targets.[^absint-ait-wcet] On cores with dynamic branch prediction, such as the Cortex-M7,[^arm-cortex-m7-trm] call time also depends on the prediction.

Rule: in hot paths and WCET-bound code, prefer calls whose target is known at compile time (templates, CRTP).

## Detailed explanation

TODO
