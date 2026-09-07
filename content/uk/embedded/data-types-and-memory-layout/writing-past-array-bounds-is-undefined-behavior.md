---
id: emb-dtypes-0016
title: "Яка небезпека? `int arr[10]; arr[10] = 0;`"
description: "Запис за межі оголошеного масиву - undefined behavior, яке компілятор не перевіряє."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

<span class="warn">Out-of-bounds доступ - undefined behavior.</span> Валідні індекси: `0..9`. `arr[10]` - за межами масиву.

На практиці: може перезаписати іншу локальну змінну на стеку (наприклад, адресу повернення), що спричиняє corruption, crash або security vulnerability.

Компілятор не перевіряє межі. Захист: `-fsanitize=address` при розробці, `static_assert` + явні перевірки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
