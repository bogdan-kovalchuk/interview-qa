---
id: emb-cppoop-0031
title: "Trap: чому методи інлайняться у bare-metal доступ лише на `-O2`, а не на `-O0`?"
description: "На -O0 компілятор не інлайнить – кожен set() стає реальним викликом функції з прологом/епілогом."
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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

На `-O0` компілятор не інлайнить – кожен `set()` стає реальним викликом функції з прологом/епілогом.

Тобто zero-overhead абстракція проявляється лише з увімкненою оптимізацією; у debug-збірці клас-обгортка коштує як виклик.

Захист: оцінюй розмір/швидкість C++-абстракцій на release-прапорцях (`-O2`/`-Os`), не на `-O0`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
