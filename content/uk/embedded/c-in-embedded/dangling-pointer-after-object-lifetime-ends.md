---
id: emb-cppfound-0017
title: "Що таке dangling pointer і коли він виникає?"
description: "When a pointer refers to storage whose lifetime has ended."
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

<span class="key">Dangling pointer</span> – вказівник, що вказує на <span class="warn">вже звільнену або знищену</span> пам'ять.<br><br>Причини:<br>1; Повернення адреси локальної змінної: <code>int* f(){ int x=5; return &amp;x; }</code> – x знищена при поверненні;<br>2; Після <code>free(ptr)</code> без обнулення: <code>free(ptr); *ptr = 1;</code> – UB;<br>3. Вказівник на об'єкт, термін дії якого закінчився.<br><br>Небезпека: пам'ять <span class="warn">виглядає валідною</span> до її перевикористання. Баги надзвичайно важко відтворити.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
