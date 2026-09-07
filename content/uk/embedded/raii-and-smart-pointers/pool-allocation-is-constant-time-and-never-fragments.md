---
id: emb-raii-0017
title: "Що таке arena/pool алокація в контексті RAII?"
description: "Виділення з масиву фіксованого розміру: O(1) вартість, нуль фрагментації, контрольований lifetime."
track: embedded
section: raii-and-smart-pointers
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

**Виділення з масиву фіксованого розміру: O(1) вартість, нуль фрагментації, контрольований lifetime.**

Замість багатьох `malloc`/`free` беремо блоки з пулу. Якщо об'єкти trivial – фазу можна завершити reset-ом арени; якщо об'єкти мають non-trivial destructors, їх треба викликати перед reset.

Правило: pool allocation дає детермінізм і відсутність фрагментації – те, чого бракує heap у embedded.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
