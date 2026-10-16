---
id: emb-cppstl-0030
title: "Як compile-time заборона heap допомагає в аудиті safety-critical коду?"
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

**Якщо глобальний `operator new` видалений або заблокований, випадкова heap-алокація стає compile/link error.**

Об'єкти можна будувати через placement new у статично виділених буферах або pools з фіксованою місткістю. Це простіше аргументувати в memory-safety review, ніж політику «просто не використовуємо heap».

Правило: `= delete` глобального `new` перетворює no-heap policy з дисципліни на структурну гарантію.[^embeddedinterviewlab]

## Detailed explanation

TODO
