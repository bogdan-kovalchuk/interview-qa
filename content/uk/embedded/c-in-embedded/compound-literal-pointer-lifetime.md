---
id: emb-cppfound-0081
title: "Trap: чи коректно у C99?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> *p = &amp;(<span class=\"code-type\">int</span>){<span class=\"code-num\">5</span>};<br><span class=\"code-fn\">printf</span>(\"%d\", *p);</code></pre>"
description: "Whether a pointer to a C99 compound literal remains valid within its block."
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

<span class="key">Так, коректно</span> у межах того ж блоку. <code>(int){5}</code> – compound literal (C99): тимчасовий об'єкт зі storage duration автоматичного блоку.<br><br><span class="warn">Але dangling pointer</span> якщо вийти за межі блоку:<br><code>int *p; { p = &amp;(int){5}; } *p; // UB – блок закінчився</code><br><br>GCC може не попередити. Безпечне використання: лише у тому ж scope де literal визначений.[^embeddedinterviewlab]

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
