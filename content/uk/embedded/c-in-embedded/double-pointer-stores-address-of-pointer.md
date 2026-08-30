---
id: emb-cppfound-0021
title: "Що таке double pointer (<code>int **pp</code>) і навіщо він потрібен?"
description: "What a double pointer stores and why functions use it."
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

<span class="key">Double pointer</span> – вказівник, що зберігає адресу іншого вказівника.<br><br>Навіщо:<br>1. <span class="key">Зміна pointer caller-а</span>: <code>void alloc(int **pp){ *pp = malloc(n); }</code> – без <code>**</code> caller не побачить нову адресу;<br>2. <span class="key">2D масиви через масиви вказівників</span>;<br>3. Просування parse-cursor: <code>void parse(char **p){ (*p)++; }</code>;<br><br>Читання типу: <code>int **pp</code> – "вказівник на вказівник на int"; <code>*pp</code> -> вказівник, <code>**pp</code> -> значення int.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
