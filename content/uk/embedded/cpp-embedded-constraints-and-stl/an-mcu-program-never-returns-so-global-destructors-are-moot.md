---
id: emb-cppstl-0021
title: "Що робить `-fno-use-cxa-atexit` і чому це ок для MCU?"
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

**Не реєструє деструктори глобальних об'єктів через `__cxa_atexit`.**

На MCU програма зазвичай ніколи не завершується, тож dtor глобалів і не потрібні – реєстрація лише тягне runtime-інфраструктуру й ROM.

Правило: статичні об'єкти на MCU «вічні»; `-fno-use-cxa-atexit` прибирає непотрібний cleanup.[^embeddedinterviewlab]

## Detailed explanation

TODO
