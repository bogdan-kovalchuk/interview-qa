---
id: emb-cppfound-0056
title: "Trap на Cortex-M0 – ризик?<br><pre class=\"code-block\"><code>uint8_t *p=(uint8_t*)0x40020000;<br>uint32_t val=*(uint32_t*)p;</code></pre>"
description: "How misaligned accesses can fault on Cortex-M0."
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

<code>p</code> – <code>uint8_t*</code>: гарантій вирівнювання нема. Cast до <code>uint32_t*</code> і розіменування:<br><br>Якщо адреса <code>0x40020000</code> вирівняна на 4 -> ОК. Але якщо <code>p</code> вказує на <code>0x40020001</code> (misaligned) -> Cortex-M0: <span class="warn">HardFault</span>. Cortex-M3/M4: повільно але без fault.<br><br>Безпечно: <code>uint32_t val; memcpy(&amp;val, p, sizeof(val));</code> – компілятор оптимізує до одного LDR якщо вирівняно.[^embeddedinterviewlab]

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
