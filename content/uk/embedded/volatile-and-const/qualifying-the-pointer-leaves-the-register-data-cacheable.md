---
id: emb-volconst-0011
title: "Trap: чому `uint32_t * volatile reg` не є правильним типом для hardware register data?"
description: "volatile застосований до pointer variable, а не до даних за адресою."
track: embedded
section: volatile-and-const
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

<span class="warn">`volatile` застосований до pointer variable, а не до даних за адресою.</span>

Компілятор не кешуватиме саму змінну `reg`, але після отримання адреси доступ до `*reg` має тип звичайного `uint32_t`. Отже, читання register data все ще може оптимізуватися як звичайна пам'ять.

Захист: використовуй `volatile uint32_t *reg` для pointer to volatile data або `volatile uint32_t * const reg`, якщо адреса фіксована.[^embeddedinterviewlab]

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
