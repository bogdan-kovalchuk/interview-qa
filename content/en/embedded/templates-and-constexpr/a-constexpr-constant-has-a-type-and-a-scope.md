---
id: emb-tmplcx-0008
title: "Why is a `constexpr` variable better than a `#define` constant?"
description: "A constexpr variable has type and scope, making it type-safe unlike textual substitution."
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
  - source_id: cpp-draft-cpp-replace
    title: "C++ working draft: Replacement of macros ([cpp.replace])"
    url: https://eel.is/c++draft/cpp.replace
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines an object-like macro: its name is replaced by the replacement list of preprocessing tokens. This is untyped textual substitution; a particular preprocessor is not described."
  - source_id: cpp-draft-lex-phases
    title: "C++ working draft: Phases of translation ([lex.phases])"
    url: https://eel.is/c++draft/lex.phases
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says macro invocations are expanded in translation phase 4, and the tokens are syntactically and semantically analyzed as a translation unit in phase 7. A particular preprocessor is not described."
  - source_id: cpp-draft-cpp-scope
    title: "C++ working draft: Scope of macro definitions ([cpp.scope])"
    url: https://eel.is/c++draft/cpp.scope
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a macro definition lasts independently of block structure until #undef or the end of the translation unit, and has no significance after translation phase 4."
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a constexpr object is declared const and must be constant-initializable; otherwise the program is ill-formed."
  - source_id: cpp-draft-dcl-init-list
    title: "C++ working draft: List-initialization ([dcl.init.list])"
    url: https://eel.is/c++draft/dcl.init.list
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines narrowing in list-initialization: an integer conversion that cannot represent all values of the source is narrowing unless the source is a constant expression whose value fits the target type. So 300 to uint8_t is narrowing."
---

## Question code

```cpp
constexpr int MAX_SENSORS = 16;
// vs  #define MAX_SENSORS 16
```

## Short answer

**It has type and scope – type-safe, unlike textual substitution.**

A `constexpr` variable has a type and ordinary scope, and its initializer must be a constant expression.[^iso-cpp-n4861][^cpp-draft-dcl-constexpr] A `#define` is preprocessor text substitution: the macro has no type and no scope, and the replacement happens in translation phase 4.[^cpp-draft-cpp-replace][^cpp-draft-lex-phases][^cpp-draft-cpp-scope]

Rule: integer compile-time constants in C++ are `constexpr`, not `#define`; `#define` stays for conditional compilation.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
