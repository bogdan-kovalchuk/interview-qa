---
id: emb-cppstl-0004
title: "Як передавати помилки без exceptions через error codes?"
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
enum class Status { Ok, Timeout, CrcError, Busy };
Status sensor_read(uint8_t a, uint16_t& out) {
  if (!bus_ready()) return Status::Busy;
  out = raw;
  return Status::Ok;
}
```

## Short answer

**`enum class` зі статусами + дані через reference/output-параметр.**

`enum class` дає типобезпеку (на відміну від голого `enum`), а викликач зобов'язаний перевірити результат. Це embedded-аналог винятків.

Правило: return codes – дефолтний error handling без exceptions.[^embeddedinterviewlab]

## Detailed explanation

TODO
