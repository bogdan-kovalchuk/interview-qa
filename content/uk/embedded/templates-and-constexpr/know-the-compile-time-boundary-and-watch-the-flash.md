---
id: emb-tmplcx-0034
title: "Що має продемонструвати кандидат у питаннях про templates і constexpr?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Розуміння межі compile-time vs runtime, уміння помітити template bloat на flash-обмеженому MCU, коли CRTP кращий за virtual.**

Плюс: `constexpr` для перенесення обчислень у build time, `if constexpr` як типобезпечний `#ifdef`, стратегії проти bloat і перевірка через linker map.

Правило: завжди розділяй «zero runtime cost» і «реальна Flash/compile вартість».[^embeddedinterviewlab]

## Detailed explanation

TODO
