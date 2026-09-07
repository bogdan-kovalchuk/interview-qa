---
id: emb-cppoop-0025
title: "Навіщо в embedded C++ використовують `-fno-exceptions` і `-fno-rtti`?"
description: "-fno-exceptions прибирає інфраструктуру обробки винятків; -fno-rtti прибирає RTTI (runtime type information)."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**`-fno-exceptions` прибирає інфраструктуру обробки винятків; `-fno-rtti` прибирає RTTI (runtime type information).**

Exceptions додають unwind/runtime support і ускладнюють детермінізм error handling; RTTI додає type metadata для `dynamic_cast`/`typeid`. Їх вимикають, щоб зменшити бінарник і відповідати AUTOSAR (Automotive Open System Architecture) / MISRA C++ (Motor Industry Software Reliability Association C++) стилю.

Правило: на цілях з цими прапорцями не використовуй `throw`, `dynamic_cast`, `typeid` – покладайся на return codes і статичний поліморфізм.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
