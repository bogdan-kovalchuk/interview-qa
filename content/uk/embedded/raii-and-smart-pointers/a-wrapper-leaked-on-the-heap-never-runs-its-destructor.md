---
id: emb-raii-0029
title: "Trap: що станеться з ресурсом, якщо об'єкт-обгортку створити на heap і забути `delete`?"
description: "Деструктор не викличеться -> ресурс не звільниться (leak), попри те що це «RAII-клас»."
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

## Short answer

<span class="warn">Деструктор не викличеться -> ресурс не звільниться (leak), попри те що це «RAII-клас».</span>

RAII гарантує очищення лише для об'єктів з автоматичним (stack) lifetime або керованих smart pointer'ом. `new LockGuard(...)` без delete = той самий забутий unlock.

Захист: тримай RAII-об'єкти на стеку або під `unique_ptr`, не як «голий» `new`.[^embeddedinterviewlab]

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
