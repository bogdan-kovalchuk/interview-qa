---
id: emb-tmplcx-0017
title: "Trap: why can `std::function` inflate Flash sharply?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-func-wrap-func
    title: "C++ working draft: Class template function ([func.wrap.func])"
    url: https://eel.is/c++draft/func.wrap.func
  - source_id: cpp-draft-func-wrap-func-con
    title: "C++ working draft: Constructors and destructor ([func.wrap.func.con])"
    url: https://eel.is/c++draft/func.wrap.func.con
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: gnu-ld-print-map
    title: "GNU ld: Command-line options (-Map, --print-map)"
    url: https://sourceware.org/binutils/docs/ld/Options.html
---

## Short answer

<span class="warn">`std::function` is template-heavy type erasure; different signatures and callable types can produce a lot of separate code.</span>

Each callable type `F` is stored as an object of type `decay_t<F>`.[^cpp-draft-func-wrap-func-con] Its template handlers are instantiated separately for each such type.[^cpp-draft-temp-inst]

Defense: for simple callbacks a function pointer + `void* context` is often sufficient. On flash-constrained MCUs check the size of `std::function` via the linker map.[^gnu-ld-print-map]

## Detailed explanation

TODO
