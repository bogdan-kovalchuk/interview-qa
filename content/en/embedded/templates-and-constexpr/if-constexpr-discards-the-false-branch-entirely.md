---
id: emb-tmplcx-0018
title: "How does `if constexpr` work and why is it better than `#ifdef`?"
description: "The condition is evaluated at compile time and the false branch is completely discarded."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Question code

```cpp
if constexpr (std::is_same_v<P, STM32F4>) {
  USART1->BRR = compute_brr(115200);
} else {
  static_assert(always_false<P>, "unsupported");
}
```

## Short answer

**The condition is evaluated at compile time; the false branch is completely discarded – no code is generated for it.**

Unlike the preprocessor, the compiler still parses both branches for syntax (if they do not depend on a template parameter), catching errors even in uncollected paths. In the example `BRR` is the baud rate register.

Rule: `if constexpr` is a type-safe replacement for `#ifdef` for platform-dependent code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
