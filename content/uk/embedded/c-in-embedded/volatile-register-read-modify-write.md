---
id: emb-cppfound-0098
title: "Що зробить?<br><pre class=\"code-block\"><code><span class=\"code-type\">uint32_t</span> reg=*((<span class=\"code-kw\">volatile</span> <span class=\"code-type\">uint32_t</span>*)<span class=\"code-num\">0x40020010</span>);<br>reg|=(<span class=\"code-num\">1</span>&lt;&lt;<span class=\"code-num\">5</span>);<br>*((<span class=\"code-kw\">volatile</span> <span class=\"code-type\">uint32_t</span>*)<span class=\"code-num\">0x40020010</span>)=reg;</code></pre>"
description: "What a volatile read-modify-write sequence does and why it can race with an ISR."
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

Read-Modify-Write (RMW) операція над hardware register:<br>1. <span class="key">Read</span>: читає поточне значення регістру з адреси <code>0x40020010</code>;<br>2. <span class="key">Modify</span>: встановлює біт 5 (<code>|= (1&lt;&lt;5)</code>), не змінюючи інші біти;<br>3. <span class="key">Write</span>: записує назад у регістр.<br><br><span class="warn">Ризик</span>: між read і write інший потік або ISR може змінити регістр -> race condition; Для атомарного RMW: STM32 BSRR (GPIO), або disable IRQ навколо RMW.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
