---
id: emb-fnptr-0035
title: "Чи може callback бути `static` функцією?"
description: "Так. static у file scope обмежує linkage функції поточним .c файлом, але її адресу все одно можна передати як callback усередині цього translation unit."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Так.**

`static` у file scope обмежує linkage функції поточним `.c` файлом, але її адресу все одно можна передати як callback усередині цього translation unit. Це навіть бажано для private handlers, які не мають бути частиною public symbol table.

Правило: callback має бути видимий там, де його адресу передають; external linkage потрібен тільки якщо інший translation unit має напряму посилатися на ім'я функції.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
