---
id: emb-tmplcx-0013
title: "Trap: why can you not say \"templates are free\"?"
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

<span class="warn">Templates may have zero runtime cost, but they have real cost in Flash and compile time.</span>

Each used function specialization is instantiated when its definition is needed,[^cpp-draft-temp-inst] and its code can take its own space in Flash; the build spends time on instantiation and type checking.

Defense: in an interview say "zero runtime cost does not mean zero flash cost", and check the linker map.[^embeddedinterviewlab]

## Detailed explanation

TODO
