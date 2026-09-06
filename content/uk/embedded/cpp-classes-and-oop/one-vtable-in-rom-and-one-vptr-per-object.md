---
id: emb-cppoop-0013
title: "Скільки коштує virtual-функція по пам'яті?"
description: "Зазвичай vtable – одна на polymorphic class у ROM (read-only memory, .rodata), vptr – один прихований pointer на кожен polymorphic object у RAM (random-access memory)."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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

**Зазвичай vtable – одна на polymorphic class у ROM (read-only memory, `.rodata`), vptr – один прихований pointer на кожен polymorphic object у RAM (random-access memory).**

Спрощена оцінка: vtable entries ≈ кількість virtual functions × розмір pointer-а; vptr ≈ один pointer на екземпляр. Реальний layout залежить від ABI (application binary interface): destructor-и, RTTI або multiple inheritance можуть додати entries.

Правило: vtable рахуй приблизно на клас (ROM), vptr – на екземпляр (RAM); при сотнях об'єктів RAM-вартість стає відчутною.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
