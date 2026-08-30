---
id: emb-dtypes-0026
title: "Чому `sizeof(int)` не можна використовувати у network/serial протоколах?"
description: "sizeof(int) залежить від платформи, тож для протоколів завжди використовуй фіксовані типи на кшталт uint16_t."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

`sizeof(int)` залежить від платформи та ABI: 2 байти на MSP430/8051, 4 байти на Cortex-M/x86.

Якщо пристрій A відправляє `int` як 2 байти, а пристрій B читає як 4 байти -> пакет некоректно інтерпретований.

**Рішення**: завжди використовуй `uint16_t`, `int32_t` тощо. Додатково перевіряй endianness між пристроями та документуй byte order у протоколі.[^embeddedinterviewlab]

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
