---
id: emb-cemb-0003
title: "Які є операції з вказівниками?"
description: "Основні операції над вказівниками – взяття адреси, розіменування, порівняння, приведення типу і pointer arithmetic у кроках sizeof(*p)."
track: embedded
section: c-in-embedded
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Основні операції: взяти адресу `&x`, розіменувати `*p`, доступ до поля через `p->field`, порівняння з `NULL` або іншим вказівником, присвоєння адреси, приведення типу, передача у функцію.[^dou-embedded-interview]

Є pointer arithmetic: `p + 1` переходить не на 1 байт, а на `sizeof(*p)` байтів. Тому `int *p` при `p++` зсувається на розмір `int`. Коректна арифметика визначена в межах одного масиву або на позицію одразу після нього; вихід за межі й розіменування невалідної адреси – undefined behavior.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
