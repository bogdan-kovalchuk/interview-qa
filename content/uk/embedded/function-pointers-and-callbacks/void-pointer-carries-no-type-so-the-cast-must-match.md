---
id: emb-fnptr-0031
title: "Trap: чому `void *context` треба приводити до правильного типу?"
description: "Неправильний cast context pointer-а дає undefined behavior при доступі до об'єкта."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">Неправильний cast context pointer-а дає undefined behavior при доступі до об'єкта.</span>

`void *` не містить runtime type information. Якщо callback очікує `struct Uart *`, а driver передав `struct Spi *`, compiler не захистить. Далі доступ до полів інтерпретує чужий layout як неправильний тип.

Захист: роби registration API typed там, де можливо; додавай magic/version поля для debug; не reuse-ь один callback signature для несумісних context object-ів без wrapper-а.[^embeddedinterviewlab]

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
