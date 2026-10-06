---
id: emb-cppoop-0018
title: "How does virtual dispatch hurt determinism on simple cores?"
description: "A virtual call is an indirect branch through the vptr and vtable, so its target is not visible from the instruction"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a virtual function call runs its final overrider in the dynamic type of the object, and that a call through a qualified-id calls the named function; the standard does not specify the mechanism (vptr/vtable)."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Describes the vtable as the table used to dispatch virtual functions, the vptr in an object of a dynamic class, and that on most platforms a vtable entry is equivalent to a function pointer. It is an ABI, not the language standard: the ABI of a given toolchain can differ, and the document says nothing about cycle costs."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents -fdevirtualize (an attempt to turn virtual function calls into direct calls; enabled at -O2, -O3 and -Os); does not guarantee that any particular call is devirtualized."
  - source_id: absint-ait-wcet
    title: "Worst-Case Execution Time Prediction by Static Program Analysis (AbsInt)"
    url: https://www.absint.com/aiT_WCET.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Says that computed calls and branches the decoder cannot resolve require user annotations listing the possible targets. It covers computed calls in general (function-pointer arrays, switch tables), not C++ virtual calls specifically, and describes one tool (aiT)."
  - source_id: arm-cortex-m7-trm
    title: "Arm Cortex-M7 Processor Technical Reference Manual (r0p2, DDI 0489B)"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
    accessed: 2026-10-06
    kind: official
    version: "r0p2"
    applicability: "Confirms that the Cortex-M7 has dynamic branch prediction with a Branch Target Address Cache (or a static predictor when no BTAC is specified); it says nothing about other Cortex-M cores and gives no cost for indirect calls."
---

## Short answer

**A virtual call is an indirect branch through the vptr/vtable, so the target is not visible from the instruction.**[^itanium-cxx-abi] On simple cores it is a few extra instructions, and the main real-time problem is analysis: the target depends on the dynamic type,[^cpp-draft-expr-call] and a worst-case execution time tool must know the possible targets.[^absint-ait-wcet] On cores with dynamic branch prediction, such as the Cortex-M7,[^arm-cortex-m7-trm] call time also depends on the prediction.

Rule: in hot paths and WCET-bound code, prefer calls whose target is known at compile time (templates, CRTP).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
