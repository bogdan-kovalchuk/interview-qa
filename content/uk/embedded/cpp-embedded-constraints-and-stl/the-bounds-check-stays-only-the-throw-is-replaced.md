---
id: emb-cppstl-0034
title: "Чи прибирає `-fno-exceptions` сам перевірочний код у `at()`?"
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

<span class="warn">Ні – bounds check лишається; у libstdc++-подібних реалізаціях шлях помилки без exceptions часто веде до `abort()`/fatal handler.</span>

Тобто bounds check у `vector::at()`/`array::at()` усе ще виконується; змінюється лише реакція на провал – аварійна зупинка без діагностики замість винятку.

Захист: для гарячого шляху, де перевірка зайва, використовуй `operator[]` з власною валідацією; для безпеки – логуй перед зупинкою.[^embeddedinterviewlab]

## Detailed explanation

TODO
