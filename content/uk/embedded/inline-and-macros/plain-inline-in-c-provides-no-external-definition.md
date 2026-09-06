---
id: emb-macros-0031
title: "Trap: чому `inline` без `static` у C може дати linker error?"
description: "У C99+ функція, оголошена просто inline (без static/extern), надає лише inline definition; вона не створює external symbol."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-06
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

У C99+ функція, оголошена просто `inline` (без `static`/`extern`), надає лише inline definition; вона не створює external symbol.

Якщо компілятор у якомусь місці вирішить не inline-ити і зробити звичайний виклик, лінкер не знайде зовнішнього визначення -> `undefined reference`.

Захист: у header пиши `static inline` – кожен translation unit (TU) отримує власне визначення, і проблеми linkage не виникає. (У C++ семантика `inline` інша й безпечніша.)[^embeddedinterviewlab]

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
