---
id: emb-cppstl-0019
title: "Які ключові прапорці компіляції для embedded C++?"
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

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

Вони прибирають: винятки, RTTI, mutex на ініціалізації static (pthread), реєстрацію dtor через `__cxa_atexit`, та `.eh_frame`-таблиці. Часто з `-Os` і `-std=c++17`.

Правило: ці прапорці роблять C++ детермінованим і компактним на голому залізі.[^embeddedinterviewlab]

## Detailed explanation

TODO
