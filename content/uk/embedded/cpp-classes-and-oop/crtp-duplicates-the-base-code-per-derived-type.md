---
id: emb-cppoop-0022
title: "Trap: який головний недолік CRTP?"
description: "Base-код дублюється для кожного похідного типу (окрема інстанціація шаблону)."
track: embedded
section: cpp-classes-and-oop
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

<span class="warn">Base-код дублюється для кожного похідного типу</span> (окрема інстанціація шаблону).

При багатьох похідних типах і великих base-методах це <span class="warn">роздуває ROM</span>. Також не можна тримати різні CRTP-типи в одному масиві – кожна інстанціація є окремим типом.

Захист: CRTP – для невеликої кількості типів; тримай base-методи дрібними, щоб дублювання було дешевим.[^embeddedinterviewlab]

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
