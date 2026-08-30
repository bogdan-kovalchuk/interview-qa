---
id: emb-cppfound-0079
title: "Як визначити тип \"вказівник на функцію що приймає <code>int</code> і повертає <code>void</code>\"?"
description: "How to read and write a C function-pointer declaration."
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

<code>void (*fp)(int);</code>. Цей запис означає вказівник на функцію.<br><br>Читання: <code>fp</code> – вказівник (<code>*fp</code>), що є функцією (<code>(*fp)(int)</code>), що повертає void.<br><br>Для зручності – <code>typedef</code>:<br><code>typedef void (*callback_t)(int);<br>callback_t fp = my_func;</code>.<br><br>Якщо без typedef для масиву: <code>void (*table[8])(int);</code> – масив з 8 function pointers;<br><br>Виклик: <code>fp(42);</code> або <code>(*fp)(42);</code> – обидва коректні.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
