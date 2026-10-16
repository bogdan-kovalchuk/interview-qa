---
id: emb-tmplcx-0023
title: "How does a template over a register give compile-time access protection?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**A template can forbid writes to a read-only register or reads from a write-only register – at compile time.**

By encoding access rights in the type (e.g. `Register<Addr, ReadOnly>`), an attempt to call `reg.write()` on an RO (read-only) register becomes a compile error. A raw `#define` cannot do that.

Rule: a typed register wrapper catches access errors before the code runs, unlike macros.[^embeddedinterviewlab]

## Detailed explanation

TODO
