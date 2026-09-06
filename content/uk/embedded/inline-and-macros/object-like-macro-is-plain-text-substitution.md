---
id: emb-macros-0002
title: "Чим object-like макрос відрізняється від звичайної константи?"
description: "Object-like макрос – це проста текстова заміна: усюди, де зустрінеться BUFFER_SIZE, препроцесор підставить 256."
track: embedded
section: inline-and-macros
level: junior
type: concept
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

```c
#define BUFFER_SIZE 256
```

**Object-like макрос – це проста текстова заміна**: усюди, де зустрінеться `BUFFER_SIZE`, препроцесор підставить `256`.

На відміну від `const` змінної, макрос не має типу і не має scope – він видимий від місця `#define` до кінця файлу (або `#undef`) і ігнорує блоки, функції та namespace.

Правило: для іменованих констант у C++ і сучасному C частіше кращі `const`/`constexpr`/`enum`, бо вони типобезпечні й видимі дебагеру.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
