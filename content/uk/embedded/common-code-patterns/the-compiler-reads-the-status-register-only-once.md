---
id: emb-patterns-0025
title: "Trap: чому без `volatile` цей polling-цикл стає нескінченним?"
description: "Компілятор читає SR один раз, бачить, що прапорець не виставлений, і більше не перечитує – у C abstract machine ніщо не змінює SR."
track: embedded
section: common-code-patterns
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

## Question code

```c
while (!(REG->SR & FLAG))
    ;
```

## Short answer

<span class="warn">Компілятор читає `SR` один раз, бачить, що прапорець не виставлений, і більше не перечитує</span> – у C abstract machine ніщо не змінює `SR`.

Результат: цикл крутиться на закешованому значенні вічно, навіть коли апаратура вже виставила прапорець.

Захист: оголоси регістр `volatile` – тоді `SR` перечитується на кожній ітерації.[^embeddedinterviewlab]

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
