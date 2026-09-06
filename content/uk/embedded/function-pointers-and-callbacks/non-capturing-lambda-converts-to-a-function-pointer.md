---
id: emb-fnptr-0037
title: "Чи можна передати C++ non-capturing lambda у C-style callback?"
description: "Так, якщо lambda не має captures і сигнатура сумісна."
track: embedded
section: function-pointers-and-callbacks
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

**Так, якщо lambda не має captures і сигнатура сумісна.**

Non-capturing lambda може перетворитися на pointer to function. Capturing lambda має прихований state object, тому не може бути звичайним C function pointer. Для state потрібен `void *context` або `std::function` там, де він прийнятний.

Embedded-правило: для C HAL callbacks у C++ використовуй non-capturing lambda або static/free function plus context.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
