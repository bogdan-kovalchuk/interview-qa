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
updated: 2026-09-07
content_revision: 2
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Wild pointer** – вказівник з garbage-адресою (значення стека), не NULL. Перевірка `if(p != NULL)` не виявляє його.

Небезпеки:
- Запис за довільною адресою -> corruption критичних даних;
- На MCU: запис у периферійні регістри -> непередбачувана поведінка hardware;
- Важко відтворити – залежить від стану стека.

Захист:
- Завжди ініціалізуй: `int *p = NULL;` або одразу `= &x`;
- `-fsanitize=address` при розробці;
- Static analysis: PC-lint, Coverity.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
