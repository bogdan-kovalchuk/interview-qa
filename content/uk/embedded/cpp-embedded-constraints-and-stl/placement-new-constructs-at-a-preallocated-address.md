---
id: emb-cppstl-0007
title: "Як збудувати об'єкт без `new` через placement new?"
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

**Placement new конструює об'єкт за наперед виділеною адресою, без heap.**

Памʼять – static-буфер чи memory-mapped регіон. `delete` тут не застосовний: деструктор треба викликати явно (`s->~Sensor()`).

Правило: placement new + явний dtor = динамічне конструювання без купи.[^embeddedinterviewlab]

## Detailed explanation

TODO
