---
id: emb-cppstl-0018
title: "Trap: що станеться зі спільним header без `#ifdef __cplusplus` guard?"
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

<span class="warn">C-компілятор зустріне `extern "C"` і впаде з syntax error</span> – це C++-конструкція, невідома C.

Header, призначений для обох мов, без guard'а зламає C-збірку.

Захист: завжди обгортай `extern "C" { ... }` у `#ifdef __cplusplus ... #endif` з обох боків.[^embeddedinterviewlab]

## Detailed explanation

TODO
