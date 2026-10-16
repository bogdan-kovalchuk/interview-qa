---
id: emb-cppstl-0020
title: "Що робить `-fno-threadsafe-statics`?"
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

**Прибирає mutex-захист навколо ініціалізації function-local static.**

За замовчуванням компілятор додає guard (можливо з pthread), щоб два потоки не ініціалізували static одночасно. На bare-metal без потоків це зайвий код і залежність.

Правило: `-fno-threadsafe-statics` доречний, коли немає конкурентного доступу до lazy-init static (single-threaded bare-metal).[^embeddedinterviewlab]

## Detailed explanation

TODO
