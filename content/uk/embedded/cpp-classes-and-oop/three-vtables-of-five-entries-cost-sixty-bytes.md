---
id: emb-cppoop-0014
title: "Порахуй спрощену вартість: 3 класи, по 5 virtual-методів. Скільки ROM на vtables?"
description: "Мінімальна оцінка: 60 байт ROM (read-only memory): 3 vtables × 5 entries × 4 байти на 32-bit target."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

**Мінімальна оцінка: 60 байт ROM (read-only memory)**: 3 vtables × 5 entries × 4 байти на 32-bit target.

У RAM (random-access memory) додатково – vptr на кожен об'єкт: 100 об'єктів × 4 байти = 400 байт RAM лише на vptr. Реальний ROM може бути більшим через ABI (application binary interface), RTTI або virtual destructors.

Правило: vtable рахуй приблизно на клас, vptr – на екземпляр; на малому MCU (microcontroller unit) саме vptr × кількість об'єктів зазвичай болючіше.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
