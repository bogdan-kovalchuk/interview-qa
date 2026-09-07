---
id: emb-raii-0004
title: "Trap: чому lock guard обов'язково має `= delete` на copy/move?"
description: "Якби guard можна було скопіювати, два деструктори звільнили б той самий мьютекс – double-release і миттєва corruption."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
LockGuard(const LockGuard&) = delete;
LockGuard& operator=(const LockGuard&) = delete;
```

## Short answer

<span class="warn">Якби guard можна було скопіювати, два деструктори звільнили б той самий мьютекс – double-release і миттєва corruption.</span>

Заборона копіювання гарантує рівно один власник lock'а й рівно одне звільнення.

Захист: будь-який клас-обгортка ресурсу має бути non-copyable (`= delete`) або move-only.[^embeddedinterviewlab]

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
