---
id: emb-cppfound-0080
title: "Що виведе?<br><pre class=\"code-block\"><code>int x=42;<br>void *p=&amp;x;<br>printf(\"%d\", *(int*)p);</code></pre>"
description: "How a void pointer is cast back before dereferencing the original object."
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

<code>42</code>.<br><br><code>void *p = &amp;x</code> – дозволено у C (implicit conversion). <code>p</code> зберігає адресу <code>x</code>, але тип "erased".<br><br><code>*(int*)p</code> – cast до <code>int*</code>, потім розіменування. Коректно оскільки <code>p</code> вказує на справжній <code>int</code>.<br><br>Якби cast до неправильного типу: <code>*(float*)p</code> -> UB (strict aliasing). Правило: cast <code>void*</code> завжди до того типу, з якого він був отриманий.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
