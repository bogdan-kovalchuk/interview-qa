---
id: emb-cppfound-0006
title: "Trap: чому <code>sizeof(arr)</code> у функції повертає 4 або 8, а не розмір масиву?"
description: "Why an array parameter is treated as a pointer inside a function."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

При передачі масиву у функцію він <span class="warn">decay-ується до вказівника</span>: <code>void f(int arr[])</code> ≡ <code>void f(int *arr)</code>.<br><br><code>sizeof(arr)</code> всередині функції = <code>sizeof(int*)</code> = 4 або 8 (розмір вказівника), а не розмір масиву.<br><br>Реальний кейс: змінили <code>int16_t buffer[256]</code> на <code>int16_t *buffer</code>, але залишили <code>sizeof(buffer)/sizeof(buffer[0])</code> -> обробляли лише 2 елементи замість 256.<br><br>Рішення: передавай розмір явно: <code>void f(int *arr, size_t n)</code>.[^embeddedinterviewlab]

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
