---
id: emb-tmplcx-0006
title: "How do you generate a CRC-32 table at compile time?"
description: "A 256-entry uint32_t table (1 KB) is built with constexpr, not in a loop at startup."
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
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a constexpr function call gives the same result as an equivalent non-constexpr call but may appear in a constant expression, and that a constexpr variable must be constant-initializable; says nothing about where the result is placed."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Defines constant initialization of static-storage variables: it is not dynamic initialization and needs no code run at startup; says nothing about the memory segment on a target board."
---

## Question code

```cpp
constexpr auto make_crc_table() {
  std::array<uint32_t, 256> t{};
  for (uint32_t i = 0; i < 256; ++i)
    t[i] = crc32_for_byte(i);
  return t;
}
constexpr auto crc_table = make_crc_table();
```

## Short answer

**The CRC-32 table of 256 `uint32_t` entries (1 KB) is computed by the compiler when the per-byte function and the table builder are `constexpr`.**

A constexpr variable must be constant-initializable,[^cpp-draft-dcl-constexpr] so the table is constant-initialized and no loop at startup fills it.[^cpp-draft-basic-start-static]

Rule: generate large immutable tables (for example, CRC) with `constexpr` rather than computing them at startup.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
