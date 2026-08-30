---
id: emb-cppfound-0099
title: "Чим небезпечний неініціалізований вказівник (wild pointer) і як захиститись?"
description: "Why a wild pointer is not detected by a NULL check and how to initialize safely."
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

<span class="key">Wild pointer</span> – вказівник з garbage-адресою (значення стека), не NULL. Перевірка <code>if(p != NULL)</code> не виявляє його.<br><br>Небезпеки:<br>• Запис за довільною адресою -> corruption критичних даних;<br>• На MCU: запис у периферійні регістри -> непередбачувана поведінка hardware;<br>• Важко відтворити – залежить від стану стека.<br><br>Захист:<br>• Завжди ініціалізуй: <code>int *p = NULL;</code> або одразу <code>= &amp;x</code>;<br>• <code>-fsanitize=address</code> при розробці;<br>• Static analysis: PC-lint, Coverity.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
