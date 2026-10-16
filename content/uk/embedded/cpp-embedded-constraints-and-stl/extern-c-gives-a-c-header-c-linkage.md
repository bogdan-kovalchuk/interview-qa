---
id: emb-cppstl-0015
title: "Як викликати C-код із C++ через `extern \"C\"`?"
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

**`extern "C"` вмикає C linkage – без name mangling, тож лінкер знаходить C-символи.**

Без нього C++ шукав би mangled-ім'я (`_Z...`), якого в C-об'єктнику немає -> undefined reference. Багато vendor headers уже мають власний `__cplusplus`-guard; тоді додаткова обгортка не потрібна.

Правило: C API (application programming interface) має бути оголошений із C linkage, але не загортай header, якщо він уже робить це сам.[^embeddedinterviewlab]

## Detailed explanation

TODO
