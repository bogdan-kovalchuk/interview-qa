---
id: emb-tmplcx-0010
title: "What is partial template specialisation?"
description: "Specialization by pattern (e.g. all pointers), not by a single type."
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
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a partial specialization is an alternative definition used instead of the primary template when the arguments match its pattern. Does not describe how to choose between several matching specializations."
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says template<> declares an explicit specialization for one set of arguments, as in the stream<char> example, not for a whole family of types."
---

## Question code

```cpp
template<typename T>
class Buffer<T*> {
  // для всіх вказівникових типів
};
```

## Short answer

**Specialization by pattern (e.g. all pointers), not by a single type.**

`Buffer<T*>` applies to any type of the form `T*` and replaces the primary template only for such arguments.[^cpp-draft-temp-spec-partial-general] Rule: partial specialization – when behavior is common to a whole class of types described by a pattern.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
