---
id: emb-cppstl-0016
title: "Як виставити C++-функції для виклику з C?"
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

**Guard `#ifdef __cplusplus` вмикає `extern "C"` лише для C++-компілятора.**

C-компілятор не знає синтаксису `extern "C"` (це C++-ключове слово); guard дозволяє одному header працювати в обох мовах.

Правило: спільні header'и завжди мають `#ifdef __cplusplus`-guard навколо `extern "C"`.[^embeddedinterviewlab]

## Detailed explanation

TODO
