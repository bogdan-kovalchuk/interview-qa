---
id: emb-macros-0041
title: "Як згенерувати унікальне ім'я змінної на основі номера рядка?"
description: "Потрібні два рівні: CAT склеює токени, а XCAT спершу розгортає __LINE__ у число, перш ніж склеїти."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 3
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
#define CAT(a, b) a##b
#define XCAT(a, b) CAT(a, b)
#define UNIQUE(p) XCAT(p, __LINE__)
```

## Short answer

**Потрібні два рівні**: `CAT` склеює токени, а `XCAT` спершу розгортає `__LINE__` у число, перш ніж склеїти.

Тоді `int UNIQUE(tmp_);` на рядку 42 дасть `int tmp_42;`. Використовується для scope-guard'ів, RAII-хелперів, тестових макросів.

Правило: і для `#`, і для `##` із вбудованими макросами завжди потрібен додатковий рівень indirection.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
