---
id: emb-cppfound-0061
title: "Trap: що не так?<br><pre class=\"code-block\"><code>int *p = malloc(sizeof(int)*10);<br>free(p);<br>printf(\"%d\", p[0]);</code></pre>"
description: "Why dereferencing freed heap memory is undefined behavior."
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

<span class="warn">Use-after-free – undefined behavior.</span> Після <code>free(p)</code> пам'ять повернута heap manager-у і може бути негайно перевикористана (наприклад, наступним <code>malloc</code>).<br><br><code>p[0]</code> після <code>free</code>: може повернути 0 (heap manager записав туди metadata), старе значення, або crash. У security контексті: джерело use-after-free exploits.<br><br>Захист: <code>free(p); p = NULL;</code>. Потім <code>if(p != NULL)</code> перед доступом.[^embeddedinterviewlab]

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
