---
id: emb-cppfound-0069
title: "Навіщо потрібен cast при роботі з <code>void*</code> і які обмеження?"
description: "C and C++ conversion rules and limitations of void pointers."
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

В <span class="key">C</span>: присвоєння <code>void*</code> до <code>T*</code> (і навпаки) не потребує explicit cast – автоматичне перетворення. <code>int *p = malloc(n);</code> – коректно у C.<br><br>В <span class="key">C++</span>: <span class="warn">обов'язковий explicit cast</span>: <code>int *p = (int*)malloc(n);</code>.<br><br>Обмеження void*:<br>• Не можна розіменувати без cast;<br>• Не можна pointer arithmetic (стандарт C);<br>• Не зберігає type-safety;<br><br>Перед розіменуванням: <code>*(int*)vp = 42;</code>. Це правило зберігає правильний тип доступу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
