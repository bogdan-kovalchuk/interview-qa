---
id: emb-fnptr-0017
title: "Чому cast function pointer-а часто приховує реальний баг?"
description: "Cast вимикає перевірку типів, але не змінює реальну сигнатуру функції."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Cast вимикає перевірку типів, але не змінює реальну сигнатуру функції.</span>

Якщо API очікує `void (*)(void *)`, а ти передаєш `void (*)(int)` через cast, caller усе одно викличе функцію за контрактом API. Аргументи будуть передані не так, як очікує callee. Це не portable і може бути UB.

Захист: пиши thin wrapper: `static void wrapper(void *ctx) { real_handler((int)(intptr_t)ctx); }`, якщо така модель справді потрібна.[^embeddedinterviewlab]

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
