---
id: emb-tmplcx-0020
title: "How do templates give type-safe physical units?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-core-guidelines-i4
    title: "C++ Core Guidelines: I.4 (make interfaces precisely and strongly typed)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#i4-make-interfaces-precisely-and-strongly-typed
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
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
