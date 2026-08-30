---
id: emb-cppfound-0086
title: "Trap: нескінченний цикл?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">256</span>];<br><span class=\"code-type\">int</span> *p=arr;<br><span class=\"code-kw\">for</span>(<span class=\"code-type\">uint8_t</span> i=<span class=\"code-num\">0</span>;<br>i&lt;<span class=\"code-num\">256</span>;<br>i++) *p++=i;</code></pre>"
description: "Why an 8-bit loop counter cannot reach the terminating value 256."
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

<span class="warn">Так, нескінченний цикл!</span> <code>uint8_t i</code> – беззнаковий 8-bit. При <code>i=255</code> -> <code>i++</code> -> wrap до 0 -> умова <code>0 &lt; 256</code> -> true. Цикл ніколи не завершується.<br><br>Виправлення: <code>for(int i=0; i&lt;256; i++)</code> або <code>for(size_t i=0; i&lt;256; i++)</code>.<br><br>GCC з <code>-Wtype-limits</code>: попередить якщо умова завжди true; Типова помилка при роботі з буферами розміром 256.[^embeddedinterviewlab]

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
