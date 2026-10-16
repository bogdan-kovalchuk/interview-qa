---
id: emb-tmplcx-0006
title: "How do you generate a CRC-32 table at compile time?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
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
