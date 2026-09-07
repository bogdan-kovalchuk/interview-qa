---
id: emb-cppstl-0004
title: "How do you report errors without exceptions, using error codes?"
description: "An enum class with statuses plus data via reference or output parameter"
track: embedded
section: cpp-embedded-constraints-and-stl
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

## Sources

<!-- generated from frontmatter -->
