---
id: emb-tmplcx-0022
title: "Templates versus macros: what are the key differences?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Templates: full type checking, arguments evaluated once, debuggable, constexpr evaluation. Macros: text, double evaluation, only preprocessor output.**

Cost: templates risk code bloat (a copy per instantiation) and slower builds; macros are fast and portable to C89 but unsafe.

Rule: in C++ choose templates for type safety; keep macros for what templates cannot do (`#`/`##`, conditional compilation).[^embeddedinterviewlab]

## Detailed explanation

TODO
