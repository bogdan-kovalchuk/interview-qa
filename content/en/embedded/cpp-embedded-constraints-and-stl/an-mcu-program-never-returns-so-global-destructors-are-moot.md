---
id: emb-cppstl-0021
title: "What does `-fno-use-cxa-atexit` do and why is it fine on an MCU?"
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

**It does not register global object destructors via `__cxa_atexit`.**

On an MCU the program usually never exits, so global destructors are not needed – registration only pulls in runtime infrastructure and ROM.

Rule: static objects on an MCU are "eternal"; `-fno-use-cxa-atexit` removes unnecessary cleanup.[^embeddedinterviewlab]

## Detailed explanation

TODO
