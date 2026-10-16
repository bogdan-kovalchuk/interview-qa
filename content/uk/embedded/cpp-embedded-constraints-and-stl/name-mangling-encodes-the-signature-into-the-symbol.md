---
id: emb-cppstl-0017
title: "Що таке name mangling і чому через нього потрібен `extern \"C\"`?"
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

**C++ кодує сигнатуру у символ (для overload resolution): `sensor_read(uint8_t)` -> `_Z10sensor_readh`; C не мангли́ть.**

Без `extern "C"` лінкер шукатиме mangled-ім'я й не знайде немангленого C-символу -> помилка лінкування.

Правило: mangling – причина, чому міжмовний інтерфейс вимагає C linkage.[^embeddedinterviewlab]

## Detailed explanation

TODO
