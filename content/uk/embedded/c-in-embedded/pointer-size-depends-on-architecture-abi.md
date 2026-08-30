---
id: emb-cemb-0004
title: "Який розмір вказівника і від чого він залежить?"
description: "Розмір вказівника залежить від адресного простору архітектури й ABI (2/4/8 байтів), а не від типу, на який він вказує."
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

Розмір вказівника залежить від адресного простору архітектури й ABI, а не від типу, на який він вказує.[^dou-embedded-interview] На 32-bit системі зазвичай `sizeof(void*) == 4`, на 64-bit – `8`, на 16-bit – `2`.

`int *`, `char *` і `struct Foo *` зазвичай мають однаковий розмір у межах однієї платформи, бо всі зберігають адресу. У embedded можуть бути нюанси з різними memory spaces або function pointers, тому правильна відповідь: перевіряти через `sizeof(pointer)` для конкретного компілятора й цілі.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
