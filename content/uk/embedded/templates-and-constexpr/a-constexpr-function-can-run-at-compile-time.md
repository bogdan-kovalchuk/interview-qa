---
id: emb-tmplcx-0005
title: "Що таке constexpr-функція?"
description: "Функція, що може обчислюватися на етапі компіляції, коли входи константні, і в runtime – інакше."
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

**Функція, що може обчислюватися на етапі компіляції, коли входи константні, і в runtime – інакше.**

Це дозволяє zero-runtime-cost lookup-таблиці, конфігураційні значення й обчислення: результат може лягти у Flash/`.rodata` як готова константа, якщо об'єкт має відповідне статичне зберігання.

Правило: `constexpr` переносить обчислення з runtime у build time там, де результат справді потрібен як constant expression.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
