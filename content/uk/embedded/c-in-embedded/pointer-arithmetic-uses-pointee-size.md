---
id: emb-cppfound-0005
title: "Що виведе?<br><pre class=\"code-block\"><code>uint8_t *p = (uint8_t*)0x1000;<br>p++;<br>printf(\"%p\", (void*)p);</code></pre>"
description: "How pointer arithmetic scales with the pointed-to type."
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

<code>0x1001</code>.<br><br>Pointer arithmetic масштабується по <code>sizeof(*p)</code>. Для <code>uint8_t*</code>: <code>sizeof(uint8_t) = 1</code>, тому <code>p++</code> -> адреса + 1 байт.<br><br>Якби <code>uint32_t *p = (uint32_t*)0x1000; p++;</code> -> <code>0x1004</code> (кроком 4 байти).<br><br>Правило: <code>p + n</code> = <code>(char*)p + n * sizeof(*p)</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
