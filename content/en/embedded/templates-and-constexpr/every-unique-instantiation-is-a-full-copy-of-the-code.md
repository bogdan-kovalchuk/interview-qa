---
id: emb-tmplcx-0014
title: "Where does template code bloat come from?"
track: embedded
section: templates-and-constexpr
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
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Short answer

<span class="warn">Each unique instantiation creates its own definitions of the functions that are used.</span>[^cpp-draft-temp-inst] In Flash such definitions usually take separate code; the compiler can fold only functions with identical code (in GCC this is `-fipa-icf`).[^gcc-optimize-options]

Example: `CircularBuffer<uint8_t,64>` and `CircularBuffer<uint16_t,64>` give separate sets of the methods the program calls, and their code differs.

Rule: watch the number of instantiations – on flash-constrained MCUs each new type can quickly grow the firmware.

## Detailed explanation

TODO
