---
id: emb-cppoop-0015
title: "Що таке vptr і де він зберігається?"
description: "vptr – прихований pointer усередині кожного об'єкта з virtual-функціями, що вказує на vtable його dynamic type."
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

**vptr – прихований pointer усередині кожного об'єкта з virtual-функціями, що вказує на vtable його dynamic type.**

Зазвичай він додається компілятором як прихований член об'єкта, тому `sizeof` зростає приблизно на розмір pointer-а (4 байти на 32-bit). Точна позиція vptr – ABI-dependent, не частина стандарту C++.

Правило: поява хоч однієї virtual-функції зазвичай додає кожному екземпляру vptr.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
