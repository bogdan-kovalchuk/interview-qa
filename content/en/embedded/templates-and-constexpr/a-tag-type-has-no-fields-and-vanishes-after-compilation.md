---
id: emb-tmplcx-0021
title: "Why does `Quantity<Tag>` have no runtime overhead?"
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
---

## Short answer

**The tag type has no fields and is not stored in the object; in this design it exists only as a template argument.** Each `Quantity<Tag>` is instantiated separately.[^cpp-draft-temp-inst] `Quantity` contains only `Rep value` (e.g. `int32_t`), so the object's size is determined by `Rep`, not by the tag. Rule: phantom types give unit safety with no extra runtime cost compared with a bare `Rep`.

## Detailed explanation

TODO
