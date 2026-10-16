---
id: emb-cppstl-0002
title: "Trap: що відбувається з `throw` і `try`/`catch` при `-fno-exceptions`?"
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

<span class="warn">У власному коді `throw`/`try`/`catch` зазвичай стають compile error; library-шляхи, які мали кинути виняток, часто завершуються `abort()`.</span>

Це не «магічне прибирання» помилок: шлях із `vector::at()` out-of-range може аварійно зупинити систему замість обробленого винятку.

Захист: аудитуй throwing API (application programming interface) стандартної бібліотеки й замінюй їх на явні перевірки/статуси.[^embeddedinterviewlab]

## Detailed explanation

TODO
