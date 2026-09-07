---
id: emb-tmplcx-0020
title: "How do templates give type-safe physical units?"
description: "The unit is encoded in the type so mixing incompatible quantities is a compile error."
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
template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };
using Millivolt = Quantity<MillivoltTag>;
using Milliamp  = Quantity<MilliampTag>;
```

## Short answer

**The unit is encoded in the type – mixing incompatible quantities is impossible (compile error).**

`set_led_current(read_battery())` will not compile (Millivolt ≠ Milliamp). At the same time `Quantity` has the size of `int32_t`: tag types exist only at compile time and are fully optimized away.

Rule: type-safe units give compile-time checking without additional runtime fields; recall the Mars Climate Orbiter crash (pound-seconds vs newton-seconds).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
