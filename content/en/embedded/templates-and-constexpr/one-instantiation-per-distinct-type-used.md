---
id: emb-tmplcx-0002
title: "How many template instantiations end up in the binary?"
description: "One instantiation for each distinct set of template arguments that is actually used."
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

**One instantiation for each DIFFERENT set of template arguments that is actually used.**

With `max<int>(a, b)` and `max<float>(x, y)` the compiler creates two function instantiations; a function template that is never called is not instantiated.[^cpp-draft-temp-inst]

This counts generated copies of code, not the final flash size: the optimizer may inline calls, so check the result with `nm -C` or the map file.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
