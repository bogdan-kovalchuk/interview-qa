---
id: emb-cppstl-0004
title: "How do you report errors without exceptions, using error codes?"
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

**`enum class` with statuses + data via reference/output parameter.**

An `enum class` gives type safety (unlike a bare `enum`), and the caller is forced to check the result. This is the embedded analogue of exceptions.

Rule: return codes are the default error handling without exceptions.[^embeddedinterviewlab]

## Detailed explanation

TODO
