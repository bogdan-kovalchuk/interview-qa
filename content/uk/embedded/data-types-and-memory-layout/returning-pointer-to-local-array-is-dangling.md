---
id: emb-dtypes-0080
title: "Знайдіть помилку? `char* get_name(void) { char buf[32] = \"test\"; return buf; }`"
description: "buf знищується після return, тож функція повертає dangling pointer на вже недійсну пам'ять стеку."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

<span class="warn">Повернення вказівника на локальний масив -> undefined behavior.</span> `buf[32]` - на стеку, знищується після return.

Caller отримує dangling pointer - вказівник на вже недійсну пам'ять. Читання -> garbage або crash.

Рішення:
1. `static char buf[32];` (але не reentrant);
2. Передати буфер через параметр: `void get_name(char *buf, size_t len);`
3. `malloc` + задокументувати що caller мусить `free`.

GCC: `warning: function returns address of local variable`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
