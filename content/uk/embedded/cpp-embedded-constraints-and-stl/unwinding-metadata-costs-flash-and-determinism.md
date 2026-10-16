---
id: emb-cppstl-0001
title: "Чому в embedded часто вимикають exceptions (`-fno-exceptions`)?"
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

**Exception/unwinding metadata може помітно збільшити бінарник, а stack unwinding погано підходить для жорсткого real-time аналізу.**

Точна ціна залежить від ABI (application binary interface), compiler runtime і стандартної бібліотеки. Деякі реалізації ще й мають додаткову runtime-інфраструктуру для `throw`/`catch`.

Правило: на flash- і real-time-обмежених цілях exceptions часто вимикають, а помилки передають кодами або `Result`-типами.[^embeddedinterviewlab]

## Detailed explanation

TODO
