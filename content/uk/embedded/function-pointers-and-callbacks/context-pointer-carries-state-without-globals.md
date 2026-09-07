---
id: emb-fnptr-0005
title: "Чому в callback API часто є параметр `void *context`?"
description: "context передає стан користувача callback-а без глобальних змінних."
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

**`context` передає стан користувача callback-а без глобальних змінних.**

Функція callback сама по собі не несе captured state, як lambda з capture у C++. Тому driver зберігає пару: function pointer + context pointer. Коли подія стається, driver викликає `cb(context)`, а callback приводить context до свого типу.

Правило: callback без context швидко змушує використовувати globals; callback із context масштабується на кілька інстансів UART/SPI/timer.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
