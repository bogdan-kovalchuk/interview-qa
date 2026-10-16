---
id: emb-cppstl-0005
title: "Що таке `std::expected<T, E>` і чим замінити його до C++23?"
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

**Тип, що несе АБО значення, АБО помилку, і робить перевірку результату явною в типі.**

До C++23 пишуть власний легкий `Result<T, E>` без heap-алокації – невеликий клас із прапорцем «успіх/помилка» та union-подібним сховищем.

Правило: `expected`/`Result` поєднує значення й помилку в одному типі без винятків і без купи.[^embeddedinterviewlab]

## Detailed explanation

TODO
