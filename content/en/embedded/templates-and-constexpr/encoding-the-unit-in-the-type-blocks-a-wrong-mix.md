---
id: emb-tmplcx-0020
title: "How do templates give type-safe physical units?"
description: "The unit is encoded in the type, so implicit mixing of incompatible quantities is a compile error."
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
  - source_id: cpp-core-guidelines-i4
    title: "C++ Core Guidelines: I.4 (make interfaces precisely and strongly typed)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#i4-make-interfaces-precisely-and-strongly-typed
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "The change_speed(Speed) example rejects a value without a unit (error: no unit); it is a design recommendation, not the behavior of a specific compiler."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines when a function or class template is implicitly instantiated: when it is referenced in a context that requires a definition. Says nothing about binary size or code placement."
---

## Question code

```cpp
template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };
using Millivolt = Quantity<MillivoltTag>;
using Milliamp  = Quantity<MilliampTag>;
```

## Short answer

**The unit is encoded in the type, so implicitly mixing incompatible quantities is not allowed (a compile error).** `set_led_current(read_battery())` does not compile, because `Millivolt` and `Milliamp` are different types with no implicit conversion. `Quantity` stores only `Rep value`, so the tag type takes no space in the object. Rule: an interface that encodes the unit in its type rejects a unitless value at compile time.[^cpp-core-guidelines-i4]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
