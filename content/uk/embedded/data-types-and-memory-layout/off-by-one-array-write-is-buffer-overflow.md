---
id: emb-dtypes-0053
title: "Яку помилку містить? `char buf[256]; buf[256] = '\\0';`"
description: "Валідні індекси buf[256] - 0..255, тож запис у buf[256] - вихід за межі масиву."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="warn">Off-by-one помилка -> buffer overflow.</span> Валідні індекси масиву `buf[256]`: `0..255`. `buf[256]` - вже за межами.

Запис туди -> undefined behavior: може зіпсувати іншу локальну змінну, адресу повернення, або `.bss`.

Правильно: `buf[255] = '\0';` або `char buf[257]` якщо потрібен 256-символьний рядок + null-terminator.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
