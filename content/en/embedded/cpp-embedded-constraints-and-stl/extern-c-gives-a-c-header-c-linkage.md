---
id: emb-cppstl-0015
title: "How do you call C code from C++ through `extern \"C\"`?"
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
