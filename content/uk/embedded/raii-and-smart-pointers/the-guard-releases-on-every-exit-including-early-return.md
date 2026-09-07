---
id: emb-raii-0019
title: "Як RAII вирішує проблему early return між lock і unlock?"
description: "RAII-guard звільняє мьютекс на кожному нормальному виході зі scope, включно з early return."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
// C: баг на error-шляху
mutex_lock(&m);
if (error) return -1; // забули unlock!
mutex_unlock(&m);
```

## Short answer

**RAII-guard звільняє мьютекс на кожному нормальному виході зі scope, включно з early return.**

```cpp
{ LockGuard lock(m);
  if (error) return -1; } // dtor розблокує
```

Типовий failure mode: early return між lock/unlock дає deadlock через забутий unlock на error path.

Правило: RAII перетворює дисципліну (пам'ятати unlock) на структурну гарантію.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
