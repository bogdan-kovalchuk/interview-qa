---
id: emb-raii-0003
title: "Як виглядає RAII lock guard для RTOS-мьютекса?"
description: "Ctor захоплює мьютекс, dtor звільняє його при виході зі scope."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
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

```cpp
class LockGuard {
  osMutexId_t m_;
public:
  explicit LockGuard(osMutexId_t m) : m_(m) {
    osMutexAcquire(m_, osWaitForever);
  }
  ~LockGuard() { osMutexRelease(m_); }
};
```

## Short answer

**Ctor захоплює мьютекс, dtor звільняє його при виході зі scope.**

RTOS означає real-time operating system. Будь-який нормальний вихід із блоку або early `return` гарантовано викличе `osMutexRelease`; якщо exceptions увімкнені, це працює і при unwinding. Це усуває забутий unlock на error-шляхах.

Правило: кожна пара acquire/release у C API (application programming interface) – кандидат на lock guard.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
