---
id: emb-cppstl-0007
title: "How do you build an object without `new`, using placement new?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Question code

```cpp
alignas(Sensor) static uint8_t buf[sizeof(Sensor)];
Sensor* s = new (buf) Sensor(config);
// потім вручну: s->~Sensor();
```

## Short answer

**Placement new constructs an object at a pre-allocated address, without the heap.**

The memory is a static buffer or a memory-mapped region. `delete` does not apply here: the destructor must be called explicitly (`s->~Sensor()`).

Rule: placement new + explicit dtor = dynamic construction without the heap.[^embeddedinterviewlab]

## Detailed explanation

TODO
