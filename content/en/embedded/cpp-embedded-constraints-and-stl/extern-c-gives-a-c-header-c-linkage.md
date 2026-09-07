---
id: emb-cppstl-0015
title: "How do you call C code from C++ through `extern \"C\"`?"
description: "extern \"C\" enables C linkage without name mangling so the linker finds C symbols."
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

```c
extern "C" {
  #include "vendor_hal.h"
  #include "freertos/task.h"
}
```

## Short answer

**`extern "C"` enables C linkage – no name mangling, so the linker finds C symbols.**

Without it C++ would look for a mangled name (`_Z...`), which does not exist in the C object file -> undefined reference. Many vendor headers already carry their own `__cplusplus` guard; in that case no extra wrapper is needed.

Rule: a C API (application programming interface) must be declared with C linkage, but do not wrap a header that already does this on its own.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
