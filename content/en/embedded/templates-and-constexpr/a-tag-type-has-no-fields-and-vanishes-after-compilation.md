---
id: emb-tmplcx-0021
title: "Why does `Quantity<Tag>` have no runtime overhead?"
description: "The tag type has no fields and is not stored in the object, so Quantity carries only the value."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
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
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines when a function or class template is implicitly instantiated: when it is referenced in a context that requires a definition. Says nothing about binary size or code placement."
---

## Short answer

**The tag type has no fields and is not stored in the object; in this design it exists only as a template argument.** Each `Quantity<Tag>` is instantiated separately.[^cpp-draft-temp-inst] `Quantity` contains only `Rep value` (e.g. `int32_t`), so the object's size is determined by `Rep`, not by the tag. Rule: phantom types give unit safety with no extra runtime cost compared with a bare `Rep`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
