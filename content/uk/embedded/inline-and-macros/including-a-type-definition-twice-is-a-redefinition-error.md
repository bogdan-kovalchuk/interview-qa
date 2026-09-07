---
id: emb-macros-0039
title: "Trap: що станеться, якщо включити header з визначенням `struct` двічі без include guard?"
description: "Redefinition error: повторне визначення того самого типу/struct/typedef у одному translation unit заборонене."
track: embedded
section: inline-and-macros
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

<span class="warn">Redefinition error</span>: повторне визначення того самого типу/`struct`/`typedef` у одному translation unit заборонене.

Подвійне включення легко стається транзитивно: `a.h` і `b.h` обидва включають `types.h`, а `main.c` включає обидва. Без guard вміст `types.h` обробиться двічі.

Захист: кожен header загортай у `#ifndef`-guard або `#pragma once` – тоді другий `#include` стає no-op.[^embeddedinterviewlab]

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
