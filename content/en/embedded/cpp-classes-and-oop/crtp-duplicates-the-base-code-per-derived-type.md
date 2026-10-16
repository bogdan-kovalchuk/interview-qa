---
id: emb-cppoop-0022
title: "Trap: what is the main drawback of CRTP?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Short answer

<span class="warn">The base code is duplicated for every derived type</span> (a separate template instantiation of every used member function).[^cpp-draft-temp-inst]

With many derived types and large base methods this can <span class="warn">inflate ROM</span>, though inlining and identical-code folding may offset it.[^gcc-optimize-options] You also cannot hold different CRTP types in one array: `SensorBase<A>` is not a base of `B`, so there is no common pointer type.[^cpp-draft-conv-ptr]

Protection: use CRTP for a small number of types; keep base methods small and move heavy logic into non-template code.

## Detailed explanation

TODO
