---
id: emb-cppfound-0058
title: "Яку адресу матиме <code>p+1</code> якщо <code>p</code> вказує на <code>uint32_t</code> за адресою <code>0x2000</code>?"
description: "How pointer arithmetic scales by the pointed-to type."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

<code>p+1 = 0x2004</code>.<br><br>Pointer arithmetic для <code>uint32_t*</code>: крок = <code>sizeof(uint32_t) = 4</code> байти. <code>0x2000 + 1*4 = 0x2004</code>.<br><br>Загальна формула: <code>p + n</code> -> адреса = <code>(uintptr_t)p + n * sizeof(*p)</code>.<br><br>Регістровий bank: якщо <code>volatile uint32_t *reg = (volatile uint32_t*)0x40020000;</code> -> <code>reg+1</code> -> регістр за адресою <code>0x40020004</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
