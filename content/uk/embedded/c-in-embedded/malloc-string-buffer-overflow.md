---
id: emb-cppfound-0100
title: "Trap: де помилка?<br><pre class=\"code-block\"><code><span class=\"code-type\">char</span> *p = <span class=\"code-fn\">malloc</span>(<span class=\"code-num\">5</span>);<br>strcpy(p, \"hello\");<br>p[<span class=\"code-num\">5</span>] = '\\<span class=\"code-num\">0</span>';</code></pre>"
description: "Why allocating five bytes is insufficient for the string hello and its terminator."
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

<span class="warn">Buffer overflow.</span> <code>malloc(5)</code> – 5 байт. <code>"hello"</code> = <code>{'h','e','l','l','o','\0'}</code> – 6 байт включно з null-terminator.<br><br><code>strcpy(p, "hello")</code> вже переповнює буфер: копіює 6 байт у 5-байтний буфер. <code>p[5] = '\0'</code> – шостий запис за межами.<br><br>Правильно: <code>malloc(strlen("hello") + 1)</code> = <code>malloc(6)</code>. Або <code>strncpy(p, "hello", 5); p[4]='\0';</code> – обрізати якщо треба.[^embeddedinterviewlab]

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
