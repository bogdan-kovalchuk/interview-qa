---
id: emb-raii-0013
title: "Trap: «RAII працює лише зі smart pointers» – у чому помилка?"
description: "RAII – це принцип scope-lifetime, а не про smart pointers."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">RAII – це принцип scope-lifetime, а не про smart pointers.</span>

Lock guard, interrupt guard, scoped handle живуть на стеку й не керують жодним вказівником – це повноцінний RAII. Smart pointer – лише один із застосувань ідеї.

Захист: думай про RAII як «ctor бере / dtor віддає», а не як про `unique_ptr`.[^embeddedinterviewlab]

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
