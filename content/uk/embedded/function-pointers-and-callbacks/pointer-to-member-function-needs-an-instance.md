---
id: emb-fnptr-0039
title: "Чим pointer to member function у C++ відрізняється від звичайного function pointer?"
description: "Pointer to member function потребує object instance для виклику."
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

**Pointer to member function потребує object instance для виклику.**

`void (Class::*pmf)()` не сумісний із `void (*)()`. Нестатичний метод має прихований `this`, тому його не можна напряму передати в C API, яке очікує free function pointer.

Правило: для C callback із C++ class використовуй static member function wrapper і передавай `this` через context pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
