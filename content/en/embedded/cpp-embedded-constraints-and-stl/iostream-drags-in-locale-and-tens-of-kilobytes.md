---
id: emb-cppstl-0027
title: "Why is `<iostream>` avoided in embedded in favour of `printf`?"
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

## Short answer

<span class="warn">`<iostream>` can pull in locale, heap buffers, global initialization and tens of KB of Flash.</span>

`std::cout` initializes heavy infrastructure before `main()`; on an MCU this is often unacceptable. `printf` (especially a trimmed/nano version) or a custom trace backend is usually much lighter.

Rule: for logging on an MCU use `printf` or a custom trace backend, not `iostream`.[^embeddedinterviewlab]

## Detailed explanation

TODO
