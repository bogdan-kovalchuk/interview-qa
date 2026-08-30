---
id: emb-cppfound-0035
title: "Trap: <code>int *p = NULL; if(p) *p = 5;</code> vs <code>int *p = NULL; *p = 5;</code> – чи безпечний перший?"
description: "Why a NULL check prevents only one class of invalid dereference."
track: embedded
section: c-in-embedded
level: junior
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

<span class="key">Перший – безпечний</span>. <code>if(p)</code> ≡ <code>if(p != NULL)</code> – перевірка перед розіменуванням. Якщо <code>p == NULL</code> -> умова false, <code>*p</code> не виконується.<br><br><span class="warn">Другий – UB</span>: <code>*p = 5</code> при <code>p == NULL</code> -> HardFault на Cortex-M.<br><br>Але: перевірка NULL не захищає від dangling pointer або wild pointer – вони ненульові, але невалідні; NULL-check – необхідна, але недостатня умова безпеки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
