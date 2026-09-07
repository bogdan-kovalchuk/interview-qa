---
id: emb-tmplcx-0012
title: "Які переваги CRTP над virtual dispatch?"
description: "Немає обов'язкового vptr (virtual pointer), немає indirect call і простіше аналізувати WCET (worst-case execution time)."
track: embedded
section: templates-and-constexpr
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

**Немає обов'язкового vptr (virtual pointer), немає indirect call і простіше аналізувати WCET (worst-case execution time).**

Після оптимізації згенерований асемблер часто зводиться до прямого виклику; інтерфейс перевіряється на етапі компіляції (відсутній метод = compile error). Розмір vptr залежить від ABI (application binary interface) і ширини вказівника.

Правило: CRTP – для сенсорів у ISR (interrupt service routine) і tight control loops; virtual – коли потрібен runtime-поліморфізм (плагіни, динамічне завантаження драйверів).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
