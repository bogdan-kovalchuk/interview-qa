---
id: emb-cppstl-0023
title: "Що зазвичай обмежують MISRA C++ правила в embedded C++?"
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

**MISRA (Motor Industry Software Reliability Association) C++ обмежує exception-based control flow, dynamic allocation, RTTI (run-time type information), небезпечні casts, `goto`, складну ієрархію успадкування та сирі unions.**

Мета – детермінізм, аналізованість і контрольований data/control flow. Конкретні формулювання залежать від версії стандарту й профілю проєкту, тому на співбесіді краще казати «обмежує/регламентує», а не «забороняє все».

Правило: MISRA C++ – про передбачуваність; під неї пишуть із return codes, static allocation і мінімумом runtime-магії.[^embeddedinterviewlab]

## Detailed explanation

TODO
