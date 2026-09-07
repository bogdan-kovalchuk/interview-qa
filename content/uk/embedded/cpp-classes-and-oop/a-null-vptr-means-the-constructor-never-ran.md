---
id: emb-cppoop-0026
title: "Trap: бачиш null vptr у глобального об'єкта – у чому причина?"
description: "Глобальні конструктори не викликані – startup не пройшов .init_array."
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

<span class="warn">Глобальні конструктори не викликані – startup не пройшов `.init_array`.</span>

Поки ctor не виконався, vptr (і решта полів) лишаються нульовими/сміттям; перший же virtual-виклик стрибне за нульовою адресою -> HardFault.

Захист: переконайся, що bare-metal startup ітерує `.init_array` і викликає глобальні ctor перед `main()`.[^embeddedinterviewlab]

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
