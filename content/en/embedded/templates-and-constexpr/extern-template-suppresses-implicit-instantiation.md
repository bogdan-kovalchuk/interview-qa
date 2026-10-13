---
id: emb-tmplcx-0016
title: "What does `extern template` do?"
description: "Lets other translation units skip implicit instantiation of non-inline members; one explicit instantiation provides the definition."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that an entity with an explicit instantiation declaration that is used in a way that would otherwise cause implicit instantiation must have an explicit instantiation definition somewhere in the program; an explicit instantiation of a class also instantiates its direct non-template members. It does not describe how a compiler avoids copies."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a function template or member function specialization is instantiated when its definition is needed; implicit instantiation of a class template instantiates only the member declarations. It says nothing about code size."
---

## Question code

```cpp
extern template class Buffer<uint8_t>;
```

## Short answer

**Allows the compiler to skip instantiating the template's members in this translation unit.**[^cpp-draft-temp-explicit] A definition must exist somewhere in the program as an explicit instantiation definition; otherwise the program is ill-formed.[^cpp-draft-temp-explicit] Rule: `extern template` in the header plus one explicit instantiation in one `.cpp` allow avoiding copies in every TU for non-inline members.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
