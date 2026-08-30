---
id: emb-cppfound-0094
title: "Як ефективно ітерувати по масиву через pointer vs індекс – різниця у генерованому коді?"
description: "How optimized compilers usually treat pointer and index iteration."
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

Pointer iteration:  <code>for(int *p=arr; p!=arr+n; p++) use(*p);</code><br>Index iteration: <code>for(int i=0; i&lt;n; i++) use(arr[i]);</code><br><br>На сучасних компіляторах з оптимізацією (<code>-O2</code>): <span class="key">код зазвичай ідентичний</span> – компілятор сам перетворює між формами.<br><br>Але: pointer iteration уникає повторного обчислення базової адреси (<code>arr + i</code> кожен раз). Без оптимізації pointer може бути швидшим. У embedded (без оптимізації): pointer iteration ефективніша для Cortex-M0.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
