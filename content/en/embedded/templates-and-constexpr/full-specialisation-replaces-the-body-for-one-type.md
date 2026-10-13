---
id: emb-tmplcx-0009
title: "What is full template specialisation?"
description: "A completely different implementation for a specific type."
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
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says template<> declares an explicit specialization, which is used instead of the general definition for that set of arguments. The declaration must be reachable from every use that would cause implicit instantiation; otherwise the program is ill-formed with no diagnostic required."
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a partial specialization is an alternative definition used instead of the primary template when the arguments match its pattern. Does not describe how to choose between several matching specializations."
---

## Question code

```cpp
template<> class SpiDriver<STM32F4> {
  // register layout саме для STM32F4
};
```

## Short answer

**A completely different implementation for a specific type.**

Full specialization is a `template<>` definition that is used instead of the primary template for one set of arguments.[^cpp-draft-temp-expl-spec] It centralizes platform-dependent code in one place instead of scattered `#ifdef` across the project.

Rule: full specialization – for one specific type/platform with a unique implementation.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
