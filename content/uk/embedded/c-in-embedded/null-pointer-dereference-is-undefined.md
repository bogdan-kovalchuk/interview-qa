---
id: emb-cppfound-0019
title: "Що таке NULL pointer і що відбувається при його розіменуванні?"
description: "What a null pointer means and why dereferencing it is undefined behavior."
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

**NULL pointer** – гарантовано невалідна адреса (null pointer constant). У C визначений як `0` або `(void*)0`. У C++ – `nullptr`.

Розіменування NULL -> <span class="warn">undefined behavior</span>. На Cortex-M: адреса `0x00000000` – початок Flash (Vector Table). Запис туди -> HardFault або пошкодження Vector Table.

Захист: завжди перевіряй перед розіменуванням: `if(p != NULL) *p = val;`; Ініціалізуй: `int *p = NULL;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
