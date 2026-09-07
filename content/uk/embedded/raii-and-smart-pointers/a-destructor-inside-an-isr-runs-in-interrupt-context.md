---
id: emb-raii-0018
title: "Trap: чим небезпечний RAII-деструктор усередині ISR?"
description: "Деструктор виконується в тому ж контексті, що й вихід зі scope – тобто в ISR (interrupt service routine)."
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

## Question code

```c
void isr() {
  LockGuard lock(m); // dtor викличе release В ISR!
  // ...
}
```

## Short answer

<span class="warn">Деструктор виконується в тому ж контексті, що й вихід зі scope – тобто в ISR (interrupt service routine).</span>

Якщо dtor робить блокуючу операцію (mutex release із RTOS, алокація, UART TX), це недопустимо в перериванні: deadlock або jitter.

Захист: в ISR-RAII дозволені лише register-level дії (interrupt enable/disable), жодних блокуючих teardown.[^embeddedinterviewlab]

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
