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

<span class="key">NULL pointer</span> – гарантовано невалідна адреса (null pointer constant). У C визначений як <code>0</code> або <code>(void*)0</code>. У C++ – <code>nullptr</code>.<br><br>Розіменування NULL -> <span class="warn">undefined behavior</span>. На Cortex-M: адреса <code>0x00000000</code> – початок Flash (Vector Table). Запис туди -> HardFault або пошкодження Vector Table;<br><br>Захист: завжди перевіряй перед розіменуванням: <code>if(p != NULL) *p = val;</code>; Ініціалізуй: <code>int *p = NULL;</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
