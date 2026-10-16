---
id: emb-cppstl-0016
title: "How do you expose C++ functions for calling from C?"
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
#ifdef __cplusplus
extern "C" {
#endif
  void app_init(void);
#ifdef __cplusplus
}
#endif
```

## Short answer

**The `#ifdef __cplusplus` guard enables `extern "C"` only for the C++ compiler.**

A C compiler does not understand the `extern "C"` syntax (it is a C++ keyword); the guard lets a single header work in both languages.

Rule: shared headers must always have an `#ifdef __cplusplus` guard around `extern "C"`.[^embeddedinterviewlab]

## Detailed explanation

TODO
