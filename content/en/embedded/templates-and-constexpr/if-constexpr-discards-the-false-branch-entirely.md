---
id: emb-tmplcx-0018
title: "How does `if constexpr` work and why is it better than `#ifdef`?"
description: "The condition is evaluated at compile time; the discarded branch produces no code and, in a template, is not instantiated."
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
  - source_id: cpp-draft-stmt-if
    title: "C++ working draft: The if statement ([stmt.if])"
    url: https://eel.is/c++draft/stmt.if
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "For if constexpr: inside a template the discarded substatement is not instantiated when the condition is no longer value-dependent after instantiation; the condition must be a constant expression. Does not say what code a given compiler emits."
  - source_id: cpp-draft-cpp-cond
    title: "C++ working draft: Conditional inclusion ([cpp.cond])"
    url: https://eel.is/c++draft/cpp.cond
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Only the first group whose controlling condition is true is processed; in a skipped group the other preprocessing tokens are ignored. Does not describe a specific preprocessor."
  - source_id: cpp-draft-temp-res
    title: "C++ working draft: Name resolution ([temp.res])"
    url: https://eel.is/c++draft/temp.res
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says the program is ill-formed, no diagnostic required, if no valid specialization can be generated for a templated entity or for a substatement of a constexpr if within a template and that template is not instantiated. Does not name specific compiler diagnostics."
---

## Question code

```cpp
template<typename P>
void init_uart() {
  if constexpr (std::is_same_v<P, STM32F4>) {
    USART1->BRR = compute_brr(115200);
  } else {
    static_assert(always_false<P>, "unsupported");
  }
}
```

## Short answer

**The condition is evaluated at compile time; in a template the discarded branch is not instantiated, so no code is generated for it.**[^cpp-draft-stmt-if] The preprocessor `#ifdef` skips the tokens of the unselected branch.[^cpp-draft-cpp-cond] The compiler, however, checks the syntax of a discarded `if constexpr` branch.[^cpp-draft-stmt-if] Parts of the discarded branch that depend on a template parameter are not instantiated, so their type errors do not appear.[^cpp-draft-stmt-if] Rule: `if constexpr` is a type-safe replacement for `#ifdef` in platform-dependent code.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
