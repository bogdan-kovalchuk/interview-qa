---
id: emb-cemb-0022
title: "Як `const` впливає на змінну?"
description: "`const` задає read-only семантику для доступу через const-qualified ім'я, але не гарантує фізичне розміщення у Flash або ROM."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`const` задає read-only семантику для компілятора: об'єкт не можна змінювати через const-qualified ім'я після ініціалізації: `const int x = 5;`. Це не є гарантією, що дані фізично будуть саме у Flash або ROM; розміщення залежить від toolchain, linker script і платформи.

З вказівниками важливо читати справа наліво: `const int *p` – вказівник на незмінні дані; `int * const p` – незмінний сам вказівник; `const int * const p` – незмінні і дані, і адреса. `const` не означає compile-time constant у всіх випадках і може бути знятий cast-ом, але запис у реально const-об'єкт дає undefined behavior.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
