---
id: emb-cppstl-0004
title: "How do you report errors without exceptions, using error codes?"
description: "How do you report errors without exceptions, using error codes?"
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
