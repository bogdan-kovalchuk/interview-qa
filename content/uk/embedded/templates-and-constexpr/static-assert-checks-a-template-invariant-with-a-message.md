---
id: emb-tmplcx-0027
title: "Як `static_assert` використовують із шаблонами?"
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

**Compile-time перевірка інваріантів типу/розміру з понятним повідомленням.**

Напр. у дефолтній гілці `if constexpr`: `static_assert(always_false<P>, "Unsupported platform")` ловить непідтримуваний тип ще на компіляції. Також `static_assert(N > 0, "...")` валідовує NTTP.

Правило: `static_assert` – головний інструмент, щоб перетворити невірне використання шаблону на зрозумілу помилку.[^embeddedinterviewlab]

## Detailed explanation

TODO
