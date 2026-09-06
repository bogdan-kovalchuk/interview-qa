---
id: emb-fnptr-0028
title: "Що таке callback lifetime problem?"
description: "Driver може зберегти callback/context довше, ніж живе об'єкт, на який вони вказують."
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

**Driver може зберегти callback/context довше, ніж живе об'єкт, на який вони вказують.**

Наприклад, реєструють `ctx = &local_config` у функції init, функція повертається, stack frame зникає, а interrupt пізніше викликає callback із dangling context. Це use-after-scope.

Правило: context pointer для async callback має вказувати на object із достатнім lifetime: static storage, heap object з ownership, або driver instance, який гарантовано живий до unregister.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
